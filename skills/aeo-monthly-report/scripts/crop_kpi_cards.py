#!/usr/bin/env python3
"""Split a Semrush Enterprise AIO KPI card row into individual card images.

    python crop_kpi_cards.py shot.png --labels a,b,c,d --prefix kpi_TRAFFIC
    python crop_kpi_cards.py shot.png --row 380 625 --labels a,b,c --prefix kpi_X
    python crop_kpi_cards.py shot.png --labels traffic,conversions,revenue,bounce-rate \
           --prefix kpi_TRAFFIC --skip revenue

Works on a full-page screenshot or a pre-cropped strip. Cards are white rectangles; depending on the
screen they are separated either by grey page background or by white gutters between grey card
borders, so three detectors are tried and the one matching --labels wins.

Requires Pillow and numpy.
"""
import argparse, sys
from PIL import Image
import numpy as np

BG_CANDIDATES = [(244, 245, 249), (247, 248, 250), (250, 250, 252)]
MIN_CARD_W = 110
MAX_UNEVENNESS = 2.2


def trim_left_nav(a):
    """Return the x offset past Semrush's dark left navigation, if present."""
    h, w, _ = a.shape
    dark = (a.mean(2) < 90).mean(0)
    x = 0
    while x < w // 3 and dark[x] > 0.70:
        x += 1
    return x if x > 20 else 0


def find_card_rows(a, min_h=140):
    """Candidate horizontal bands of white cards, topmost first."""
    h, w, _ = a.shape
    rows = np.where((a > 250).all(2).mean(1) > 0.55)[0]
    if len(rows) == 0:
        return []
    bands, start, end = [], rows[0], rows[0]
    for r in rows[1:]:
        if r - end > 25:
            bands.append((start, end))
            start = r
        end = r
    bands.append((start, end))
    out = []
    for s, e in bands:
        if e - s < min_h:
            continue
        s2, e2 = max(0, s - 12), min(h, e + 12)
        out.append((s2, e2))
        # a tall band usually means the KPI row merged with the charts below it —
        # offer the top slice as a fallback candidate
        if e2 - s2 > 430:
            for depth in (300, 350, 400):
                out.append((s2, min(h, s2 + depth)))
    return out


def _runs(mask, w, minlen):
    out, s = [], None
    for x in range(w):
        if mask[x] and s is None:
            s = x
        elif not mask[x] and s is not None:
            if x - s >= minlen:
                out.append((s, x))
            s = None
    if s is not None and w - s >= minlen:
        out.append((s, w))
    return out


def card_spans(strip, expect=None):
    """Return (start, end) x-ranges for each card in a KPI strip."""
    a = np.array(strip.convert("RGB")).astype(int)
    h, w, _ = a.shape
    band = a[int(h * .10):int(h * .90)]
    cands = []

    # 1 · grey page background between cards
    for bg in BG_CANDIDATES:
        col = (np.abs(band - np.array(bg)).sum(2) < 14).mean(0)
        for thresh in (0.995, 0.98, 0.95, 0.90):
            for minlen in (28, 20, 12):
                runs = _runs(col > thresh, w, minlen)
                inner = [r for r in runs if r[0] > 5 and r[1] < w - 5]
                if not inner:
                    continue
                edges = [0] + [(s + e) // 2 for s, e in inner] + [w]
                if runs and runs[0][0] <= 5:
                    edges[0] = runs[0][1]
                if runs and runs[-1][1] >= w - 5:
                    edges[-1] = runs[-1][0]
                cands.append([(edges[i], edges[i + 1]) for i in range(len(edges) - 1)])

    # 2 · white card bodies, merging gaps caused by charts inside a card
    card = (band > 250).all(2).mean(0) > 0.45
    for gap in (25, 40):
        merged = []
        for r in _runs(card, w, 1):
            if merged and r[0] - merged[-1][1] < gap:
                merged[-1] = (merged[-1][0], r[1])
            else:
                merged.append(list(r))
        sp = [tuple(r) for r in merged if r[1] - r[0] >= 60]
        if sp:
            cands.append(sp)

    # 3 · grey card borders with white gutters between them.
    # Card borders are thin (1-3px); the page edge and scrollbar are wide, so filter on width.
    # Outer bounds come from the white extent, since the first card's border merges with the page edge.
    L, sat = band.mean(2), band.max(2) - band.min(2)
    wcols = np.where(card)[0] if card.any() else np.array([0, w - 1])
    left, right = int(wcols[0]), int(wcols[-1]) + 1
    for bthresh in (0.70, 0.55):
        lines = [r for r in _runs(((L > 195) & (L < 248) & (sat < 22)).mean(0) > bthresh, w, 1)
                 if r[1] - r[0] <= 6]
        if len(lines) >= 2:
            cuts = [(lines[i][1] + lines[i + 1][0]) // 2
                    for i in range(len(lines) - 1)
                    if 6 <= lines[i + 1][0] - lines[i][1] <= 45]
            cuts = [c for c in cuts if left + 40 < c < right - 40]
            if cuts:
                edges = [left] + cuts + [right]
                cands.append([(edges[i], edges[i + 1]) for i in range(len(edges) - 1)])

    def ok(sp):
        wid = [e - s for s, e in sp]
        return sp and min(wid) >= MIN_CARD_W and max(wid) / max(1, min(wid)) <= MAX_UNEVENNESS

    def evenness(sp):
        wid = [e - s for s, e in sp]
        return max(wid) / max(1, min(wid))

    cands = [c for c in cands if ok(c)]
    if not cands:
        return []
    if expect:
        exact = [c for c in cands if len(c) == expect]
        if exact:
            return min(exact, key=evenness)
    return min(cands, key=evenness)


def card_row_extent(strip, pad=8):
    """Vertical extent of the KPI cards inside a strip.

    Auto-detected bands sometimes run past the KPI row into the chart below it. The cards are the
    topmost contiguous block of mostly-white rows. One extent is computed for the whole strip so
    every card comes out the same height.
    """
    a = np.array(strip.convert("RGB")).astype(int)
    h, w, _ = a.shape
    frac = (a > 248).all(2).mean(1)
    runs, s0 = [], None
    for y in range(h):
        if frac[y] > 0.55 and s0 is None:
            s0 = y
        elif frac[y] <= 0.55 and s0 is not None:
            runs.append((s0, y))
            s0 = None
    if s0 is not None:
        runs.append((s0, h))
    runs = [r for r in runs if r[1] - r[0] >= 100]
    if not runs:
        return 0, h
    y1, y2 = runs[0]
    return max(0, y1 - pad), min(h, y2 + pad)


def bubble_overlap(strip):
    """Locate the solid-black Intercom launcher in the right half of the strip."""
    a = np.array(strip.convert("L"))
    h, w = a.shape
    x0 = int(w * 0.45)
    d = (a[:, x0:] < 45).astype(np.int64)
    ii = np.pad(d.cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    win = 40
    for y in range(0, h - win, win // 2):
        for x in range(0, d.shape[1] - win, win // 2):
            s = ii[y + win, x + win] - ii[y, x + win] - ii[y + win, x] + ii[y, x]
            if s >= win * win * 0.92:
                return (x + x0, y)
    return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument("image")
    p.add_argument("--labels", required=True, help="comma-separated, left to right")
    p.add_argument("--prefix", required=True,
                   help="kpi_ALLMODELS | kpi_CHATGPTONLY | kpi_ALLTOPICS | kpi_TRAFFIC")
    p.add_argument("--row", nargs=2, type=int, metavar=("Y1", "Y2"),
                   help="pin the card row if auto-detect picks the wrong band")
    p.add_argument("--skip", default="", help="comma-separated labels to not write out")
    p.add_argument("--outdir", default=".")
    a = p.parse_args()

    labels = [x.strip() for x in a.labels.split(",") if x.strip()]
    skip = {x.strip() for x in a.skip.split(",") if x.strip()}

    img = Image.open(a.image).convert("RGB")
    arr = np.array(img).astype(int)
    x0 = trim_left_nav(arr)
    if x0:
        img = img.crop((x0, 0, img.size[0], img.size[1]))
        arr = np.array(img).astype(int)
        print(f"trimmed {x0}px of left navigation")

    bands = [tuple(a.row)] if a.row else find_card_rows(arr)
    if not bands:
        sys.exit("Could not find a card row. Pass --row Y1 Y2.")

    strip, spans, tried = None, [], []
    for y1, y2 in bands:
        c = img.crop((0, y1, img.size[0], y2))
        sp = card_spans(c, expect=len(labels))
        tried.append((y1, y2, len(sp)))
        if len(sp) == len(labels):
            strip, spans = c, sp
            if not a.row:
                print(f"card row at y={y1}-{y2}")
            break
    if strip is None:
        sys.exit(f"No band split into {len(labels)} cards.\n"
                 f"Tried (y1, y2, cards found): {tried}\n"
                 f"Pass --row Y1 Y2 to point at the row, or fix --labels.")

    if bubble_overlap(strip):
        print("WARNING: Intercom bubble overlaps this row. Dismiss it and re-screenshot.")

    ytop, ybot = card_row_extent(strip)
    for i, ((s, e), lab) in enumerate(zip(spans, labels), 1):
        if lab in skip:
            print(f"  skipped {lab}")
            continue
        out = f"{a.outdir.rstrip('/')}/{a.prefix}_{i:02d}_{lab}.png"
        strip.crop((max(0, s - 6), ytop, min(strip.size[0], e + 6), ybot)).save(out)
        print(f"  {out}")


if __name__ == "__main__":
    main()

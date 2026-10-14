#!/usr/bin/env python3
"""Enforce the AEO deck's slide length limits.

    python check_slide_copy.py slides.md

Expected block format:

    ## SLIDE 9 — Performance by Platform
    HEAD: AI Overviews gained the most ground
    DECK: All three platforms improved position this month.
    - AI Overviews: mentions +7.4%, position 1.6 to 1.3
    - Gemini: best position at 1.15
    NOTES: ...
    IMAGE: slide09_performance_by_model.png

Exits 1 if anything is over the limit.
"""
import re, sys

HEAD_MAX, DECK_MAX, BULLET_MAX, BULLETS_MAX = 8, 30, 12, 4
BANNED = ["it's worth noting", "worth noting", "moreover", "furthermore", "delve",
          "landscape", "robust", "leverage", "unlock", "load bearing", "fast-paced",
          "in order to", "utilize"]


def words(s):
    return len(re.findall(r"[A-Za-z0-9%$/.+—–-]+", s))


def main(path):
    text = open(path, encoding="utf-8").read()
    blocks = re.split(r"^## SLIDE ", text, flags=re.M)[1:]
    problems, n = [], 0

    for b in blocks:
        title = b.splitlines()[0].strip()
        n += 1
        head = re.search(r"^HEAD:\s*(.+)$", b, re.M)
        deck = re.search(r"^DECK:\s*(.+)$", b, re.M)
        body = re.split(r"^NOTES:", b, flags=re.M)[0]
        bullets = re.findall(r"^[-*]\s+(.+)$", body, re.M)

        if not head:
            problems.append((title, "no HEAD line"))
        else:
            h = head.group(1).strip()
            if words(h) > HEAD_MAX:
                problems.append((title, f"HEAD {words(h)} words (max {HEAD_MAX}): {h}"))
            if ":" in h:
                problems.append((title, f"HEAD uses a colon — split or shorten: {h}"))

        if deck and words(deck.group(1)) > DECK_MAX:
            problems.append((title, f"DECK {words(deck.group(1))} words (max {DECK_MAX})"))

        if len(bullets) > BULLETS_MAX:
            problems.append((title, f"{len(bullets)} bullets (max {BULLETS_MAX})"))
        for bl in bullets:
            clean = re.sub(r"\*\*|__", "", bl).strip()
            if words(clean) > BULLET_MAX:
                problems.append((title, f"bullet {words(clean)} words (max {BULLET_MAX}): {clean[:70]}"))
            if clean.count("—") + clean.count(" - ") > 0 and words(clean) > 9:
                problems.append((title, f"bullet has an em-dash clause — move it to NOTES: {clean[:60]}"))
            if re.match(r"\*\*", bl.strip()):
                problems.append((title, f"bullet has a bold lead-in: {clean[:50]}"))

        low = body.lower()
        for w in BANNED:
            if w in low:
                problems.append((title, f'banned phrase "{w}"'))

        for m in re.findall(r"position[^.\n]{0,40}", body, re.I):
            if re.search(r"\bup\b|\+\d", m) and "improved" not in m.lower():
                problems.append((title, f'position written as "up"/"+" — use "improved from X to Y": {m.strip()[:60]}'))

    print(f"{n} slides checked")
    if not problems:
        print("PASS — everything within limits")
        return 0
    print(f"\n{len(problems)} problems:\n")
    cur = None
    for t, p in problems:
        if t != cur:
            print(f"  SLIDE {t}")
            cur = t
        print(f"      - {p}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "slides.md"))

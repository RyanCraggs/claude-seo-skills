#!/usr/bin/env python3
"""Turn the Prompt Rankings CSV into per-prompt verdicts and a model summary.

    python parse_prompt_rankings.py export.csv --out prompts.json [--themes themes.json]

Deterministic. No agent should ever do this by reading rows — that is how a frequency collapse gets
reported as a position win.

Verdict logic, in order:
  WENT TO ZERO   was appearing, now zero days
  NEW ENTRY      was zero days, now appearing
  FREQUENCY LOSS days down more than 20% — checked BEFORE position, because a prompt that stops
                 appearing on its weak days posts a large fake position gain
  WIN            position improved AND days held or grew
  LOSS           position worsened
  FREQUENCY GAIN days up more than 20%
  hold           everything else
"""
import argparse, json, sys, csv, re
from collections import Counter


def num(v):
    if v is None:
        return None
    v = str(v).strip()
    if v in ("", "N/A", "NA", "-", "—"):
        return None
    try:
        return float(v)
    except ValueError:
        return None


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        sys.exit("empty CSV")
    cols = list(rows[0].keys())

    def find(*pats):
        for c in cols:
            for p in pats:
                if re.search(p, c, re.I):
                    return c
        return None

    c_prompt = find(r"^prompt$", r"prompt")
    c_model = find(r"^model$", r"model")
    day_cols = [c for c in cols if re.search(r"days? with mention", c, re.I)]
    pos_cols = [c for c in cols if re.search(r"avg.*position", c, re.I)]
    if not (c_prompt and c_model and len(day_cols) == 2 and len(pos_cols) == 2):
        sys.exit(f"unexpected columns: {cols}")

    # the export puts the CURRENT period first in each pair
    cur_days, pri_days = day_cols
    cur_pos, pri_pos = pos_cols
    out = []
    for r in rows:
        p = (r.get(c_prompt) or "").strip()
        if not p:
            continue
        out.append({
            "prompt": p,
            "model": (r.get(c_model) or "").strip().replace("Chat GPT", "ChatGPT"),
            "days_cur": num(r.get(cur_days)), "days_pri": num(r.get(pri_days)),
            "pos_cur": num(r.get(cur_pos)), "pos_pri": num(r.get(pri_pos)),
        })
    return out, {"current": cur_days, "prior": pri_days}


def merge(rows):
    """The export is long-format: one row per period. Fold to one row per prompt+model."""
    keyed = {}
    for r in rows:
        k = (r["prompt"], r["model"])
        d = keyed.setdefault(k, {"prompt": r["prompt"], "model": r["model"],
                                 "days_cur": None, "days_pri": None,
                                 "pos_cur": None, "pos_pri": None})
        for f in ("days_cur", "days_pri", "pos_cur", "pos_pri"):
            if r[f] is not None:
                d[f] = r[f]
    return list(keyed.values())


def verdict(r):
    dc, dp, pc, pp = r["days_cur"], r["days_pri"], r["pos_cur"], r["pos_pri"]
    if dc is None or dp is None:
        return "incomplete"
    if dc == 0 and dp > 0:
        return "WENT TO ZERO"
    if dp == 0 and dc > 0:
        return "NEW ENTRY"
    if dp == 0:
        return "absent"
    if (dc - dp) / dp < -0.20:
        return "FREQUENCY LOSS"
    if pc is not None and pp is not None and (pc - pp) < -0.10 and dc >= dp:
        return "WIN"
    if pc is not None and pp is not None and (pc - pp) > 0.10:
        return "LOSS"
    if (dc - dp) / dp > 0.20:
        return "FREQUENCY GAIN"
    return "hold"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--out", default="prompts.json")
    ap.add_argument("--themes", help="optional JSON mapping prompt -> theme")
    a = ap.parse_args()

    raw, periods = load(a.csv)
    rows = merge(raw)
    themes = json.load(open(a.themes)) if a.themes else {}

    for r in rows:
        r["verdict"] = verdict(r)
        r["theme"] = themes.get(r["prompt"], "")
        r["d_days"] = None if None in (r["days_cur"], r["days_pri"]) else r["days_cur"] - r["days_pri"]
        r["d_pos"] = None if None in (r["pos_cur"], r["pos_pri"]) else round(r["pos_cur"] - r["pos_pri"], 3)

    models = {}
    for m in sorted({r["model"] for r in rows}):
        g = [r for r in rows if r["model"] == m]
        dc = sum(r["days_cur"] or 0 for r in g)
        dp = sum(r["days_pri"] or 0 for r in g)
        wc = [r for r in g if r["days_cur"] and r["pos_cur"] is not None]
        wp = [r for r in g if r["days_pri"] and r["pos_pri"] is not None]
        models[m] = {
            "days_current": dc, "days_prior": dp,
            "weighted_position_current": round(
                sum(r["pos_cur"] * r["days_cur"] for r in wc) / sum(r["days_cur"] for r in wc), 3) if wc else None,
            "weighted_position_prior": round(
                sum(r["pos_pri"] * r["days_pri"] for r in wp) / sum(r["days_pri"] for r in wp), 3) if wp else None,
        }

    counts = Counter(r["verdict"] for r in rows)
    themed = {}
    for t in sorted({r["theme"] for r in rows if r["theme"]}):
        g = [r for r in rows if r["theme"] == t]
        themed[t] = {"prompts": len({r["prompt"] for r in g}),
                     "days_current": sum(r["days_cur"] or 0 for r in g),
                     "days_prior": sum(r["days_pri"] or 0 for r in g)}

    doc = {
        "source_csv": a.csv,
        "period_labels": periods,
        "row_count": len(rows),
        "prompt_count": len({r["prompt"] for r in rows}),
        "model_count": len({r["model"] for r in rows}),
        "verdict_counts": dict(counts),
        "positive": counts["WIN"] + counts["FREQUENCY GAIN"] + counts["NEW ENTRY"],
        "negative": counts["LOSS"] + counts["FREQUENCY LOSS"] + counts["WENT TO ZERO"],
        "days_total_current": sum(r["days_cur"] or 0 for r in rows),
        "days_total_prior": sum(r["days_pri"] or 0 for r in rows),
        "by_model": models,
        "by_theme": themed,
        "rows": sorted(rows, key=lambda r: (r["prompt"], r["model"])),
    }
    json.dump(doc, open(a.out, "w"), indent=2)

    print(f"{doc['prompt_count']} prompts x {doc['model_count']} models = {doc['row_count']} rows")
    if doc["model_count"] < 3:
        print(f"  WARNING: only {doc['model_count']} model(s). The export drops models silently — re-export.")
    print(f"  positive {doc['positive']}   negative {doc['negative']}   {dict(counts)}")
    print(f"  days {doc['days_total_prior']} -> {doc['days_total_current']}")
    for m, v in models.items():
        print(f"  {m:22} days {v['days_prior']:>5} -> {v['days_current']:<5} "
              f"pos {v['weighted_position_prior']} -> {v['weighted_position_current']}")
    print(f"  wrote {a.out}")


if __name__ == "__main__":
    main()

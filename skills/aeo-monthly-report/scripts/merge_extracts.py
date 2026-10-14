#!/usr/bin/env python3
"""Fold the per-agent extraction fragments into one month file.

    python merge_extracts.py extracted/2026-08.*.json --out extracted/2026-08.json

Each transcription agent writes its own fragment so they can run in parallel without stepping on each
other. This just merges them and reports anything two agents disagreed about.
"""
import argparse, glob, json, sys

TOP = ("month", "date_range", "country", "pulled_on")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fragments", nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    paths = []
    for f in a.fragments:
        paths.extend(sorted(glob.glob(f)) or [f])
    paths = [p for p in paths if p != a.out]
    if not paths:
        sys.exit("no fragments found")

    merged, notes, conflicts = {}, [], []
    for p in paths:
        frag = json.load(open(p))
        for k, v in frag.items():
            if k == "notes":
                notes.extend(v or [])
                continue
            if k in merged and merged[k] != v:
                if k in TOP:
                    conflicts.append(f"{k}: {merged[k]!r} ({merged['_src_' + k]}) vs {v!r} ({p})")
                    continue
                conflicts.append(f"{k}: two fragments disagree — kept the first ({merged['_src_' + k]})")
                continue
            merged[k] = v
            merged["_src_" + k] = p

    for k in [k for k in merged if k.startswith("_src_")]:
        del merged[k]
    if notes:
        merged["notes"] = notes

    json.dump(merged, open(a.out, "w"), indent=2)
    print(f"merged {len(paths)} fragments -> {a.out}")
    for p in paths:
        print(f"  {p}")
    missing = [k for k in TOP if k not in merged]
    if missing:
        print(f"  WARNING: missing top-level keys {missing}")
    for c in conflicts:
        print(f"  CONFLICT {c}")
    return 1 if conflicts or missing else 0


if __name__ == "__main__":
    sys.exit(main())

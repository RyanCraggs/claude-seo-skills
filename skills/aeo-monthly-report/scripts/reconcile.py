#!/usr/bin/env python3
"""Cross-check a month's extracted figures before anything is written about them.

    python reconcile.py extracted/2026-08.json --prior extracted/2026-07.json --prompts prompts.json

Most transcription errors show up as a broken sum, so these checks are cheaper and more reliable than
re-reading the screenshots. Exits 1 on any FAIL. Nothing gets written into slide copy until this is
green or the failure is understood and logged.
"""
import argparse, json, sys

FAIL, WARN, OK = "FAIL", "WARN", "ok  "
results = []


def check(level_if_bad, label, ok, detail=""):
    results.append((OK if ok else level_if_bad, label, "" if ok else detail))


def close(a, b, tol=0):
    return a is not None and b is not None and abs(a - b) <= tol


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("current")
    ap.add_argument("--prior")
    ap.add_argument("--prompts")
    a = ap.parse_args()

    cur = json.load(open(a.current))
    pri = json.load(open(a.prior)) if a.prior else None
    pr = json.load(open(a.prompts)) if a.prompts else None

    # --- filters
    check(FAIL, "country is United States", cur.get("country") == "United States",
          f"got {cur.get('country')!r}")
    if pri:
        check(FAIL, "prior month same country", cur.get("country") == pri.get("country"),
              f"{cur.get('country')!r} vs {pri.get('country')!r} — never compare across filters")

    # --- Visibility Overview internal sum
    vo = cur.get("visibility_overview") or {}
    mbm = vo.get("mentions_by_model") or {}
    parts = {k: v for k, v in mbm.items() if k != "All Models" and v is not None}
    allm = mbm.get("All Models")
    if allm is not None and parts:
        check(WARN, "model bars sum to All Models bar", close(sum(parts.values()), allm),
              f"parts {sum(parts.values())} vs All Models {allm}")
        check(WARN, "All Models bar equals the Mentions card", close(allm, vo.get("mentions")),
              f"All Models {allm} vs card {vo.get('mentions')} "
              f"({(vo.get('mentions') or 0) - allm} unattributed) — happened in Jul 2026, ask Semrush")
    check(WARN, "topic count captured", vo.get("topics_total") is not None,
          "read it off the Performing Topics pagination")

    # --- Prompt Tracking totals
    pbm = cur.get("performance_by_model") or {}
    kpi = cur.get("ai_rankings_kpi") or {}
    if pbm and kpi.get("responses_with_mentions") is not None:
        s = sum(v.get("mentions") or 0 for v in pbm.values())
        check(FAIL, "per-model mentions sum to Responses with mentions",
              close(s, kpi["responses_with_mentions"]),
              f"{s} vs {kpi['responses_with_mentions']}")

    # --- prompt export against the panel
    if pr:
        check(FAIL, "prompt export has all three models", pr.get("model_count") == 3,
              f"got {pr.get('model_count')} — the CSV drops models silently, re-export")
        if pbm:
            alias = {"Google AI Overview": "Google AI Overview", "AI Overview": "Google AI Overview"}
            for m, v in (pr.get("by_model") or {}).items():
                panel = pbm.get(alias.get(m, m)) or pbm.get(m)
                if panel and panel.get("mentions") is not None:
                    check(WARN, f"export days match panel mentions — {m}",
                          close(v["days_current"], panel["mentions"]),
                          f"export {v['days_current']} vs panel {panel['mentions']} — "
                          "usually means the export window is not the calendar month")
        if kpi.get("responses_with_mentions") is not None:
            check(WARN, "export day total matches Responses with mentions",
                  close(pr.get("days_total_current"), kpi["responses_with_mentions"]),
                  f"{pr.get('days_total_current')} vs {kpi['responses_with_mentions']}")

    # --- Traffic
    tr = cur.get("traffic") or {}
    bym = {k: v for k, v in (tr.get("by_model") or {}).items() if v is not None}
    if bym and tr.get("traffic") is not None:
        check(WARN, "traffic by model sums to the Traffic card", close(sum(bym.values()), tr["traffic"], 2),
              f"{sum(bym.values())} vs {tr['traffic']}")
    if tr.get("by_host_total") is not None:
        check(WARN, "traffic by host total matches the Traffic card",
              close(tr["by_host_total"], tr.get("traffic")),
              f"{tr['by_host_total']} vs {tr.get('traffic')}")

    # --- deltas must be the tool's, and present
    missing = [k for k in ("traffic_delta", "conversions_delta", "bounce_rate_delta")
               if tr and k in tr and tr[k] is None]
    check(WARN, "traffic deltas captured from the cards", not missing, f"missing {missing}")

    # --- leaderboard share column
    lb = cur.get("brand_leaderboard") or []
    check(WARN, "brand leaderboard has share values",
          bool(lb) and all(r.get("share_of_voice") is not None for r in lb),
          "the share column is cut off on screen — use the panel's export arrow")

    # --- report
    width = max(len(l) for _, l, _ in results) + 2
    print(f"\nReconciliation — {cur.get('month')} ({cur.get('date_range')})\n")
    for lvl, label, detail in results:
        print(f"  [{lvl}] {label:<{width}}{detail}")
    fails = sum(1 for l, _, _ in results if l == FAIL)
    warns = sum(1 for l, _, _ in results if l == WARN)
    print(f"\n  {fails} fail, {warns} warn, {len(results)-fails-warns} ok")
    if fails:
        print("  Do not write slide copy until the failures are resolved.")
    for n in cur.get("notes") or []:
        print(f"  note: {n}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())

# Assets

**`example-slides-july-2026.md`** — a July 2026 deck for a fictional college, written to spec. Passes
`check_slide_copy.py` with no flags. Use it as the shape for every month: same 21 slides, same
HEAD / DECK / bullets / NOTES / IMAGE blocks.

**`workbook-template.xlsx`** — the metrics workbook, filled with **synthetic** data for the same fictional
client so the formulas and verdicts have something to chew on. Clear the month columns before real use. Tabs:

| Tab | What it does |
|---|---|
| Metrics | One row per metric, one column per month. MoM and YTD auto-calculate. |
| Deltas | Read-only. Do not type here. |
| Prompt Tracking | 75 prompt×model rows, position AND days per month. Set the current month in B3; the Verdict column then writes the gains and declines slides. |
| Product Rankings | Program-level mentions and share of voice. |
| Monthly Pull Checklist | Tick as you go. |
| Change Log | Platform changes, tool bugs, anything breaking comparability. |

Each month: add the new month's figures, change the current-month cell on Prompt Tracking, and read
the Verdict column. Don't re-derive movement by eye from the raw export.

The workbook reproduces the tool's own KPI cards — days-with-mention summed across all 75 rows equals
the "Responses with mentions" card exactly. If they disagree, the pull is wrong.

---
name: aeo-monthly-report
description: Build a monthly AEO/GEO client report from Semrush Enterprise AIO, either by hand or as an orchestrated run that fans transcription out to cheap subagents. Use whenever the user mentions the monthly AEO report, the AIO deck, or starts a new month's pull. Also use when they share Semrush Enterprise AIO screenshots or prompt-ranking CSVs, asks which screens to screenshot or which lists to export, asks to crop KPI cards, asks for slide copy for this deck, asks to audit a finished deck against its data, or asks to assemble the report with agents. Covers the pull checklist, the agent pipeline, the crop map, the workbook, the slide copy, and the verification gate — and enforces the deck's hard length limits on headlines and bullets.
---

# Monthly AEO report (Semrush Enterprise AIO)

Monthly client deck, delivered through an agency partner. Produced the first week of each month,
covering the **previous full calendar month**. ~4 hours production plus two 30-minute meetings.

> Built for a real engagement and anonymized for publication. The client here — **Cedar Valley
> Technical College** — is fictional, and every number in the examples and workbook is synthetic. The
> methodology, gates and tool gotchas are real.

## Rule zero

**Report what Semrush displays. Never compute a figure yourself.** Show pulled values and the tool's
own deltas. If a number isn't on a screen you can point at, it doesn't go in the deck — including
percentage changes.

Every serious error in the July 2026 cycle broke this rule: back-calculating a prior month from a
displayed percentage, reading a peak off a trend chart, comparing a worldwide pull to a US pull, and
quoting a figure from an older report whose filters nobody recorded.

**Set an explicit calendar month range on every screen** — the literal dates, not "Previous month."
**Country = United States, always.** Worldwide swung AI Visibility 12 points in a single month.

## Two ways to run

**Orchestrated** — the user supplies the screenshots and exports and asks for the pieces.
Follow `references/pipeline.md`. Cheap agents transcribe in parallel, scripts do the arithmetic, a
reconciliation gate runs before any copy is written, and an adversarial agent checks the copy against
the data afterwards.

**By hand** — the six steps below.

1. **Pull** — `references/pull-checklist.md`. Screenshots and exports with exact nav paths.
2. **Crop** — `scripts/crop_kpi_cards.py` + `references/crop-map.md`.
3. **Parse** — `scripts/parse_prompt_rankings.py` turns the CSV into verdicts. Never read the rows by eye.
4. **Reconcile** — `scripts/reconcile.py`. A FAIL stops everything.
5. **Write** — `references/slide-spec.md`. The length limits are not suggestions.
6. **Check** — `scripts/check_slide_copy.py`. Fix every flag.

Read `references/gotchas.md` before trusting any number. Three tool bugs and two metric traps in there
have each produced a wrong slide.

## The three rules that matter most

**1. Slides are small.** One head, one short paragraph, three or four short bullets. Everything else
goes in speaker notes. See `slide-spec.md` for limits and before/after examples.

**2. Always read position AND frequency together.** Average position alone lies — a prompt that stops
appearing on the days it ranked badly posts a large fake position gain. July 2026 had three.
`parse_prompt_rankings.py` checks frequency first for exactly this reason.

**3. Every visibility number names its model and its universe.** The KPI cards are model-filtered, and
AI Visibility (all topics) and Prompt Tracking (25 chosen prompts) are different universes that never
reconcile. AI Overviews can be the biggest source of all-topic mentions and the weakest of three
platforms on tracked prompts at the same time — both were true in July 2026.

## Files

| Path | What |
|---|---|
| `references/pipeline.md` | The orchestrated run: agents, models, phases, gates |
| `references/extraction-schema.md` | JSON contract between transcription agents and scripts |
| `references/pull-checklist.md` | Screens, filters, exports, in order |
| `references/crop-map.md` | Which KPI squares to cut and how to name them |
| `references/slide-spec.md` | Deck skeleton and the hard length limits |
| `references/gotchas.md` | Tool bugs, metric traps, sanity checks |
| `scripts/parse_prompt_rankings.py` | CSV → per-prompt verdicts + model summary |
| `scripts/reconcile.py` | Cross-checks the month's figures. The gate. |
| `scripts/merge_extracts.py` | Folds parallel agent fragments into one month file |
| `scripts/crop_kpi_cards.py` | Splits a KPI row into individual card images |
| `scripts/check_slide_copy.py` | Enforces head/deck/bullet limits and banned phrasing |
| `assets/themes.json` | The 25 tracked prompts mapped to six themes |
| `assets/example-slides-july-2026.md` | A full deck written to spec (fictional client) |
| `assets/workbook-template.xlsx` | The data layer (synthetic data) |

## Standing context

- **Client (example):** a two-year public technical college with dozens of programs across allied health and
  trades. Local, not national — regional queries are the whole game. Swap in your own client here.
- **Agency contact:** whoever owns the relationship. Their standing asks go in this section.
- **Tracked set:** 25 prompts × 3 models (ChatGPT, Gemini, Google AI Overviews) = 75 rows.
- **Deck:** Google Slides, agency template. **Never import a .pptx** — write copy for pasting.
- **Appendix:** each month's deck carries prior months. Split them into an archive deck.

## Deprioritised — do not re-propose

- **Reddit as a workstream.** A top-3 cited source, but the college only appears in its local city
  subreddit. A county college has no addressable national subreddit surface. One monitoring line only.
- **Sentiment tracking.** Negative sentiment runs at zero. One sentence, build nothing on it.

## Recurring open items

- **GA4 conversion event is broken.** It fires multiple times per session — one page recorded 47
  conversions on 26 sessions, another 11 on 19. Report as "conversion events" with a footnote and chase
  the retagging every month until it's fixed.
- Confirm whether the program-level pattern holds — institution mentions up while individual programs fall.
- Tag the prompt set by theme in AIO so clusters can be reported directly. `assets/themes.json` has the
  mapping ready.
- The prior reports (Mar–Jun 2026) are not comparable to each other — different windows, at least one
  worldwide pull. Re-pulling them on standard settings takes about an hour and would give a real trend
  line plus the year-to-date view the agency contact asked for.

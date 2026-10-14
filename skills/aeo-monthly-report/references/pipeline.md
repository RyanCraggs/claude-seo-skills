# Orchestrated run

One expensive orchestrator, several cheap agents, and scripts for anything deterministic. The user supplies
screenshots and exports; the run returns the pieces they assemble by hand into the Slides template.

## The division of labour, and why

| Work | Who | Why |
|---|---|---|
| Reading numbers off screenshots | **haiku agents, in parallel** | High volume, zero judgment. Vision tokens are the cost, so never do this in the orchestrator. |
| Parsing the prompt CSV, cropping cards, reconciling sums | **scripts** | Deterministic. An agent doing arithmetic is a defect waiting to happen. |
| Reading the prior deck and its comments | **haiku agent** | Fetch and list. No interpretation. |
| Deciding what any of it means | **orchestrator only** | Every bad slide last cycle came from interpretation running ahead of verified data. |
| Checking the copy against the data | **sonnet agent, adversarial** | Needs to reason about whether a claim is supported. Cheaper than the orchestrator, sharper than haiku. |

**Agents never interpret, never calculate, never write prose.** They return JSON. If an agent's output
contains a sentence about what a number means, the run is wrong.

---

## Phase 0 — Intake (orchestrator)

Confirm the inputs exist before spending anything. Required:

- Visibility Overview screenshots, **current and prior month**, Country = United States
- Prompt Tracking > Overview, one per model, current month (prior month if comparing panels)
- AI Rankings KPI row, Product Rankings, Query Fan-Outs
- Prompt Rankings CSV export
- Brand Leaderboard **export** (the on-screen share column is cut off)
- AI Referral Traffic (GA), current and prior month
- Landing Page Performance export

Missing anything, say which and stop. Do not proceed on partial inputs — that is how a worldwide pull
gets compared to a US pull.

## Phase 1 — Extract (5 haiku agents, one message, parallel)

Each writes `extracted/<month>.<section>.json`. Give every agent the schema at
`references/extraction-schema.md` and this instruction verbatim:

> You are transcribing a Semrush Enterprise AIO screen into JSON. Read values exactly as displayed.
> Do not calculate anything. Do not infer a bar's value from its length — if a bar has no printed
> number, write null and add a line to "notes". Convert percentages to fractions. Keep the sign
> Semrush shows on deltas even when it looks backwards. Return only JSON matching the schema. Do not
> describe, summarise or interpret anything.

| Agent | Model | Screens | Fills |
|---|---|---|---|
| `extract:visibility` | haiku | Visibility Overview, both months | `visibility_overview`, top-level month/country |
| `extract:prompts` | haiku | Prompt Tracking > Overview per model, Brand Leaderboard export, Most Cited Sources, Top Concepts | `prompt_tracking_overview`, `performance_by_model`, `brand_leaderboard`, `most_cited_sources`, `top_concepts` |
| `extract:rankings` | haiku | AI Rankings KPI row, Product Rankings, Query Fan-Outs | `ai_rankings_kpi`, `product_rankings`, `query_fanouts` |
| `extract:traffic` | haiku | AI Referral Traffic, both months, Landing Pages | `traffic`, `landing_pages` |
| `read:priordeck` | haiku | Prior month's deck in Drive | see below |

`read:priordeck` returns JSON only:

```json
{"open_comments": [{"author":"","text":"","slide":"","status":""}],
 "carried_recommendations": [{"text":"","first_appeared":"","status":""}],
 "prior_figures_cited": [{"slide":"","claim":""}]}
```

That last list matters — it catches slides quoting figures from older reports whose filters nobody
recorded.

## Phase 2 — Compute (scripts, no agents)

```bash
python scripts/merge_extracts.py extracted/<month>.*.json --out extracted/<month>.json
python scripts/parse_prompt_rankings.py <export>.csv --out prompts.json --themes assets/themes.json
python scripts/crop_kpi_cards.py <shot>.png --labels ... --prefix kpi_ALLMODELS
```

## Phase 3 — Reconcile (script, and it is a gate)

```bash
python scripts/reconcile.py extracted/<month>.json --prior extracted/<prior>.json --prompts prompts.json
```

**Any FAIL stops the run.** Report what failed and what pull would fix it. Do not write a word of copy
against unreconciled numbers. Warnings get carried into the deck's notes, not silently dropped.

## Phase 4 — Interpret and write (orchestrator only)

Now — and only now — read `prompts.json`, the reconciled extract, and the prior-deck fragment, and
write the slide copy to `references/slide-spec.md`. Rules that bite:

- Report what Semrush displays. Never compute a figure. See `gotchas.md`, rule zero.
- Position and frequency together, always.
- Name the model and the universe on every visibility figure.
- One head, one short paragraph, three or four short bullets.

Also draft replies to each open comment from the prior deck.

## Phase 5 — Verify the copy (sonnet agent, adversarial)

Hand it `extracted/<month>.json`, `prompts.json` and the draft copy. Prompt:

> You are auditing slide copy against its source data. For every number, date, percentage, comparison
> and named entity in the copy, find it in the supplied JSON. Return JSON only:
> `{"unsupported": [{"claim":"","slide":"","reason":""}], "contradictions": [...], "computed": [...]}`
> "computed" means any figure that appears to be derived rather than read from a card — a percentage
> change not present in the data, a prior-month absolute not in the prior extract, a number read off a
> chart. Do not rewrite anything. Do not comment on style. If a claim is supported, say nothing about it.

Fix everything it returns, then:

```bash
python scripts/check_slide_copy.py slides.md
```

## Phase 6 — Package

Hand back, and nothing else:

1. `slides-<month>.md` — copy, passing the length check
2. `crops/` — KPI cards and chart regions, named per `crop-map.md`
3. `AEO_Metrics.xlsx` — the workbook, updated
4. `reconcile-<month>.txt` — the gate output, warnings included
5. `comment-replies-<month>.md` — a draft reply per open comment
6. Any pull still outstanding, named

---

## Cost notes

- Vision dominates. Four transcription agents on haiku is the single biggest saving in the run.
- Never let the orchestrator read a screenshot it doesn't need to reason about.
- Don't spend a second agent re-transcribing to catch errors — `reconcile.py` catches most of them
  through broken sums, for free. Re-transcribe only a value that has no arithmetic check and looks off.
- If an extraction agent returns prose instead of JSON, re-run that one agent. Don't repair its output
  in the orchestrator; that's how interpretation leaks back in.

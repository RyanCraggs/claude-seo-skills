# Pull checklist — Semrush Enterprise AIO

Nav verified against a live Enterprise AIO instance, 8/2/26. **This is a different product from the
standard Semrush AI Visibility Toolkit.** There is no "Brand Performance" screen. The public Semrush
KB describes the other product and will send you looking for screens that don't exist.

## Rule zero

Report what Semrush displays. Never compute a figure yourself. Set an explicit calendar month range on
every screen — the literal dates, not "Previous month." Country = United States, always.

## Before you touch anything

- [ ] **Dismiss the Intercom chat widget** (bottom right). It sits on top of table data and cost a
      column two months running.
- [ ] **Click a neutral area of the page** before capturing. An active card renders with a blue outline.
- [ ] Confirm the scope in the top-left header. **AI Visibility is domain-scoped** (reads the agency
      account, domain filter `cedarvalleytech.example`). **Prompt Tracking and Traffic Analysis are
      project-scoped** (must read "<Agency> / <Client>").
- [ ] Duplicate last month's deck. Move the prior-month appendix into the archive deck.

## 1 · AI Visibility — the all-topic universe · ~20 min

**Path:** AI Visibility > Visibility Overview
**Filters:** `<client domain>` · All Models · **Country = United States** · the reporting month

> Country = Worldwide admits irrelevant markets. July read **22** on Worldwide and **34** on US.
> Always US.

| | Capture | Feeds |
|---|---|---|
| [ ] | Screenshot the 4 KPI cards — AI Visibility, Mentions, Monthly Audience, Cited Pages | Slide 7 |
| [ ] | Screenshot Mentions by Model bar chart | Slide 7 |
| [ ] | Screenshot the trend line (Mentions / Visibility / Audience toggle) | Slide 8 — the divergence visual |
| [ ] | Export **Performing Topics** (export arrow, top right of table) | Slide 7, topic count |
| [ ] | Export **Topic Opportunities** | Slide 18 — forward-looking recommendations |
| [ ] | Note the total topic count shown in pagination ("1–10 of 397") | Slide 8 |

**Optional:** AI Visibility > Competitor Research, if you want more than the Brand Leaderboard gives.

## 2 · Prompt Tracking — the 25 managed prompts · ~35 min

**Path:** Prompt Tracking > Overview
**Filters:** Previous month · Compare to: Preceding period

| | Capture | Feeds |
|---|---|---|
| [ ] | Screenshot the 6 KPI cards **once per model** — ChatGPT, Gemini, Google AI Overview. The cards are model-filtered. | Slides 9, 10, 17 |
| [ ] | Screenshot Performance by Model | Slide 9 |
| [ ] | Screenshot Brand Leaderboard — **read the share percentages off this screen** | Slide 17 |
| [ ] | Screenshot Most Cited Sources | Slide 17 |
| [ ] | Screenshot Top Concepts | Slide 17 |

**Path:** Prompt Tracking > Rankings > AI Rankings

| | Capture | Feeds |
|---|---|---|
| [ ] | Screenshot the 6 KPI cards with **all three models** selected | Slide 10 |
| [ ] | **Export Prompt Rankings** — the per-prompt table | Slides 11, 12, 13 |
| [ ] | Verify the export: check the Model column and row count. 25 × 3 models × 2 periods = **150 rows**. A 50-row ChatGPT-only file means the export dropped models — re-export. | — |
| [ ] | Screenshot / export **Product Rankings** — program-level mentions | Slide 14 |
| [ ] | Screenshot Query Fan-Outs | Slide 20 |
| [ ] | Check Tags Overview. If still empty, the prompt set is untagged — flag it. | Slide 20 |

## 3 · Traffic · ~15 min

**Path:** Traffic Analysis > AI Referral Traffic (GA)
**Filters:** Previous month · Compare to: Preceding period

> GA is already integrated here. **Do not build a manual GA4 segment** — it's ~20 minutes of wasted work.

| | Capture | Feeds |
|---|---|---|
| [ ] | Screenshot the 4 KPI cards — Traffic, Conversions, Revenue, Bounce Rate | Slide 15 |
| [ ] | Screenshot Traffic by Model and Traffic by Host | Slide 15 |
| [ ] | Screenshot Traffic over Time (Last 6 months, Month) — **crop the current month**, it renders as a cliff to zero | Slide 15 |
| [ ] | Export **Landing Page Performance (AI)** | Slide 16 |
| [ ] | Record the stated % changes. They let you back out the prior month's absolute values. | Workbook |

`AI Referral Traffic (Adobe)` and `Agent Analytics` were locked on the agency's plan. Ask the account
owner annually whether that's changed.

## 4 · Never use Share PDF

The PDF export **ignores the date filter** and returns a trailing 30 days from export time. Screenshot
the cards; use the per-widget export arrow for tables.

## Time budget

| Stage | Min |
|---|---|
| Setup | 5 |
| AI Visibility | 20 |
| Prompt Tracking | 35 |
| Traffic | 15 |
| Load + analyse | 45 |
| Write + build | 60 |
| QA | 20 |
| **Total** | **200 (3.3 hrs)** |

Excludes the two 30-minute meetings.

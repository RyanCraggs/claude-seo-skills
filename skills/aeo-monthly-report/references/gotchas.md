# Gotchas

Read before trusting any number. Each of these has already produced a wrong slide.

## Rule zero

**Report what Semrush displays. Never compute a figure yourself.** Show pulled values and the tool's own
deltas. If a number isn't on a screen you can point at, it doesn't go in the deck — including percentage
changes.

Set an explicit calendar month range on every screen — the literal dates, not "Previous month." Then the
value is the calendar month and the delta is Semrush's own, comparing it to the equal-length window
immediately before. Disclose that once on the reporting period slide:

> Period-over-period changes are Semrush's own, comparing each month to the equal-length window
> immediately before it.

**Country = United States, always.** Worldwide swung AI Visibility 12 points in a single month, and a
worldwide-vs-US comparison manufactured a double-digit decline that did not exist.

## Tool bugs

**Share PDF ignores the date filter.** With "Previous month" (Jul 1–31) selected on screen, the PDF
returned Jul 4 – Aug 2 — a trailing 30 days from export time. Brand mentioned 652 vs 631, domain cited
471 vs 452, Gemini mentions 738 vs 712. Never source a deck figure from the PDF export.

**Prompt Rankings CSV silently drops models.** With all three models selected and 149 rows paginating
on screen, the first export returned 50 ChatGPT-only rows. Check the Model column and the row count:
25 × 3 × 2 periods = 150.

**KPI cards are model-filtered.** Whatever model chip is set filters the whole card row. Prior decks
reported single blended-looking numbers with no model named.

**Country defaults to Worldwide,** which admits irrelevant markets — a Colombian row appeared in the US
topic table. July AI Visibility read 22 Worldwide, 34 US.

**The Intercom widget sits on table data.** Dismiss it before capturing.

**Traffic over Time shows the current month as a cliff to zero.** It's an incomplete month, not a crash.

## Metric traps

**Average position lies when read alone.** A prompt that stops appearing on its bad days posts a large
position "gain". July 2026:

| Prompt | Position | Days with mention |
|---|---|---|
| medical coding classes online | 2.86 → 1.00 | 13 → 3 |
| online associates degrees | 4.84 → 1.00 | 11 → 4 |

Both would have gone on a Notable Gains slide. Both are losses. **Always check days with mention first**
— the workbook's Verdict column does this automatically and labels them FREQUENCY LOSS.

**Position deltas display as positive when they improve.** The card reads "1.2 ▲ +0.2" for an
improvement from 1.4. Write "improved from 1.4 to 1.2" in the deck.

**AI Visibility is a 0–100 composite, not a percentage.** Don't append a % sign.

**AI Visibility and Prompt Tracking are different universes** and will never reconcile. Hundreds of
topics vs 25 chosen prompts.

**Conversions count GA4 key events, not applications.** One page recorded 47 conversions on 26
sessions. Site-wide, 74% of key events fire on a single page at 0.88 per view. Report as "conversion
events" with a footnote.

## Sanity checks

Run these before writing. If any fails, something is wrong with the pull.

- Days with mention summed across all 75 prompt×model rows **should equal the "Responses with mentions"
  KPI card exactly.** In July: 1,868 both ways.
- Per-model days totals should equal the Mentions column in Performance by Model. July: Gemini 738,
  ChatGPT 652, AI Overviews 478.
- Traffic by Model should sum to the Traffic card.
- Stated % changes should back-calculate to sensible prior-month absolutes.

## Platform changes on the record

| Date | Change | Effect |
|---|---|---|
| 2026-05-07 | Google stopped showing FAQ rich results. Google says unused structured data causes no problems and FAQPage remains valid Schema.org. | Keep the markup. It's now a machine-parseability play for AI extraction, not SERP real estate. |
| 2026-05-14 | AI Visibility database expanded to 32 countries; prompt DB past 261M. | Verify the AI Visibility denominator before reading a MoM move as performance. |
| 2026-06-26 | Semrush 2026 AI Visibility Index. ChatGPT cites ~15 sources per response, Gemini ~3. | Explains why AI Overviews drives mentions and ChatGPT drives clicks. |

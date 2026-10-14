# Keyword, Competitive & Content Gap Analysis

Three linked pieces, all export-driven (Claude interprets, doesn't pull the data).

## Inputs (from the user)

- **Keyword rankings export** (Ahrefs/Semrush): keyword, organic traffic, position, ranking URL. For established sites, filter to top positions (1–3) and/or SV > 1,000; for newer sites, top-10 is fine since there's less to work with.
- **Competitor table:** for each competitor — DR, referring domains, backlinks, ranking keywords, estimated organic traffic.
- **Content gap export:** keywords competitors rank for (top 10/top 100) that the client doesn't.
- The client's own **keyword strategy** doc, if they have one, to align recommendations.

If the user hasn't provided these yet, ask for them by name — this whole section depends on them.

## Keyword analysis

Open with the trend where you have it ("[Client] has seen strong growth in keywords ranking positions 1–3 over the past couple years" + `[SCREENSHOT: ranking growth]`), then interpret the top keywords.

Present a **Top 10 High-Traffic Keywords** table (keyword · organic traffic · position · URL) and pull out patterns:
- Branded vs. non-branded mix (branded share signals awareness/intent). Compute this explicitly rather than eyeballing it — and **recategorize brand misspellings** (dropped, doubled or swapped letters in the brand name) as branded intent, since they inflate the non-branded bucket and overstate genuine category reach. When one branded term dominates (a large share of all top-3 traffic), flag the concentration as both a strength and a risk.
- Utility terms (login, careers) — good for usability even if not new-patient intent.
- Category strengths worth doubling down on ("[Condition] is a core strength — more [condition] content is likely to win quickly").
- Awareness terms that can bridge into conversion content via internal linking.
- The genuine non-branded wins — even if low-traffic — often reveal a content "beachhead" (a theme where the blog already ranks) worth widening.

Link the full ranking report (user's spreadsheet).

## Competitive analysis

**First, curate the competitor set.** A Semrush "organic competitors" export (or the Ahrefs equivalent) is a keyword-overlap list, not a list of real business rivals. It will be padded with noise: drug-manufacturer sites, brand-name collisions (other companies sharing the client's name), foreign-market sites, review/aggregator sites, and unrelated domains that happen to share keywords. Filter down to the genuine, comparable business competitors before building the table — this is analyst judgment, not a copy-paste. Separate true head-to-head peers from much larger "category giants," and present the peer set as the main table with the giants noted as the tier to aim at over time.

**Keep the table columns fixed to the house standard** (same as the sample audits), with the client's row **bolded**:

| Name | DR | Ref. Domains | Backlinks | Keywords | Traffic |
|---|---|---|---|---|---|

Do **not** restructure this table to match whatever columns an export happens to have. If the provided export lacks some of these columns, keep the columns and fill the missing cells with `[TK: from Ahrefs]`, then request the export that has them. In particular, a **Semrush organic-competitors export has no DR, referring domains, or backlink counts** (those are Ahrefs metrics) — so those three columns will usually need an Ahrefs export to complete. Map the columns you do have: Keywords ← Organic Keywords, Traffic ← Organic Traffic.

**Get the client's own row on the same basis as the competitors.** The competitor export omits the seed domain, and a keyword *Positions* export is top-3-only — not comparable to competitors' all-position totals. Pull the client's total DR, referring domains, backlinks, Organic Keywords, and Organic Traffic from the Domain Overview so the bolded row is apples-to-apples. If only top-3 data is available, mark the cell with an asterisk and note the limitation rather than presenting it as total.

Then interpret honestly: where the client's authority (DR) sits relative to competitors, and whether keyword/traffic footprint lags sites of similar or lower authority. Note when raw traffic is inflated by branded search (see keyword analysis) and therefore overstates non-branded competitiveness. The usual read: solid authority, but a keyword-coverage and traffic gap that represents clear upside.

**Recommended next steps:**
- [ ] Continue building high-quality backlinks to close the authority gap.
- [ ] Go deeper in high-value condition/diagnosis/treatment (or product/use-case) topics to widen keyword coverage.

For newer sites, also analyze **shared referring domains** — DR 50+ DoFollow domains linking to ≥2 competitors but not the client — as concrete link targets. Present a table (referring domain · DR · monthly traffic · which competitors) and recommend prioritizing relevant, actionable ones (medical/industry publications, consumer health media) over hard-to-replicate ecosystem links.

## Content gap analysis

> One of the most effective ways to grow visibility is closing keyword "gaps" — terms competitors rank for but the client doesn't. These are missed high-intent opportunities.

Present a table of top gap keywords (keyword · US search volume · number of competitors ranking, or KD/intent/top competitor/position for newer sites). Recommend the specific pages/hubs to build to capture them, and internal-linking so Google connects them to the client's core topics. Link the full gap report.

Note that your own keyword research (for the editorial program) considers more terms than competitors currently rank for — the gap list is a floor, not a ceiling.

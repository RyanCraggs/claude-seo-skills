# Content Library Analysis (conditional)

Only for established sites with a real blog/content library. Three parts: decile methodology, the content-triage table, and the low-hanging-fruit update workflow.

## Inputs

- **From the user:** a per-article export with, ideally: URL, last-updated date, 12-month search clicks and impressions (Google Search Console), and count of high-value backlinks (DR 50+, from Ahrefs). Keyword rankings per article help too.
- Claude can't pull GSC or Ahrefs data — request the export. With it, Claude does the decile math and assigns recommended actions.

## Decile methodology

Divide the whole library into 10 groups by traffic: **Decile 1 = highest-performing, Decile 10 = lowest.** Deciles make a large library tractable — top deciles are pieces to protect and update, middle deciles have upside, bottom deciles surface redundancies and redirect candidates.

## The "Recommended Action" triage table

Assign every article an action from this logic, then report counts per category in a table (category · number of articles · qualifying criteria · steps to take):

| Category | Criteria | Steps |
|---|---|---|
| **redirect unless there's non-SEO value** | Deciles 8–10 AND no DR 50+ backlinks | Check for non-search value (social/email/referral performance, business-critical content). If none, redirect to the closest related article — ideally in the top 3 deciles to avoid future chains. |
| **check backlink profile** | Deciles 6–10 BUT has DR 50+ backlinks | Inspect the backlinks. If relevant to the article, keep. If not, treat like "redirect unless there's non-SEO value." |
| **look for consolidation opportunities** | Deciles 6–7 AND no DR 50+ backlinks | Identify each article's intent; look for a higher-performing article with similar intent to combine into. If none, decide keep vs. redirect on overall value. |
| **editorial call: keep or consolidate** | Deciles 4–5 AND no valuable backlinks | Judge value to the library and business. Keep if clearly valuable; otherwise look to consolidate. |
| **low-hanging fruit update** | Ranks position 5–20 for a keyword with 500+ SV | Top of the rolling update list — see below. |
| **keep and update — soonest** | Deciles 1–3 AND not updated in over a year | Rolling update list, after low-hanging fruit. |
| **keep and update — sooner** | Deciles 1–3 AND not updated in 6 months | After "soonest." |
| **keep and update — soon** | Deciles 1–3 AND not updated in 3 months | After "sooner." |
| **keep and update** | Deciles 1–3 BUT updated within 3 months | End of the rolling update list. |

Adjust category names/thresholds only if the client's data or goals call for it; otherwise keep them consistent across audits.

## Low-hanging-fruit update workflow

These are the fastest wins: articles ranking position 5–20 for a 500+ SV keyword — "OK content, not GREAT content" — sorted by organic traffic so the biggest movers go first.

Recommend this update process (as a checklist):

- [ ] **Study the top 3 organic results** (incognito) for each target keyword: article length, structure (headings, lists, tables), expertise signals (expert quotes, medical review), and anything else making them stronger. Aim to beat them.
- [ ] **Fix heading hierarchy** — one H1, then logical H2 › H3 › H4.
- [ ] **Review all links** — remove/replace broken or outdated ones; improve anchor text; add "…according to [source]." citations linked to authoritative external sources.
- [ ] **Optimize the Power Trio** — title near 60 chars, meta 155–160 chars, primary keyword early, secondary keywords in the meta, meta written for clicks.

## Topical authority tie-in

Report the category-level content distribution (e.g., how many articles per theme) and note where coverage is deep vs. thin. Recommend strong internal linking within each theme to build topic clusters — articles in a theme should link to each other with anchor text reflecting each one's distinct focus. (This connects to the E-E-A-T Authority section and the internal-linking work in `onpage.md`.)

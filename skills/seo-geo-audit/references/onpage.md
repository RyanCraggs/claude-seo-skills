# On-Page & Content Analysis

Two parts: the Power Trio (title tag, meta description, H1) and internal linking opportunities.

## The Power Trio

> The Title Tag, Meta Description, and H1 are the three most important on-page SEO elements. Google leans on them heavily to understand a page's topic and intent, which makes them among the most influential on-page signals.

### Inputs

- **From the user:** an export listing pages with missing/long/short titles, missing/long/short meta descriptions, and missing/duplicate/multiple H1s (Semrush, Screaming Frog).
- **Claude can spot-check live** by fetching a few key pages and reading their `<title>`, meta description, and H1.

### Thresholds

- **Title tag:** < 60 characters; primary keyword near the front; numbers/brackets/dates can lift CTR.
- **Meta description:** 130–160 characters (keep under ~155 to avoid truncation); include the primary keyword plus a secondary; write for clicks.
- **H1:** exactly one per page; unique; clearly describes the page topic.

### How to write it

For each of the three elements, report the issue types and counts, each with an "(aka …)" translation:

- Missing entirely → *not taking advantage of prime keyword real estate; leaves Google to guess*
- Too long → *likely truncated in results; reader may not grasp the page; lowers CTR*
- Too short → *not using available keyword real estate*

Then one fix block covering all three:

```
**How to fix:**

- [ ] Make sure every page's [element] is optimized for character length, keyword inclusion, and clarity to the searcher. Prioritize pages already generating organic traffic.
```

Link each issue's count to the details spreadsheet on established sites.

## Internal linking opportunities

> Adding relevant internal links alone can lift rankings and traffic.

### Method

Build the opportunity list by taking each page's top keywords by traffic, then finding mentions of those keywords on *other* pages that could link to them. Filter to keep it high-impact and manageable:

- keyword search volume > 1,000
- target page is already getting traffic
- target page ranks position ≤ 25

### Output

A short instruction plus a spreadsheet pointer:

```
**What to do:**

- [ ] Go to [the internal-linking tab of the spreadsheet]
- [ ] On each Source page, find the Keyword, and link it to the Target page
```

If no export exists, Claude can still identify a handful of opportunities live by fetching a few high-value pages and noting unlinked keyword mentions that point to relevant targets — framed as examples, not an exhaustive list.

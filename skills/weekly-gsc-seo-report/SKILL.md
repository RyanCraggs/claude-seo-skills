---
name: weekly-gsc-seo-report
description: Use when the user asks for the weekly SEO report, a WoW (week-over-week) Search Console update for the configured site, content-section movement, or "top movers" — or when a scheduled task asks for it. Pulls Google Search Console data via a GSC MCP server and writes a report on sitewide, /blog/, homepage and non-blog clicks and impressions WoW, a branded-demand check, the top 3 click and impression movers in /blog/, wins, and verified new pages, in a skeptical-analyst house voice. Can deliver to a Slack DM. GSC-only, with no AI-visibility data.
---

# Weekly GSC SEO Report

Builds a weekly client SEO report from Google Search Console. The site, buckets, branded terms and
delivery all live in `config.json`; the examples use a fictional brand, Northwind (`northwind.example`). It covers:
1. **Sitewide**: clicks and impressions, week over week.
2. **Blog bucket** (`/blog/`, all locale mirrors): the leading indicator for the content program, since that's where new content is published.
3. **Core** (everything else) = sitewide minus Blog.
4. **Homepage + branded demand**: on a brand-led site the homepage and branded queries drive most clicks, so most sitewide swings come from here, not from content.
5. **Top movers**: top 3 /blog/ pages by |click delta| and top 3 by |impression delta|, in either direction.
6. **Highlights**: wins, verified new pages, and patterns across locales or page clusters.

Before starting, read:
- `config.json`: site, thresholds, delivery target, and tool prefixes. Everything instance-specific lives there.
- `reference/gsc-queries.md`: exact call templates (Recipes A–F) and validation numbers.
- `reference/voice.md`: tone, structure, and the target sample.

If the GSC or Slack tools are deferred, load them with ToolSearch using the prefixes in `config.json`. If a prefix isn't found, search for the tool name (`get_advanced_search_analytics`, `slack_send_message`) and use whatever prefix comes back.

## Workflow

### 1. Settle the date windows
- Run `date` in the configured timezone to anchor today.
- **Default:** current_week = the most recent fully completed Monday–Sunday before today. prior_week = the 7 days before that.
- **If the user names dates, use them exactly**, even if they aren't Mon–Sun (e.g. Wed–Tue). Note in the subtitle that the windows follow the requested dates.
- State both ranges explicitly in the report.
- GSC needs about 1–2 days to fill in. If the requested end date is yesterday or today, warn that the last day may be incomplete.

### 2. Pull the data (all calls `data_state="all"`)
- Recipe A: sitewide daily rows for both weeks. Sum the 7 rows each.
- Recipe B: Blog daily rows for both weeks. Sum the 7 rows each.
- Recipe C: Blog page list for both weeks, `row_limit=150`, sorted by clicks.
- Recipe D: sitewide page list (top 25) for both weeks, to get homepage and other core page moves.
- Recipe E: sitewide top queries for both weeks, for the branded-demand check.
- Recipe F: verify any candidate "new" page before calling it new.
- Optional: query-level data for the single biggest /blog/ mover (Recipe C2). Small blogs often return few or no query rows because of anonymization. If so, say the query detail is anonymized and stop.

### 3. Compute
- WoW % for sitewide, Blog, Core, and Homepage (clicks and impressions). Homepage = sum of the root variants in `config.json` (https and http, www and non-www — whichever are present).
- Blog's share of the sitewide impression change, and Homepage's share of the sitewide click change.
- **Daily shape:** scan the daily rows for spikes (a day at 2x+ the window's median). A spike in either week distorts WoW. Name the spike days and give the baseline (e.g. "141 clicks on Sep 27 vs a ~27/day baseline").
- **Branded-demand check:** compare the branded queries (Recipe E rows containing any `branded_terms` from config) across weeks. If branded clicks moved a lot at a stable position (~1–1.5), say it's a demand swing, not a ranking change. Never guess why demand moved (press, launches, ads). Say GSC can't tell.
- **Top movers (Blog):** from the Recipe C join, top 3 by |click delta| and top 3 by |impression delta|. Write the direction explicitly ("−230 impressions"). Blog clicks are usually 0–2 per page. If no click delta reaches the noise floor, say "none worth listing; every /blog/ URL had 0–N clicks" instead of listing noise.
- **Locale clusters:** `/blog/` matches `/es/blog/`, `/fr/blog/`, `/de/blog/`, `/pt/blog/` too. When the same slug moves across locales, report it as one cluster with a per-locale breakdown (e.g. "EN 38, DE 44, ES 39, PT 15, FR 5").
- **Wins:** largest positive deltas. With click counts this small, judge wins by impressions plus position.
- **New pages:** Recipe F only. Check the slug over the 2 weeks before current_week. Note that a slug filter like `magnesium-before-bed` can also match older `/news/` articles; only count `/blog/` URLs.

### 4. Write the report
Follow `reference/voice.md`. Structure:

```
**{Site} — Weekly SEO Report ({Mon D – Mon D, YYYY})**
_Compared against {prior range}{; note if windows follow requested non-Mon–Sun dates}_

{1–3 sentence honest lead: the real story. Usually: is the sitewide move branded demand / homepage, or content? Call out spikes. Follow up on last week's watch item if known.}

• **Sitewide:** {clicks} clicks ({±%} WoW, from {prior}) and {impr} impressions ({±%}, from {prior})
• **Blog (/blog/, all locales):** ... impressions-as-signal framing, share of the sitewide impression move, any daily distortion
• **Core (non-blog):** ...
• **Homepage (https + http):** ... and its share of the sitewide click move

**Top movers by clicks (Blog)**: 3 bullets, or "none worth listing" with the reason
**Top movers by impressions (Blog)**: 3 bullets (path, ±delta, prior → current, avg position move)

**Highlights**: new pages (verified, with locale breakdown), slips worth watching, steady pages

_Caveat: {domain} pages with /blog/ in the URL, including locale mirrors; data_state=all; blog clicks are single-digit noise, impressions are the signal; GSC can't explain branded-demand swings; AI-visibility not included._
```
Aim for about 10–14 bullets and stay under Slack's 5,000-character limit. Use shortened paths (drop the scheme and domain). Keep small numbers exact; round large ones.

### 5. Deliver
- If `delivery.method` = `slack`, send the full report with `{slack prefix}slack_send_message`, `channel_id` = `delivery.slack_recipient_id`. Return the message link.
- If running interactively and the user hasn't asked to send, show the report in chat and ask before sending.
- If running as a scheduled task, or the user said "send it", send without asking.

### 6. Failure handling
- If GSC is unavailable or any pull fails, do NOT fabricate or estimate numbers. Send (or show) a short note that the report couldn't run, and why.
- If a call fails on permissions, say so plainly instead of working around it.
- If the Slack send fails, leave the full report in your final output so it isn't lost.

## Hard rules
- Never sum a page list to get a total.
- Never invent causes, AI Overview/ChatGPT citations, search volume, or DR.
- No hype adjectives. Write "X vs Y (±Z%)", never "down significantly".
- Small samples are noise. Blog clicks almost always are; say so instead of trending them.

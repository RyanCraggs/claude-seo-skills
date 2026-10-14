# GSC query recipes

All recipes use one tool: the GSC MCP server's `get_advanced_search_analytics`. It takes explicit `start_date`/`end_date`, `dimensions`, filters, and `sort_by`. The tool prefix depends on what the server is named in your install. In the original setup it was `mcp__gscServer__`. If tools are deferred, load them first, e.g. `ToolSearch: select:mcp__gscServer__get_advanced_search_analytics,mcp__gscServer__list_properties`.

All the recipes are independent, so run both weeks of each in parallel.

## Non-negotiable settings

1. **`data_state: "all"`** on every call. This matches the GSC dashboard. `"final"` lags 2–3 days and undercounts a recent week.
2. **Totals come from daily rows, never from a page list.** A `dimensions=page` list is capped and drops the zero-click long tail. Get totals with `dimensions=date` and sum the 7 rows.
3. **Bucket totals come from a filtered aggregate.** Apply the page filter AND `dimensions=date`, then sum the days.
4. **Homepage = combine root variants** (`https`/`http`, `www`/non-`www`). On some sites the `http://www.` variant still gets hundreds of impressions a week, so don't skip it.

## Recipe A — sitewide weekly total
Run for each week. Sum `clicks` and `impressions` across the 7 rows. Keep the rows for the spike check.
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date="YYYY-MM-DD", end_date="YYYY-MM-DD",
  dimensions="date", data_state="all", row_limit=10)
```

## Recipe B — Blog weekly total (/blog/)
Same as A, plus the bucket filter. Sum the 7 rows.
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=..., end_date=...,
  dimensions="date", data_state="all", row_limit=10,
  filter_dimension="page", filter_operator="contains", filter_expression="/blog/")
```
Core (non-blog) = Recipe A minus Recipe B, per week.

## Recipe C — Blog page list (movers, wins, new pages)
Run for BOTH weeks and join on page URL.
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=..., end_date=...,
  dimensions="page", data_state="all",
  filter_dimension="page", filter_operator="contains", filter_expression="/blog/",
  sort_by="clicks", sort_direction="descending", row_limit=150)
```
- A young blog is small (~20–25 URLs across locales), so the list is usually complete. Check `has_more`; if it's false, a URL missing from one week really had no impressions that week.
- **Click delta / impression delta** = current − prior per URL. Treat a URL missing from one week as 0 there.
- Group locale mirrors of the same slug when they move together.

## Recipe C2 — per-page queries (optional, biggest mover)
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=<prior start>, end_date=<current end>,
  dimensions="query,date", data_state="all",
  filter_dimension="page", filter_operator="equals", filter_expression="<full page URL>",
  sort_by="impressions", row_limit=60)
```
Blog pages here usually return only a handful of 1-impression rows because most queries are anonymized. If the rows don't account for the move, say "query detail is anonymized" rather than forcing a keyword story.

## Recipe D — sitewide page list (homepage + core moves)
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=..., end_date=...,
  dimensions="page", data_state="all", row_limit=25)
```
Use it for the homepage variants and to name which core pages (e.g. /shop, /news/ press releases) moved. Don't sum it for totals.

## Recipe E — sitewide top queries (branded-demand check)
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=..., end_date=...,
  dimensions="query", data_state="all", row_limit=15)
```
Branded = the query contains any `branded_terms` from config. Compare branded clicks and positions across weeks.

## Recipe F — verify a "new" page
Check the 14 days before current_week:
```
get_advanced_search_analytics(
  site_url="sc-domain:northwind.example", start_date=<current start − 14d>, end_date=<current start − 1d>,
  dimensions="page", data_state="all",
  filter_dimension="page", filter_operator="contains", filter_expression="<url slug>", row_limit=10)
```
It's new only if `/blog/` URLs with that slug had ≤ 5 impressions in total. The slug can match older `/news/` URLs (e.g. `magnesium-before-bed` matches `/news/northwind-launch-why-magnesium-before-bed-works`), so ignore non-`/blog/` rows.

## Validation reference (data_state=all)
Record two windows you've checked by hand in the GSC dashboard, so a fresh install can confirm it reproduces known numbers. Example rows (fictional Northwind data):

| Window | Sitewide clicks / impr | /blog/ clicks / impr | Homepage (https+http www) clicks |
|---|---|---|---|
| Sep 23–29, 2026 (Wed–Tue) | 418 / 4,126 | 3 / 914 | 321 |
| Sep 30 – Oct 6, 2026 (Wed–Tue) | 197 / 3,051 | 3 / 436 | 108 |

If a re-run doesn't match, check `data_state` first, then whether the account can see the same property. Numbers can shift slightly in the first few days after a window ends.

## Limits
GSC gives clicks, impressions, CTR, and position per query or page. It does NOT give AI Overview, ChatGPT, or Perplexity citations, search volume, or causes. Never fill those in.

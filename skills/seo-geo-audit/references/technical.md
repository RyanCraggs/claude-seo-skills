# Technical Analysis

Covers three things: (1) the health-score framing, (2) indexability & crawlability issues, and (3) Core Web Vitals / site speed. Includes the current-site vs. staging-site pattern for redesigns.

## Inputs

- **From the user (ask for these):** a crawl export (Semrush Site Audit, Screaming Frog, or Ahrefs) with the health score and issue counts; a PageSpeed Insights report or screenshots for mobile *and* desktop.
- **Claude can add live:** spot-check indexability by fetching key pages and checking for `noindex` meta tags, canonical tags, and robots directives — this is how a sitewide-noindex bug was caught on one redesign, so always check the homepage's `<head>` when a redesign or pre-launch site is involved.

## Section intro (template)

> This section evaluates how easily search engines can discover, access, and index [client]'s content. Strong crawlability ensures important pages are reachable; proper indexation ensures they can appear in results. Roadblocks here — orphan pages, broken links, redirect chains — limit visibility and performance.

## Health score

State the score out of 100 and one line on what it reflects: "The Health Score reflects the number of errors on the site that affect SEO." Then walk the specific issues. A score in the 80s is good — say so.

## Indexability & crawlability issues

Write each as its own `###` sub-section titled with the issue and instance count. Standard issue types and their fix logic:

**Orphan pages** — live pages with no internal links pointing to them.
- Fix: confirm each is needed; redirect the ones that aren't to the closest-intent page; for the rest, add contextual internal links with descriptive anchor text from relevant high-traffic areas, and add to nav if appropriate.

**Links to broken pages** — links pointing at 4XX pages. Split by link type (href link / redirect / sitemap URL) if the export does.
- Fix: find the anchor text on the source page; remove or repoint the link to a live page. For sitemap-sourced ones, investigate why an invalid URL is in the sitemap and remove it.

**Canonical points to 4XX** — canonical tag points at a broken page, so the instruction is ignored and the wrong version can get indexed.
- Fix: replace the canonical with the valid live URL that should be indexed.

**Page has links to redirect** — internal links point to a URL that redirects instead of the final destination. Works, but slows load and dilutes link equity.
- Fix: repoint each link to the final URL (source page → find anchor text → swap the target).

**Redirect chains** — links pointing to a redirect that redirects again. Same problem, worse.
- Fix: repoint to the final destination directly.

**Sitewide noindex (redesign/pre-launch)** — a `<meta name="robots" content="noindex">` on pages that should be indexed. On Framer/Webflow/staging setups this is often an accidental sitewide toggle ("discourage search engines") or a per-page hide, or a non-production publish state. This is a **Top Priority** — it silently erases rankings on the next crawl.
- Fix: locate the source (site settings toggle, per-page SEO setting, or publish state) and remove it on production pages.

**Thin content / orphan FAQ pages (redesign)** — one-sentence pages that duplicate content already on a main FAQ page. Google treats them as thin.
- Fix: unless a full long-form answer is planned, remove them from the site and sitemap.

**Images missing alt text** — hurts accessibility and image/search visibility and starves LLMs of image context.
- Fix: add a short (< 120-char) description in the CMS media/alt field.

## Core Web Vitals / site speed

Explain CWV in one pass, then report the numbers.

> Google looks at Core Web Vitals — three metrics that reflect real user experience: **LCP** (how long the largest element takes to load), **INP** (how fast the page responds to interaction), and **CLS** (how much elements shift while loading).

Report mobile and desktop separately. State clearly whether the site **passed or failed** the CWV field-data assessment on each, and give the Lighthouse performance scores. Mobile almost always lags desktop — say so and make mobile the priority.

Break out the contributing metrics against their goals:

| Metric | Goal | Why it matters |
|---|---|---|
| First Contentful Paint (FCP) | < 1.8s | when the first content appears |
| Largest Contentful Paint (LCP) | < 2.5s | when the biggest element finishes |
| Total Blocking Time (TBT) | < 200ms | how long scripts freeze the page |
| Speed Index | < 3.4s mobile / < 1.3s desktop | how fast content visually fills in |
| Cumulative Layout Shift (CLS) | low & stable | whether things jump around |

Then diagnose the usual two root causes and give fix blocks:

**1. The hero/LCP image is delaying render.**
- [ ] Remove lazy loading from the hero image
- [ ] Add `fetchpriority="high"` so the browser loads it first
- [ ] Compress/resize the image; serve WebP or AVIF; use responsive sizing so mobile doesn't load a desktop-sized image; preload it if above the fold
- [ ] Audit scripts that delay image rendering

**2. Too much JavaScript is blocking the main thread.**
- [ ] Audit front-end code, focusing on third-party scripts; remove anything unnecessary
- [ ] Defer or delay non-critical JS so it loads after primary content
- [ ] Limit redundant/overlapping third-party tools; replace heavy libraries with lighter ones
- [ ] Load critical CSS first; defer non-critical CSS/JS

If the site is on a builder with heavy client-side hydration (Framer, some Webflow setups), note honestly that platform overhead caps how much the dev team can fix without migrating — and that LLMs generally don't execute JS when crawling, so hydration-dependent content can be invisible to AI search. Frame a possible CMS migration as a consideration for teams aiming to be best-in-class on performance, not a mandate.

Always link the full PageSpeed Insights report and leave `[SCREENSHOT: PageSpeed mobile]` / `[SCREENSHOT: PageSpeed desktop]` placeholders.

## Current-site vs. staging-site pattern (redesigns only)

When a new site is in staging, split the technical analysis into two headed sub-sections:

- **Technical Analysis – Current Site:** protect what's ranking; flag anything actively harmful (the noindex bug lives here).
- **Technical Analysis – New Site (in staging):** launch-readiness gaps to fix *before* going live — orphan pages, missing H1s, missing alt text, slow pages, missing schema. Emphasize mapping old ranking URLs to new-site pages so authority survives the launch, and running a fresh crawl after launch since staging→production can change URLs and settings.

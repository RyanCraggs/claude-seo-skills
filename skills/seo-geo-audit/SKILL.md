---
name: seo-geo-audit
description: Use whenever the user wants to create, write, or assemble an SEO or GEO audit — or any single section of one — in a client-ready, partner-style format. Triggers include "write an SEO audit", "GEO audit", "audit this site", or requests to build a specific audit section (technical, Core Web Vitals, schema, on-page / Power Trio, E-E-A-T, keywords, competitive analysis, content gap, AI/LLM visibility, CRO). Also triggers when the user hands over Semrush / Ahrefs / Screaming Frog / PageSpeed exports or screenshots and wants them turned into audit narrative. Use it even if the user just says "audit" plus a URL, or drops keyword/competitor spreadsheets and asks for help writing them up.
---

# SEO/GEO Audit

Assemble client-ready SEO/GEO audits in a consistent house style. There is **one method** with **branching logic**: the same backbone of sections runs on every site, and a handful of optional sections switch on or off depending on the site's maturity and situation. An established content site (say, a health publisher with ~300 articles) gets the blog decile analysis and internal linking work; a pre-launch or redesigning site (say, a device brand rebuilding on a staging site) gets the current-vs-staging split, CRO, and Google Business Profile.

The audit is part assessment, part instruction manual: every issue is explained in plain English, tied to *why it matters*, and paired with a checklist of concrete fixes.

## First, always

**Read `references/voice-and-formatting.md` before writing any prose.** It governs the entire deliverable — the tone, the "(aka …)" explainers, the "How to fix:" blocks, the checkbox action items, and the Google Docs import conventions. The audit is worthless if it reads like a generic SEO report instead of a partner-grade audit.

## Division of labor

Some sections are built from data only the user can pull; others Claude assesses live. Default behavior:

- **Fetch and assess live** (`web_fetch` the site): schema, E-E-A-T signals (author bios, editorial policy, review bylines, references, About page), on-page spot-checks, and reputation signals (social profiles, review platforms, Google Business Profile). Do this by default — the user has confirmed they want real assessment, not just transcription.
- **Ask the user for exports/screenshots**: health score, crawl errors (orphans, broken links, redirects), Core Web Vitals numbers, keyword rankings, competitor tables, backlink counts, and AI-visibility data (Gumshoe / Semrush AI / custom-GPT). Claude cannot pull these (no Semrush/Ahrefs API). When a section needs them and they're absent, ask for the specific export rather than guessing or fabricating numbers.

Never invent metrics. If a number isn't provided and can't be fetched, leave a clearly marked placeholder (see voice file) and tell the user what to supply.

## Workflow

1. **Intake.** Run the intake questions below (skip any the user has already answered in conversation). Their answers set the branch and the optional-section switches.
2. **Plan the section list.** Use the branching table to decide which sections are in and in what order. Confirm the plan with the user if the scope is a full audit; skip confirmation if they asked for a single section.
3. **Build each section.** Open that section's reference file, gather inputs (fetch live or request exports), and write it to the section template and house voice.
4. **Assemble.** Stitch sections in order with cover, table of contents, and sign-off. Output as Markdown that imports cleanly into Google Docs (see assembly rules).

For a single-section request, do steps 1 (lightly) → 3 only.

## Intake questions

Ask these at the start of a full audit (as tappable options where possible). Most gate an optional section:

1. **Client name + primary URL(s)?** (and any staging/new-site URL)
2. **Site maturity:** pre-launch / newly launched / established with a content library?
3. **Redesign or migration in progress?** (a staging or replatformed site to compare against the live one)
4. **Industry / is this YMYL?** (health, finance, legal → stricter E-E-A-T bar and Medical* schema types)
5. **Content library size?** (roughly how many blog/articles — gates the decile analysis and internal linking)
6. **Local or physical presence?** (gates the Google Business Profile section)
7. **Key competitors?** (for competitive analysis and content gap)
8. **Which data can you export vs. want me to fetch live?**
9. **Your name, title + email** for the sign-off.

## Branching logic

| Section | Reference file | Included when |
|---|---|---|
| Executive summary | (assembled last, see below) | Always |
| Technical: indexability & crawlability + health score | `technical.md` | Always |
| Technical: Core Web Vitals / speed | `technical.md` | Always |
| Current-site vs. staging-site split | `technical.md` | Redesign/migration in progress |
| Schema | `schema.md` | Always |
| On-page Power Trio + internal linking | `onpage.md` | Always (internal linking needs enough pages) |
| Content library (decile analysis, triage, low-hanging fruit) | `content-library.md` | Established site with a real content library |
| E-E-A-T (Experience, Authority, Backlinks, Trust, Reputation) | `eeat.md` | Always |
| Google Business Profile | `eeat.md` | Local/physical presence |
| Keyword analysis | `keywords-competitive.md` | Always |
| Competitive analysis + content gap | `keywords-competitive.md` | Always (needs competitor list) |
| GEO / AI visibility | `geo.md` | Always |
| CRO recommendations | `cro.md` | Pre-launch/redesign, or when conversion is a stated concern |
| Prioritized recommendations roadmap | `voice-and-formatting.md` | Always (front for established sites, back for pre-launch) |

## Section index (what each file covers)

- **`technical.md`** — health score framing, indexability/crawlability issues (orphan pages, broken links, canonical→4XX, links-to-redirects, redirect chains), and Core Web Vitals (FCP/LCP/TBT/CLS/Speed Index) with mobile-vs-desktop framing and fix checklists. Includes the current-vs-staging pattern.
- **`schema.md`** — how to fetch and check live schema, plus recommendations by site type (Organization/WebSite/WebPage baseline; MedicalOrganization/MedicalWebPage for health; Product for e-commerce; BreadcrumbList, ProfilePage/Person).
- **`onpage.md`** — the Power Trio (title tag, meta description, H1) with character thresholds and issue-count framing, plus internal linking opportunities.
- **`content-library.md`** — decile methodology, the "recommended action" triage table, and the low-hanging-fruit update workflow.
- **`eeat.md`** — Experience & Expertise, Authority (topical + backlinks), Trust, Reputation, and Google Business Profile, each with a checklist of what "good" looks like.
- **`keywords-competitive.md`** — top-keyword tables, competitive comparison table, and content-gap methodology.
- **`geo.md`** — AI Overviews, LLM/AI-search visibility, the two-mechanism model (get mentioned / get cited), and strategic implications.
- **`cro.md`** — conversion recommendations framed as "what competitors are doing → why it works → what you can do."

## Global threshold cheat-sheet

Consistent across audits (details in the section files):

- Title tag: < 60 characters, keyword near the front
- Meta description: 130–160 characters (keep under ~155 to avoid truncation)
- H1: exactly one per page, unique, describes the topic
- FCP goal: < 1.8s · LCP goal: < 2.5s · TBT goal: < 200ms · CLS: low/stable
- Speed Index goal: < 3.4s mobile, < 1.3s desktop · Server response: < 200ms
- Image alt text: < 120 characters
- "High-value backlink" = from a site with Domain Rating (DR) 50+
- Internal-linking filter: keyword SV > 1,000, target page getting traffic and ranking position ≤ 25
- Low-hanging-fruit content: ranks position 5–20 for a keyword with 500+ SV
- Content deciles: split the library into 10 traffic-ranked groups; deciles 1–3 protect/update, 8–10 redirect/consolidate

## Assembly & output

- **Order:** cover → table of contents → executive summary → (roadmap here for established sites) → technical → schema → on-page → content library → E-E-A-T → keywords → competitive/gap → GEO → CRO → (Key Next Steps / roadmap here for pre-launch sites) → sign-off.
- **Full depth, not compressed.** Assembling the full audit means concatenating each section at its full standalone depth — never a shortened version to save space. A finished audit runs long (the samples are 30–40+ pages) because each section itemizes exhaustively. If the assembled draft feels thin, the fix is more complete coverage per section (more itemized issues, fuller "what's working" lists, detailed "how to improve" sub-steps, exemplars), not tighter writing. See the depth benchmarks in the voice file.
- **Executive summary is written last**, distilling one "Key Finding" line per major section, plus a short Purpose paragraph noting the YMYL/E-E-A-T stakes where relevant.
- **Format:** output Markdown structured for a clean Google Docs import — real headings, real tables, real links, and GitHub-style checkboxes (`- [ ]`) for action items. Save to a `.md` file and present it. Offer a `.docx` version (use the `docx` skill) if the user wants a locked-down Drive deliverable.
- **Details spreadsheet:** for established sites with large issue counts, reference "the details spreadsheet" for granular row-level data (the user maintains this) rather than dumping hundreds of rows into the doc.
- **Images:** the source audits embed screenshots (PageSpeed, dashboards, leaderboards). Claude can't create these — leave a labeled placeholder like `[SCREENSHOT: PageSpeed mobile report]` where one belongs so the user drops it in.

## Composing with other skills

For page-level depth beyond the site-wide audit, point the user to (or invoke) these skills from the open-source [SuperSEO Skills](https://github.com/inhouseseo/superseo-skills) pack, if installed: `eeat-audit` for a 1–10 score on a representative page, `page-audit` for a full single-page workup, `content-brief` / `keyword-deep-dive` for follow-on content planning. The audit names the opportunity; those skills execute it.

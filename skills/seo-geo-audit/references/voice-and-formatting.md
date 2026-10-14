# Voice & Formatting

This is the house style. Read it before writing any section. It is what separates a partner-grade audit from a generic SEO report.

## The voice in one line

Expert but warm — a knowledgeable partner explaining things clearly, never talking down, always translating jargon and always saying *why* something matters before saying *what to do*.

## Core conventions

**Tight prose, exhaustive coverage — these are different things, and both are required.** Concision governs *sentences*: make the point, translate jargon once, don't restate an idea two ways, keep praise to a line, no throat-clearing. It does **not** mean covering less. The sample audits are long (30–40+ pages) because they *itemize exhaustively* — every issue gets its own subsection with instance counts, every "what's already working" list is complete, every "how to improve" block has detailed sub-steps, and trust/authority sections include a "what good looks like" exemplar. Length comes from completeness, not padding. When assembling a full audit, do **not** compress a section below its full standalone depth to save space — a full audit is the sum of full-depth sections. If a section feels short, the fix is more itemized coverage, not more words per point.

**Depth benchmarks (match the samples).** E-E-A-T is typically the longest section (Experience, Authority w/ topical + backlinks, Trust w/ an exemplar, Reputation w/ social + review platforms + an analysis paragraph). Technical, Core Web Vitals, the content-library decile analysis, and GEO are the other heavy sections. On-page itemizes each issue type with counts. Treat the original sample audits (30–40+ pages each) as the depth bar for each section.

**Explain the "why" first.** Every issue opens with what the thing is and why it affects SEO/the reader, then moves to the fix. Never list a problem without its stakes.

> Orphan pages are live pages that have no internal links pointing to them, meaning users and search engines cannot navigate to them through the site. This prevents the pages from being discovered or indexed, limiting their SEO value.

**Use "(aka …)" plain-English translations.** Right after a technical count or term, add a parenthetical that says what it means for a normal human. Multiple in a row is fine.

> **65 pages are missing the title tag entirely** (aka not taking advantage of prime keyword real estate and helping the reader understand what the page is about)

**"How to fix:" / "How to improve:" blocks.** After describing an issue, give a labeled block of checkbox action items. Steps are imperative and specific enough to act on without a follow-up question.

```
**How to fix:**

- [ ] Review the list of pages and confirm all are active and needed.
- [ ] For active pages, add contextual internal links with descriptive anchor text from relevant, high-traffic areas.
```

**Instance counts as headers.** Name each issue with its count, e.g. `### Orphan pages (44 instances)`. For established sites, link the count to the row-level detail in the details spreadsheet.

**Reinforce what's working.** These audits are not scolds. Call out strengths genuinely ("This is great!", "[Client]'s backlink profile is one of its strongest competitive advantages"). For mature sites, many recommendations are simply "continue what you're already doing" — frame those as `(Continue to)…`.

**Prioritize by traffic/impact.** When telling the user what to do first, anchor on organic traffic and impact ("Prioritize updating pages that are generating organic traffic").

**Comparison and data tables.** Use tables for competitive comparisons, keyword lists, content-triage categories, and anything with parallel structure. Bold the client's own row in competitor tables.

**Section intros.** Each major section opens with 1–3 sentences on what it evaluates and why it matters, before diving into findings.

## Checkbox / status conventions

- Open action item: `- [ ]`
- Completed item (when tracking progress on a living doc): `- [x] ~~struck-through text~~`
- The prioritized roadmap uses these so the client can check items off over time.

## The Prioritized Recommendations Roadmap

A checklist grouped by priority tier, with each item linking to the section that explains it. Established sites get it near the top (right after the executive summary); pre-launch sites get an equivalent "Key Next Steps and Top Priorities" list at the end (usually a numbered 1–5 sequence rather than tiers).

Tiers, in order:

- **Top Priority** — indexing/crawl blockers, broken things, LCP, anything actively losing rankings or traffic
- **High Priority** — Power Trio fixes, low-hanging-fruit content, schema errors, key internal linking, core trust gaps
- **Medium Priority** — enhancements like additional schema types, PR/authority pushes
- **Nice to Have** — small polish items (styling, optional schema)
- **Keep It Going!** — things the client is already doing well and should continue (backlinks, reviews, social, content)

Each roadmap item: a short imperative, the section link in parentheses, and a spreadsheet link if applicable.

## Executive summary format

Written last. Two parts:

1. **Purpose** — 2–3 sentences on what the audit set out to do and the stakes. For YMYL sites, name the E-E-A-T / Your-Money-or-Your-Life context explicitly.
2. **Key Findings** — one bolded lead-in per major section (Technical, On-Page/Content, E-E-A-T, Competitive, GEO) followed by a one-sentence takeaway. Keep it skimmable and honest — lead with the good news where it's real, flag the real risks plainly.

## Cover, ToC, sign-off

- **Cover:** title "SEO/GEO Audit" (or "SEO Audit" if no GEO section), "for [client]", the date, and a `[LOGO placeholder]`.
- **Table of contents:** list the included sections with links. In Google Docs the user can regenerate a live ToC; provide the heading structure so it builds correctly.
- **Sign-off:** end with your name, title, and email under a "Questions?" heading.

## Google Docs import notes

The deliverable is a Google Doc, produced as Markdown the user imports (File → Open → upload .md, or paste into Docs). To survive the import:

- Use ATX headings (`#`, `##`, `###`) for real Docs heading styles and a working ToC.
- Use real Markdown tables (pipes) — they convert to Docs tables.
- Use `- [ ]` checkboxes — they import as Docs checklist items.
- Use inline `[text](url)` links.
- Avoid HTML, nested callout boxes, and exotic formatting that won't survive conversion.

## Placeholders

Never fabricate a metric. When data is missing:

- Numbers the user must supply: `[TK: mobile LCP from PageSpeed]`
- Screenshots the user must drop in: `[SCREENSHOT: Gumshoe leaderboard]`
- Client-specific detail to confirm: `[CONFIRM: number of active articles]`

Tell the user, in your chat message (not buried in the doc), exactly which placeholders remain and what to supply.

## What to avoid

- Generic, un-translated jargon with no "why."
- Problem lists with no fix blocks.
- Fabricated or hand-waved numbers.
- A scolding tone — the client is a partner, and much of what they're doing is already working.
- Over-formatting the chat response about the audit; the *audit* is richly formatted, but conversation about it stays natural.

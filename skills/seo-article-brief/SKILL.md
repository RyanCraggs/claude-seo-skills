---
name: seo-article-brief
description: >
  Produce an SEO article brief from a research document (keyword deep dive + content brief) and the user's brief template. Use this skill whenever the user shares a research file and asks to produce a brief, fill out the brief template, or create a content brief for a client article. Triggers include "write the brief", "fill out the template", "do the brief for [keyword]", "here's the research", or any time a research document and a client name are provided together. Always use this skill before attempting to write a brief from scratch.
---

# SEO Article Brief

You are acting as a senior SEO strategist. Your job is to take a research document (produced by the keyword deep dive and content brief skills) and produce a complete, copy-paste-ready article brief that fits the user's brief template. The output goes directly into the chat — not a Word doc or artifact — so the user can copy sections into their own template.

---

## Step 1: Before Writing

### Build the link inventory before you write anything

The linking sections are the part of this brief that goes wrong most often, and the cause is almost always the same: guessing a slug that looks plausible instead of reading one that exists. A slug like `/blog/cetirizine-for-hives` is exactly the kind of thing a language model invents with total confidence — it's well-formed, it's topically correct, and it 404s. Writers paste it into a draft, and nobody catches it until QA.

So do the retrieval first, as its own discrete step, before drafting any part of the brief. You are assembling two lists — live pages and planned pages — and every URL you later put in a table has to come from one of them.

**1. Pull the live URL inventory from the sitemap, not from Google.**

Fetch the client's sitemap and read the URLs out of it.

| Client type | Sitemap | Linkable content paths |
| :-- | :-- | :-- |
| **Flat sitemap** (e.g. a large health publisher, ~500+ URLs) | `/sitemap.xml` — one file | `/blog/{slug}` plus condition and treatment pages (`/allergies`, `/asthma`, treatment pages like `/allergies/immunotherapy`) |
| **Sitemap index** (e.g. a multi-locale brand) | `/sitemap.xml` is an index; follow it to the locale child you're briefing (`sitemap_en-US.xml`) and ignore the others | `/blog/{slug}`, `/news/{slug}` (press), plus any hub section such as `/learn/{topic}` |
| Any new client | Try `/sitemap.xml`; if it returns an index, follow the children. Note the real content path before writing a single URL | — |

Patterns worth knowing before you start:

*Brand-name and ingredient-name duplicates.* Health clients often publish the same mechanism under both brand and ingredient names — separate pages on whether an antihistamine causes drowsiness, one per brand name. When you're briefing at the ingredient level, check whether brand-level pages already cover it, and say so in Strategy if the new page would cannibalize them.

*Young sites.* A client with a handful of live posts and more shipped briefs than that lives mostly in the planned-page inventory from Drive, and a thin Internal Links table is the honest output rather than a failure. Evidence or hub pages are strong link-out targets for physiological claims; press pages (`/news/{slug}`) are for credibility links, not topical clustering. Some CMSs put literal parentheses in slugs (`/news/author-(2025)-title-of-the-study`); copy them exactly.

Prefer this over a `site:` search. A `site:` query returns a sampled, ranked, partial slice of the index — you'll see 10–20 results when the client has 250 pages, with no way to know which 230 you missed. The sitemap is the client's own declaration of every URL they publish. It's one fetch, it's complete, and the strings are exact — which matters, because real slugs are frequently ugly in ways you would never guess. `/blog/cetirizine-vs.-loratadine` has a period in it. `/blog/allergies-vs-a-cold-what%E2%80%99s-the-difference` has a URL-encoded curly apostrophe. Copy them verbatim; do not tidy them up.

Note the client's canonical content path while you're in there — check both the sitemap and the `rel=canonical` tag on a post.

Some sites also answer on a second path — `/blogs/{slug}` alongside `/blog/{slug}` — and that's the trap: the duplicate returns a real article with a 200, so a spot-check makes it look fine. It's a non-canonical path whose canonical tag points back at `/blog/`. An internal link to it isn't broken — it's worse than broken in a quiet way, because nothing visibly fails while you hand equity to a URL Google has been told to ignore. Use the path the sitemap declares. If a client's site answers on two paths, the sitemap is the tiebreaker, not whichever one a search result or a manual check happened to surface.

Scan the inventory for pages topically adjacent to the keyword: same medication, same condition, same body system, same patient question. Pull more candidates than you need — you'll pick the best five per section, and having 15 to choose from is what makes those five genuinely relevant rather than merely real.

Do this in two or three passes with different search terms, not one. A sitemap of ~500+ URLs is big enough that a fetch tool summarizing it can quietly drop entries — in testing, a first pass on the condition name missed a brand-name page about it entirely, and only a second pass on a bare substring of the core noun surfaced it. Vary the angle each pass: the condition, then the medication (brand *and* ingredient names both, since the client publishes under both), then a bare substring of the core noun. Overlapping passes are how you find the page that would otherwise have looked like it didn't exist — and a page you fail to find is indistinguishable, in the output, from a page that isn't there.

**2. Pull the planned-page inventory from shipped briefs in Drive.**

Articles you have already briefed but not yet published won't appear in the sitemap. They're still among the most valuable internal links available, because you control both ends and can plan the relationship before either page exists. Search Drive for the client's brief docs — they follow the pattern `[Topic] - Article Brief - [Client]`:

```
title contains 'Article Brief' and title contains '[Client]'
```

A client's briefs live across several Drive folders, so search by title pattern rather than pinning a folder ID. Open any brief that looks topically related and read its **URL** and **Headline (H1)** fields — that gives you the planned slug and the anchor context. If a brief's URL field is empty or still says TK, treat the destination as TK rather than inventing a slug for it.

**3. Cross-reference performance data if the user shared it.**

If there's a GSC or analytics export in play, use it to rank the candidates from step 1 — a high-impression page makes a better crosslink source than an equally relevant page nobody visits. This is prioritization, not discovery: it can reorder URLs already in your inventory, never add new ones.

**4. Harvest the anchor text by reading the crosslink destinations.**

The sitemap proves a URL exists. It says nothing about whether the words you want to link on are on the page. Those are two different claims, and steps 1–3 only cover the first.

Here's the distinction that drives everything in this step. An **Internal Links** anchor is a *specification* for copy the writer is about to author — you can propose the phrasing, because the sentence doesn't exist yet. A **Post-Publish Crosslinking** anchor is copy that already exists on a live page — you can only *quote* it. Telling a client to link the phrase "non-drowsy antihistamine" on a page where that phrase does not appear isn't a suggestion, it's an instruction that can't be followed. Whoever picks it up will either stall or quietly invent something, and the second outcome is worse.

So shortlist 6–8 crosslink candidates from the inventory and fetch each one. Pull two things from every page: the verbatim sentence containing the phrase you want to anchor, and the heading of the section it sits in.

Ask for exact quotes, not an assessment. A fetch tool asked "does this page discuss drowsiness?" will say yes about a page that mentions it once in a trademark disclaimer in the footer. Ask it to quote every sentence containing the target words and to state explicitly if there are none — the explicit negative is the useful answer, because it's the one that saves you from writing a row you can't support.

Expect a meaningful share to fail, and budget fetches accordingly. In testing on one brief, five crosslink candidates were shortlisted off the sitemap on topical relevance alone: two turned out to contain **zero** mentions of the target topic anywhere on the page, and two more had only the bare phrase sitting in a bulleted list. Meanwhile the single best row on the finished table — a page whose body already contained the exact target keyword, in a relevant sentence, unlinked — hadn't been shortlisted at all and only surfaced on a second sweep. Fetch more candidates than you need, for exactly the same reason you pull more sitemap URLs than you need.

While you're in these pages, read enough to sanity-check the *relevance* claims you're about to make about them, not just the anchor. A live page can be topically adjacent by slug and wrong by content — a treatment page written entirely for adults is a poor destination for an article aimed at parents of young children, and you only learn that by opening it. If a destination carries specific numbers the new article will also cite (a dosing range, a duration), note them: the brief should tell the writer to reuse the live page's figures rather than introduce a second, contradictory set.

### Flag legal or compliance issues
If the keyword involves an unapproved drug or compound, check whether the client can legally prescribe or facilitate access to it before writing the CTA and Desired Customer Action sections. For clients that prescribe:
- Substances the FDA restricts from compounding cannot be offered — do not imply the client facilitates access
- Off-label uses of approved medications are generally fine to prescribe — frame CTAs around provider consultation
- When in doubt, add a Legal Note to the Strategy section and flag for legal review before publication

### Note word count constraints
Check whether the client caps word count. If the research recommends a higher count (e.g., 5,000+ for a pillar page), note this in the brief and explain that the article functions as a cluster hub supported by spoke pages — adjust the outline accordingly.

---

## Step 2: Output Format Rules

The brief is output as plain text in the chat. The user copies it into their own Google Doc brief template. Do not create a Word doc or artifact unless explicitly asked.

### Meta table
Output as a markdown table with two columns: field name (bold) and value.

### Secondary keywords
Always output as a bulleted list — never pipe-separated or comma-separated inline.

### Competitor Analysis
**List** the competitor URLs as a bulleted list with hyperlinks first, then output a **markdown table** with these exact columns:
- Competitor (name + publish date + word count if known)
- Pros — things to also do
- Cons — how to be better

Do not use sub-bullets or prose in this section. Keep each cell concise.

### Article Structure — Content Body
This is the most important formatting section. Follow these rules exactly:

1. Each top-level item is a `- [ ]` checkbox
2. **H2s and H3s get their own standalone checkbox line** — do not combine the heading with its description on the same line
3. Immediately below each H2 or H3 checkbox, add indented `- [ ]` sub-bullets with brief guidance (1–2 lines each)
4. H3s are indented one level below their parent H2
5. Featured snippet targets, content gap flags, and PAA notes go on a separate italic line immediately after the H2 checkbox — not inside a sub-bullet
6. Tables suggested in the outline are rendered inline as markdown tables inside the relevant H2 block
7. The outline is a brief, not the article — keep sub-bullets tight. No paragraphs.

Example format:
```
- [ ] **H2: How Cetirizine Is Dosed for Seasonal Allergies**
   - [ ] Adults and children 6+: 5–10mg once daily, per the label
   - [ ] Start at 5mg if drowsiness is a concern; cite the label, not a blog
   - [ ] Don't exceed the labeled daily maximum

- [ ] **H2: Side Effects**
   - [ ] **H3: Common Side Effects**
      - [ ] Drowsiness, dry mouth, fatigue
      - [ ] Compare drowsiness rates against loratadine and fexofenadine
```

### Linking sections

Both tables are built entirely from the inventory you assembled in Step 1. Nothing goes in either table that you didn't read out of a sitemap or a shipped brief.

- **Internal Links to Include**: 5 rows max. Pages the new article should link OUT to. Markdown table: URL | Suggested anchor text. The anchor cell should name the anchor phrase *and* the section it belongs in — "cetirizine" on its own is not actionable; "'cetirizine' — in the comparison table H2 and the dosing H2" is.
- **Post-Publish Crosslinking**: 5 rows max. Existing pages that should link IN to the new article once it's live. Markdown table: URL to Go Into | Anchor Text to Link / Notes.
- Do not use catalog or index pages (e.g. a treatments listing) as crosslink destinations — they rarely link out to individual blog posts.

**The two tables have different anchor rules, and collapsing them is the failure mode this section exists to prevent.**

Internal Links anchors are specifications — the writer authors that sentence, so propose the phrasing and the section.

Post-Publish Crosslinking anchors are quotations. Each row needs three things: the anchor phrase in bold, the destination section heading, and the verbatim sentence it sits in.

| URL to Go Into | Anchor Text to Link / Notes |
| :-- | :-- |
| /blog/do-antihistamines-make-you-drowsy | Anchor: **"loratadine"** — in the H3 "Which Antihistamines Are Least Sedating?", in the existing sentence *"Newer options like loratadine are far less likely to make you sleepy."* |

The quoted sentence is what makes the row executable: whoever implements it can Ctrl-F the page and land on the exact spot. Without it you've handed them a scavenger hunt.

Rank crosslink rows by anchor quality, strongest first:

1. The target keyword itself already appears on the page, in a relevant sentence, unlinked. The best row you can get — the link is a one-word edit.
2. A closely related phrase appears in a relevant section.
3. Only the bare concept appears, as a list item or a single clause. Passes equity but reads thin — say so, and note that expanding it to a full clause first would improve it.

**Verification gate — two claims, two checks. Run both before you output either table.**

*Existence.* For every row in both tables, name the source: which sitemap line, or which brief doc. If you can't name one, the row is a guess.

*Anchorability.* For every Post-Publish Crosslinking row, name the verbatim sentence you're anchoring on and the page you read it from. A row whose anchor you cannot quote does not ship — not reworded, not softened, cut.

**When a good destination has no anchorable text, don't force it and don't quietly drop it.** Move it to a short list under the crosslinking table headed *"Requires new copy before a link can exist,"* and say what's missing.

That list is frequently the most valuable thing in the section. When a client's main side-effects hub turns out to contain no mention of a side effect they have four separate articles about, you haven't found a bad crosslink — you've found an orphaning problem the brief wasn't scoped to look for, and you found it by opening pages nobody else opens. Present it as a separate work item with the specific fix (add a short section, then link), not as a crosslink row dressed up with a caveat.

**URL format.** Both tables use the full live path — e.g. `/blog/{slug}` — because the writer copies these straight into a draft and a bare slug forces them to reconstruct the prefix. This differs from the brief's own **URL** field in the meta table, which stays a bare slug (`/cetirizine-dosage`); the client's CMS supplies the prefix there. That asymmetry is intentional, not an inconsistency to normalize.

**Mark every row with its provenance.** Each URL is in one of three states, and the writer needs to know which:

| State | How to write it |
| :-- | :-- |
| Live now | `/blog/{slug}` — plain, no annotation |
| Briefed, not yet published | `/blog/{slug}` *(planned — from the [topic] brief)* |
| Neither | Don't include it |

The parenthetical on planned links is doing real work: it tells the writer the link will 404 today, and it tells whoever does QA that the row is expected rather than broken.

**Under-fill rather than pad.** Four sourced, anchorable links beat five where one is invented. A single dead link — or a live link with a fabricated anchor — costs more trust than a thin section does, because it makes the writer doubt the other four. When a topic genuinely has fewer than five relevant neighbors on the site, say so in a line under the table ("only three relevant existing pages — this is an underbuilt cluster") rather than padding to five. That observation is useful strategic information; a fabricated fifth row is not.

### Graphics
Always suggest:
- At least one 🆚 Table if a comparison is natural to the topic
- At least one 🖼️ Infographic
- Describe what each contains and where it's embedded

---

## Step 3: Client Brand Language Note

Most health clients have standing brand and legal rules. Store each client's version and append it to the end of the Strategy section on every brief for that client. A typical version for a client that prescribes:

*Note on [Client] brand language: Do not use brand names for medications — use ingredient names throughout. Do not describe providers as "[Client] providers" — they work with [Client]. Avoid language implying efficacy guarantees; frame efficacy claims as "the [study] found that..." per [Client] legal guidelines.*

For YMYL topics or unapproved substances, add a separate Legal Note below the brand language note (see Step 1 above).

---

## Step 4: Full Brief Structure (in order)

Output these sections in this exact order:

1. **Meta table** (H1, target keyword, secondary keywords as bullets, URL, title tag, meta description, author TK, expert TK, reviewer TK, word count)
2. **Audience**
   - Who is this for? (2–3 specific groups, not generic)
   - Takeaways and Next Steps (bulleted list)
   - Desired Customer Action (bulleted list; mind legal constraints)
3. **Competitor Analysis**
   - Bulleted URL list
   - Comparison table
4. **Strategy** (bulleted list of differentiation points; brand/legal note at end)
5. **Article Structure — Content Body** (full outline with checkboxes; see formatting rules above)
6. **Linking and Graphics**
   - Internal Links table
   - Suggested Graphics checklist
   - Post-Publish Crosslinking table
7. Do NOT include the "For New Writers / Reminders" boilerplate — that lives in the user's template and does not need to be reproduced here

---

## Step 5: Tone and Judgment Reminders

- This is a senior-level deliverable. Write with the same editorial judgment as an experienced SEO strategist, not a template-filler.
- If the research flags a keyword as Hard or not worth pursuing as a standalone page, say so clearly in the brief (the word count/difficulty note or strategy section is the right place).
- If the research reveals compliance concerns the user may not have flagged, raise them before writing — don't bury them in a footnote.
- The linking sections are the most commonly underdeveloped part of briefs, and the retrieval in Step 1 is what fixes that. Doing it properly costs one sitemap fetch, one Drive search, and six to eight page fetches — cheap enough that there's no reason to skip it and reason from memory instead. Five real, relevant, sourced links per section is the standard; not five generic ones, and never a plausible-looking guess.
- A crosslink row is two claims, not one: that the page exists, and that the words are on it. The sitemap only settles the first. If you find yourself writing an anchor phrase you have not read on the destination page, stop — you are writing an instruction nobody can execute.
- If the inventory turns up an obvious cluster gap — a topic that clearly should exist on the site and doesn't — flag it in the Strategy section. You've just read the client's entire URL list, which puts you in a better position to spot that than anyone reading the brief will be.
- Featured snippet targets and AIO citation angles should be called out explicitly in the outline, not just mentioned in the strategy section.
- Comparison tables in the outline should be rendered as actual markdown tables, not described.

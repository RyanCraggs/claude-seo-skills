---
name: keyword-research-sheet
description: >
  Use this skill whenever the user is building a keyword research
  spreadsheet for a client. Triggers on phrases like "start keyword research," "build the KW sheet,"
  "add keywords to the list," "write notes for the sheet," "expand the keyword list," or any time
  materials are shared (intake form, Semrush exports, GSC data) and the goal is to produce or update
  a client-facing keyword research Excel file. The skill covers the full workflow in two phases —
  pre-kickoff (15–20 keywords) and post-kickoff expansion (35–40 keywords including refresh candidates)
  — and governs spreadsheet format, column structure, color conventions, font, SERP research via Chrome,
  Google Trends lookups, and Notes column content standards.
---

# Keyword Research Sheet

This skill governs how to build the [Client] Keyword Research spreadsheet from scratch,
step by step, across two phases. Follow it every time a new client keyword research project begins.

---

## Phase 1 Overview: Pre-Kickoff (15–20 Keywords)

Materials arrive in steps — do not wait for everything before starting.

### Step 1 — Ingest Client Materials

The following will be shared over the course of the project. Process each as it arrives:

| Material | What to extract |
|---|---|
| Client intake form | Goals (traffic vs. conversion), primary audience, known content areas, competitor names, legal/brand guardrails, existing content notes |
| Internal sales/kickoff notes | Strategic opportunity areas, categories to prioritize, client budget/growth signals, upsell flags |
| Semrush: Gap keywords (vs. competitors) | Keywords competitors rank for that the client doesn't — filter to KD ≤ 55 and Vol ≥ 500 |
| Semrush: Client top keywords | Current ranking keywords — identify underperformers (high impressions, low CTR, pos 5–20) for later refresh candidates |
| Semrush: Organic positions export | Current ranking keywords with position, volume, KD, and URL — cross-reference against existing pages |
| GSC data (queries + pages) | Impressions, clicks, CTR, and position for existing pages — identify refresh opportunities |

**Cross-reference before recommending any keyword:** Check whether the client already has a page targeting that topic. Use the GSC pages export and, when in doubt, fetch the live URL in Chrome to confirm.

---

### Step 2 — Identify Seed Topics and Build the Keyword Magic List

After reviewing the materials, generate a list of seed topics/keywords spanning:
- Categories the client named in the intake form
- Areas where competitors rank but the client has zero coverage (from gap analysis)
- Side effects / symptom / treatment question formats (these consistently outperform for health clients)
- Branded vs. generic variants — prefer generic where the client has no landing page
- New categories the client is entering (especially post-rebrand or expansion)

Share this seed list with the user. The user will manually run the seeds through Semrush Keyword Magic Tool and return a CSV export. Do not proceed to Step 3 until that export is received.

---

### Step 3 — Select 15–20 Keywords for Pre-Kickoff Sheet

From the Keyword Magic Tool export, select 15–20 keywords using this logic:

**Selection criteria:**
- Prefer KD ≤ 55 for a mid-authority site; KD ≤ 45 for early months
- Include at least one keyword per strategic category identified in Step 2 (breadth > depth at this stage)
- Do not include multiple entry points to the same cluster unless that cluster is a named client priority — use the preliminary list to gauge client interest across categories, not to go deep on one
- Avoid keywords where the client already has a strong existing page (check GSC and live pages)
- Prioritize proven format matches: for health clients, side effects + treatment + dosage articles consistently outperform general explainers
- Flag KD 55–65 keywords as "stretch" targets with a note in the sheet — include 2–3 per batch to show strategic ambition, not as first articles

**Validation before finalizing:**
1. For each keyword, check whether a live page exists at the client's domain targeting it
2. If a page exists, remove the keyword from the new-articles list and flag it as a refresh candidate instead
3. Confirm the URL actually targets the keyword (not just mentions it contextually)

---

### Step 4 — Research Each Keyword

For each keyword in the final 15–20 list, do the following before writing the Notes column:

**SERP research (required — use Chrome MCP):**
- Navigate to `https://www.google.com/search?q=[keyword]&gl=us&hl=en`
- Record the top 3–5 organic results: domain, page title, approximate publish/update date if visible
- Note: which result types appear (featured snippet, PAA, video carousel, shopping, Reddit/forum discussions)
- Note: whether any direct competitors appear (named competitors from intake form)
- Note: the general competitive level of the SERP (major institutions, small clinic blogs, consumer health publishers, telehealth brands)

**Google Trends (required — use Chrome MCP):**
- Navigate to `https://trends.google.com/trends/explore?q=[url-encoded-keyword]&geo=US`
- Note the 5-year trend direction: rising, declining, seasonal, stable, spiked recently
- Note any seasonal peaks (month/season) if applicable
- Note if there's a recent spike that suggests a news hook or regulatory event

**Secondary keywords:**
- From the Keyword Magic Tool export, identify 3–5 related keywords that cluster around the same intent
- Prefer secondaries with KD ≤ 45 and volume ≥ 200 that are not already in the sheet as primary keywords
- Include volume and KD for each secondary in the Notes

---

### Step 5 — Build the Spreadsheet

See **Spreadsheet Specification** section below for full column, formatting, and color details.

Build the sheet with all 15–20 keywords. Save as:
`[Client Name] Keyword Research.xlsx`

---

## Phase 2 Overview: Post-Kickoff Expansion (35–40 Keywords)

After the kickoff meeting and client feedback:

### Step 6 — Expand to 35–40 Keywords

The expanded sheet should include:
- All approved or retained keywords from Phase 1
- **New article keywords** to fill any categories client confirmed interest in
- **Refresh/Overhaul candidates** for existing underperforming pages (see criteria below)

Target ratio: **2–3 new articles per 1–2 refreshes** per monthly production cycle.

**Refresh candidate criteria (from GSC data):**
- High impressions (>200K/yr) with low CTR (<1.5%) — title/meta failure
- Ranking position 5–15 with meaningful volume — content depth or format gap
- Ranking position 1–5 but very low CTR — featured snippet structure missing or title not click-worthy
- Outdated clinical data, broken internal links, or framing that contradicts current product offering

**For each refresh candidate:**
1. Fetch the live page in Chrome using `get_page_text`
2. Read the actual content — do not guess at what's there
3. Identify the specific, concrete reason for underperformance based on what's actually on the page
4. Write Notes grounded in what you found, not in assumptions
5. Fill column I (URL) with the exact current live URL

**Additional Semrush export:** The user will share an expanded Keyword Magic Tool export after the kickoff. Use this to source the new article additions. Apply the same cross-referencing and validation steps from Phase 1.

---

## Spreadsheet Specification

### File Naming
`[Client Name] Keyword Research.xlsx`

Sheet tab naming convention: use the date (e.g., `6/26`) for the original and `Copy of [date]` for the working version. Keep the original tab intact; work in the copy.

---

### Font
**Manrope, 10pt, Normal weight** — apply to all body cells. Headers use **Manrope, 10pt, Bold, White (#FFFFFF)**.

---

### Columns (in order)

| Col | Header | Type | Notes |
|---|---|---|---|
| A | Keyword / Topic | Text | Primary keyword |
| B | Potential Title | Text | Proposed article title |
| C | Cluster/Topic | Text | Category label (see color conventions) |
| D | Difficulty | Number | KD from Semrush — apply color scale (see below) |
| E | Search Volume | Text | Monthly volume with comma formatting |
| F | Search Traffic Potential | Text | Estimated cluster traffic (e.g., "~33,100" or "~280,000 (cluster)") |
| G | Production Type | Dropdown | Options: New, Overhaul, Refresh |
| H | Funnel Stage | Dropdown | Options: top, middle, bottom |
| I | URL (if already exists) | Text | Live URL for refresh/overhaul rows; "N/A" for new articles |
| J | Lookup | Dropdown | Options: 🔍 SERP, 🔍 GSC — indicates primary research source for the Notes |
| K | Strategy Notes | Text (long) | See Notes Content Standard below |
| L | [Client] Team Feedback | Text | Leave blank — for the client team's use |
| M | Client Approved? | Text | Leave blank — filled after client review |

**Note:** Column names should match the client's approved sheet exactly. The columns above are a house default; adjust header names for future clients as needed but preserve the column order and types.

---

### Column D — Keyword Difficulty Color Scale

Apply cell background fill based on KD value. Use these exact hex codes:

| KD Range | Fill Color | Hex |
|---|---|---|
| 0–20 | Green | `#D5F5E3` |
| 21–35 | Light green / Yellow-green | `#EAFAF1` blending to `#FEF9E7` |
| 36–50 | Yellow | `#FEF9E7` |
| 51–65 | Orange | `#FAD7A0` |
| 66–80 | Red-orange | `#F5CBA7` |
| 81–100 | Red | `#F1948A` |

Implementation: set fill using openpyxl `PatternFill` based on the numeric KD value. Apply to the KD cell only, not the entire row.

---

### Row Color Conventions (by Cluster/Topic)

Apply a light background fill to the entire row based on the Cluster/Topic value. These are illustrative for a health client — adapt cluster names and colors to fit each new client's categories, but maintain the principle of visually grouping by category:

| Cluster | Fill Hex |
|---|---|
| Cluster A (e.g. Allergies) | `#E8F4FD` (light blue) |
| Cluster B (e.g. Sleep) | `#FEF9E7` (light yellow) |
| Cluster C (e.g. Skin) | `#F9EBEA` (light pink) |
| Cluster D (e.g. Mental health) | `#FDEDEC` (light red-pink) |
| Cluster E (e.g. Heart health) | `#EAFAF1` (light green) |
| Side Effects (non-drug-named) | `#F5EEF8` (light purple) |
| Nutrition | `#FDF2E9` (light orange) |

**For Overhaul/Refresh rows:** apply a slightly darker shade of the same cluster color to visually distinguish them from new article rows. If openpyxl doesn't have a built-in darkening function, use a predefined darker hex per cluster stored in a lookup dictionary.

---

### Header Row
- Background: `#1A1A2E` (very dark navy)
- Font: White, Bold, 10pt Manrope
- Alignment: Center, vertical center, wrap text
- Row height: 40

---

### Body Rows
- Font: Manrope 10pt Normal
- Alignment: vertical top, wrap text
- No fixed row height — let rows auto-expand to content
- Apply border: thin `#D9D9D9` on all sides of each cell

---

### Freeze Panes
Freeze row 1 (header row). Set `ws.freeze_panes = "A2"`.

---

### Column Widths (approximate — adjust to content)

| Col | Width |
|---|---|
| A | 26 |
| B | 48 |
| C | 22 |
| D | 11 |
| E | 13 |
| F | 24 |
| G | 13 |
| H | 11 |
| I | 40 |
| J | 9 |
| K | 90 |
| L | 18 |
| M | 14 |

---

## Strategy Notes Content Standard

The Notes column (K) is the most important column in the sheet. It must be grounded in real research — not guessed. Every note should follow this structure:

### For New Article Keywords:

**Opening line:** State the strategic case in one sentence — volume, KD, opportunity gap, and why it's a fit for this client. Include any direct competitor presence on the SERP.

**SERP section:**
`SERP: [Result 1 — domain, title, date if visible], [Result 2], [Result 3], [Result 4 if notable], [Result 5 if notable]. [Note any SERP features — featured snippet, video carousel, PAA, shopping, Reddit/forum]. [Note any named client competitors in the SERP.]`

**Trends/Seasonality:**
`Trends/Seasonality: [Direction — rising/declining/stable/seasonal/spiked]. [Peak month/season if applicable]. [News hook if relevant.]`

**Secondaries:**
`Secondaries: [keyword 1] ([volume] vol, KD [kd]), [keyword 2] ([volume] vol, KD [kd]), [keyword 3] ([volume] vol, KD [kd])`

**Note:** For stretch keywords (KD 55+), add a flag at the start: "Stretch keyword (KD [X]) —" and explain why it's worth including despite the difficulty.

---

### For Overhaul/Refresh Keywords:

**Opening line:** `OVERHAUL.` or `REFRESH.` (use OVERHAUL for pages needing substantial rewrite; REFRESH for pages needing targeted additions/fixes). Follow with GSC performance data: `GSC: [clicks] clicks | [impressions] impressions | [CTR]% CTR | pos [position].`

**Diagnosis:** Based on reading the actual live page in Chrome, state specifically what is wrong. Examples of what to look for:
- Title/meta is passive, generic, or doesn't match searcher query language
- Content contradicts patient/user experience (especially dangerous for health content)
- Clinical data is outdated — cite the year of the most recent study used
- Dosage or chart information exists only as an image without descriptive alt text or filename
- Missing PAA sections for high-volume follow-up questions
- CTA routes to wrong destination (e.g., generic page instead of eligibility flow)
- Article only covers one dimension of the searcher's intent (e.g., deficiency but not supplementation)
- Article discourages readers from the client's own product offerings
- Drug name misspelled or medical claims framed in ways that may undermine trust

**Priority actions:** Numbered list of specific, concrete actions (3–6 items). Frame these as actions for the writer/editor, not abstract observations.

**Do not include:**
- Internal notes about cannibalization checks (flag separately to the EP/team lead)
- Suggestions to check with legal unless the legal note is directly relevant to what a writer needs to know before drafting

---

## Quality Checks Before Delivering Any Sheet

Before presenting the file:

1. Every keyword has been cross-checked — no duplicate coverage of an existing strong page
2. SERP research was done live in Chrome for every keyword — no guessed or assumed SERP composition
3. Google Trends was checked for every keyword — no "check Google Trends" placeholder left in the Notes
4. All refresh rows have column I filled with a verified live URL
5. Column D colors reflect the correct KD range
6. No fixed row heights — rows auto-expand
7. Font is Manrope 10pt throughout
8. The file is named correctly and saved to `/mnt/user-data/outputs/`

---

## Phase Triggers and Conversation Flow

The materials arrive in steps. Here is how to handle each handoff:

| What arrives | What to do |
|---|---|
| Intake form + internal notes only | Extract strategic priorities, identify category opportunities, ask user to confirm before running any research |
| Semrush gap/positions CSVs | Cross-reference for coverage gaps and underperforming pages; generate seed topic list; share with user before proceeding |
| Keyword Magic Tool export (Phase 1) | Select 15–20 keywords; validate against existing pages; research each via Chrome; build the sheet |
| Kickoff meeting feedback | Note which categories client confirmed interest in; identify which keywords to keep, cut, or deprioritize |
| Expanded Keyword Magic Tool export (Phase 2) | Add new article keywords for confirmed categories; identify refresh candidates from GSC; expand sheet to 35–40 rows |

Always confirm the current phase with the user before building or expanding the sheet. Never build the full sheet before the Keyword Magic Tool export has been received and validated.

---
name: refresh-sprint
description: "Run a multi-page content refresh sprint end to end: scope contract from the SOW, per-URL fact base, cannibalization map, title/H1/H2/meta recommendations, verification gates, and building or QAing the client refresh sheet. Use when the user starts or continues a refresh sprint for any client, shares target URLs plus an SOW, or asks to build, apply, or fact-check a refresh sprint sheet."
---

# Content refresh sprint

Takes N existing URLs and produces a per-URL instruction sheet a writer executes without further research: proposed title, H1, H2 stack, meta, rationale, risk, figure checks. The deliverable is the sheet, not the content.

The sprint fails in one direction: **instructions that assume content the page does not have.** A recommendation that reads well but can't be executed from the existing page is worse than none — the writer either invents the content (scope breach, factual risk) or silently skips it. Every gate below exists to catch that.

## Gates — never carry a known failure forward

1. Scope contract signed off before any page work (Phase 0)
2. Every row has a fact file before any recommendation is written (Phase 2)
3. Zero mechanical failures from the check script (Phase 6)
4. Every H2-stack line provenance-tagged and grounded, or cut to Stage 2 (Phase 7)
5. Export diff 100% clean before telling the client it's done (Phase 10)

## Run layout

One working dir per sprint. Everything is a file — no phase holds state in context.

```
scope.md              scope contract, agreed with the user in Phase 0
rows.json            row -> {url, metrics, current title/h1/h2s}
pagefacts/{row}.json headings + figures + locations, from live pages
querymap.json        query -> {leader, owner, flag}; primary/secondary per row
recs/{row}.json      proposed title/h1/h2_stack/meta/why/risk
checks.json          mechanical check output
verdicts/{row}.json  adversarial verification per rec line
```

## Model assignment

You (the orchestrating model) keep: scope contract, query ownership, cross-column consistency, sheet writes, client report. Fan out to Sonnet: page extraction, recommendation drafting, verification. Haiku is fine for pure extraction if pages are simple. Mechanical checks are a script, never agent judgment. Send all parallel agents in one message.

---

## Phase 0 — Scope contract (you, with the user)

Get the SOW. Do not start without it. Extract and write `scope.md`:

- **In scope** — the exact deliverable list (e.g. TL;DR, key takeaways, FAQ, SEO/GEO updates, trust block, byline/last-reviewed)
- **Out of scope** — usually: new facts, new tables, new examples, new templates, new sections. Name them explicitly.
- **Figure updates** — allowed from which primary sources? (A finance client: the relevant government agencies. A health client: CDC/NIH/peer-reviewed + clinical review.) This list is client-specific and is the only licence to change a number.
- **Stage 2 destination** — where does out-of-scope work go? Everything you cut needs a named home or the client thinks you missed it.
- **Review chain** — who signs off on claims? YMYL clients need a named clinical/legal reviewer column and a tighter no-new-facts rule.

Confirm the in/out list with the user before Phase 1. This is the cheapest step and the one every later cell gets tested against.

## Phase 1 — Row set and metrics

From GSC (12mo) + Semrush, build `rows.json`: url, impressions, clicks, primary keyword candidates with position/volume/KD, **Click Potential**, top queries with impr/clicks/pos, unique internal inlinks, current title/H1/H2-1/H2-2.

Inlink count matters more than it looks: a page with 200+ inlinks is a hub whose URL must not change and whose authority is the real asset, even when its own traffic is poor.

## Phase 2 — Fact base (fan out, Sonnet)

The highest-leverage phase. One extraction pass per URL, reused by every later phase. Batch 3–5 URLs per agent.

Prompt template:

> Fetch <URLS>. For each, return JSON only, no prose:
> `{url, last_updated, word_count, headings:[{level, text, order}], figures:[{value, claim, stated_year|null, location, sourced:bool}], examples:[...], tables:[...], internal_links:[...], faq:[{q,a}]}`
> `location` is one of body | faq | schema | table | widget | h2-1-block. **Check all four:** rendered body, collapsed/accordion FAQ blocks, JSON-LD structured data, and any calculator or estimator widget. Content inside a collapsed FAQ or in JSON-LD is on the page — record it with its location, do not omit it.
> `figures` = every number a reader could act on: dollar amounts, percentages, timeframes, counts, form numbers, limits. Record the year the page states, not the year you infer. `sourced` = whether the page names a source.
> `examples` = sample answers, templates, worked examples that already exist verbatim.
> Do not evaluate or recommend. Extract only.

**Gate:** one fact file per row, non-empty headings and figures arrays. A page whose figures array is empty either genuinely has none (rare) or the fetch failed — re-check by hand before proceeding.

## Phase 3 — Query map and ownership (you)

For every query above a volume floor across the whole set:

- **leader** = the URL with most clicks / best position today
- **owner** = the URL you want to win it
- flag every row where **owner ≠ leader** — that is a deliberate reassignment, not a silent one. It needs a 60-day checkpoint in the report.
- **outside-set collisions**: run the same check against URLs *not* in the sprint. A proposed title that an out-of-scope page already owns verbatim is a self-inflicted wound.

Then assign per row: one primary, ~5 secondaries. In the secondary cell, mark each borrowed query `OWNED BY <page> — link, do not target` and each moved query `REASSIGNED HERE FROM <page>`. The writer must not be able to re-target by accident.

**Exclude from targeting and from reporting:** navigational/brand queries, bare ambiguous acronyms (a three-letter string that means something else to most searchers), and one-month anomaly spikes. Note the exclusion in the Risk cell so the numbers aren't re-litigated later.

## Phase 4 — Play classification

Click Potential decides what winning means:

- **A — click recovery** (CP 60–90): SERP still pays organic. Optimise title/H1 for CTR, chase position.
- **B — AIO citation** (CP ≤ 20): AI Overviews take the clicks. Optimise for extraction — direct-answer H2s, ~40–60 word answer blocks, clean entities. Do not promise CTR gains.
- **A/B — mixed**: split query set. Say which queries fall on which side.

Mislabelling here wastes the whole unit: you cannot recover clicks on a SERP that has none.

## Phase 5 — Recommendations (fan out, Sonnet)

4–6 rows per agent. Each agent gets `scope.md`, `querymap.json`, and only its rows' `pagefacts` — never the whole fact base.

Prompt template:

> Using ONLY scope.md, querymap.json and the attached pagefacts, write `recs/{row}.json`:
> `{title, h1, h2_stack, meta, why, risk}`
>
> **title** ≤60 chars, primary phrasing first, year only if the page's figures can carry it. Append the char count as `"  (52)"`.
> **meta** ≤160 and ≥110 chars, opens with the primary phrasing, includes one hard figure only if that figure is in pagefacts.
> **h2_stack**: numbered lines, sequential from 1. Every line carries a provenance tag: `(keep)` `(keep, tighten)` `(keep, demote)` `(rename from "X")` `(promote from H2-2)` `(merge X + Y)` or a bracketed note naming the existing content it uses. A line you cannot tag from pagefacts does not go in the stack — append it under `STAGE 2:` instead.
> Line 1 is a direct-answer H2 matching the primary query, with a ~40–60 word answer block. If the live H2-1 is "Key takeaways" or similar, replace it — that slot is the most valuable heading on the page. If the live H2-1 already answers the primary query, tag it `(keep)`; do not "promote" what is already H2-1.
> Where the page has no content for a query, write `[one line + link to <url>]`, not a section.
> **why**: the specific numbers — impressions, clicks, position, KD, CP, inlinks — and the one structural fact that makes this page winnable.
> **risk**: LOW/MEDIUM/HIGH plus what breaks. Then a `FIGURE CHECK:` block listing every figure whose stated_year is older than the year in your proposed title, every figure with `sourced:false` that carries weight, and every pair of on-page figures that contradict each other.
> Never propose adding a figure, table, example or section that is not in pagefacts.

## Phase 6 — Mechanical checks (script)

Run this before any human reads the recs. Deterministic, free, catches the embarrassing class of error.

```python
import json, re, glob, os
rows = json.load(open('rows.json'))
recs = {r: json.load(open(f'recs/{r}.json')) for r in rows}
n = lambda s: re.sub(r'\s+', ' ', s or '').strip()
fails, titles, h2s = [], {}, {}

for row, rec in recs.items():
    t = rec.get('title', '')
    m = re.search(r'\s\((\d+)\)\s*$', t)
    body = t[:m.start()].strip() if m else t.strip()
    if not m: fails.append((row, 'title', 'no char count appended'))
    elif int(m.group(1)) != len(body): fails.append((row, 'title', f"count {m.group(1)} != {len(body)}"))
    if len(body) > 60: fails.append((row, 'title', f'{len(body)} chars > 60'))

    meta = n(rec.get('meta', ''))
    if len(meta) > 160: fails.append((row, 'meta', f'{len(meta)} > 160'))
    if len(meta) < 110: fails.append((row, 'meta', f'{len(meta)} chars - wasting space'))

    stack = rec.get('h2_stack', '')
    nums = [int(x) for x in re.findall(r'^(\d+)\.', stack, re.M)]
    if nums != list(range(1, len(nums) + 1)): fails.append((row, 'h2_stack', f'numbering {nums}'))
    for line in stack.split('\n'):
        if re.match(r'^\d+\.', line) and not re.search(r'\((keep|rename|promote|demote|merge)|\[', line):
            fails.append((row, 'h2_stack', f'untagged: {line[:60]}'))

    titles.setdefault(n(body).lower(), []).append(row)
    for line in stack.split('\n'):
        s = n(re.sub(r'\[.*?\]|\(.*?\)', '', re.sub(r'^\d+\.\s*', '', line))).lower()
        if len(s) > 12: h2s.setdefault(s, []).append(row)

    yrs = [int(y) for y in re.findall(r'\b(20\d\d)\b', t)]
    if yrs and os.path.exists(f'pagefacts/{row}.json'):
        facts = json.load(open(f'pagefacts/{row}.json'))
        stale = [f for f in facts.get('figures', [])
                 if f.get('stated_year') and int(f['stated_year']) < max(yrs)]
        if stale and 'FIGURE CHECK' not in rec.get('risk', ''):
            fails.append((row, 'risk', f'{len(stale)} pre-{max(yrs)} figures, no FIGURE CHECK'))

for s, rs in list(titles.items()) + list(h2s.items()):
    if len(set(rs)) > 1:
        fails.append((','.join(map(str, sorted(set(rs)))), 'collision', s[:60]))

json.dump(fails, open('checks.json', 'w'), indent=1)
for f in fails: print(*f, sep='\t')
print(f'\n{len(fails)} failures')
```

**Gate:** zero failures. Collisions are the one class that needs judgment — one of the two rows must yield and link instead.

## Phase 7 — Adversarial verification (fan out, Sonnet)

Same batching as Phase 5, but a different agent than wrote the recs.

> For each numbered line in `recs/{row}.json` h2_stack, and for every figure cited in title/meta/risk, decide from `pagefacts/{row}.json` alone:
> `GROUNDED` — the content exists; name the heading or figure it maps to.
> `PARTIAL` — some exists; say exactly what is missing.
> `UNGROUNDED` — the page has nothing to build it from.
> Also flag: any line claiming `(keep)` on a heading not in pagefacts.headings; any `(promote from H2-2)` where the heading is already H2-1; any figure cited at a value different from pagefacts; any rename target string that appears in another row's headings.
> Return JSON only. Do not rewrite anything.

**Gate:** every UNGROUNDED line cut to `STAGE 2:`. Every PARTIAL either narrowed to what exists or cut. A figure mismatch is a hard stop — re-check the live page by hand, including collapsed FAQs and JSON-LD, before deciding who is wrong.

## Phase 8 — Cross-column consistency (you)

Read each row as a writer would, top to bottom. The columns must tell one story:

- Does the meta promise what the H1 and H2-1 deliver?
- Does Why cite the metric that justifies the Play?
- Does Risk name every figure the stack touches?
- Does the stack contradict Risk ("add the stat" vs "do not add stats")?
- Do any two rows' stacks point at each other in a loop?
- Is every reassigned query's destination row actually set up to receive it?

This is the pass no subagent does well. Budget real time for it.

## Phase 9 — Write to the sheet

Re-read the header row first, every time. Clients edit sheets mid-sprint; an edit targeting a deleted column fails with "the name given to this range is invalid" and a shifted column writes to the wrong place silently.

Working protocol via Claude-in-Chrome:

1. `triple_click` the name box at ~`[50, 153]`
2. `type` the ref + `\n` (e.g. `Q13\n`)
3. `key` `Return` — enters edit mode
4. `key` `cmd+a` — selects existing contents
5. `type` line 1
6. For each further line: `wait 0.4` → `key cmd+Return` → `wait 0.4` → `type` line
7. `key` `Return` — commits

**The 0.4s waits are mandatory.** Without them Sheets silently drops every other in-cell line break in a fast batch, producing `...(keep)2. Next item` on one line. This cost a full re-do pass across 47 cells on one sprint. Single-line cells need no waits.

Other hard-won rules:

- Batch 5–8 cells per `browser_batch`. More risks a timeout.
- **Never** use clipboard writes (`javascript_tool` + `writeText` + `cmd+v`) — it hangs the extension and costs minutes of recovery.
- A cell whose text starts with `+`, `-` or `=` is read as a formula. Lead with a word or prefix the line.
- Sheets eats a leading apostrophe. Retype if you need one.

## Phase 10 — Verify by export (script)

Never trust the write. Export via Drive and diff against the intended payload.

```python
import json, re
d = json.load(open(EXPORT_PATH))['fileContent']
lines = [l for l in d.split('\n') if l.startswith('| https://')]
rows = {i + 2: [c.strip() for c in l.strip().strip('|').split(' | ')]
        for i, l in enumerate(lines)}
unesc = lambda s: re.sub(r'\\(.)', r'\1', s)
norm  = lambda s: re.sub(r'\s+', ' ', s).strip()

# 1. content diff: export flattens newlines to spaces, so flatten both sides
for (row, col_idx), want in INTENDED.items():
    got = unesc(rows[row][col_idx])
    if norm(want.replace('\n', ' ')) != norm(got):
        print('MISMATCH', row, col_idx, repr(want[:90]), repr(got[:90]))

# 2. dropped-line-break detector: a numbered line glued to the previous one
for row, cells in rows.items():
    for ci in MULTILINE_COLS:
        g = unesc(cells[ci])
        if re.search(r'[^\s]\d\. [A-Z(\'\"]', g):
            print('MISSING BREAK', row, ci, g[:100])
```

The export escapes markdown characters (`\+`, `\[`, `\~`, `1\.`) — unescape before comparing or you will chase phantom mismatches. **Gate:** zero mismatches, zero missing breaks.

## Phase 11 — Writer one-sheet and client report

**Writer one-sheet** (companion doc): what each deliverable means concretely, how TL;DR relates to the intro and H2-1, the Deliverables Done column, the per-page workflow steps, the quality bar, and the sentence that matters most — *if the page doesn't have it, don't write it; flag it for Stage 2.*

**Client report** in four separate sections. Keeping them separate is the point:

1. **What changed** — by theme, with counts, not a cell-by-cell log
2. **Taste calls you may want to revert** — every title rewrite, primary reassignment and play relabel, with the trade-off named in one line each
3. **Needs your data call** — internal contradictions you can't resolve from outside, conflicting metrics in their own file
4. **Structural notes** — anything odd you found in their sheet: broken validation, stale tab notes, deleted columns, shifted headers

## House defaults

- Titles ≤60 chars, char count appended in the cell. 61–62 is a judgment call; over 65 truncates and loses the brand.
- Metas 110–160 chars, primary phrasing first, one hard figure where the page has one.
- "Key takeaways" as H2-1 is always a wasted slot. Replace with a direct-answer H2.
- Direct-answer block: ~40–60 words, first position under the H2.
- H2-1 may echo the H1; sentence-case it when the strings are identical.
- TL;DR replaces the intro. H2-1 stays.
- No content for a query → one line plus an internal link, never a stub section.
- Query owned by another page → link to it, mark `OWNED BY`, do not target.
- A page needing more than the SOW allows goes to Stage 2 whole. Do not half-build it.
- Every figure claim needs a year and a source, or it doesn't ship.

## Failure catalog — check for these by name

| Failure | How it shows up | Catch |
|---|---|---|
| Instruction assumes absent content | "Add a step-by-step walkthrough" on a page with no steps | Phase 7 UNGROUNDED |
| Phantom figure | Cite a stat that isn't on the page | Phase 7 figure mismatch |
| False phantom | Stat IS on the page but in a collapsed FAQ or JSON-LD; cmd+F misses it | Phase 2 `location` field |
| Year drift | Title says 2026, body figures say 2024 | Phase 6 staleness check |
| Self-contradiction | Page states two values for one fact (30 days vs 45 days) | Phase 5 FIGURE CHECK |
| Self-inflicted cannibalization | Proposed string another row or an out-of-scope page owns | Phase 6 collision |
| Silent owner≠leader | Reassign a query without flagging it | Phase 3 flag + 60-day checkpoint |
| Phantom promote | "Promote from H2-2" when it's already H2-1 | Phase 7 heading check |
| Duplicate section | Add an H2 that duplicates an existing one under a new name | Phase 7 + Phase 8 |
| Char count lies | Appended count doesn't match the string | Phase 6 |
| Dropped line breaks | `(keep)2. Next` glued in the cell | Phase 9 waits, Phase 10 detector |
| Structural drift | Client deletes or inserts a column mid-sprint | Re-read headers before every write pass |
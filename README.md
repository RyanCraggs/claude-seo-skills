# Claude skills for SEO, content and AEO work

Six Claude skills I built and run on real client work, then anonymized for
publication. Each one encodes a workflow that kept going wrong by hand: invented URLs in briefs,
refresh instructions that assumed content the page didn't have, and AI-visibility reports that quoted
numbers nobody could point to.

The pattern across all six is the same: **retrieve before you write, and gate every claim on something
you can check.**

| Skill | What it does |
|---|---|
| [`seo-article-brief`](skills/seo-article-brief/SKILL.md) | Turns keyword research into a copy-paste-ready article brief. Builds a link inventory from the sitemap and shipped briefs first, so every internal link exists and every crosslink anchor is quoted verbatim from the live page. |
| [`keyword-research-sheet`](skills/keyword-research-sheet/SKILL.md) | Two-phase keyword research spreadsheet (15–20 keywords pre-kickoff, 35–40 after), with live SERP and Google Trends checks per keyword and a fixed Excel spec. |
| [`refresh-sprint`](skills/refresh-sprint/SKILL.md) | Multi-URL content refresh: scope contract from the SOW, per-page fact base, query ownership map, title/H1/H2/meta recs, a mechanical check script and adversarial verification. Fans out to cheaper subagents. |
| [`weekly-gsc-seo-report`](skills/weekly-gsc-seo-report/SKILL.md) | Weekly week-over-week Search Console report: sitewide, content section, core and homepage buckets, a branded-demand check, top movers and verified new pages, in a skeptical-analyst voice. All site settings live in `config.json`; optional Slack delivery. |
| [`seo-geo-audit`](skills/seo-geo-audit/SKILL.md) | Full client-ready SEO/GEO audit, section by section: technical, Core Web Vitals, schema, on-page, content-library deciles, E-E-A-T, keywords and competitive gap, AI visibility and CRO. Branches on site maturity, assesses what it can live, asks for exports for the rest and never invents a metric. |
| [`aeo-monthly-report`](skills/aeo-monthly-report/SKILL.md) | Monthly AEO/GEO deck from Semrush Enterprise AIO. Agents transcribe screenshots to JSON, scripts do every calculation and a reconciliation gate runs before any copy is written. Includes scripts, a workbook and a worked example. |

## Pairs well with

[SuperSEO Skills](https://github.com/inhouseseo/superseo-skills) by InhouseSEO (Apache 2.0) covers the research steps these skills build on. Its `keyword-deep-dive` and `content-brief` produce the research doc that `seo-article-brief` turns into a client brief, and `seo-geo-audit` hands page-level follow-ups to its `eeat-audit` and `page-audit`. Install them from that repo; they aren't included here.

## Install

**Claude apps (claude.ai / desktop):** zip a skill folder (e.g. `skills/refresh-sprint/`) and upload it
under Settings → Capabilities → Skills.

**Claude Code:** copy a skill folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a
project.

```bash
git clone https://github.com/RyanCraggs/claude-seo-skills.git
cp -r claude-seo-skills/skills/refresh-sprint ~/.claude/skills/
```

## Anonymization

Client names, URLs, contacts and metrics have been removed. The AEO report uses a fictional client,
**Cedar Valley Technical College** (`cedarvalleytech.example`). Its example deck, workbook and
`sample-data/` are synthetic but internally consistent, so you can run the scripts end to end:

```bash
cd skills/aeo-monthly-report
python scripts/parse_prompt_rankings.py assets/sample-data/prompt-rankings-2026-07.csv \
       --out /tmp/prompts.json --themes assets/themes.json
python scripts/reconcile.py assets/sample-data/extracted-2026-07.json --prompts /tmp/prompts.json
python scripts/check_slide_copy.py assets/example-slides-july-2026.md
```

The tool gotchas, failure catalogs and gates come from real runs.

## Adapting them

The brief and keyword-sheet skills assume my template and house style: Manrope, the column order and
the brief section order. Change those to match your own. Everything that is specific to one client is
marked `[Client]` or written up as an example pattern.

## License

Apache 2.0 — see [LICENSE](LICENSE). You're free to use, adapt and redistribute these skills, including commercially. If you redistribute them or anything built from them, keep the [NOTICE](NOTICE) file with the attribution, include the license, and mark the files you changed.

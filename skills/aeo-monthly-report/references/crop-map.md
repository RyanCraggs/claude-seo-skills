# Crop map

Individual KPI squares beat rebuilt tables — they carry Semrush's own styling and take seconds.

## Run the script

```bash
python scripts/crop_kpi_cards.py <screenshot.png> --row <y1> <y2> \
       --labels share-of-voice,brand-visibility,... --prefix kpi_ALLMODELS
```

It finds the card gutters, splits, and warns if the Intercom bubble overlaps anything. `--row` is
optional; without it the script auto-detects the topmost row of white cards.

## Naming — the filename must say which universe

Three cards share a name across sets and are **not** the same number. In July: Brand Visibility was
84% all-models and 83% ChatGPT-only; Mentions was 2,016 all-models and 652 ChatGPT-only; Share of Voice
happened to read 73% in both, which is a coincidence and a trap.

| Prefix | Source | Universe |
|---|---|---|
| `kpi_ALLMODELS_` | Prompt Tracking > Rankings, all 3 models | 25 tracked prompts |
| `kpi_CHATGPTONLY_` | Prompt Tracking > Overview, ChatGPT filter | 25 tracked prompts, one model |
| `kpi_ALLTOPICS_` | AI Visibility > Visibility Overview, US | All visible topics |
| `kpi_TRAFFIC_` | Traffic Analysis > AI Referral Traffic (GA) | Site traffic |

**Never mix cards from two prefixes in one row on a slide.**

## What to cut

### `kpi_ALLMODELS_` — 6 cards → slide 10
share-of-voice · brand-visibility · responses-with-mentions · mentions · total-responses · avg-position

### `kpi_CHATGPTONLY_` — 6 cards → slides 9, 17
share-of-voice · brand-visibility · mentions · source-visibility · citations · sentiment

> `source-visibility` is the strongest single card for slide 17. `sentiment` is the donut — use it once
> to show sentiment is a non-issue, then stop.

### `kpi_ALLTOPICS_` — 4 cards → slide 7
ai-visibility (the gauge) · mentions · monthly-audience · cited-pages

### `kpi_TRAFFIC_` — 4 cards → slide 15
traffic · conversions · revenue · bounce-rate

> **Skip `revenue`.** It reads "$0 / N/A" because revenue isn't tracked, and a $0 on a client slide
> invites a question you can't answer. The script drops it automatically with `--skip revenue`.

## Region crops — charts and tables

| Crop | Slide |
|---|---|
| Mentions by Model bars | 7 |
| Mentions trend line | 8 — the divergence visual |
| Performing Topics table | 7 |
| Performance by Model | 9 |
| Prompt Rankings table | 11 |
| **Product Rankings with the red/green delta bars** | 14 — carries the slide |
| Traffic by Model + Host donut | 15 |
| Traffic over Time | 15 — crop the current month off |
| Landing Page Performance | 16 |
| Brand Leaderboard | 17 |
| Most Cited Sources | 17 |
| Top Concepts | 17 |
| Query Fan-Outs | 20 |

## Rules of thumb

- One KPI card per number you'd otherwise type into a table.
- If a slide has more than 6 cards on it, it's a table — use the region crop instead.
- Charts always beat a rebuilt version. The client sees the same thing you see in the tool, which
  makes the number feel checkable.

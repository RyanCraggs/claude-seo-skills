# Slide spec

## Hard limits

The agency template fits: **one head, one short paragraph, three or four short bullets.** That's it.
Anything longer overflows the slide and someone has to rewrite it by hand.

| Element | Limit |
|---|---|
| **HEAD** | ≤ 8 words. Sentence case. No colons-plus-subtitle constructions. |
| **DECK** (paragraph) | ≤ 30 words, 1–2 sentences. Optional — cut it if the bullets carry the slide. |
| **BULLETS** | **3–4 maximum.** ≤ 12 words each. No bold lead-ins. No sub-bullets. |
| **NOTES** | Unlimited. Everything you want to say out loud lives here, not on the slide. |

A bullet is a **claim with a number**, not a sentence with clauses. If a bullet needs an em-dash to
explain itself, the explanation belongs in NOTES.

## Format to write in

```
## SLIDE 9 — Performance by Platform

HEAD: AI Overviews gained the most ground
DECK: All three platforms improved position this month. Google AI Overviews improved most, on both how often we appear and where we rank.
- AI Overviews: mentions +8.1%, position 1.6 → 1.3
- Gemini: best position at 1.14, only platform losing frequency
- ChatGPT: flat on frequency, position 1.40 → 1.19
NOTES: Lower position is better — say it out loud the first time. AI Overviews was called our weakest
platform in earlier reports and we prescribed FAQs, location signals and schema. This is that work
landing. Worth claiming explicitly.
IMAGE: slide09_performance_by_model.png
```

Then run `python scripts/check_slide_copy.py slides.md`. Fix every flag.

## Worked before/after

**Too long — this was a real bullet from the July draft (33 words):**
> **Google AI Overviews is the month's win.** Mentions up 8.1% and average position improved from 1.6
> to 1.3 — the biggest gain of any platform. This is the AI Overviews work from earlier reports landing.

**Fixed (7 words on the slide, the rest in notes):**
> - AI Overviews: mentions +8.1%, position 1.6 → 1.3
>
> NOTES: Biggest gain of any platform, and it's the AI Overviews work from earlier reports landing.

**Too long (28 words):**
> - **The institution is being named more; the programs are being named less.** Cedar Valley Tech mentions
>   up 81 — but eight of our nine tracked programs declined.

**Fixed (two bullets, 8 and 6 words):**
> - Cedar Valley Tech mentions up 81, share of voice 63%
> - Eight of nine programs lost mentions

## Deck skeleton — 21 slides

| # | Slide | Purpose |
|---|---|---|
| 1 | Cover | Month and title |
| 2 | What's Inside | Section page numbers |
| 3 | Reporting Period | Calendar month. Note any period change once, here. |
| 4 | The Headlines | 4 bullets max. Lead with the win. |
| 5 | The Prompts We Track | The agency contact's standing ask. Themes table + one discussion question. |
| 6 | Visibility Overview: definitions | The four metrics explained. Reusable month to month. |
| 7 | Visibility Overview: the numbers | KPI cards + what moved |
| 8 | The Divergence | Tracked prompts vs all topics. The report's spine. |
| 9 | Performance by Platform | Per-model table |
| 10 | Prompt Ranking | The six KPI cards + win/loss counts |
| 11 | Notable Gains | Position AND frequency both improved |
| 12 | Notable Declines | Includes the fake-gain trap |
| 13 | Weak Cluster | Whichever theme is eroding |
| 14 | Program-Level Visibility | Institution vs programs |
| 15 | AI Referral Traffic | Traffic, conversions, bounce |
| 16 | Where AI Traffic Lands | Landing pages + the conversion footnote |
| 17 | Competitive Position | Leaderboard, cited sources, one sentiment line |
| 18 | Recommended Optimizations | 5 max, each tied to a specific finding |
| 19 | Ongoing Optimizations | Carry-forward with status. Mark unstarted items. |
| 20 | Looking Ahead | New metrics, platform changes |
| 21 | Close | Thank you |

## Writing rules

- **Position:** write "improved from 1.6 to 1.3". Never "up" or "+0.2". The tool shows an improvement
  as a positive number and a client will read that backwards.
- **Bounce rate:** down is good. Don't file a rising bounce rate under good news.
- **Every visibility figure names its model.** "75% share of voice on ChatGPT", not "75% share of voice".
- **Recommendations name a target.** "Add the full credential name to the H1 on the five surgical tech and
  nursing program pages", not "improve program pages".
- **Unactioned recommendations get flagged as unactioned.** A recommendation appearing for the third
  time is a different conversation than a new one, and a more useful one.
- **Banned:** "it's worth noting", "moreover", "furthermore", "delve", "landscape", "robust",
  "leverage" as a verb, "unlock", anything that could appear in a McKinsey deck.

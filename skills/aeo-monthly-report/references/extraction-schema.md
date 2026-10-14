# Extraction schema

The contract between the transcription agents and the scripts. One file per month:
`extracted/<YYYY-MM>.json`. Agents fill it. Scripts consume it. Nothing else.

**Every value is read off a screen.** No agent computes anything. Fields ending `_delta` hold the
number Semrush displays next to the card, converted to a fraction (`+17%` → `0.17`, `+2 pts` → `0.02`,
`-0%` → `0.0`). If a delta isn't displayed, the field is `null` — never derived.

```jsonc
{
  "month": "2026-08",                    // the calendar month pulled
  "date_range": "Aug 1-31, 2026",        // exactly as shown in the date chip
  "country": "United States",            // must be United States
  "pulled_on": "2026-09-05",

  "visibility_overview": {               // AI Visibility > Visibility Overview
    "ai_visibility": 34,                 // 0-100 composite, NOT a percentage
    "mentions": 612,
    "monthly_audience": 14200000,
    "cited_pages": 388,
    "topics_total": 397,                 // from the Performing Topics pagination "1-10 of N"
    "mentions_by_model": {
      "All Models": 550, "AI Overview": 251, "Gemini": 128, "AI Mode": 88, "ChatGPT": 83
    }
  },

  "ai_rankings_kpi": {                   // Prompt Tracking > Rankings, ALL models selected
    "share_of_voice": 0.73,        "share_of_voice_delta": 0.02,
    "brand_visibility": 0.84,      "brand_visibility_delta": 0.0,
    "responses_with_mentions": 1868, "responses_with_mentions_delta": 22,
    "mentions": 2016,              "mentions_delta": 51,
    "total_responses": 2231,       "total_responses_delta": 26,
    "avg_position": 1.2,           "avg_position_delta": 0.2   // shown positive when it IMPROVES
  },

  "prompt_tracking_overview": {          // Prompt Tracking > Overview, one block per model
    "ChatGPT": {
      "share_of_voice": 0.73, "share_of_voice_delta": 0.02,
      "brand_visibility": 0.83, "brand_visibility_delta": 0.0,
      "brand_mentioned": 652, "brand_mentioned_delta": 1,
      "brand_not_mentioned": 123, "brand_not_mentioned_delta": -1,
      "source_visibility": 0.63, "source_visibility_delta": 0.08,
      "domain_cited": 471, "domain_cited_delta": 64,
      "domain_not_cited": 281, "domain_not_cited_delta": -60
    }
    // repeat for "Gemini" and "Google AI Overview"
  },

  "performance_by_model": {              // the Performance by Model panel
    "Gemini": {"share_of_voice": 0.84, "visibility": 0.95, "mentions": 738},
    "ChatGPT": {"share_of_voice": 0.73, "visibility": 0.83, "mentions": 652},
    "Google AI Overview": {"share_of_voice": 0.61, "visibility": 0.70, "mentions": 478}
  },

  "brand_leaderboard": [                 // export it — the share column is cut off on screen
    {"rank": 1, "brand": "Cedar Valley Technical College", "share_of_voice": 0.731}
  ],

  "most_cited_sources": [
    {"domain": "cedarvalleytech.example", "source_visibility": 0.63, "responses_with_citation": 471}
  ],

  "top_concepts": [
    {"concept": "academic programs & credentials", "mentions": 2390, "positive": 1188, "negative": 0}
  ],

  "product_rankings": [                  // Prompt Tracking > Rankings > Product Rankings
    {"product": "Cedar Valley Technical College",
     "mentions_current": 1712, "mentions_prior": 1631,
     "sov_current": 0.634, "sov_prior": 0.601}
  ],
  "product_rankings_total": 128,

  "query_fanouts": [ {"prompt": "colleges that have surgical tech programs", "queries": 18} ],

  "traffic": {                           // Traffic Analysis > AI Referral Traffic (GA)
    "traffic": 1046,     "traffic_delta": 0.17,
    "conversions": 158,  "conversions_delta": 0.88,
    "revenue": null,     "revenue_delta": null,
    "bounce_rate": 0.28, "bounce_rate_delta": -0.12,
    "by_model": {"ChatGPT": 983, "Google Gemini": 41, "Perplexity": 14,
                 "Microsoft Copilot": 6, "Claude.ai": 2},
    "by_host_total": 1046
  },

  "landing_pages": [
    {"url": "https://www.cedarvalleytech.example/", "ai_sessions": 156, "ai_conversions": 16}
  ],
  "landing_pages_total": 276,

  "notes": [ "anything odd the transcriber saw — cut-off columns, overlapping UI, blank panels" ]
}
```

## Rules for whoever fills this

- **Transcribe, never calculate.** If a number isn't visible, use `null` and add a line to `notes`.
- **Percentages become fractions.** `66.0%` → `0.66`. `+9%` → `0.09`.
- **Position deltas keep the sign Semrush shows**, even though it displays an improvement as positive.
  `reconcile.py` knows to expect that.
- **Never guess a bar's value from its length.** Unlabeled bar → `null` plus a note.
- **`country` must read "United States".** Anything else and the whole file is discarded.

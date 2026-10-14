# E-E-A-T Analysis

Experience, Expertise, Authoritativeness, and Trustworthiness — Google's content-quality framework. YMYL sites (health, finance, legal, anything affecting well-being) are held to a stricter bar. Claude assesses most of this **live** by fetching the site.

Sub-sections: Experience & Expertise · Authority (Topical + Backlinks) · Trust · Reputation · Google Business Profile (conditional).

## Section intro (template)

> E-E-A-T stands for Experience, Expertise, Authoritativeness, and Trustworthiness — the framework Google uses to evaluate content quality. YMYL sites are held to stricter standards. Because [client] provides [medical/financial] information, Google's algorithms carefully evaluate how well the site demonstrates expertise, reliable sourcing, and transparent guidance.

Optionally reference Google's Search Quality Evaluator Guidelines and leave a `[SCREENSHOT: Google QRG excerpt]` placeholder.

## Experience & Expertise

**Sample posts from both clinical and non-clinical authors** (check the blog index for the author roster first, then open at least one of each). The gap that matters most on YMYL sites — a medical post written by a non-clinician with no visible clinical reviewer — only surfaces if you look across author types, not just one representative post. For each, check for:
- Author name present and clickable → links to a real author profile page
- Author profile pages that are comprehensive (bio, credentials, role)
- Clinical/expert reviewer name present and clickable → comprehensive reviewer profile page
- A "References" section at the end of articles
- Editorial policy page linked from articles

Report what's already in place positively (established sites usually do most of this), then give targeted improvements. Common ones:

- [ ] **Underline the author's name** if it isn't visually obviously a link (small but real UX/clarity fix).
- [ ] **Add a distinct Clinical/Editorial Review Policy section** to the editorial policy page: how content is reviewed, who reviews it, and how often. Point to strong examples (Verywell Health's editorial process; Verywell Mind's review board).
- [ ] **For new/pre-launch sites:** add leadership/expert bios (names, roles, credentials, experience), "Reviewed by" bylines on health/science content, "Last reviewed" dates, a Medical/Scientific Advisory Board page, and a stated content-review process. Reference a well-built author page as a model.

For a page-level score on a representative article, the `eeat-audit` skill can be run separately — mention it as a deeper option.

## Authority

Two parts: **Topical Authority** and **Backlinks.**

### Topical authority

Demonstrating subject-matter depth across a defined set of themes, with interlinking. Report the site's content distribution by theme and name where it's deep vs. thin. Recommend internal linking to build topic clusters (ties to `content-library.md` and `onpage.md`).

For new sites with little content, recommend a **hub-and-spoke plan**: identify the core hubs (e.g., How It Works, [Product] Education, Safety & Eligibility, Regulatory, Research & Evidence, Support) and build pillar/trust pages *before* scaling blog volume — for YMYL, foundational trust pages come first.

### Backlinks

> Backlinks remain a crucial authority/trust signal. When authoritative sites link to [client], it validates credibility to users and search engines.

**Inputs (from user):** backlink profile numbers from Ahrefs — total backlinks, DoFollow vs. NoFollow, DR distribution (low 0–9, high 50+), and a sample of high-DR referring domains. Claude can't pull these.

Report the profile, then assess:
- **Strengths:** high DoFollow share (passes ranking value); presence of high-DR publications/universities (strong YMYL credibility signals). Name a few real high-DR linkers.
- **Watch-outs (esp. newer sites):** misattributed/unrelated links (e.g., a different company sharing the brand name), homepage-only concentration (little equity reaching trust pages), links to thin/outdated pages, and off-site claims that overstate outcomes (YMYL compliance risk).

**How to improve:**
- [ ] Help internal experts earn press (tools like Qwoted, Source of Sources / HARO-style lists) for organic reporter connections.
- [ ] Continue building niche-relevant links from health/industry publications.
- [ ] Build links to *trust pages*, not just the homepage (Research, Regulatory, Safety, How It Works).
- [ ] Create linkable authority assets (plain-language regulatory explainers, safety guides, research summaries, comparison pages).
- [ ] Leverage high-authority pages for internal linking so equity spreads to valuable pages.
- [ ] Prioritize relevance over raw DR; audit low-DR/spam links periodically.

Leave `[SCREENSHOT: backlink profile]` if a dashboard image belongs here.

## Trust

> In YMYL, trust is essential — for readers and for the algorithms evaluating quality. Google expects transparency, credible sourcing, and visible review processes.

Check live and report what's present (established sites usually have): "Clinically/Expertly reviewed by" byline, visible "Last updated" date, a References section, editorial policy linked, clear privacy practices, secure/clean site.

**Improvements:**
- [ ] **Change footer anchor "Company" → "About Us"** — clearer, matches what people look for when evaluating who's behind a YMYL site; raters look specifically for an identifiable About page.
- [ ] **Cite sources explicitly in-text** — "according to [source]" linked to the resource, or linked footnotes; cite respected journals, government agencies (NIH, CDC), recognized experts.
- [ ] **New sites:** add testimonials/quotes from real people (customers, clinicians, researchers — permission & claim-compliance handled), an editorial and corrections policy, and trust modules near CTAs (safety, intended use, regulatory status, research, support).

Point to a strong model (e.g., GoodRx's "Why Trust Our Experts" block: who wrote/reviewed it, credentials, link to editorial process, link to the medical team).

## Reputation

> Reputation is a key trust pillar and shapes how users and search engines perceive credibility, especially in health. Assess it by searching `[domain] -site:[domain]`.

Report:
- **Social presence** — the platforms and follower counts. **Pull current follower counts live** (fetch each linked profile or search for it) rather than leaving a placeholder. Note which audiences each reaches (e.g., LinkedIn → B2B partners; Instagram/TikTok → consumers) and where there's untapped opportunity.
- **Third-party review platforms** — ratings and counts. Check the platforms that matter for the vertical: Google, Trustpilot, and Reviews.io broadly, plus **BBB for DTC/telehealth/e-commerce brands** (a poor BBB rating is a common and load-bearing risk there). Flag low ratings or empty profiles as risks/opportunities.

**How to improve:**
- [ ] Proactively encourage reviews on trusted platforms via post-appointment email/SMS touchpoints; even a few verified reviews lift perceived credibility.
- [ ] Continue monitoring and responding to reviews — especially 1–2 star ones, with compassion and an invitation to continue offline; prospective patients read the replies.
- [ ] Continue increasing third-party validation (clinician/founder quotes and interviews in reputable publications).
- [ ] Expand social presence where the opportunity is biggest (often TikTok for reach/relatability) with short educational clips.

Leave `[SCREENSHOT: reputation/social snapshot]` if useful.

## Google Business Profile (conditional — local/physical presence)

Even when GBP isn't a major acquisition channel, it matters for **entity trust** — it validates a real business with consistent contact info. Report the profile snapshot (name, category, rating, review count, address, phone, hours, photos) and what the reviews indicate (thin volume, possible misattribution, quality of the owner's responses).

**How to improve:**
- [ ] Complete missing info (hours, description — claim-compliant, no unsupported health claims).
- [ ] Add official photos (office/team/product/brand).
- [ ] Use Google Posts for milestones (launch, research, regulatory updates).
- [ ] Add proactive Q&A for branded questions.
- [ ] Add UTM tracking to the website link to measure GBP-sourced traffic.
- [ ] Manage misattributed reviews via Google's process; collect reviews only from legitimate interactions; respond carefully in a YMYL context (no medical advice or outcome claims).

# Schema Markup

Claude assesses this **live**. Fetch the homepage and a representative interior page (a blog post for content sites, a product page for e-commerce), extract any JSON-LD or microdata, and evaluate it.

## Inputs

- **Claude fetches live:** the site's actual schema via `web_fetch`. Look in `<head>` and inline `<script type="application/ld+json">` blocks.
- Point the user to the validator to confirm any recommended markup: https://validator.schema.org/ and docs at https://schema.org/docs/schemas.html

## Section intro (template)

> Schema markup helps search engines understand your content and can enhance search appearance with rich snippets. For a [health/YMYL] site like [client], structured data is especially important to support E-E-A-T and content credibility.

State plainly whether schema is present. Two situations:

- **Schema already implemented (mature site):** say so positively, then list the specific errors to fix and enhancements to consider.
- **No schema detected (new/pre-launch site):** the validator returns "No items detected." Frame this as a *foundational opportunity*, not a crisis — adding it early builds clean structure as the site grows.

## Common errors to catch

When schema exists, validate the properties actually belong to the type. A common pattern: properties copied from one type's documentation onto another type that doesn't support them (e.g. a `Person`- or `Service`-only property on `Organization`) → recommend removing.

List each fix as a checkbox under the page it appears on.

## Recommendations by site type

**Baseline (every site):**
- `Organization` — brand entity: name, URL, logo, social profiles, contact, short description
- `WebSite` — identifies the domain as the official site
- `WebPage` — on the homepage: name, URL, description, primary image, publisher
- `BreadcrumbList` — once the site has depth beyond the homepage; helps Google read hierarchy and improves SERP navigability

**Health / YMYL:**
- `MedicalOrganization` in place of / alongside `Organization`
- `MedicalWebPage` on educational blog posts to surface them more effectively. Key elements: `@type: MedicalWebPage`, `headline`, `author`, `reviewedBy`, `datePublished`, `dateModified`, `image`, `publisher`, `publishingPrinciples` (link to editorial policy / review process)
- `ProfilePage` + `Person` on author and reviewer pages

**E-commerce / device:**
- `Product` with, at minimum, name plus one of `review` / `aggregateRating` / `offers`
- For merchant/shopping eligibility, add `image` (≥1200px), nested `offers` with `price` + `priceCurrency`, `availability`, `priceValidUntil`, `url`, at least one identifier (`gtin`/`mpn`/`sku`/`productID`), and `brand`. Google favors listings with real third-party `aggregateRating`/`review`.

**FAQ nuance — handle carefully.** Google reduced FAQ rich-result visibility in 2023. State this honestly. The defensible position: don't rely on `FAQPage` schema for rich results, but it can still be a low-priority nice-to-have on a genuinely dedicated FAQ page (some argue it helps AI-driven search), and FAQ *content* should stay visible and crawlable on-page regardless. Do not present FAQ schema as a growth lever.

## Output shape

Group recommendations by page (Homepage / Blog Posts / Author & Reviewer Pages / Product Pages), with fixes as checkboxes and a short "Optional Enhancements" list at the end. Close with the validator and documentation links.

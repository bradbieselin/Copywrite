# Google Search Ads (Responsive Search Ads) Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A complete responsive search ad asset set: 15 headlines, 4 descriptions, pin recommendations, 4 sitelink extensions with descriptions, 4 callout extensions, and 2 structured snippet extensions |
| **Turnaround** | Single prompt execution — review and character-count verification in 15-20 minutes |
| **Quality bar** | Ready to paste into Google Ads after brand review and character count verification; every headline works standalone and in combination with any other headline |
| **Best for** | DTC and service brands running Google Search campaigns — branded search, competitor conquesting, category/generic keyword targeting, and product-specific campaigns |

---

## Client Brand Variables

Copy the block below and fill in every field before running the prompt. Leave nothing blank — if a field does not apply, write "N/A" so the model knows to skip it intentionally.

```
[BRAND_NAME] =
[BRAND_VOICE] =
[TARGET_AUDIENCE] =
[PRODUCT_SERVICE] =
[PRICE_RANGE] =
[KEY_DIFFERENTIATOR] =
[COMPETITOR_NAMES] =
[WORDS_TO_USE] =
[WORDS_TO_AVOID] =
[TONE_SCALE] = (1 = very casual/irreverent ... 10 = very polished/premium)
[CAMPAIGN_GOAL] =
[ADDITIONAL_CONTEXT] =
```

### Additional Google Search-specific variables

```
[TARGET_KEYWORD] = (The primary keyword or keyword theme this ad group targets)
[SECONDARY_KEYWORDS] = (2-4 additional keywords in the same ad group)
[LANDING_PAGE_URL] = (The URL users will land on after clicking)
[DISPLAY_URL_PATHS] = (Two optional URL path fields, 15 chars each, e.g., /luxury-candles and /shop)
[GEOGRAPHIC_TARGET] = (Location targeting if relevant, e.g., "US only," "New York metro")
[PROMOTIONAL_OFFER] = (Any active offer — discount, free shipping, free trial, etc. Write "None" if no offer is active)
```

### Variable definitions (for the person filling this in)

- **BRAND_NAME**: Exact brand name as it should appear in ad copy. Keep it short — every character counts in Google Search.
- **BRAND_VOICE**: 2-4 adjective descriptors. Note: Google Search ads are inherently more direct and benefit-focused than social ads. Voice still matters but manifests differently — through word choice and claim style rather than tone and narrative.
- **TARGET_AUDIENCE**: Who is searching for this keyword? What is their intent at the moment of search? Are they researching, comparing, or ready to buy?
- **PRODUCT_SERVICE**: The specific product or service being advertised. Be precise.
- **PRICE_RANGE**: Exact price or range. Price in headlines is a strong qualifier — it attracts ready buyers and filters out non-buyers.
- **KEY_DIFFERENTIATOR**: The single strongest competitive advantage. This should appear in multiple headlines.
- **COMPETITOR_NAMES**: 2-4 competitors. Used for positioning and to ensure differentiation. Never use competitor names in Google Search ads (policy violation).
- **WORDS_TO_USE**: Keywords, benefit phrases, and brand terms that should appear. Note: the TARGET_KEYWORD should be included in headlines — Google rewards keyword relevance with higher Quality Scores.
- **WORDS_TO_AVOID**: Banned words or phrases. Also note any claims that are not legally approved.
- **TONE_SCALE**: Google Search ads are naturally more direct than social. A tone-3 brand on Instagram might be a tone-5 on Search. Adjust accordingly.
- **CAMPAIGN_GOAL**: What conversion action do you want? Purchase, lead form submission, phone call, appointment booking, etc.
- **TARGET_KEYWORD**: The primary keyword this ad group is built around. This keyword (or close variants) should appear in at least 40% of headlines.
- **SECONDARY_KEYWORDS**: Related keywords in the same ad group. Weave these into descriptions and some headlines.
- **LANDING_PAGE_URL**: Where the click goes. The ad copy should align with the landing page content — if the page is about a specific product, the ad should be about that product.
- **DISPLAY_URL_PATHS**: The two customizable path fields in the display URL (e.g., ember-and-oak.com/luxury-candles/shop). Max 15 characters each.
- **PROMOTIONAL_OFFER**: Any active offer to include. If there is a specific offer, it should appear in at least 2 headlines and 1 description.
- **GEOGRAPHIC_TARGET**: If location matters, it can be included in a headline or description for local relevance.

---

## The Prompt

Paste the following prompt into Claude along with the filled-in brand variables above.

---

```
You are a Google Ads specialist and direct-response copywriter with deep expertise in responsive search ad (RSA) construction. You understand Quality Score mechanics, headline-description combinatorics, character limits, and the psychology of search intent. You have managed accounts spending $50k+/month on Search and know exactly what makes an ad win the click in a competitive SERP.

Your job: create a complete responsive search ad asset set for the brand and campaign described below.

## BRAND BRIEF

[Paste filled-in brand variables here]

## GOOGLE SEARCH-SPECIFIC BRIEF

[Paste filled-in Google Search-specific variables here]

## INSTRUCTIONS

### Critical constraints:

1. **Headlines: 30 characters maximum each.** This is a hard limit. Spaces and punctuation count as characters. There is no flexibility — Google will reject any headline over 30 characters. Count every headline carefully.

2. **Descriptions: 90 characters maximum each.** Same rules. Spaces and punctuation count. Stay as close to 90 characters as possible without exceeding — longer descriptions take up more SERP real estate, which improves CTR.

3. **Callout extensions: 25 characters maximum each.** Hard limit.

4. **Sitelink headline: 25 characters maximum.** Sitelink description lines: 35 characters maximum each (2 lines per sitelink).

### Headline strategy (15 headlines total):

You must write exactly 15 headlines. They must be distributed across these categories:

**Keyword-focused headlines (at least 3):**
Include the target keyword or a close variant. These drive relevance and Quality Score. The keyword should feel natural, not forced.

**Benefit-focused headlines (at least 3):**
Lead with a specific benefit the searcher cares about. Answer "why should I click this?" What do they get? What problem does this solve? How does their life improve?

**Number/stat headlines (at least 3):**
Include a specific number — price, percentage, quantity, rating, years in business, number of customers, etc. Numbers stand out in a text-heavy SERP and build credibility.

**CTA headlines (at least 3):**
Drive action. Use direct imperatives: "Shop," "Try," "Get," "Order," "Start," "Discover," "Save." Make the next step clear.

**Brand name headlines (at least 3):**
Include the brand name. At least one should be the brand name alone. Others can combine the brand name with a benefit or keyword (e.g., "Ember & Oak Luxury Candles").

### Additional headline rules:

- Every headline must work standalone. Google may show any 2-3 headlines together in any combination. A headline that only makes sense next to a specific other headline is a bad headline.
- Every headline must also work in combination with any other headline. Avoid two headlines that say the same thing — if both appear, the ad looks repetitive.
- Maximize character usage. A 16-character headline in a 30-character slot is wasted space. Aim for 25-30 characters per headline.
- Use title case for headlines (capitalize the first letter of each major word).
- Do not use exclamation marks in headlines — Google often rejects them or they look spammy in the SERP.
- Include the keyword in at least 40% of headlines (6+ out of 15).
- Power words that perform well in Search: Free, New, Exclusive, Premium, Proven, Top-Rated, Award-Winning, Trusted, Fast, Easy, Save, Best, Official. Use where appropriate and truthful.

### Description strategy (4 descriptions):

Write exactly 4 descriptions, each 90 characters maximum.

- **Description 1:** Lead with the primary benefit and include the keyword. This is your workhorse description.
- **Description 2:** Stack secondary benefits or features. Use a list format with separators (pipes or dashes work well).
- **Description 3:** Include social proof — reviews, ratings, customer count, awards, press mentions, or years in business.
- **Description 4:** CTA-focused with urgency or offer details. If there is a promotion, it goes here.

Each description must complement any headline combination. Do not repeat what the headlines say — descriptions should add new information.

### Pin recommendations:

After listing all headlines, provide pinning recommendations. Pinning locks a specific headline to a specific position (Headline 1, Headline 2, or Headline 3). Use pinning sparingly — Google recommends against it because it limits optimization. Only pin when:
- A headline MUST appear for legal/compliance reasons
- The brand name must always be visible
- A specific offer must always show

Provide 1-2 pin recommendations maximum, with justification.

### Sitelink extensions (4 sitelinks):

Each sitelink needs:
- **Sitelink headline** (25 chars max): Clear label for the linked page
- **Description line 1** (35 chars max): First line of supporting text
- **Description line 2** (35 chars max): Second line of supporting text
- **URL:** The destination page (can be a suggested path)

Sitelinks should cover different facets of the business: product pages, about/story pages, bestsellers, reviews, contact, FAQs, specific collections, etc. They should complement the main ad, not repeat it.

### Callout extensions (4 callouts):

Short, punchy phrases that highlight key selling points. 25 characters max each. These appear as a row beneath the ad. They are NOT clickable — they are pure value communication. Examples: "Free Shipping Over $50" or "Handcrafted in Small Batches" or "4.9 Star Rating."

### Structured snippet extensions (2):

Choose a header category (Brands, Types, Styles, Destinations, Models, etc.) and provide 4-6 values for each. These show as "Types: value1, value2, value3" beneath the ad.

Write the complete asset set now. Count every character. Maximize every slot.
```

---

## Output Format

The final output must contain exactly:

- **15 headlines** with character counts displayed, organized by category
- **4 descriptions** with character counts displayed
- **Pin recommendations** with justifications (1-2 pins)
- **4 sitelink extensions**, each with headline, 2 description lines, and suggested URL path
- **4 callout extensions** with character counts
- **2 structured snippet extensions** with header and 4-6 values each

Every character count must be explicitly noted in parentheses after each element. Example: `Shop Luxury Candles Today (26 chars)`

Formatting: Use markdown headers and tables where appropriate. Group headlines by category for easy review.

---

## Quality Checks Before Sending

Run through every item on this list before delivering to the client. If any check fails, revise before sending.

1. **Character count verification — headlines.** Count every headline manually. Every headline must be 30 characters or fewer, counting spaces and punctuation. This is the single most important check. A headline at 31 characters will be rejected by Google Ads. Do not trust your initial count — recount.

2. **Character count verification — descriptions.** Every description must be 90 characters or fewer. Maximize usage — aim for 80-90 characters. Descriptions under 70 characters are wasting valuable SERP real estate.

3. **Character count verification — extensions.** Callouts: 25 chars max. Sitelink headlines: 25 chars max. Sitelink description lines: 35 chars max each. Verify every one.

4. **Keyword density check.** The target keyword (or close variant) should appear in at least 6 of the 15 headlines (40%+). Count them. If fewer than 6 contain the keyword, add more keyword-focused headlines and remove a lower-priority one.

5. **Combinatorial compatibility test.** Pick any 3 headlines at random. Read them together. Do they make sense? Do any two say the same thing? Are any two structurally identical (e.g., both start with "Shop" or both are questions)? Repeat this test 5 times with different random combinations.

6. **Headline uniqueness scan.** Read all 15 headlines in sequence. No two headlines should convey the same message. "Shop Now" and "Buy Today" are effectively the same headline. Each must add distinct value.

7. **Policy compliance.** No superlatives without substantiation ("Best candles in the world" requires third-party verification). No competitor names. No exclamation marks in headlines. No all-caps words. No misleading claims.

---

## Example Output

The following is a complete example using the fictional brand below.

### Example Brand Variables

```
[BRAND_NAME] = Ember & Oak
[BRAND_VOICE] = Refined, warm, artisanal, quietly confident
[TARGET_AUDIENCE] = Women and men aged 28-50, upper-middle to high income, who buy candles as home decor and self-care rituals. They appreciate craftsmanship, natural ingredients, and aesthetic packaging. They search for specific candle types and are willing to pay premium prices for quality.
[PRODUCT_SERVICE] = Luxury hand-poured soy candles, 100% natural soy wax, cotton wicks, fragrance oils sourced from Grasse, France. Core collection of 12 scents. Signature vessel is a reusable ceramic tumbler.
[PRICE_RANGE] = $48-$72 per candle, $125-$180 for gift sets
[KEY_DIFFERENTIATOR] = Fragrance oils sourced directly from Grasse, France — the perfume capital of the world. Every candle is hand-poured in small batches in Portland, Oregon, using 100% natural soy wax and lead-free cotton wicks. The ceramic vessel is designed to be reused.
[COMPETITOR_NAMES] = Boy Smells, Diptyque, Byredo, P.F. Candle Co.
[WORDS_TO_USE] = "hand-poured," "small batch," "Grasse-sourced fragrance," "natural soy wax," "reusable vessel," "crafted in Portland"
[WORDS_TO_AVOID] = "cheap," "discount," "mass-produced," "artificial," "knock-off"
[TONE_SCALE] = 8 (refined, warm, understated luxury — confident in quality without being pretentious)
[CAMPAIGN_GOAL] = Drive purchases of individual candles and gift sets through branded and category search
[ADDITIONAL_CONTEXT] = 4.8 star average rating across 2,400+ reviews. Featured in Vogue, Architectural Digest, and Bon Appetit. Free shipping on orders over $75. Currently offering a complimentary matchbox with every order. The brand's holiday gift set is a top seller November-January.

[TARGET_KEYWORD] = luxury candles
[SECONDARY_KEYWORDS] = hand-poured candles, soy candles, premium candles, artisan candles
[LANDING_PAGE_URL] = https://www.emberandoak.com/collections/all
[DISPLAY_URL_PATHS] = /Luxury-Candles /Shop
[GEOGRAPHIC_TARGET] = United States
[PROMOTIONAL_OFFER] = Complimentary matchbox with every order (no code needed)
```

---

### Headlines (15 total)

**Keyword-Focused Headlines:**

| # | Headline | Chars | Category |
|---|---|---|---|
| 1 | Luxury Candles Hand-Poured | 26 | Keyword |
| 2 | Premium Soy Luxury Candles | 26 | Keyword |
| 3 | Artisan Luxury Candles | 22 | Keyword |
| 4 | Hand-Poured Luxury Candles | 26 | Keyword |
| 5 | Natural Soy Luxury Candles | 26 | Keyword |
| 6 | Luxury Candles From Ember & Oak | 30 | Keyword + Brand |

**Benefit-Focused Headlines:**

| # | Headline | Chars | Category |
|---|---|---|---|
| 7 | Grasse-Sourced Fragrance Oils | 30 | Benefit |
| 8 | Scents Crafted in Portland | 26 | Benefit |
| 9 | Reusable Ceramic Vessel | 23 | Benefit |

**Number/Stat Headlines:**

| # | Headline | Chars | Category |
|---|---|---|---|
| 10 | 4.8 Stars From 2,400+ Reviews | 30 | Number |
| 11 | 12 Signature Scents Available | 29 | Number |
| 12 | 100% Natural Soy Wax Candles | 28 | Number |

**CTA Headlines:**

| # | Headline | Chars | Category |
|---|---|---|---|
| 13 | Shop the Full Collection | 24 | CTA |
| 14 | Order Yours Today | 17 | CTA |
| 15 | Discover Your Signature Scent | 29 | CTA |

---

### Descriptions (4 total)

| # | Description | Chars |
|---|---|---|
| 1 | Hand-poured luxury candles made with natural soy wax and Grasse-sourced fragrance oils. | 87 |
| 2 | Small batch. Cotton wicks. Reusable ceramic vessel. Crafted with care in Portland, OR. | 86 |
| 3 | Rated 4.8 stars by 2,400+ customers. As featured in Vogue and Architectural Digest. | 83 |
| 4 | Free shipping over $75. Complimentary matchbox with every order. Shop the collection now. | 88 |

---

### Pin Recommendations

**Pin 1:** Pin Headline 6 ("Luxury Candles From Ember & Oak") to **Headline Position 1**.
Justification: This headline contains both the target keyword and the brand name. Pinning it to Position 1 ensures the ad always leads with keyword relevance and brand identity, which supports Quality Score and brand recognition on branded search queries.

**Pin 2:** No additional pin recommended. Allow Google to dynamically optimize Headlines 2 and 3 for maximum CTR. Over-pinning restricts the algorithm and reduces the number of ad combinations Google can test.

---

### Sitelink Extensions (4)

**Sitelink 1: Bestsellers**

| Field | Content | Chars |
|---|---|---|
| Headline | Shop Our Bestsellers | 20 |
| Description Line 1 | Our most-loved scents in one place | 34 |
| Description Line 2 | Curated by 2,400+ customer reviews | 34 |
| Suggested URL | /collections/bestsellers | — |

**Sitelink 2: Gift Sets**

| Field | Content | Chars |
|---|---|---|
| Headline | Luxury Gift Sets | 16 |
| Description Line 1 | Beautifully packaged gift sets | 30 |
| Description Line 2 | Starting at $125 with free ship | 31 |
| Suggested URL | /collections/gift-sets | — |

**Sitelink 3: Our Story**

| Field | Content | Chars |
|---|---|---|
| Headline | Our Story and Process | 21 |
| Description Line 1 | Hand-poured in Portland, Oregon | 31 |
| Description Line 2 | Fragrance oils from Grasse France | 34 |
| Suggested URL | /pages/our-story | — |

**Sitelink 4: Reviews**

| Field | Content | Chars |
|---|---|---|
| Headline | Read Customer Reviews | 21 |
| Description Line 1 | See why customers rate us 4.8/5 | 31 |
| Description Line 2 | Over 2,400 verified reviews | 27 |
| Suggested URL | /pages/reviews | — |

---

### Callout Extensions (4)

| # | Callout | Chars |
|---|---|---|
| 1 | Free Shipping Over $75 | 22 |
| 2 | Hand-Poured Small Batches | 25 |
| 3 | 100% Natural Soy Wax | 20 |
| 4 | Free Matchbox With Order | 24 |

---

### Structured Snippet Extensions (2)

**Structured Snippet 1:**

| Field | Content |
|---|---|
| Header | Types |
| Values | Signature Collection, Seasonal Collection, Gift Sets, Travel Size, Limited Edition |

**Structured Snippet 2:**

| Field | Content |
|---|---|
| Header | Styles |
| Values | Floral, Woodsy, Citrus, Warm Spice, Fresh, Gourmand |

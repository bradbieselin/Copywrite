# Google Performance Max Campaign Asset Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A complete Performance Max asset group: 5 short headlines, 5 long headlines, 5 descriptions, business name, 2 CTA options, 5 image direction concepts, a 15-30 second video script outline, and audience signal suggestions |
| **Turnaround** | Single prompt execution — review and character-count verification in 15-20 minutes |
| **Quality bar** | Ready to upload into Google Ads Performance Max campaign after brand review and character verification; assets work across Search, Display, YouTube, Discover, Gmail, and Maps placements |
| **Best for** | DTC and e-commerce brands running Google PMax campaigns to maximize conversions across all Google inventory — especially brands that want a cohesive message across multiple placements without creating separate campaigns for each channel |

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

### Additional PMax-specific variables

```
[FINAL_URL] = (The landing page URL for the asset group)
[PRODUCT_FEED_AVAILABLE] = (Yes/No — is this PMax campaign connected to a Google Merchant Center product feed?)
[KEY_PRODUCT_CLAIMS] = (2-4 specific, verifiable claims about the product — e.g., "dermatologist tested," "made with organic ingredients," "ships in 24 hours")
[EXISTING_CREATIVE_ASSETS] = (Describe any existing photos, videos, or brand assets that can be used or referenced for creative direction)
[CONVERSION_ACTION] = (The specific conversion being optimized for — Purchase, Lead, Add to Cart, etc.)
[GEOGRAPHIC_TARGET] = (Location targeting if relevant)
[SEASONAL_CONTEXT] = (Any seasonal relevance — holiday, summer, back-to-school, etc. Write "Evergreen" if not seasonal)
```

### Variable definitions (for the person filling this in)

- **BRAND_NAME**: Exact brand name. This will appear as the "Business name" in PMax, so it must be accurate.
- **BRAND_VOICE**: 2-4 adjective descriptors. PMax assets run across many placements, so voice must be versatile enough to work in Display banners, YouTube pre-rolls, Gmail promotions, and Search simultaneously.
- **TARGET_AUDIENCE**: Demographics + psychographics + purchase intent signals. PMax uses audience signals to find converters, so be specific about who your buyer is and what signals indicate purchase readiness.
- **PRODUCT_SERVICE**: The specific product or service. If this asset group is for a single product, be precise. If it covers a category, describe the category.
- **PRICE_RANGE**: Exact price or range. Price is often visible in PMax Shopping placements via the product feed, so text ad copy should align.
- **KEY_DIFFERENTIATOR**: The strongest competitive advantage. This must come through clearly across all asset types.
- **COMPETITOR_NAMES**: 2-4 competitors. Used to inform positioning. Never mentioned directly in assets.
- **WORDS_TO_USE**: Brand vocabulary and product terms. These should be woven naturally across headlines and descriptions.
- **WORDS_TO_AVOID**: Banned terms. Especially important in PMax since assets appear in many contexts.
- **TONE_SCALE**: PMax assets skew slightly more direct than organic social content because many placements are interruption-based (Display, YouTube pre-roll, Gmail). Adjust accordingly.
- **CAMPAIGN_GOAL**: What conversion action is this PMax campaign optimized for? This shapes CTA language.
- **FINAL_URL**: Where clicks go. All assets should align with this page's content and offer.
- **PRODUCT_FEED_AVAILABLE**: If Yes, PMax will also run Shopping ads from the feed. Text assets should complement (not repeat) product feed data.
- **KEY_PRODUCT_CLAIMS**: Specific, verifiable claims. These become the backbone of descriptions and headlines. They must be truthful and substantiated.
- **EXISTING_CREATIVE_ASSETS**: What visual assets already exist? This shapes image direction — we may suggest new concepts or ways to repurpose existing assets.
- **CONVERSION_ACTION**: The specific conversion event. Shapes CTA language and urgency level.
- **GEOGRAPHIC_TARGET**: Location can be referenced in descriptions for relevance.
- **SEASONAL_CONTEXT**: If seasonal, assets should reference the season or occasion. If evergreen, assets should be timeless.

---

## The Prompt

Paste the following prompt into Claude along with the filled-in brand variables above.

---

```
You are a Google Ads Performance Max specialist and direct-response copywriter. You understand how PMax dynamically assembles assets across Search, Display, YouTube, Discover, Gmail, and Maps placements. You know that every asset must work in isolation AND in any combination with other assets, across wildly different contexts — from a YouTube pre-roll to a Gmail promotion tab to a Display banner on a news site.

Your job: create a complete Performance Max asset group for the brand and campaign described below.

## BRAND BRIEF

[Paste filled-in brand variables here]

## PMAX-SPECIFIC BRIEF

[Paste filled-in PMax-specific variables here]

## INSTRUCTIONS

### Critical constraints:

1. **Short headlines: 30 characters maximum each.** Hard limit. Spaces and punctuation count. These appear in Search-like placements and small Display formats.

2. **Long headlines: 90 characters maximum each.** These appear in larger Display placements, Discover, and YouTube companion banners. They have more room for storytelling.

3. **Descriptions: 90 characters maximum each.** These complement headlines and provide supporting information. They must add value beyond what headlines say.

4. **Business name: Must match the brand name exactly.** This appears alongside assets in most placements.

### Short headline strategy (5 short headlines):

Write exactly 5 short headlines, each 30 characters maximum. These must cover different angles because Google will rotate them across placements:

- **Headline 1 — Keyword/product focused:** Name the product or category clearly. Someone seeing this in a Search placement should immediately know what is being offered.
- **Headline 2 — Benefit focused:** Lead with the primary benefit. What does the customer get?
- **Headline 3 — Differentiator focused:** What makes this brand/product different from everything else?
- **Headline 4 — Social proof or credibility:** A number, rating, award, or trust signal.
- **Headline 5 — CTA focused:** Drive action. Tell the reader exactly what to do.

Each headline must work standalone in a small Display banner (where it may be the ONLY text visible alongside the brand name and an image).

### Long headline strategy (5 long headlines):

Write exactly 5 long headlines, each 90 characters maximum. These appear in larger placements where there is more room. They should be more descriptive and compelling than short headlines:

- **Long Headline 1 — Value proposition:** Clearly state what the product is and why it matters, in one line.
- **Long Headline 2 — Problem/solution:** Reference the problem the audience has and position the product as the answer.
- **Long Headline 3 — Social proof expansion:** Expand on credibility — reviews, press features, customer count, awards.
- **Long Headline 4 — Differentiator story:** Explain what makes this product different in a way that is more detailed than the short headline allows.
- **Long Headline 5 — Urgency or offer:** If there is an active promotion, lead with it. If not, create value-based urgency (e.g., "Your skin deserves better than what you are using now").

### Description strategy (5 descriptions):

Write exactly 5 descriptions, each 90 characters maximum. Descriptions provide supporting information and appear beneath headlines in most placements:

- **Description 1 — Primary benefit + keyword:** The workhorse description. Include the product name/category and primary benefit.
- **Description 2 — Feature stack:** List 2-3 key features or ingredients separated by pipes or dashes.
- **Description 3 — Social proof + trust:** Reviews, ratings, press mentions, certifications, or customer count.
- **Description 4 — Offer or value communication:** Price, free shipping, money-back guarantee, subscription savings, or promotional offer.
- **Description 5 — CTA + differentiator:** Close with action and a final reason to choose this brand.

### Business name:

Provide the exact business name as it should appear in PMax placements (typically the brand name).

### CTA text options (2):

Google PMax allows you to select a CTA button text. Provide 2 recommendations from the available options: Shop Now, Learn More, Get Offer, Sign Up, Subscribe, Book Now, Contact Us, Get Quote, Apply Now, Download, Order Now. Explain which is best for the primary campaign goal and which serves as a testing alternative.

### Image direction notes (5 concepts):

PMax requires image assets in multiple sizes (landscape 1200x628, square 1200x1200, portrait 960x1200). Provide 5 distinct image concepts that would work across these formats. For each concept, describe:

- What the image shows
- The composition and focal point
- The mood/lighting
- Any text overlay (if recommended)
- Which placement context this image concept serves best (Display, Discover, YouTube thumbnail, etc.)

These are direction notes for a designer or photographer — be specific and actionable.

### Video script outline (15-30 seconds):

PMax strongly favors asset groups that include video. Write a video script outline for a 15-30 second video that can run as a YouTube ad (skippable or non-skippable) or in Discover/Display video placements. Structure:

- **Seconds 0-3 (Hook):** What appears on screen and what is said/shown to stop the scroll or prevent the skip
- **Seconds 3-10 (Problem/Setup):** Establish the problem or context
- **Seconds 10-20 (Solution/Product):** Introduce the product and key benefits
- **Seconds 20-30 (CTA/Close):** Drive the viewer to take action

Include notes on: visual style, pacing, music mood, text overlay recommendations, and whether the video should feel produced or UGC.

### Audience signal suggestions:

PMax uses audience signals to guide its algorithm toward likely converters. Provide recommendations for:

- **Custom segments:** 3-5 search terms or URLs that indicate purchase intent
- **Your data:** What first-party audiences to upload (purchasers, email subscribers, cart abandoners, etc.)
- **Interests and detailed demographics:** 3-5 Google affinity or in-market audience categories
- **Demographics:** Recommended demographic targeting or exclusions

Write the complete asset group now. Count every character for headlines and descriptions. Make every asset work in isolation and in combination.
```

---

## Output Format

The final output must contain exactly:

- **5 short headlines** with character counts (30 chars max each)
- **5 long headlines** with character counts (90 chars max each)
- **5 descriptions** with character counts (90 chars max each)
- **1 business name**
- **2 CTA text options** with reasoning
- **5 image direction concepts** with format, composition, mood, overlay, and placement notes
- **1 video script outline** (15-30 seconds, timestamped)
- **Audience signal suggestions** across 4 categories

Character counts must be explicitly displayed in parentheses after each headline and description.

---

## Quality Checks Before Sending

Run through every item on this list before delivering to the client. If any check fails, revise before sending.

1. **Character count verification — short headlines.** Every short headline must be 30 characters or fewer. Count manually. This is the most common failure point.

2. **Character count verification — long headlines.** Every long headline must be 90 characters or fewer. Maximize usage — aim for 70-90 characters. Short long headlines waste the opportunity for more expressive copy.

3. **Character count verification — descriptions.** Every description must be 90 characters or fewer. Same principle — maximize without exceeding.

4. **Cross-placement compatibility test.** Read each short headline and imagine it appearing in a tiny Display banner next to a small product image. Does it make sense with zero context? If the headline requires explanation, rewrite it.

5. **Combination test.** Pick one short headline, one long headline, and one description at random. Read them together. Do they conflict? Do they repeat each other? Do they tell a coherent story? Repeat this test 5 times.

6. **Angle diversity check.** Read all 5 short headlines in sequence, then all 5 long headlines. Each should approach the product from a different angle. If two headlines are saying the same thing with different words, replace one.

7. **Video script viability.** Read the video script aloud with a timer. Does the hook land in 3 seconds? Does the full script fit in 30 seconds? Is the CTA clear and specific? Would you watch this if it appeared before a YouTube video?

---

## Example Output

The following is a complete example using the fictional brand below.

### Example Brand Variables

```
[BRAND_NAME] = Bare Route
[BRAND_VOICE] = Clean, confident, approachable, science-informed
[TARGET_AUDIENCE] = Women aged 24-38 who are transitioning to cleaner skincare. They have tried mass-market products and are frustrated with breakouts, irritation, or ingredient lists they cannot understand. They research ingredients, read reviews, and are willing to pay more for products that actually work and are transparent about what is inside. Household income $55k-$110k.
[PRODUCT_SERVICE] = Bare Route Core Kit — a 3-step skincare routine (Gentle Cleanser, Hydrating Serum with hyaluronic acid and niacinamide, Barrier Repair Moisturizer with ceramides and squalane). 30-day supply. Dermatologist tested. Fragrance-free. Vegan and cruelty-free.
[PRICE_RANGE] = $68 for the Core Kit (individual products: $24 cleanser, $32 serum, $28 moisturizer — kit saves $16)
[KEY_DIFFERENTIATOR] = Every product has 10 or fewer ingredients, all clinically tested at effective concentrations. No fragrance, no essential oils, no filler ingredients. The brand publishes full ingredient percentages on their website — not just ingredient names.
[COMPETITOR_NAMES] = CeraVe, The Ordinary, Cocokind, Versed
[WORDS_TO_USE] = "clean ingredients," "clinically tested," "barrier repair," "transparent formula," "fewer ingredients, better results," "dermatologist tested"
[WORDS_TO_AVOID] = "anti-aging" (brand avoids age-anxiety marketing), "miracle," "flawless," "perfection," "detox," "toxin-free" (scientifically inaccurate)
[TONE_SCALE] = 5 (approachable and warm, but informed — like a friend who happens to have a chemistry degree)
[CAMPAIGN_GOAL] = Drive sales of the Core Kit as the primary entry point for new customers
[ADDITIONAL_CONTEXT] = 4.7 star average across 3,200+ reviews. Featured in Allure Best of Beauty 2025 and Byrdie. Free shipping on orders over $50. 30-day money-back guarantee. Subscribe and save available at $57.80/kit (15% off). The brand was founded by a cosmetic chemist who was frustrated with how many unnecessary ingredients are in most skincare products.

[FINAL_URL] = https://www.bareroute.com/products/core-kit
[PRODUCT_FEED_AVAILABLE] = Yes
[KEY_PRODUCT_CLAIMS] = Dermatologist tested; 10 or fewer ingredients per product; full ingredient percentages published; fragrance-free and vegan
[EXISTING_CREATIVE_ASSETS] = Professional product photography (flat lays and lifestyle shots of woman applying serum), founder headshot, ingredient close-up photography, customer before/after photos (with consent), unboxing UGC videos from customers
[CONVERSION_ACTION] = Purchase
[GEOGRAPHIC_TARGET] = United States
[SEASONAL_CONTEXT] = Evergreen
```

---

### Short Headlines (5)

| # | Short Headline | Chars | Angle |
|---|---|---|---|
| 1 | Bare Route Core Skincare Kit | 28 | Product/Keyword |
| 2 | Fewer Ingredients. Real Results. | 30 | Benefit (note: period counts) |
| 3 | 10 or Fewer Ingredients Each | 28 | Differentiator |
| 4 | 4.7 Stars From 3,200+ Reviews | 30 | Social Proof |
| 5 | Try the Core Kit Today | 22 | CTA |

---

### Long Headlines (5)

| # | Long Headline | Chars | Angle |
|---|---|---|---|
| 1 | The 3-Step Skincare Routine With 10 or Fewer Clinically Tested Ingredients Per Product | 86 | Value Proposition |
| 2 | Frustrated With Breakouts and Ingredient Lists You Cannot Understand? Meet Bare Route | 86 | Problem/Solution |
| 3 | Rated 4.7 Stars by 3,200+ Customers and Named an Allure Best of Beauty 2025 Winner | 83 | Social Proof |
| 4 | Every Ingredient Percentage Published. No Fragrance. No Filler. Just What Your Skin Needs | 90 | Differentiator |
| 5 | Your Complete Skincare Routine for $68 With Free Shipping and a 30-Day Money-Back Guarantee | 90 | Offer/Value |

---

### Descriptions (5)

| # | Description | Chars | Angle |
|---|---|---|---|
| 1 | Bare Route Core Kit: cleanser, serum, and moisturizer with clinically tested clean ingredients. | 90 | Primary benefit + keyword (note: period at end counts) |
| 2 | Hyaluronic acid. Niacinamide. Ceramides. Squalane. Dermatologist tested. Fragrance-free. | 87 | Feature stack |
| 3 | Allure Best of Beauty 2025. 4.7 stars from 3,200+ verified reviews. Try it risk-free. | 85 | Social proof + trust |
| 4 | Save $16 with the Core Kit bundle. Free shipping over $50. 30-day money-back guarantee. | 87 | Offer/value |
| 5 | Discover why 3,200+ women switched to Bare Route. Shop the Core Kit and see the difference. | 90 | CTA + differentiator |

---

### Business Name

**Bare Route**

---

### CTA Text Options (2)

**Primary recommendation: Shop Now**
Reasoning: The campaign goal is direct purchases of the Core Kit. "Shop Now" is the most direct CTA for purchase-intent campaigns and aligns with e-commerce conventions. Users who click "Shop Now" have higher purchase intent than those who click "Learn More."

**Testing alternative: Get Offer**
Reasoning: "Get Offer" implies the user is receiving something of value (the bundle savings, the money-back guarantee). It can outperform "Shop Now" in Display and Discover placements where users are not actively shopping but can be enticed by a perceived deal. Test this in a separate asset group or as an A/B variant.

---

### Image Direction Notes (5 Concepts)

**Concept 1: The Core Kit Product Flat Lay**

What it shows: All three Bare Route Core Kit products arranged on a clean, minimal surface — marble, light linen, or matte white. The products should be the clear focal point with ample negative space around them for text overlays in Display formats.

Composition and focal point: Centered product arrangement with slight asymmetry (serum bottle slightly forward, cleanser and moisturizer flanking). Focal point is the serum bottle (the hero product).

Mood/lighting: Bright, clean, natural light. Soft shadows. The mood is "fresh morning bathroom counter" — not sterile, not moody. Warm white tones.

Text overlay: Optional brand name in small type at top. The products should speak for themselves. In Display banners, the headline and description will appear adjacent.

Best placement context: Display banners (landscape and square), Discover feed, Gmail promotions. This is the workhorse product image.

**Concept 2: The Ingredients Close-Up**

What it shows: A close-up macro shot of actual ingredients used in the products — a squalane oil droplet, a ceramide cream texture swirl, or a niacinamide serum texture on fingertips. The image should make the viewer curious about what they are looking at.

Composition and focal point: Extreme close-up, slightly abstract. The texture of the ingredient is the focal point. The product bottle should be visible but blurred in the background.

Mood/lighting: Studio lighting, slightly editorial. Cool tones with warm undertones. The mood is "science meets beauty" — clinical precision with a human touch.

Text overlay: Small text overlay: "10 or Fewer Ingredients" in a clean sans-serif font positioned at the bottom of the frame.

Best placement context: Discover feed (where editorial imagery performs well), Display on beauty and lifestyle publisher sites, YouTube companion banners.

**Concept 3: Lifestyle Application Shot**

What it shows: A woman (mid-20s to mid-30s, natural makeup or no makeup, clear or realistically textured skin — not airbrushed) applying the serum in her bathroom. The moment should feel real and unposed — she is looking in the mirror, applying a drop to her cheek, with morning light coming through a window.

Composition and focal point: Medium shot from slightly behind and to the side, capturing both the woman and her reflection. The serum bottle is visible on the counter. Focal point is her hands on her face with the product.

Mood/lighting: Warm natural morning light. Soft, slightly golden. The mood is "calm morning routine" — not rushed, not posed, just a real moment.

Text overlay: None recommended. Let the lifestyle moment carry the image. Headlines and descriptions provide context in the ad unit.

Best placement context: YouTube video thumbnails, Display banners on lifestyle sites, Instagram-like Discover feed placements. This image makes the brand feel approachable and human.

**Concept 4: The Transparent Label Visual**

What it shows: A product label or a stylized graphic showing the ingredient list with percentages visible — leaning into the brand's transparency differentiator. This could be a close-up of the actual product packaging or a designed graphic that mirrors the website's ingredient transparency page.

Composition and focal point: The ingredient list is the hero. Frame it so that individual ingredients and their percentages are legible. Surround with negative space.

Mood/lighting: Clean, white background. Bright and crisp. The mood is "nothing to hide" — transparency as a visual concept.

Text overlay: "Full Ingredient Percentages Published" or "Nothing to Hide" in a bold, clean font.

Best placement context: Display banners (especially on health and wellness publisher sites), Gmail promotions, and Discover. This image targets the research-minded buyer who cares about ingredient integrity.

**Concept 5: Social Proof Compilation**

What it shows: A collage or grid of customer review quotes overlaid on a soft brand-colored background, with small product images. Feature 3-4 short, punchy review quotes and the star rating. Think of this as a "review wall" visual.

Composition and focal point: Grid layout with the 4.7-star rating prominent in the center or top. Review quotes in clean typography surrounding it. Product images small in corners.

Mood/lighting: Branded background color (soft, muted — not white, not dark). Clean, infographic-style. The mood is "trusted by thousands."

Text overlay: The star rating and review quotes ARE the text overlay. Add "3,200+ Reviews" as an anchor number.

Best placement context: Display banners, Gmail promotions, Discover. This image is designed to build instant credibility for cold audiences who have never heard of the brand.

---

### Video Script Outline (30 seconds)

**Format:** Hybrid — opens UGC/casual, transitions to polished product shots. Feels like a real person's recommendation with brand-quality visuals supporting it.

**Seconds 0-3 (Hook):**
Visual: Close-up of a woman looking at the back of a skincare product bottle, squinting at the ingredient list, looking frustrated. She puts it down and looks directly at the camera.
On-screen text: "Can you pronounce everything in your skincare?"
Audio/voiceover: "If you cannot read the ingredient list on your skincare, why are you putting it on your face?"

**Seconds 3-10 (Problem/Setup):**
Visual: Quick montage of common skincare products with long, dense ingredient lists. Cut to a phone screen scrolling through confusing ingredient names. Then show a bathroom cabinet full of half-used products — the visual shorthand for "nothing has worked."
On-screen text (seconds 5-7): "The average skincare product has 25+ ingredients."
On-screen text (seconds 7-10): "Most of them are filler."
Audio/voiceover: "The average skincare product has over 25 ingredients. Most of them are fillers, fragrances, and things you have never heard of. That is not skincare. That is a chemistry experiment on your face."

**Seconds 10-20 (Solution/Product):**
Visual: Clean transition to the Bare Route Core Kit on a bright, minimal surface. Close-up of the ingredient list — short, legible, every percentage visible. Then the three products being used in sequence: cleanser, serum, moisturizer. The woman from the hook now has the Bare Route products. She flips the bottle and the ingredient list is visible in 2 seconds.
On-screen text (seconds 12-14): "10 or fewer ingredients per product."
On-screen text (seconds 15-17): "Every percentage published."
On-screen text (seconds 17-20): "Dermatologist tested. Fragrance-free."
Audio/voiceover: "Bare Route makes skincare with 10 or fewer ingredients per product. Every percentage published right on the label. Dermatologist tested. Fragrance-free. Clinically effective concentrations — no fillers, no guesswork."

**Seconds 20-30 (CTA/Close):**
Visual: The Core Kit in its packaging, price displayed. Quick cut to 4.7-star rating and the Allure Best of Beauty badge. Final frame is the brand logo, URL, and CTA.
On-screen text (seconds 22-24): "Core Kit — $68"
On-screen text (seconds 24-26): "4.7 stars. 3,200+ reviews. Allure Best of Beauty."
On-screen text (seconds 27-30): "Try it risk-free. bareroute.com"
Audio/voiceover: "The Core Kit is $68 with free shipping and a 30-day money-back guarantee. Rated 4.7 stars by over 3,200 customers. Try it risk-free at bareroute.com."

**Production notes:**
- Music: Light, clean, slightly upbeat — think lo-fi with a subtle build. Not trendy or distracting.
- Pacing: Quick cuts (1-2 seconds each) during the problem section. Slower, steadier shots during the solution section. The contrast in pacing mirrors the message: chaos of the old way vs. simplicity of Bare Route.
- Style: The first 3 seconds should feel UGC or organic. After the transition to the product, the quality steps up to polished brand content. This hybrid feel performs well on YouTube and Discover because it opens with relatability and closes with credibility.
- The video should be produced in both landscape (16:9 for YouTube) and square (1:1 for Discover and Display) formats.

---

### Audience Signal Suggestions

**Custom Segments (search terms indicating purchase intent):**
1. "best skincare routine for sensitive skin"
2. "clean skincare brands"
3. "skincare with few ingredients"
4. "niacinamide serum reviews"
5. "CeraVe alternative" / "The Ordinary alternative"

**Custom Segments (URLs indicating intent):**
1. byrdie.com (skincare editorial)
2. theordinary.com (competitor browsing)
3. cerave.com (competitor browsing)
4. reddit.com/r/SkincareAddiction (research community)
5. ewg.org/skindeep (ingredient research)

**Your Data (first-party audiences to upload):**
- Past purchasers (for exclusion from prospecting and as a seed for lookalike signals)
- Email subscribers who have not purchased (warm audience)
- Cart abandoners (30-day window)
- Website visitors — product page viewers who did not purchase (14-day window)
- Website visitors — blog/ingredient pages (signals research intent)

**Interests and Detailed Demographics:**
1. In-market: Beauty & Personal Care > Skin Care Products
2. In-market: Beauty & Personal Care > Facial Cleansers
3. Affinity: Beauty Mavens
4. Affinity: Health & Fitness Buffs > Green Living Enthusiasts
5. Life Event: Recently moved (new routines often trigger skincare changes)

**Demographics:**
- Age: 24-38 (primary), allow 18-44 for algorithmic expansion
- Gender: Female (primary), allow all genders for algorithmic expansion
- Household income: Top 50% (aligns with the $68 kit price point and the audience's willingness to invest in quality skincare)
- Parental status: No restriction (not relevant to purchase intent for this product)

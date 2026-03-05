# Collection / Category Landing Page Copy Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | Complete copy for a DTC brand's collection or category page — the page where customers browse a product line, curated set, or themed grouping. Includes hero copy, category selling points, navigation guidance, individual product card descriptions, and a bottom CTA. |
| **Turnaround** | 20-30 minutes with Claude, plus 10-15 minutes for QA and product-specific tweaks |
| **Quality bar** | Ready to paste into Shopify collection page, Webflow CMS, or hand off to a designer. The copy should make the collection feel curated and intentional — not like a list of SKUs dumped onto a page. Each product description should make a customer say "that one is for me" within 3 seconds. |
| **Best for** | Product line pages, curated collection launches, seasonal edits, category pages (e.g., "All Cleansers"), routine/system pages (e.g., "The Complete Morning Routine"), gift guide collections |

---

## Client Brand Variables

Fill in every variable below before pasting into Claude. If a variable is not applicable, write "N/A" — do not delete the line.

```
[BRAND_NAME] =
[BRAND_VOICE] =
[TARGET_AUDIENCE] =
[PRODUCT_SERVICE] = (the collection name and the products within it — list each product with a 1-sentence description)
[PRICE_RANGE] = (range across the collection, and individual product prices if available)
[KEY_DIFFERENTIATOR] = (what makes this collection/line unique as a set — why these products together)
[COMPETITOR_NAMES] =
[WORDS_TO_USE] =
[WORDS_TO_AVOID] =
[TONE_SCALE] = (1 = very casual/playful, 10 = very formal/clinical)
[CAMPAIGN_GOAL] =
[ADDITIONAL_CONTEXT] =
```

### Variable Guidance

- **PRODUCT_SERVICE**: For collection pages, this variable is critical. List the collection name and every product in it. For each product, include: product name, one-sentence description of what it does, price, and any standout feature. Example:
  ```
  Collection: "The Routine" — a 4-step daily skincare system
  1. Clean Slate Gel Cleanser — lightweight gel cleanser for daily use, removes dirt and oil without stripping — $28
  2. Tone & Balance Mist — alcohol-free balancing toner, preps skin for serum absorption — $24
  3. Daily Defend Serum — vitamin C + niacinamide serum for brightening and protection — $42
  4. Barrier Repair Moisturizer — ceramide-rich daily moisturizer that locks everything in — $36
  ```
- **KEY_DIFFERENTIATOR**: For collections, this should explain why these products belong together and why buying the set is better than buying individual products from different brands. What is the through-line? Shared ingredient philosophy? A step-by-step system? A curated edit for a specific use case?
- **CAMPAIGN_GOAL**: Be specific about the conversion goal. Is this page meant to sell the full set? Drive individual product purchases? Push customers toward a bundle discount? Direct people to a quiz?
- **ADDITIONAL_CONTEXT**: Include any bundle pricing, set discounts, or special offers for buying the full collection. Also note if there is a product quiz or recommendation tool that the page should link to.

---

## The Prompt

Paste the filled-in variables above this prompt, then paste the prompt below into Claude.

---

```
You are a senior DTC copywriter who specializes in collection and category page copy. You understand that collection pages are not product listing pages — they are curated shopping experiences. A great collection page makes the customer feel like someone thoughtful picked these products for a reason, guides them to the right product for their situation, and makes the whole line feel more valuable than the sum of its parts.

Using the brand variables I have provided above, write complete copy for the [PRODUCT_SERVICE] collection page for [BRAND_NAME].

Follow this exact section order. Do not skip any section. Do not combine sections. Label each section clearly.

---

### SECTION 1: COLLECTION HERO

Write the collection hero with these components:

**Headline**: 6-10 words. The headline should frame the collection as a curated experience, not a product dump. It should answer the question: "What is this collection, and why should I care?" Write the headline as the opening line of a story — not a product announcement.

**Subheadline**: 12-20 words. The subheadline adds specificity. What does this collection do for the customer? What problem does it solve as a set?

**Intro paragraph**: 50-75 words. This is the narrative introduction to the collection. Write it as a story — why this collection exists, who it is for, and what it means to use these products together. This paragraph should make the customer feel like the collection was designed specifically for someone like them. Do not list products here. Paint the picture of the outcome.

Rules for the hero:
- The headline should feel editorial, not commercial. Think magazine cover line, not banner ad.
- The intro paragraph should create a sense of intentionality — every product in this collection is here for a reason.
- Include a note for the hero image/visual treatment. Be specific about what kind of imagery supports the narrative (e.g., "all four products arranged in order of use on a clean bathroom shelf" vs. "flat lay on marble").

---

### SECTION 2: CATEGORY SELLING POINTS

Write 3 short benefit callouts for the collection as a whole. These are the reasons to buy the collection (or from this category) rather than buying individual products elsewhere.

Each callout should have:
- A bold headline (3-5 words) that names the benefit
- A supporting sentence (15-25 words) that adds detail

These callouts should focus on what the COLLECTION offers — not what any individual product offers. Think: shared philosophy, ingredient synergy, step-by-step simplicity, tested-together guarantee, value of the set.

Format these as three short blocks that can be displayed side-by-side on the page (think: three columns or three icon blocks).

Include an icon or visual suggestion for each callout.

---

### SECTION 3: PRODUCT GRID INTRO

Write a short guidance paragraph (40-70 words) that helps the customer navigate the collection. This sits above the product grid and acts like a knowledgeable sales associate.

Rules:
- Name the bestseller or most popular starting point
- Offer a conditional recommendation ("if you are looking for X, start with Y")
- If the collection has a specific order or routine, state it clearly
- Keep the tone helpful, not pushy. This is wayfinding, not upselling.
- If the collection is meant to be used as a set, say so — but acknowledge that individual products work on their own too.

---

### SECTION 4: PRODUCT CARD COPY

Write short product descriptions for each product in the collection (there should be 4-6 products based on the brand variables). Each product card gets:

- **Product name**: As provided in the brand variables
- **One-line description**: 15-25 words. This is the description that appears on the product card in the grid. It must communicate the ONE key differentiator for this specific product — not a list of features, not a vague benefit, but the single most important thing this product does that makes someone click through to learn more.
- **Price**: As provided
- **Micro-CTA or tag**: A short tag like "Bestseller," "Start Here," "The Foundation," "For Sensitive Skin," etc. Only assign tags to 1-2 products — not every product. Tags should help with navigation.

Rules for product card copy:
- Focus each description on ONE key differentiator. If the product does five things, pick the one that matters most to the target audience.
- Write in a consistent structure across all cards so the grid feels cohesive.
- Avoid starting every description with the same word or structure. Vary your sentence openings.
- Descriptions should make the customer understand what this product does WITHOUT clicking through. But they should also create enough curiosity to click.
- Do not use superlatives ("the best," "the most powerful") in product card copy. Let the specificity do the selling.

---

### SECTION 5: BOTTOM CTA

Write a cross-sell or "not sure which?" section that sits below the product grid. This section should include:

1. **Headline**: 5-8 words. Frame this as a helpful guide, not a sales push. Examples: "Not Sure Where to Start?" or "Find Your Perfect Match" or "Build Your Routine in 2 Minutes."
2. **Body copy**: 2-3 sentences that acknowledge the customer might need help choosing. Offer a clear next step — a quiz, a buying guide, a chat with the team, or a recommended starter product.
3. **CTA button text**: Action-oriented, low-commitment. Examples: "Take the Quiz," "See Our Guide," "Chat With Us."

If the brand has a bundle or set offer, include a secondary element:
4. **Bundle callout** (optional): A short line promoting the full-set purchase with any associated discount or value proposition.

Include a note for the design team on how to lay out this section.

---

### GENERAL RULES FOR ALL SECTIONS:
- Make the collection feel curated and intentional. Every word should reinforce that these products were chosen (or designed) to work together.
- Help the customer navigate to the right product. Do not make them figure it out on their own.
- Keep paragraphs to 2-3 sentences maximum.
- Write in active voice.
- Do not use exclamation marks more than once on the entire page.
- If a claim needs verification, flag it with [CONFIRM WITH CLIENT].
- Include visual and layout notes for the design team in brackets.
```

---

## Output Format

The output should follow this exact structure:

```
## SECTION 1: COLLECTION HERO

**Headline:** [6-10 words]
**Subheadline:** [12-20 words]

[Intro paragraph: 50-75 words]

[IMAGE/VIDEO NOTE: description]

---

## SECTION 2: CATEGORY SELLING POINTS

**[Callout 1 Headline — 3-5 words]**
[Supporting sentence: 15-25 words]
[ICON NOTE: description]

**[Callout 2 Headline — 3-5 words]**
[Supporting sentence: 15-25 words]
[ICON NOTE: description]

**[Callout 3 Headline — 3-5 words]**
[Supporting sentence: 15-25 words]
[ICON NOTE: description]

---

## SECTION 3: PRODUCT GRID INTRO

[Guidance paragraph: 40-70 words]

---

## SECTION 4: PRODUCT CARDS

**[Product 1 Name]** — $[price]
[One-line description: 15-25 words]
[Tag if applicable]

**[Product 2 Name]** — $[price]
[One-line description: 15-25 words]
[Tag if applicable]

**[Product 3 Name]** — $[price]
[One-line description: 15-25 words]

**[Product 4 Name]** — $[price]
[One-line description: 15-25 words]

[Repeat for up to 6 products]

---

## SECTION 5: BOTTOM CTA

**Headline:** [5-8 words]

[Body copy: 2-3 sentences]

**CTA Button:** [text]

[Bundle callout if applicable]

[DESIGN NOTE: layout guidance]
```

### Word Count Targets

| Section | Target Word Count |
|---|---|
| Collection Hero (headline + subheadline + intro) | 80-110 words |
| Category Selling Points (all three) | 60-90 words |
| Product Grid Intro | 40-70 words |
| Product Cards (all combined) | 80-150 words |
| Bottom CTA | 50-80 words |
| **Total page copy** | **310-500 words** |

Note: Collection pages are deliberately shorter than product pages. The copy is a navigation tool — it guides the customer through the grid, not past it. Brevity is a feature here.

---

## Quality Checks Before Sending

Run through every item below before delivering to the client. If any check fails, revise before sending.

1. **Collection narrative check**: Read Section 1 aloud. Does it tell a story about why these products exist together? Or does it read like a generic "shop our products" page? If you could swap in any brand name and it would still make sense, it is too generic. Rewrite.
2. **Product card differentiator check**: Cover up the product names and read only the descriptions. Can you tell the products apart based solely on the description? If two descriptions could be swapped without anyone noticing, they are not specific enough. Each card must communicate a unique value proposition.
3. **Navigation clarity check**: After reading Section 3, does the customer know which product to look at first and why? If the grid intro does not give the customer a clear starting point, add one.
4. **Consistent structure check**: Read all product card descriptions in sequence. Do they follow a parallel structure that feels cohesive? Are the sentence lengths roughly similar? Does the grid feel like one person wrote it in one sitting?
5. **Tag discipline check**: Confirm that no more than 2 products have special tags (Bestseller, Start Here, etc.). If every product has a tag, none of them stand out. Remove excess tags.
6. **Word count check**: Collection pages should be tight. If total copy exceeds 500 words, look for places to cut. Every word on a collection page must earn its place — this is not the page for long explanations.
7. **Brand voice match**: Read the full page. Does it sound like the brand described in the variables? Check specifically for words on the WORDS_TO_AVOID list and confirm that WORDS_TO_USE appear naturally.

---

## Example Output

The following is a complete example output using the fictional brand below. This demonstrates the expected quality, length, and format for every section.

**Brand variables used for this example:**

```
[BRAND_NAME] = Bare Route
[BRAND_VOICE] = Clean, confident, and calm. We sound like a dermatologist who also happens to have great taste. We do not use hype language or make miracle claims. We believe skincare should be simple, effective, and transparent. Our voice is approachable but knowledgeable — we explain the "why" without lecturing.
[TARGET_AUDIENCE] = Women and men aged 25-45 who are tired of complicated skincare routines and ingredient hype. They have tried the 10-step routines. They have spent too much money on products that promised everything and delivered nothing. They want something that works, is simple to use, and does not require a chemistry degree to understand. They care about what goes on their skin but they are not skincare obsessives — they want to look good and get on with their day.
[PRODUCT_SERVICE] =
Collection: "The Routine" — a 4-step daily skincare system designed to be the only routine you need.
1. Clean Slate Gel Cleanser — lightweight gel cleanser for daily use, removes dirt and oil without stripping skin's natural moisture barrier — $28
2. Tone & Balance Mist — alcohol-free balancing toner in a fine mist format, preps skin for serum absorption and restores pH after cleansing — $24
3. Daily Defend Serum — vitamin C (15%) + niacinamide (5%) serum for brightening, evening skin tone, and environmental protection — $42
4. Barrier Repair Moisturizer — ceramide-rich daily moisturizer that locks in the previous steps and strengthens the skin's moisture barrier — $36
[PRICE_RANGE] = $24-$42 individual / $110 for the full set (save $20)
[KEY_DIFFERENTIATOR] = Four steps, four products, one routine. Every product in The Routine was formulated to work with the others — same pH progression, complementary active ingredients, layering-optimized textures. Most brands sell individual products and hope you figure out the order. We designed the system.
[COMPETITOR_NAMES] = N/A
[WORDS_TO_USE] = the routine, system, simple, effective, barrier, clean ingredients, dermatologist-informed, daily ritual, fewer steps, real results
[WORDS_TO_AVOID] = miracle, anti-aging (use "age-well" if needed), chemical-free (everything is a chemical), toxic, clean beauty (too vague), luxury
[TONE_SCALE] = 6 (measured, confident, approachable but not overly casual)
[CAMPAIGN_GOAL] = Drive purchases of the full 4-product set ("The Routine" bundle at $110). Secondary goal: if they will not buy the set, get them to start with one product (ideally the Daily Defend Serum, which is the hero SKU).
[ADDITIONAL_CONTEXT] = The brand has been live for 14 months. They have sold about 8,000 sets and have a 4.6-star average rating. They have a skin type quiz on the site that recommends whether to start with the full set or an individual product. The set comes in a reusable linen pouch. All products are vegan, cruelty-free, and fragrance-free. The brand does not use the phrase "clean beauty" because they consider it meaningless — they prefer "transparent ingredients" and list every ingredient with a plain-English explanation on each product page.
```

---

### EXAMPLE OUTPUT BEGINS HERE

---

## SECTION 1: COLLECTION HERO

**Headline:** Four Steps. One Routine. Skin That Works.

**Subheadline:** The Routine is a complete daily skincare system — formulated so every product works with the next, not against it.

You have tried the 10-step routines. You have bought the serums that promised visible results in a week and delivered a new breakout instead. The Routine is something different: four products, designed as a system, each one formulated to complement the others. Same pH progression, complementary actives, textures that layer without pilling. This is not a collection of products. It is one routine that actually works, start to finish.

[IMAGE NOTE: All four products arranged left to right in order of use on a clean, minimal bathroom shelf — white or light stone surface. Products should be spaced evenly with enough room to see each label. The image should feel calm and orderly, reinforcing "simplicity." If possible, show a subtle morning light source from the left side. Consider a secondary image below: a flat lay of the full set inside the reusable linen pouch, partially unzipped, on a bed or dresser.]

---

## SECTION 2: CATEGORY SELLING POINTS

**Designed as a System**
Every product in The Routine was formulated to work together — same pH progression, complementary actives, textures that layer in the right order.
[ICON NOTE: Simple line icon of four circles connected by a line or arrow, suggesting a sequence or system.]

**Fewer Steps, Real Results**
Four steps replace the patchwork of eight or ten products from different brands that were never meant to meet each other on your face.
[ICON NOTE: Simple line icon of a single clean path or a "4" with a checkmark, suggesting simplicity and completeness.]

**Transparent Down to the Last Drop**
Every ingredient is listed with a plain-English explanation. No proprietary blends, no hidden fragrances, no marketing buzzwords on the label.
[ICON NOTE: Simple line icon of an open book or a magnifying glass over a list, suggesting transparency and readability.]

---

## SECTION 3: PRODUCT GRID INTRO

If you are new to Bare Route, the Daily Defend Serum is where most people start — it is our bestseller and delivers the most visible results on its own. But The Routine is built to work as a system. Each step prepares your skin for the next, so you will see the best results when you use all four together. Below, they are listed in order of use: cleanser, toner, serum, moisturizer.

---

## SECTION 4: PRODUCT CARDS

**Clean Slate Gel Cleanser** — $28
A daily gel cleanser that removes dirt, oil, and sunscreen without stripping your skin's natural moisture barrier. Gentle enough for every morning and evening.
*Start Here*

**Tone & Balance Mist** — $24
An alcohol-free mist that rebalances your skin's pH after cleansing and preps it to absorb the active ingredients in your serum. Two spritzes, done.

**Daily Defend Serum** — $42
15% vitamin C and 5% niacinamide in a lightweight serum that brightens, evens tone, and defends against daily environmental stress. This is the workhorse.
*Bestseller*

**Barrier Repair Moisturizer** — $36
A ceramide-rich daily moisturizer that locks in your serum and strengthens your skin's moisture barrier. Light enough for morning, nourishing enough for night.

---

## SECTION 5: BOTTOM CTA

**Headline:** Not Sure Where to Start?

Every skin type is different, and The Routine works a little differently depending on yours. Our skin type quiz takes two minutes and tells you whether to start with the full set or a single product — plus how to adjust The Routine for your specific needs. No email required, no sales pitch at the end.

**CTA Button:** Take the Skin Type Quiz

**Bundle Callout:** Want the full system? The Routine Set includes all four products in a reusable linen pouch for $110 — that is $20 off buying them individually.

[DESIGN NOTE: This section should feel like a helpful off-ramp, not a sales push. Consider a two-column layout: the quiz CTA on the left with a brief illustration of the quiz flow (skin type, concerns, recommendation), and the bundle callout on the right with a product shot of the set in its linen pouch. Background should be slightly different from the rest of the page — a soft color block or a subtle texture change — so it feels like a distinct moment. Include a secondary text link below the quiz CTA: "Or chat with our skincare team" linking to customer support.]

---

### EXAMPLE OUTPUT ENDS HERE

# Email Post-Purchase Sequence (4-Email Series)

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A complete 4-email post-purchase sequence that turns one-time buyers into loyal repeat customers, covering order confirmation, shipping anticipation, review request, and cross-sell |
| **Turnaround** | 45-60 minutes per sequence |
| **Quality bar** | Production-ready copy that treats customers like people, not order numbers. Every email should make the customer feel good about their purchase and excited about the brand. |
| **Best for** | DTC brands building or overhauling their post-purchase automation, brands with low repeat purchase rates, clients whose current transactional emails feel robotic and template-driven |

---

## Client Brand Variables

Fill in every variable before pasting the prompt into Claude. If a variable is not applicable, write "N/A" — do not leave it blank.

```
[BRAND_NAME] — The brand's name exactly as it appears in customer-facing copy
[BRAND_VOICE] — 3-5 adjectives describing how the brand sounds (e.g., "direct, knowledgeable, slightly witty, no BS")
[TARGET_AUDIENCE] — Demographics + psychographics (e.g., "men and women 25-40 who want effective skincare without a 12-step routine")
[PRODUCT_SERVICE] — What the brand sells, in plain language (e.g., "clean, science-backed skincare essentials")
[PRICE_RANGE] — Lowest to highest price point for core products (e.g., "$24-65")
[KEY_DIFFERENTIATOR] — The one thing that makes this brand different from every competitor (e.g., "3-product routines backed by dermatologist research, no filler ingredients, no filler steps")
[COMPETITOR_NAMES] — 2-4 competitors the brand is positioned against (e.g., "CeraVe, The Ordinary, Drunk Elephant")
[WORDS_TO_USE] — Brand-approved vocabulary (e.g., "effective, straightforward, proven, real results, simple")
[WORDS_TO_AVOID] — Words that are off-brand or off-limits (e.g., "luxury, pamper, indulge, miracle, anti-aging, flawless")
[TONE_SCALE] — Where the brand sits on a 1-10 scale: 1 = ultra-corporate/formal, 10 = unhinged meme brand (e.g., "6 — smart and direct with a dry wit")
[CAMPAIGN_GOAL] — Primary goal for this sequence (e.g., "increase repeat purchase rate by 20% within 30 days of first order, generate 15%+ review submission rate")
[ADDITIONAL_CONTEXT] — Anything else: product usage instructions, typical shipping times, review platform used, cross-sell strategy, subscription option, loyalty program, etc.
```

### Dynamic Product Tokens

These tokens will be replaced by the ESP's dynamic content engine. Use them exactly as written in the copy:

```
[CUSTOMER_FIRST_NAME] — The customer's first name
[PRODUCT_NAME] — The product they purchased
[ORDER_NUMBER] — Their order number
[REVIEW_URL] — Direct link to leave a review for their specific product
[CROSS_SELL_PRODUCT] — The recommended cross-sell product name
[CROSS_SELL_URL] — Direct link to the cross-sell product page
[CROSS_SELL_IMAGE] — Dynamic image of the cross-sell product
[CROSS_SELL_PRICE] — Price of the cross-sell product
```

---

## The Prompt

Copy everything between the `---START PROMPT---` and `---END PROMPT---` markers. Replace all bracketed variables with the client's actual information before pasting into Claude.

---START PROMPT---

You are a senior DTC email strategist and copywriter who specializes in post-purchase customer experience. You understand that the moment after purchase is the most emotionally charged moment in the customer relationship — the buyer has committed money and is feeling a mix of excitement and buyer's anxiety. Your job is to reinforce that they made a great decision, build anticipation for the product, transition them from customer to fan, and set up the next purchase naturally. You never treat customers like transactions. Every email should feel like it was written by a real person who genuinely cares about the customer's experience.

**Your task:** Write a complete 4-email post-purchase sequence for the following brand.

### Brand Information

- **Brand name:** [BRAND_NAME]
- **Brand voice:** [BRAND_VOICE]
- **Target audience:** [TARGET_AUDIENCE]
- **Product/service:** [PRODUCT_SERVICE]
- **Price range:** [PRICE_RANGE]
- **Key differentiator:** [KEY_DIFFERENTIATOR]
- **Competitors:** [COMPETITOR_NAMES]
- **Words to use:** [WORDS_TO_USE]
- **Words to avoid:** [WORDS_TO_AVOID]
- **Tone scale (1-10):** [TONE_SCALE]
- **Campaign goal:** [CAMPAIGN_GOAL]
- **Additional context:** [ADDITIONAL_CONTEXT]

### Sequence Structure and Requirements

Write exactly 4 emails following this structure:

**Email 1 — Order Confirmation + Excitement Building (Send: Immediately after purchase)**
- Purpose: This is NOT just a receipt. It's the first brand experience after the customer committed their money. Reinforce the decision, build excitement, and make them feel like they joined something — not just bought something.
- Body length: 100-200 words
- Must include: Order number reference [ORDER_NUMBER], the product name [PRODUCT_NAME], a genuine "thank you" that doesn't feel templated, one interesting detail about the product or brand that makes them feel smart for buying, what to expect next (shipping timeline)
- Must NOT include: Upsells, cross-sells, or any ask. This email is purely about making the customer feel great.
- Emotional target: Validation + excitement ("I made a great choice")

**Email 2 — Shipping / Anticipation Builder (Send: 3 days after purchase, or triggered by shipping notification)**
- Purpose: Keep the excitement alive during the waiting period. Give them something useful to do or know before the product arrives. Turn the waiting into part of the experience.
- Body length: 100-200 words
- Must include: A reference to their order being on its way, 2-3 specific tips for when the product arrives (how to use it, how to store it, how to get the most out of it), a sense of insider knowledge ("most people don't know this, but...")
- Must NOT include: Any sales push. This email is pure value and anticipation.
- Emotional target: Anticipation + insider feeling ("I already feel like a pro")

**Email 3 — Check-In + Review Request (Send: 10 days after purchase)**
- Purpose: Check in on their experience. Ask for a review in a way that feels natural and easy — not transactional. Make leaving a review feel like contributing to a community, not doing the brand a favor.
- Body length: 100-200 words
- Must include: A genuine check-in question, a specific mention of [PRODUCT_NAME], a clear but non-pushy review request, the [REVIEW_URL] link, a note about how reviews help other customers (not the brand)
- Must NOT include: Incentives for reviews (no "leave a review for 10% off" — this devalues the review), demanding language, guilt about not reviewing
- Emotional target: Community + helpfulness ("my opinion actually matters")

**Email 4 — Cross-Sell / Replenishment (Send: 21 days after purchase)**
- Purpose: Introduce a complementary product or replenishment naturally. Make the recommendation feel like a thoughtful suggestion from someone who knows the customer's needs, not a sales pitch. This email should feel helpful.
- Body length: 100-200 words
- Must include: A reference to their original purchase [PRODUCT_NAME], the cross-sell recommendation [CROSS_SELL_PRODUCT] with [CROSS_SELL_URL], a specific reason why these products work well together, a [CROSS_SELL_IMAGE] placeholder, [CROSS_SELL_PRICE]
- Must NOT include: Heavy discounting, "you might also like" generic recommendations, language that implies their current product isn't enough
- Emotional target: Helpful discovery + smart upgrade ("oh, that makes sense")

### Formatting Requirements for EVERY Email

For each of the 4 emails, provide exactly this structure:

```
### Email [NUMBER]: [DESCRIPTIVE TITLE]
**Send timing:** [When this email triggers]
**Purpose:** [One-sentence internal note on this email's job]

**Subject Line Options:**
1. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
2. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
3. [Subject line] — [Predicted open rate ranking: Best/Good/Test]

**Preview Text:** [40-90 characters, complements subject line]

**Body Copy:**
[Full email body with formatting cues in brackets]
[Include all relevant dynamic tokens]

**CTA Button Text:** [Exact text for the primary button]

**Internal Notes:**
- Purpose: [What this email accomplishes in the relationship arc]
- A/B test suggestion: [One specific test to run]
- Segmentation note: [Conditional logic or exclusion rules]
- KPI to watch: [Primary metric]
- Timing note: [Any considerations about when this email should or shouldn't send]
```

### Writing Rules

1. **Human first, brand second.** Every email should sound like it was written by a person who happens to work at the brand — not by the brand's marketing department. Use "I" and "we" naturally. Reference the customer by name with [CUSTOMER_FIRST_NAME].
2. **No upselling in Emails 1-2.** The first two emails are about the customer's experience, not revenue. Any sales push before the customer has received their product will feel predatory and damage trust.
3. **Product specificity.** Always use [PRODUCT_NAME] — never say "your order" or "your recent purchase." The specific product name reminds them what they're excited about.
4. **Review request psychology.** In Email 3, frame the review as helping other customers make a decision — not as helping the brand. People are more motivated by helping peers than helping companies. Make the review process feel quick and easy (e.g., "takes 30 seconds").
5. **Cross-sell as recommendation.** In Email 4, the cross-sell should feel like a friend saying "oh, if you liked that, you'd love this." Frame it through the lens of their original purchase: "Now that you have [PRODUCT_NAME], [CROSS_SELL_PRODUCT] is the natural next step because..."
6. **Short paragraphs.** Max 2-3 sentences per paragraph. Mobile-first formatting. White space between sections.
7. **Anticipation building.** Emails 1-2 should make the customer more excited to receive their product, not just confirm logistics. Include interesting details, tips, or facts that make them feel like insiders.
8. **Tone consistency.** All 4 emails should sound like the same person writing over time. The tone warms slightly across the sequence (from grateful to familiar) but never shifts dramatically.
9. **No buyer's remorse triggers.** Never use language that could reintroduce doubt. No "hope you like it" (implies they might not). Instead: "you're going to love how [specific benefit]."
10. **Dynamic token placement.** Use tokens naturally within sentences, not as standalone blocks. "[CUSTOMER_FIRST_NAME], your [PRODUCT_NAME] is on its way" reads better than "[CUSTOMER_FIRST_NAME] — order update for [PRODUCT_NAME]."

---END PROMPT---

---

## Output Format

The output should be structured exactly as follows:

- **Total emails:** 4
- **Per email:** Subject lines (3), preview text (1), body copy with dynamic tokens and formatting cues, CTA button text (1), internal notes (5 sub-items)
- **Word counts per email body:** 100-200 words each
- **Total deliverable word count:** Approximately 800-1,600 words of copy, plus internal notes
- **Formatting:** Markdown with clear headers, bracketed formatting cues, and dynamic tokens matching the ESP's expected format
- **Naming convention:** Each email should have a descriptive title reflecting its role in the customer journey (e.g., "Email 1: You Made a Great Call")

---

## Quality Checks Before Sending

Run through every item before delivering to the client:

1. **No premature selling.** Emails 1 and 2 must contain zero upsells, cross-sells, or purchase asks. If you see any sales language in the first two emails, remove it immediately. The only job of Emails 1-2 is to make the customer feel great and build anticipation.
2. **Dynamic token accuracy.** Verify every dynamic token is correctly formatted: [CUSTOMER_FIRST_NAME], [PRODUCT_NAME], [ORDER_NUMBER], [REVIEW_URL], [CROSS_SELL_PRODUCT], [CROSS_SELL_URL], [CROSS_SELL_IMAGE], [CROSS_SELL_PRICE]. Missing brackets or typos will break the ESP integration.
3. **Review request tone.** Read Email 3 aloud. Does it sound like a friend asking "hey, how's it going?" or does it sound like a brand demanding feedback? If it feels transactional, rewrite it. Check that there are no incentives offered for reviews.
4. **Cross-sell logic.** Does the cross-sell in Email 4 make logical sense given the original purchase? The recommendation should feel like a natural complement, not a random product push. Ask: "If my friend bought [PRODUCT_NAME], would I genuinely suggest [CROSS_SELL_PRODUCT]?"
5. **Voice consistency across sequence.** Read all 4 emails in order. Does the tone warm naturally from Email 1 (grateful, excited) to Email 4 (familiar, helpful)? If any email breaks the tone arc, adjust it.
6. **Word count compliance.** Each email must be 100-200 words. Post-purchase emails should be concise and focused. If any email exceeds 200 words, trim the least essential content.
7. **Mobile readability.** No paragraph longer than 3 sentences. No sentence longer than 25 words. Check that CTAs are clear and tappable on a phone screen.

---

## Example Output

Below is a complete example output using the fictional brand **Bare Route** to demonstrate the quality bar and format expected from every deliverable.

**Brand variables used for this example:**
- Brand name: Bare Route
- Brand voice: Direct, knowledgeable, slightly witty, no BS, refreshingly honest
- Target audience: Men and women 25-40 tired of overcomplicated skincare routines, 12-step regimens, and products with ingredient lists that require a chemistry degree. They want effective skincare that respects their time and intelligence.
- Product/service: Clean, science-backed skincare essentials — a streamlined lineup of 5 core products (Daily Reset Cleanser, Barrier Repair Moisturizer, The SPF 30, Clarity Serum, Night Mode Overnight Treatment)
- Price range: $24-65
- Key differentiator: 3-product routines backed by dermatologist research. No filler ingredients, no filler steps. Everything in the line works together — or alone.
- Competitors: CeraVe, The Ordinary, Drunk Elephant
- Words to use: Effective, straightforward, proven, real results, simple, science-backed, works
- Words to avoid: Luxury, pamper, indulge, miracle, anti-aging, flawless, perfect skin, glow-up
- Tone scale: 6 — smart and direct with a dry wit. Think a knowledgeable friend who doesn't sugarcoat things.
- Campaign goal: Increase repeat purchase rate by 20% within 30 days of first order, generate 15%+ review submission rate
- Additional context: Typical shipping time is 3-5 business days. Reviews are collected via Judge.me. Cross-sell strategy: if customer buys the cleanser, recommend the moisturizer. If they buy the moisturizer, recommend The SPF 30. If they buy any single product, recommend the 3-Step Starter Set ($72, down from $89 if purchased separately). Products should be used in order: cleanser, serum/treatment, moisturizer, SPF. Night routine drops the SPF. Brand has a subscribe-and-save option at 15% off.

---

### Email 1: You Made the Right Call

**Send timing:** Immediately after purchase
**Purpose:** Make the customer feel great about their decision. Confirm the order. Build excitement for what's coming. Zero selling.

**Subject Line Options:**
1. Your [PRODUCT_NAME] is official. Here's what happens next. — Best (confirms the purchase, creates forward momentum, product-specific)
2. Good call, [CUSTOMER_FIRST_NAME]. — Good (personal, affirming, short — high open rate potential)
3. Order confirmed. Your skin just got an upgrade. — Test (confident, benefit-forward, slightly bold)

**Preview Text:** Order [ORDER_NUMBER] confirmed. The good stuff is coming. (55 characters)

**Body Copy:**

[HERO IMAGE: Clean product shot of their purchased product against a minimal white/gray background]

[CUSTOMER_FIRST_NAME] —

Your **[PRODUCT_NAME]** is in the queue. Order **[ORDER_NUMBER]** is confirmed and we're packing it now.

Quick thing you should know: every Bare Route product is formulated with a short, transparent ingredient list. No fillers, no "proprietary blends" that mean nothing. Your [PRODUCT_NAME] has 11 active ingredients. We could name all of them. (Most brands can't say that.)

**What happens next:**
- Your order ships within 24 hours
- You'll get a tracking email as soon as it leaves our warehouse
- Expected delivery: 3-5 business days

Thanks for choosing the straightforward route. We're going to take good care of your skin.

— The Bare Route Team

**CTA Button Text:** View Your Order

**Internal Notes:**
- Purpose: Reinforce the purchase decision, establish the brand's "smart and transparent" positioning, and create a positive first impression beyond the transaction. This email sets the tone for the entire post-purchase relationship.
- A/B test suggestion: Test subject line 1 (informational with product name) vs. subject line 2 (short and personal) to determine whether this audience prefers specificity or warmth in post-purchase communications
- Segmentation note: If this is a repeat customer, adjust the opening to "Welcome back, [CUSTOMER_FIRST_NAME]" and drop the ingredient education (they already know). If first-time buyer, keep the education to reinforce their decision.
- KPI to watch: Open rate. Post-purchase confirmation emails should hit 60-70%+ open rates. If below 50%, the subject lines need work.
- Timing note: This must send within minutes of purchase. Delay undermines the confirmation experience. If the ESP has a queue delay, set this flow to highest priority.

---

### Email 2: Your [PRODUCT_NAME] Is On Its Way (Read This Before It Arrives)

**Send timing:** 3 days after purchase (or triggered by shipping confirmation event)
**Purpose:** Build anticipation during the shipping wait. Provide insider tips that make the customer feel knowledgeable and excited to start using the product. Zero selling.

**Subject Line Options:**
1. Read this before your [PRODUCT_NAME] arrives — Best (creates urgency to open, useful framing, product-specific)
2. 3 things most people get wrong about skincare — Good (curiosity + authority, positions brand as expert)
3. Your order is on its way + a quick tip — Test (straightforward, lower curiosity but high clarity)

**Preview Text:** A few things that'll make a real difference. (47 characters)

**Body Copy:**

[HERO IMAGE: Lifestyle shot — product in a clean bathroom setting or being held]

[CUSTOMER_FIRST_NAME] —

Your **[PRODUCT_NAME]** is on its way. While you wait, a few tips that'll help you get the most out of it from day one.

**When it arrives:**

1. **Start simple.** If this is your first Bare Route product, use it on its own for a week before adding anything new. Your skin needs time to adjust, and stacking products on day one is the most common skincare mistake.

2. **Less is more. Literally.** A pea-sized amount of [PRODUCT_NAME] is all you need. Most people use 3x too much product and wonder why it feels heavy or pills up. Less product, better absorption.

3. **Consistency beats intensity.** The biggest results come from using it daily, not from using it aggressively. Twice a day (morning and night) for 2 weeks will show you what this product can really do.

One more thing most people don't know: our formulas are designed to work with your skin's natural pH cycle. Morning application works with your skin's higher pH. Night application works with the repair cycle. Same product, different benefits depending on timing.

Your skin's about to have a very good month.

**CTA Button Text:** Track Your Order

**Internal Notes:**
- Purpose: Turn the shipping wait into a positive brand experience. The tips serve two functions: they make the customer feel like an insider, and they set up proper usage expectations (which reduces returns and improves product efficacy). No selling — just value.
- A/B test suggestion: Test this tip-based version vs. a "day in the life" version showing how Bare Route fits into a morning routine. Both are educational but use different narrative structures.
- Segmentation note: If the product purchased is the cleanser, tailor tips to cleansing best practices. If it's the moisturizer, tailor to moisturizing technique. Product-specific tips will outperform generic skincare advice. If customer is a repeat buyer, swap tips for "what's new at Bare Route" content instead.
- KPI to watch: Open rate and click-through rate. This email should achieve 40-50% open rate. Track "Track Your Order" CTR — high click rates indicate engaged customers who are likely to convert again.
- Timing note: Ideally this email is triggered by the shipping notification event, not a static timer. If the ESP supports it, use the fulfillment event as the trigger. If not, 3 days post-purchase is a safe proxy for most shipping timelines.

---

### Email 3: How's Your Skin Doing?

**Send timing:** 10 days after purchase
**Purpose:** Genuine check-in on their experience. Natural transition into a review request that feels like community contribution, not a brand demand. No incentives for reviews.

**Subject Line Options:**
1. Quick question about your [PRODUCT_NAME] — Best (personal, specific, curiosity — "what question?")
2. It's been 10 days. How's your skin? — Good (check-in tone, genuine, references time for credibility)
3. [CUSTOMER_FIRST_NAME], we'd love to hear from you — Test (personal, warm, direct ask)

**Preview Text:** 30 seconds of your time helps more than you think. (52 characters)

**Body Copy:**

[CUSTOMER_FIRST_NAME] —

You've had your **[PRODUCT_NAME]** for about 10 days now. Enough time to form an honest opinion.

So — how's it going?

We're genuinely curious. And here's why your answer matters: **the next person deciding whether to try [PRODUCT_NAME] is going to read what you write.** We don't run ads with models. We let real customers tell the real story.

If you have 30 seconds, we'd love a quick review:

[BUTTON: Leave a Quick Review]

Doesn't need to be long. Doesn't need to be poetic. Just honest. That's the whole Bare Route thing.

A few prompts if you're staring at a blank box:
- How does your skin feel compared to 10 days ago?
- Was it easy to work into your routine?
- Would you recommend it to a friend?

Thanks for being part of this. Seriously.

— The Bare Route Team

[Review link: [REVIEW_URL]]

**CTA Button Text:** Leave a Quick Review

**Internal Notes:**
- Purpose: Generate authentic reviews that fuel acquisition. The framing — "the next person is going to read what you write" — leverages social motivation rather than brand loyalty. People are more willing to help a stranger make a good decision than to help a brand get more sales. The review prompts lower friction by eliminating the "what do I even say?" barrier.
- A/B test suggestion: Test this version (peer-helping framing) vs. a version that says "your review helps us make better products" (brand-improvement framing). Peer-helping typically wins for DTC brands.
- Segmentation note: Only send to customers whose order has been delivered (use tracking data if available). If the order hasn't arrived by day 10, delay this email until 3 days after delivery confirmation. Exclude customers who have already left a review. For customers who purchased multiple products, ask about the hero product (highest price).
- KPI to watch: Review submission rate. Target 15%+ of recipients leaving a review. If below 10%, test the subject line, simplify the review link (direct to form, no extra clicks), or add review prompts within the email itself.
- Timing note: 10 days is optimal for most products — enough time to form an opinion but recent enough that the experience is fresh. For skincare specifically, 10 days allows for visible results without waiting for a full skin cycle.

---

### Email 4: The Natural Next Step

**Send timing:** 21 days after purchase
**Purpose:** Introduce a complementary product that makes logical sense given their original purchase. Frame it as a helpful recommendation, not a sales push. This should feel like a knowledgeable friend saying "now that you have X, you should really try Y."

**Subject Line Options:**
1. If you liked [PRODUCT_NAME], this is the next move — Best (builds on existing positive experience, curiosity, natural progression)
2. The product that makes your [PRODUCT_NAME] work harder — Good (benefit-focused, implies synergy, smart framing)
3. [CUSTOMER_FIRST_NAME], a suggestion from someone who knows your routine — Test (personal, authority, conversational)

**Preview Text:** Your [PRODUCT_NAME] has a partner in crime. (43 characters)

**Body Copy:**

[CUSTOMER_FIRST_NAME] —

You've been using your **[PRODUCT_NAME]** for about 3 weeks now. If it's doing its job (and our formulation team is very confident it is), your skin is already responding.

Here's something worth knowing: **[PRODUCT_NAME] works well alone. It works even better with [CROSS_SELL_PRODUCT].**

[CROSS_SELL_IMAGE]

**[CROSS_SELL_PRODUCT] — [CROSS_SELL_PRICE]**

Here's why they're a pair: [PRODUCT_NAME] handles the active work — the cleansing, treating, or protecting. [CROSS_SELL_PRODUCT] handles the support — locking in the results and prepping your skin for what's next in the cycle.

Think of it as a one-two combination. You're already doing step one. Step two is where the compounding results happen.

**The straightforward version:** Your results at 30 days with both products will be noticeably better than with one alone. That's not marketing. That's formulation science.

If you want to simplify it further, our **3-Step Starter Set ($72)** bundles everything into one routine. It saves you $17 vs. buying separately, and it takes the guesswork out entirely.

[BUTTON: See How [CROSS_SELL_PRODUCT] Fits Your Routine]

**CTA Button Text:** See How [CROSS_SELL_PRODUCT] Fits Your Routine

**Internal Notes:**
- Purpose: Drive second purchase through logical recommendation. The cross-sell is framed through the lens of their existing product ("makes your [PRODUCT_NAME] work better") rather than a standalone pitch. The bundle mention gives a natural upgrade path for customers who want simplicity. This email should feel like expert advice, not a sales email.
- A/B test suggestion: Test the single cross-sell product recommendation vs. leading with the 3-Step Starter Set bundle. For some audiences, a bundle at a discount outperforms individual product recommendations because it removes the decision of "which one next?"
- Segmentation note: Cross-sell product should be dynamically determined based on their original purchase. Map the logic: Cleanser buyers get Moisturizer. Moisturizer buyers get SPF. Single product buyers get the Starter Set. Serum buyers get Night Mode. If the customer already purchased the cross-sell product, serve a different recommendation or skip this email. If the customer has repurchased their original product, send a subscribe-and-save offer instead.
- KPI to watch: Click-through rate and conversion rate. This email should benchmark 3-5% CTR and 1-3% conversion. If CTR is high but conversion is low, the product page may not be closing — audit the PDP.
- Timing note: 21 days is chosen specifically because the customer has used the product long enough to see results but hasn't yet started the repurchase consideration process. This is the window where a complementary product recommendation feels natural rather than premature.

---

### Sequence Summary

| Email | Day | Purpose | Ask | Target Word Count | Primary KPI |
|---|---|---|---|---|---|
| 1 — You Made the Right Call | 0 | Confirm + validate decision | None | 100-200 | Open rate (60-70%+) |
| 2 — Read This Before It Arrives | 3 | Anticipation + insider tips | None | 100-200 | Open rate (40-50%) |
| 3 — How's Your Skin Doing? | 10 | Check-in + review request | Review | 100-200 | Review submission (15%+) |
| 4 — The Natural Next Step | 21 | Cross-sell recommendation | Purchase | 100-200 | CTR (3-5%), CVR (1-3%) |

**Recommended ESP setup notes:**
- Email 1 must be highest-priority and send within minutes of purchase. Any delay longer than 5 minutes creates a negative experience.
- Email 2 should ideally trigger from the shipping/fulfillment event rather than a static timer. If the ESP does not support fulfillment event triggers, use the 3-day timer as a proxy.
- Email 3 should only send to customers whose order status is "delivered." If delivery tracking is not available, add a 2-day buffer beyond the expected delivery window to be safe. Never ask for a review before the product arrives.
- Email 4 cross-sell product should be mapped dynamically based on purchase history. Build a simple product-to-recommendation matrix and set it up as conditional content in the ESP.
- Add an exit condition: if the customer makes a second purchase at any point during the sequence, skip directly to Email 3 (review request for the new product) and restart the cross-sell timer.
- Tag all customers who complete the full sequence without purchasing again as "post-purchase-no-repeat" for a targeted winback or re-engagement campaign at day 45.
- Customers who leave a review in Email 3 should be tagged as "reviewer" and entered into a loyalty or ambassador program flow if one exists.

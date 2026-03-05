# Email Abandoned Cart Recovery Sequence (3-Email Series)

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A complete 3-email abandoned cart recovery sequence with escalating urgency, including subject lines, preview text, short body copy, CTAs, and dynamic product tokens |
| **Turnaround** | 30-45 minutes per sequence |
| **Quality bar** | Production-ready copy that integrates with Klaviyo, Omnisend, or any ESP's abandoned cart flow with dynamic product blocks |
| **Best for** | DTC brands launching or refreshing their cart abandonment automation, brands with cart abandonment rates above 65%, clients whose current abandoned cart emails feel generic or robotic |

---

## Client Brand Variables

Fill in every variable before pasting the prompt into Claude. If a variable is not applicable, write "N/A" — do not leave it blank.

```
[BRAND_NAME] — The brand's name exactly as it appears in customer-facing copy
[BRAND_VOICE] — 3-5 adjectives describing how the brand sounds (e.g., "warm, sophisticated, inviting, grounded")
[TARGET_AUDIENCE] — Demographics + psychographics (e.g., "women 28-45 who invest in home ambiance and self-care rituals")
[PRODUCT_SERVICE] — What the brand sells, in plain language (e.g., "hand-poured soy candles in seasonal and signature scents")
[PRICE_RANGE] — Lowest to highest price point for core products (e.g., "$32-58")
[KEY_DIFFERENTIATOR] — The one thing that makes this brand different from every competitor (e.g., "100-hour burn time with scent profiles designed by a former perfumer")
[COMPETITOR_NAMES] — 2-4 competitors the brand is positioned against (e.g., "Yankee Candle, Boy Smells, Diptyque")
[WORDS_TO_USE] — Brand-approved vocabulary (e.g., "cozy, handcrafted, warm, intentional, ritual")
[WORDS_TO_AVOID] — Words that are off-brand or off-limits (e.g., "cheap, bargain, basic, mainstream, fake")
[TONE_SCALE] — Where the brand sits on a 1-10 scale: 1 = ultra-corporate/formal, 10 = unhinged meme brand (e.g., "5 — warm and conversational but elegant")
[CAMPAIGN_GOAL] — Primary goal for this sequence (e.g., "recover 10-15% of abandoned carts within 48 hours")
[ADDITIONAL_CONTEXT] — Anything else: typical cart value, most-abandoned products, free shipping threshold, discount caps, return policy, etc.
```

### Dynamic Product Tokens

These tokens will be replaced by the ESP's dynamic content engine. Use them exactly as written in the copy:

```
[PRODUCT_NAME] — The specific product left in cart
[PRODUCT_IMAGE] — Dynamic image block showing the abandoned product
[PRODUCT_PRICE] — The price of the abandoned product
[CART_URL] — Direct link back to the customer's saved cart
[CUSTOMER_FIRST_NAME] — The customer's first name (if available)
```

---

## The Prompt

Copy everything between the `---START PROMPT---` and `---END PROMPT---` markers. Replace all bracketed variables with the client's actual information before pasting into Claude.

---START PROMPT---

You are an expert DTC email copywriter specializing in abandoned cart recovery. You understand the psychology of cart abandonment — the customer was interested enough to add to cart, which means the desire exists. Your job is not to create desire; it is to remove friction and reignite the moment. You know that the best abandoned cart emails feel like a helpful nudge from a friend, not a desperate sales pitch from a brand.

**Your task:** Write a complete 3-email abandoned cart recovery sequence for the following brand.

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

Write exactly 3 emails following this escalating strategy:

**Email 1 — Friendly Reminder (Send: 1 hour after abandonment)**
- Tone: Light, casual, helpful. Like a friend saying "hey, you left this here."
- Strategy: NO discount. NO urgency. Simply remind them what they left behind and make it easy to go back.
- Body length: 75-150 words. SHORT. This is a tap on the shoulder, not a speech.
- Must include: The product by name (using [PRODUCT_NAME] token), a product image placeholder, a direct link back to cart, a one-line reason why the product is worth it
- Must NOT include: Any discount or incentive, fake urgency, guilt-tripping, "your cart is expiring" nonsense

**Email 2 — Social Proof Nudge (Send: 24 hours after abandonment)**
- Tone: Confident, warm, trust-building. Let other customers do the selling.
- Strategy: NO discount. Use reviews and social proof to address the hesitation that caused the abandonment.
- Body length: 75-150 words. Still short. Social proof should be the hero, not lengthy copy.
- Must include: 2-3 customer review snippets specifically about the type of product left in cart, a star rating visual reference, the product by name again, a product image placeholder
- Must NOT include: Any discount or incentive, desperation ("don't miss out!"), passive-aggressive tone

**Email 3 — Urgency + Incentive (Send: 48 hours after abandonment)**
- Tone: Direct, genuine, warm. This is a real offer, not fake scarcity.
- Strategy: Introduce a small discount OR free shipping. Create honest urgency around the incentive having an expiration.
- Body length: 75-150 words. Tight and action-oriented.
- Must include: A specific incentive (percentage off or free shipping — use brand context to decide), a real deadline for the incentive (48-hour window), the product by name, risk reversal (return policy, guarantee, etc.), the strongest CTA of the sequence
- Must NOT include: Fake countdown timers, "last chance EVER" language, guilt about abandoning, multiple competing CTAs

### Formatting Requirements for EVERY Email

For each of the 3 emails, provide exactly this structure:

```
### Email [NUMBER]: [DESCRIPTIVE TITLE]
**Send timing:** [When this email triggers relative to cart abandonment]
**Strategy:** [One sentence: what this email does and does NOT do]

**Subject Line Options:**
1. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
2. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
3. [Subject line] — [Predicted open rate ranking: Best/Good/Test]

**Preview Text:** [40-90 characters, complements subject line]

**Body Copy:**
[Full email body — SHORT — with formatting cues in brackets]
[Include dynamic tokens: [PRODUCT_NAME], [PRODUCT_IMAGE], [PRODUCT_PRICE], [CART_URL]]

**CTA Button Text:** [Exact button text]

**Internal Notes:**
- Strategy: [What this email does in the recovery arc]
- A/B test suggestion: [One specific test to run]
- Segmentation note: [Conditional logic or exclusion rules]
- KPI to watch: [Primary metric]
- Recovery rate benchmark: [Expected % of carts recovered by this email]
```

### Writing Rules

1. **Brevity is everything.** Abandoned cart emails are not the place for storytelling. Get in, remind, get out. 75-150 words per email body, no exceptions.
2. **Show the product.** Every email must have a [PRODUCT_IMAGE] placeholder. The product image does most of the selling in cart recovery emails.
3. **Use the product name.** Always reference [PRODUCT_NAME] — never say "the item in your cart" or "your product." The specific name re-triggers the desire.
4. **One CTA per email.** One button. One action. "Go back to your cart" or "Complete your order." No secondary links competing for attention.
5. **Conversational, not corporate.** These emails should feel like they were written by a human who works at the brand, not an automated system. Avoid "We noticed you left something in your cart" — that's been done a million times.
6. **Escalation is key.** Email 1 is a nudge. Email 2 is reassurance. Email 3 is a genuine offer. Do not front-load the incentive. People who will buy without a discount should never see one.
7. **Dynamic tokens.** Use [PRODUCT_NAME], [PRODUCT_IMAGE], [PRODUCT_PRICE], and [CART_URL] exactly as written. The ESP will replace these dynamically.
8. **No guilt.** Never use language that makes the customer feel bad for not buying. "Your cart is getting lonely" is tired. "We're heartbroken you left" is manipulative. Keep it light.
9. **Email 3 honesty.** The incentive in Email 3 should be genuine and specific. "Here's 10% off" with a 48-hour window is honest urgency. "This deal won't last forever!!!" is not.
10. **Mobile-first.** Every email will be read on a phone. Short paragraphs. Big CTA button. Scannable in 5 seconds.

---END PROMPT---

---

## Output Format

The output should be structured exactly as follows:

- **Total emails:** 3
- **Per email:** Subject lines (3), preview text (1), body copy with dynamic tokens and formatting cues, CTA button text (1), internal notes (5 sub-items)
- **Word counts per email body:** 75-150 words each. Hard limit. Cart recovery emails that run long underperform.
- **Total deliverable word count:** Approximately 500-900 words of copy, plus internal notes
- **Formatting:** Markdown with clear headers, bracketed formatting cues, and dynamic tokens in the exact format the ESP expects
- **Naming convention:** Each email should have a descriptive title reflecting its role in the escalation (e.g., "Email 1: The Gentle Nudge")

---

## Quality Checks Before Sending

Run through every item before delivering to the client:

1. **Word count discipline:** Each email body must be 75-150 words. Cart recovery emails are NOT the place for long copy. If any email exceeds 150 words, cut it. Read it on a phone screen preview — if you have to scroll more than once, it's too long.
2. **Escalation logic:** Confirm the three emails follow the correct escalation: reminder (no discount) then social proof (no discount) then incentive (discount or free shipping). If Email 1 mentions a discount, the sequence is broken.
3. **Dynamic token accuracy:** Verify that [PRODUCT_NAME], [PRODUCT_IMAGE], [PRODUCT_PRICE], and [CART_URL] appear correctly and are not misspelled or missing brackets. The ESP will break if tokens are wrong.
4. **No guilt language:** Read each email and ask: "Would I feel bad after reading this?" If yes, rewrite. Check for passive aggression, fake sadness, loneliness metaphors, or any language that pressures through guilt.
5. **CTA specificity:** Each CTA button should be clear and action-oriented. "Complete Your Order" is fine. "Shop Now" is generic. "Return to Your [PRODUCT_NAME]" is best when the ESP supports dynamic CTA text.
6. **Subject line distinctiveness:** All 9 subject lines across the 3 emails should use different approaches. No two should start with the same word or use the same emotional trigger.
7. **Brand voice consistency:** Read all 3 emails in sequence. They should sound like the same person wrote them, matching the brand voice variables exactly. The tone should warm up slightly across the sequence but never shift dramatically.

---

## Example Output

Below is a complete example output using the fictional brand **Ember & Oak** to demonstrate the quality bar and format expected from every deliverable.

**Brand variables used for this example:**
- Brand name: Ember & Oak
- Brand voice: Warm, inviting, sophisticated but not stuffy, grounded, intentional
- Target audience: Women 28-45 who invest in their living spaces, appreciate craftsmanship, see candles as part of a daily ritual — not just background decor. They shop at West Elm, drink good wine, and notice when a scent fills a room.
- Product/service: Hand-poured soy candles in signature and seasonal scents (Fireside Amber, Cedar & Vanilla, Wild Honeysuckle, Smoked Fig, Coastal Morning)
- Price range: $32-58
- Key differentiator: 100-hour burn time (3x competitors), scent profiles designed by a former fine fragrance perfumer, hand-poured in small batches in Portland
- Competitors: Yankee Candle, Boy Smells, Diptyque, Voluspa
- Words to use: Handcrafted, warm, intentional, ritual, small-batch, slow down, glow
- Words to avoid: Cheap, basic, mainstream, fake, synthetic, mass-produced
- Tone scale: 5 — warm and conversational but with an elegance to it. Think a good friend who also has excellent taste.
- Campaign goal: Recover 12-15% of abandoned carts within 48 hours
- Additional context: Average cart value is $48. Free shipping on orders over $50. Most abandoned product is the Fireside Amber ($38). Return/exchange policy: 30-day no-questions-asked. The brand does NOT do frequent discounts — any incentive should feel special and rare. Preferred incentive: free shipping (lower threshold to $0) rather than percentage off.

---

### Email 1: Still Thinking It Over?

**Send timing:** 1 hour after cart abandonment
**Strategy:** Light, friendly reminder. Show the product. Make it effortless to return to cart. Absolutely no discount or pressure.

**Subject Line Options:**
1. You left something warm behind — Best (sensory, intriguing, brand-aligned without being clickbait)
2. Still on your mind? — Good (short, personal, works well as a gentle nudge)
3. Your [PRODUCT_NAME] is waiting — Test (direct, product-specific, uses dynamic token in subject)

**Preview Text:** It's still in your cart — and still hand-poured. (49 characters)

**Body Copy:**

[PRODUCT_IMAGE: Dynamic image block showing the abandoned product]

Hey [CUSTOMER_FIRST_NAME] —

Good taste. The **[PRODUCT_NAME]** is one of our most-loved scents — hand-poured in small batches with a 100-hour burn time that outlasts anything on your shelf.

We saved your cart so you can pick up right where you left off. No rush. But if you've been thinking about it, trust the instinct.

**[PRODUCT_NAME] — [PRODUCT_PRICE]**

[BUTTON: Return to Your Cart]

**CTA Button Text:** Return to Your Cart

**Internal Notes:**
- Strategy: This email is a simple, warm reminder. The product image and name do the heavy lifting. The copy just needs to make returning to cart feel effortless and reaffirm that they chose well. No discount, no urgency — just a nudge.
- A/B test suggestion: Test subject line 1 (sensory/emotional) vs. subject line 3 (product-specific with dynamic token) to determine if personalization or brand atmosphere drives higher opens for this audience
- Segmentation note: Exclude customers who have already completed their purchase since abandonment. If cart value is over $50, mention free shipping eligibility in the body. If customer is a repeat buyer, adjust tone to "Welcome back — you left your [PRODUCT_NAME] behind."
- KPI to watch: Click-through rate back to cart. Benchmark 8-12% CTR for first cart recovery email.
- Recovery rate benchmark: 5-8% of total abandoned carts should recover from this email alone.

---

### Email 2: People Really Love That One

**Send timing:** 24 hours after cart abandonment
**Strategy:** Social proof to overcome hesitation. Real reviews about the product they left behind. Still no discount — let other customers close the sale.

**Subject Line Options:**
1. Here's what people say about [PRODUCT_NAME] — Best (specific, curiosity, leverages social proof in subject)
2. 1,200+ five-star reviews. Here's why. — Good (number-driven credibility, curiosity gap)
3. You picked a good one — Test (short, affirming, less aggressive)

**Preview Text:** Don't just take our word for it. (33 characters)

**Body Copy:**

[PRODUCT_IMAGE: Dynamic image block showing the abandoned product]

We get it — spending [PRODUCT_PRICE] on a candle is a decision. So let us step aside and let our customers do the talking.

**On [PRODUCT_NAME]:**

⭐⭐⭐⭐⭐ *"This candle turned my living room into a place I actually want to be. The scent is sophisticated without being overpowering. I'm on my third one."* — Rebecca M.

⭐⭐⭐⭐⭐ *"I've spent twice this on candles that burned out in a week. Ember & Oak burns forever and the scent is still going strong at the halfway mark."* — Sarah L.

⭐⭐⭐⭐⭐ *"Bought it for myself. Bought two more as gifts. No regrets on any of them."* — Kate D.

**1,200+ five-star reviews** and counting. Your **[PRODUCT_NAME]** is still in your cart.

[BUTTON: Complete Your Order]

**CTA Button Text:** Complete Your Order

**Internal Notes:**
- Strategy: The customer added to cart, so desire exists. The hesitation is likely price, timing, or uncertainty about quality. Social proof addresses quality directly. The reviews are crafted to address specific objections: scent quality, burn time (value for money), and giftability.
- A/B test suggestion: Test this version with written reviews vs. a version featuring Instagram UGC screenshots showing the candle in real homes. Visual social proof can outperform text reviews for aesthetic brands.
- Segmentation note: If the abandoned product has specific reviews in the review platform (Yotpo, Judge.me), pull actual reviews dynamically. If not, these templated reviews work as fallback. Exclude anyone who purchased since Email 1.
- KPI to watch: Click-through rate and conversion rate. This email often has the highest conversion of the 3-email series because social proof resolves the specific objection holding the customer back.
- Recovery rate benchmark: Additional 3-5% of remaining abandoned carts (those not recovered by Email 1).

---

### Email 3: Free Shipping on Us (Just This Once)

**Send timing:** 48 hours after cart abandonment
**Strategy:** Genuine incentive with a real deadline. Free shipping offer (brand's preferred incentive) with a 48-hour expiration. Honest urgency, not manufactured panic.

**Subject Line Options:**
1. Free shipping on your [PRODUCT_NAME] — ends Thursday — Best (specific offer + specific deadline + product name = high intent subject line)
2. We don't do this often: free shipping, 48 hours — Good (scarcity framing, brand honesty, time-bound)
3. One small thing to make this easier — Test (soft, curiosity, empathetic framing)

**Preview Text:** We removed the last barrier. 48 hours only. (45 characters)

**Body Copy:**

[PRODUCT_IMAGE: Dynamic image block showing the abandoned product]

[CUSTOMER_FIRST_NAME] —

We're not big on discounts. We'd rather put that money into better wax, better scents, better everything. But we also know that sometimes free shipping is the nudge that turns "maybe" into "yes."

So here it is: **free shipping on your order. No minimum. 48 hours only.**

**Your cart:**
[PRODUCT_NAME] — [PRODUCT_PRICE]
Shipping: ~~$5.95~~ **FREE**

This offer expires in 48 hours and won't be extended. We mean that kindly — we just don't do this often.

And if you're still on the fence: every Ember & Oak candle comes with a **30-day, no-questions-asked return policy.** If you don't love it, we'll make it right.

[BUTTON: Get Free Shipping on Your [PRODUCT_NAME]]

**CTA Button Text:** Get Free Shipping on Your [PRODUCT_NAME]

**Internal Notes:**
- Strategy: This is the closer. The incentive is free shipping (not a percentage discount), which aligns with the brand's positioning — they don't discount, they remove friction. The 48-hour window is genuine and honest. The return policy removes the last layer of risk. Everything is designed to make saying "yes" feel easy and smart.
- A/B test suggestion: Test free shipping vs. 10% off to determine which incentive recovers more carts at a lower cost. For premium brands, free shipping often outperforms percentage discounts because it doesn't devalue the product.
- Segmentation note: Only send to customers who received Emails 1 and 2 but did NOT purchase. If cart value already qualifies for free shipping (over $50), swap the incentive to a small gift-with-purchase or a free travel-size candle. Exclude repeat customers with 3+ orders — they should receive a different, loyalty-focused recovery email.
- KPI to watch: Conversion rate and revenue recovered. This email should have the highest conversion rate of the sequence.
- Recovery rate benchmark: Additional 3-5% of remaining abandoned carts. Total sequence recovery target: 12-15%.

---

### Sequence Summary

| Email | Timing | Strategy | Incentive | Target Word Count | Recovery Benchmark |
|---|---|---|---|---|---|
| 1 — Still Thinking It Over? | 1 hour | Gentle reminder | None | 75-150 | 5-8% |
| 2 — People Really Love That One | 24 hours | Social proof | None | 75-150 | 3-5% |
| 3 — Free Shipping on Us | 48 hours | Incentive + urgency | Free shipping | 75-150 | 3-5% |

**Total expected recovery rate:** 12-15% of abandoned carts

**Recommended ESP setup notes:**
- Add a checkout completion trigger to exit customers from this flow the moment they purchase. Do not send Email 2 or 3 to someone who already converted.
- Email 3's incentive should auto-generate a unique discount code or free shipping code tied to the customer's email. Generic codes get shared and abused.
- If the brand has multiple products in the abandoned cart, show the highest-priced item as the hero image and list other items below it.
- Set up a "cart recovery" tag for all customers who convert through this flow for future cohort analysis and to exclude them from aggressive promotional sends for 14 days.
- Consider adding a fourth email at 7 days for high-value carts (over $100) with a personal note from the founder. This is optional and brand-dependent.

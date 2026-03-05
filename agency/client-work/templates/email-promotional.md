# Email Promotional (Single Email, 4 Variants)

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A single promotional email in 4 ready-to-use variants: Product Launch, Sale/Discount, Restock Notification, and Limited Edition/Collab Drop. Each variant is a standalone email with subject lines, preview text, body copy, and CTA. |
| **Turnaround** | 30-45 minutes for all 4 variants |
| **Quality bar** | Production-ready promotional copy that drives clicks and conversions. Every variant should have a clear hook in the first two lines (above-the-fold content), honest urgency, and a single compelling CTA. |
| **Best for** | DTC brands running seasonal campaigns, launching new products, announcing restocks, or promoting limited editions. Use this template any time the client needs a one-off promotional email that isn't part of an automated sequence. |

---

## Client Brand Variables

Fill in every variable before pasting the prompt into Claude. If a variable is not applicable, write "N/A" — do not leave it blank.

```
[BRAND_NAME] — The brand's name exactly as it appears in customer-facing copy
[BRAND_VOICE] — 3-5 adjectives describing how the brand sounds (e.g., "playful, honest, a little cheeky, energetic")
[TARGET_AUDIENCE] — Demographics + psychographics (e.g., "women 25-40 who want snacks that taste amazing without compromising on ingredients")
[PRODUCT_SERVICE] — What the brand sells, in plain language (e.g., "organic snack mixes and crunchy bites in bold flavors")
[PRICE_RANGE] — Lowest to highest price point for core products (e.g., "$8-24")
[KEY_DIFFERENTIATOR] — The one thing that makes this brand different (e.g., "organic snacks that taste like a flavor explosion, not like cardboard")
[COMPETITOR_NAMES] — 2-4 competitors (e.g., "RXBar, KIND, Lesser Evil")
[WORDS_TO_USE] — Brand-approved vocabulary (e.g., "crunchy, wild, bold, real, flavor-packed")
[WORDS_TO_AVOID] — Words that are off-brand (e.g., "guilt-free, skinny, diet, cheat day")
[TONE_SCALE] — 1-10 scale (e.g., "7 — playful and fun but not trying too hard")
[CAMPAIGN_GOAL] — Primary goal (e.g., "drive first-day sales for new product launch" or "clear 500 units of seasonal inventory")
[ADDITIONAL_CONTEXT] — Specific promo details: product name, discount percentage, restock product, collab partner, launch date, inventory quantities, promo code, expiration date, etc.
```

### Promotional-Specific Variables

These additional variables are needed for promotional emails. Fill in whichever apply to the specific variant being used:

```
[PROMO_PRODUCT_NAME] — The specific product being promoted (new launch, restocked item, etc.)
[PROMO_PRODUCT_PRICE] — Price of the promoted product
[PROMO_PRODUCT_IMAGE] — Hero image of the promoted product
[DISCOUNT_CODE] — Promo code if applicable
[DISCOUNT_AMOUNT] — Percentage or dollar amount off
[SALE_END_DATE] — When the promotion expires
[INVENTORY_COUNT] — Remaining stock for scarcity (only if real)
[COLLAB_PARTNER] — Name of collaboration partner if applicable
[LAUNCH_DATE] — Date the product becomes available
```

---

## The Prompt

Copy everything between the `---START PROMPT---` and `---END PROMPT---` markers. Replace all bracketed variables with the client's actual information before pasting into Claude.

---START PROMPT---

You are a high-performing DTC email copywriter who writes promotional emails that get clicked. You understand that every promotional email is competing with 50+ other emails in the inbox, and you have roughly 3 seconds to earn the open and another 5 seconds to earn the click. You write punchy, compelling copy that gets to the point fast. You lead with the most interesting thing, use social proof and scarcity honestly, and make every CTA impossible to ignore. You never write generic promotional emails that could belong to any brand — every word should feel like it came from THIS brand.

**Your task:** Write a single promotional email in 4 distinct variants for the following brand. Each variant serves a different promotional purpose but should all sound like the same brand.

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

### Variant Structure and Requirements

Write 4 complete email variants, each for a different promotional scenario:

**Variant A — Product Launch Announcement**
- Purpose: Announce a new product and drive first-day/first-week sales. Build excitement around something genuinely new.
- Body length: 100-200 words
- Must include: The product name and what it is, why it exists (the "gap" it fills), 1-2 key features or differentiators, the price, a sense of newness and first-mover advantage, one social proof element (beta tester quote, internal team hype, waitlist size)
- First 2 lines: Must work as "above the fold" content — if the customer only sees the first two lines in their email preview, they should know exactly what's new and why it matters.
- CTA: Drive to product page or pre-order page. Single CTA.

**Variant B — Sale / Discount Promotion**
- Purpose: Drive volume during a sale event. Make the discount feel worthwhile without devaluing the brand.
- Body length: 100-200 words
- Must include: The specific discount amount and code, what's included (sitewide, specific products, bundles), a clear deadline, a reason for the sale (seasonal, anniversary, appreciation — never "we need to clear inventory"), a bestseller callout to reduce decision fatigue
- First 2 lines: Lead with the offer. Do not bury the discount below a greeting. The number should appear in the first sentence.
- CTA: Drive to sale page or collection with code auto-applied. Single CTA.

**Variant C — Restock Notification**
- Purpose: Notify customers that a previously sold-out product is back. Leverage the built-in demand and scarcity.
- Body length: 100-200 words
- Must include: The product name and the fact that it's back, acknowledgment that it sold out (social proof built in), why it sold out (popularity, organic demand — not supply chain issues), a "this is your shot" framing without fake urgency, inventory context if appropriate (e.g., "limited restock of 500 units")
- First 2 lines: Product name + "back in stock" should appear in the first sentence. Do not build up to the news. Lead with it.
- CTA: Drive directly to the product page. Single CTA.

**Variant D — Limited Edition / Collab Drop**
- Purpose: Create excitement around a limited edition product or brand collaboration. Drive urgency through genuine scarcity and exclusivity.
- Body length: 100-200 words
- Must include: The collab partner or limited edition concept, why this partnership or edition exists, what makes it different from the core line, specific scarcity details (quantity produced, drop date, time-limited availability), the price, a "for the real fans" energy without being exclusionary
- First 2 lines: The collab partner or limited edition name should appear in the first sentence. Lead with the most exciting element.
- CTA: Drive to the drop page. Single CTA. Consider "Shop the Drop" or "Get Yours Before They're Gone."

### Formatting Requirements for EVERY Variant

For each of the 4 variants, provide exactly this structure:

```
### Variant [LETTER]: [VARIANT TYPE]
**Promotional purpose:** [One-sentence description]

**Subject Line Options:**
1. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
2. [Subject line] — [Predicted open rate ranking: Best/Good/Test]
3. [Subject line] — [Predicted open rate ranking: Best/Good/Test]

**Preview Text:** [40-90 characters, complements subject line]

**Body Copy:**
[Full email body with formatting cues]
[First 2 lines must work as standalone above-the-fold content]

**CTA Button Text:** [Exact button text]

**Internal Notes:**
- Strategy: [What makes this variant effective]
- A/B test suggestion: [One specific test to run]
- Send timing: [Best day/time to send this type of promo]
- Segmentation note: [Who should and shouldn't receive this]
- KPI to watch: [Primary metric]
```

### Writing Rules

1. **First 2 lines are everything.** In every variant, the first two lines of the email body should work as above-the-fold content. If a customer opens this email and only sees the first two lines before scrolling, they should know exactly what's being offered and why they should care. Do not waste the opening on greetings or pleasantries.
2. **Lead with the most compelling hook.** Each variant type has a different hook. Product launch: what's new and why it's exciting. Sale: the discount number. Restock: the product is back. Collab: the partnership reveal. Get to the hook in the first sentence.
3. **Honest scarcity only.** If quantity is limited, state the real number. If the sale has a real end date, state it. Never use "limited time" without a specific time. Never use "selling fast" unless there's data to support it. Fake urgency destroys trust and unsubscribes people.
4. **Specific numbers.** "20% off" is better than "big savings." "Only 300 made" is better than "limited edition." "Ends Friday at midnight EST" is better than "don't wait." Specificity is credibility.
5. **Single CTA, crystal clear.** One button. One action. The button text should tell the customer exactly what happens when they click. "Shop the New [Product Name]" beats "Shop Now." "Get 20% Off" beats "Learn More."
6. **Social proof where natural.** Every variant should include at least one social proof element: a review quote, a sold-out history, a waitlist size, a customer count, or an influencer mention. Social proof should feel organic, not forced.
7. **Brand voice consistency.** All 4 variants should unmistakably sound like the same brand. A customer who receives Variant A in January and Variant B in March should feel like they're hearing from the same person.
8. **Short paragraphs.** 2-3 sentences max per paragraph. Scannable on mobile. If you squint at the email and it looks like a wall of text, add more white space.
9. **No stacking promotions.** Each variant should have ONE offer, ONE CTA, ONE action. Do not combine a product launch with a discount with a free shipping offer. Complexity kills conversion.
10. **Urgency proportional to variant.** Product launch: moderate urgency (newness). Sale: high urgency (deadline). Restock: high urgency (will sell out again). Collab: highest urgency (true limited run). Match the urgency level to the reality of the offer.

---END PROMPT---

---

## Output Format

The output should be structured exactly as follows:

- **Total variants:** 4 (A: Product Launch, B: Sale/Discount, C: Restock, D: Limited Edition/Collab)
- **Per variant:** Subject lines (3), preview text (1), body copy with formatting cues, CTA button text (1), internal notes (5 sub-items)
- **Word counts per variant body:** 100-200 words each
- **Total deliverable word count:** Approximately 800-1,600 words of copy across all 4 variants, plus internal notes
- **Formatting:** Markdown with clear headers, variant labels (A/B/C/D), bracketed formatting cues
- **Naming convention:** Each variant labeled by type (e.g., "Variant A: Product Launch")

---

## Quality Checks Before Sending

Run through every item before delivering to the client:

1. **Above-the-fold test:** For each variant, read only the first 2 lines of the body copy. Without scrolling further, do you know exactly what the email is about and why you should care? If not, rewrite the opening. The first 2 lines must stand alone as compelling content.
2. **Single CTA enforcement:** Each variant must have exactly one CTA button. If you see two buttons, secondary links, or competing actions, remove all but the primary one. Promotional emails with multiple CTAs have lower click rates.
3. **Scarcity honesty audit:** Check every urgency or scarcity claim in all 4 variants. Is it real? Is it specific? "Limited edition" must include a number. "Sale ends" must include a date and time. "Selling fast" must be provably true. Remove any vague urgency language.
4. **Subject line variety:** All 12 subject lines across the 4 variants should use different approaches. Check for repetitive formulas, repeated opening words, or similar emotional triggers. Each set of 3 should offer distinct testing angles.
5. **Brand voice audit:** Read all 4 variants back-to-back. Do they sound like the same brand? The tone may vary slightly (a sale email is more energetic than a restock email) but the personality should be identical.
6. **Specific numbers check:** Each variant should include at least 2 specific numbers: price, discount percentage, units available, review count, date, or time. Vague promotional emails underperform specific ones.
7. **Word count compliance:** Each variant body must be 100-200 words. Promotional emails are scanned, not read. If any variant exceeds 200 words, cut the least essential content.

---

## Example Output

Below is a complete example output using the fictional brand **Wild Bites** to demonstrate the quality bar and format expected from every deliverable. This example shows a product launch variant (Variant A) for a new flavor, with all 4 variants written out.

**Brand variables used for this example:**
- Brand name: Wild Bites
- Brand voice: Playful, honest, a little cheeky, energetic, approachable
- Target audience: Women 25-40 who want snacks that aren't boring health food
- Product/service: Organic snack mixes and crunchy bites in bold flavors
- Price range: $8-24
- Key differentiator: Organic snacks that actually taste like a flavor explosion, not cardboard
- Competitors: RXBar, KIND, Lesser Evil
- Words to use: Crunchy, wild, bold, real, snack smarter, flavor-packed, game-changer
- Words to avoid: Guilt-free, skinny, diet, cheat day, clean eating, superfood
- Tone scale: 7 — playful and fun but not trying too hard
- Campaign goal: Drive first-week sales for the new Spicy Dill Pickle flavor
- Additional context: Wild Bites is launching a 6th flavor: Spicy Dill Pickle. It was the #1 requested flavor from their Instagram poll (8,200 votes). Priced at $8 per bag, $18 for a 3-pack. Available as single flavor or added to the Flavor Frenzy sampler ($28 for all 6 flavors). Beta testers called it "dangerously addictive." The brand also runs a summer sale (20% off sitewide, code WILDSUMMER, ends July 15), frequently restocks the Smoky Ranch Crunch which sells out often, and recently did a collab with hot sauce brand Heater Co. for a limited edition "Fire Crunch" bag (only 1,000 made, $12 each).

---

### Variant A: Product Launch

**Promotional purpose:** Announce the new Spicy Dill Pickle flavor and drive first-week purchases.

**Subject Line Options:**
1. New flavor drop: Spicy Dill Pickle is here. — Best (clear, specific, newness signal — no ambiguity about what's inside)
2. You voted. We made it. Say hi to flavor #6. — Good (community involvement, curiosity gap, numbered novelty)
3. The flavor 8,200 of you asked for — Test (social proof in subject, curiosity, big number)

**Preview Text:** Crunchy. Tangy. A little spicy. Very addictive. (49 characters)

**Body Copy:**

[HERO IMAGE: Product shot of Spicy Dill Pickle bag with a few pieces scattered artfully, bold green and yellow color palette]

**It's here. Spicy Dill Pickle just dropped.**

Our newest flavor exists because 8,200 of you voted for it in our Instagram poll. You asked, we spent 6 months perfecting it, and now it's sitting in our warehouse ready to be in your mouth.

Here's what our beta testers said:

*"Dangerously addictive. I finished the bag in one sitting and I'm not even sorry."* — actual beta tester feedback

**Spicy Dill Pickle — $8/bag | 3-pack $18**

Crunchy organic bites with real dill, a kick of cayenne, and that tangy pickle punch that hits right. Bold enough to be interesting. Not so spicy your eyes water. (Unless you eat the whole bag at once. Which you might.)

**Grab it before your favorite snack influencer posts about it.**

Want to try all 6 flavors? The updated **Flavor Frenzy sampler is now $28** — all 6 flavors, one box, zero boring bites.

[BUTTON: Try Spicy Dill Pickle]

**CTA Button Text:** Try Spicy Dill Pickle

**Internal Notes:**
- Strategy: This launch email leverages built-in demand (the Instagram poll) as both social proof and community ownership. The beta tester quote creates credibility without feeling like a formal testimonial. The two price points ($8 single, $28 sampler) give an upsell path without requiring a second CTA.
- A/B test suggestion: Test subject line 1 (direct product announcement) vs. subject line 3 (social proof number) to see if this audience responds more to newness or community validation
- Send timing: Tuesday or Wednesday at 10 AM local time. Product launch emails perform best mid-week, mid-morning when inbox competition is lower and purchase intent is higher.
- Segmentation note: Send to full engaged list but personalize for segments: subscribers who voted in the Instagram poll should get a version that says "You voted for this" in the subject line. Existing customers who've purchased 2+ times should see the sampler upsell more prominently. New subscribers should see the single bag as hero.
- KPI to watch: Click-through rate and first-day revenue. Benchmark 4-8% CTR for product launch emails to engaged lists. Track sampler vs. single bag click-through to inform future pricing strategy.

---

### Variant B: Sale / Discount Promotion

**Promotional purpose:** Drive volume during the Wild Summer sale — 20% off sitewide.

**Subject Line Options:**
1. 20% off everything. Code: WILDSUMMER. Ends July 15. — Best (full offer in subject line — nothing to guess, highest clarity-to-open ratio)
2. Summer's here. So is 20% off your favorite crunch. — Good (seasonal tie-in, specific discount, product reference)
3. Your snack drawer called. It's feeling empty. — Test (playful, brand voice, curiosity — lower clarity but high personality)

**Preview Text:** Sitewide. Every flavor. Every bundle. No exceptions. (53 characters)

**Body Copy:**

[HERO IMAGE: Lifestyle shot — multiple Wild Bites bags on a beach towel, picnic blanket, or poolside setting. Summer vibes.]

**20% off everything at Wild Bites. Right now.**

Code: **WILDSUMMER** | Ends July 15 at midnight EST

This is our once-a-year summer sale. Every bag. Every bundle. Every flavor — including the brand-new Spicy Dill Pickle. No exclusions, no hoops, no "minimum purchase required" nonsense.

**Don't know where to start? Here's what's flying off the shelves:**

1. 🥇 **Smoky Ranch Crunch** — our bestseller for a reason ($8 → $6.40)
2. 🔥 **Spicy Dill Pickle** — newest drop, already a fan favorite ($8 → $6.40)
3. 🎉 **Flavor Frenzy Sampler** — all 6 flavors, one box ($28 → $22.40)

Over 4,200 five-star reviews. Organic ingredients you can actually pronounce. Flavors that make 3 PM the best part of your day.

**WILDSUMMER** expires July 15. After that, full price until next summer. We mean it.

[BUTTON: Shop 20% Off Everything]

**CTA Button Text:** Shop 20% Off Everything

**Internal Notes:**
- Strategy: Lead with the number. The discount amount appears in the subject line, the first line of the body, and the CTA. Zero ambiguity. The bestseller list reduces decision fatigue — instead of browsing the entire catalog, the customer has 3 recommended starting points with discounted prices already calculated. The "once a year" framing creates honest urgency without fake scarcity.
- A/B test suggestion: Test subject line 1 (full offer transparency) vs. subject line 3 (brand personality, curiosity) to determine if promotional or personality-led subjects drive more revenue for sale emails
- Send timing: Saturday or Sunday morning for summer-themed sales. Follow up with a "last chance" reminder email on July 14 to capture procrastinators.
- Segmentation note: Send to full list with engagement filter (opened or clicked in last 90 days). VIP customers (3+ orders) should receive early access 24 hours before the general list. Subscribers who haven't purchased yet should see a version with "first order" language.
- KPI to watch: Revenue per email sent (RPE) and average order value (AOV). Sale emails should drive higher volume but may lower AOV — track both. If AOV drops more than 15% vs. non-sale periods, the discount may be attracting cherry-pickers rather than basket-builders.

---

### Variant C: Restock Notification

**Promotional purpose:** Notify customers that Smoky Ranch Crunch is back in stock after selling out.

**Subject Line Options:**
1. Smoky Ranch Crunch is back. (Act fast.) — Best (product name + back in stock + parenthetical urgency — clean and clear)
2. It sold out in 3 days. It's back. — Good (scarcity history as social proof, curiosity about what "it" is)
3. The restock you've been waiting for — Test (assumes subscriber has been waiting, personal, anticipation)

**Preview Text:** It sold out. You asked. We restocked. Move quick. (51 characters)

**Body Copy:**

[HERO IMAGE: Smoky Ranch Crunch bag, hero shot, possibly with a "BACK IN STOCK" banner overlay]

**Smoky Ranch Crunch is back in stock.**

It sold out in 3 days last time. We restocked as fast as we could, but this is a limited run — once these bags are gone, we're looking at 4-6 weeks before the next batch.

If you missed it the first time, here's why 4,200+ people made it our #1 bestseller: smoky seasoning, real ranch flavor, organic crunch that doesn't quit. It's the flavor that turned first-time buyers into subscription customers.

**Smoky Ranch Crunch — $8/bag | 3-pack $18**

No waitlist this time. Just first come, first served.

[BUTTON: Grab Smoky Ranch Before It's Gone Again]

**CTA Button Text:** Grab Smoky Ranch Before It's Gone Again

**Internal Notes:**
- Strategy: Restock emails have built-in urgency and social proof — the product already proved its demand by selling out. The copy leans into this without being aggressive. The "3 days" sell-out timeframe and "4-6 weeks" restock timeline are specific and credible. The bestseller framing reinforces desirability for customers who haven't tried it.
- A/B test suggestion: Test a version that includes a "notify me" option for the next restock vs. pushing only the immediate purchase. Capturing intent data on restock emails helps predict demand for future production runs.
- Send timing: Send immediately when stock is available. Restock emails are time-sensitive — every hour of delay is lost sales. If possible, trigger this email automatically from inventory management system.
- Segmentation note: Priority send to: (1) customers who signed up for the back-in-stock notification, (2) customers who previously purchased this product, (3) subscribers who clicked the original sold-out announcement. Secondary send to the rest of the engaged list 2-4 hours later to give priority segments a head start.
- KPI to watch: Conversion rate and time-to-sellout. If the restock sells out faster than the original run, increase the next production batch. Track which segment (back-in-stock waitlist vs. general list) has the highest conversion rate.

---

### Variant D: Limited Edition / Collab Drop

**Promotional purpose:** Announce the Wild Bites x Heater Co. "Fire Crunch" limited edition collaboration.

**Subject Line Options:**
1. Wild Bites x Heater Co. Only 1,000 bags made. — Best (collab reveal + specific scarcity number in subject = high urgency + high curiosity)
2. We made a snack with a hot sauce brand. It's wild. — Good (unexpected pairing = curiosity, brand voice, playful)
3. Fire Crunch drops today. 1,000 bags. That's it. — Test (product name + scarcity + finality. Bold and direct.)

**Preview Text:** Our hottest collab. Literally. Only 1,000 made. (49 characters)

**Body Copy:**

[HERO IMAGE: Fire Crunch bag — co-branded packaging with both Wild Bites and Heater Co. logos, dramatic red/orange color palette, flames optional but encouraged]

**Introducing Fire Crunch — a Wild Bites x Heater Co. collaboration.**

We teamed up with the hot sauce brand that's been setting mouths on fire since 2019. The result: a limited edition crunchy snack mix with Heater Co.'s signature cayenne-habanero blend, smoked paprika, and a finish that builds heat without burning you out.

**Only 1,000 bags made. When they're gone, they're gone.**

This isn't a permanent flavor. We made one batch, numbered every bag, and when the run is done, it's done. This is for the ones who like their snacks bold and their hot sauce collection deep.

**Fire Crunch — $12 per bag**

Heater Co.'s founder tried the final version and said: *"This is the first snack that does our sauce justice."* We'll take that as a win.

Available now. No restock. No "back by popular demand." This is a one-time thing.

[BUTTON: Get Fire Crunch Before It's Gone]

**CTA Button Text:** Get Fire Crunch Before It's Gone

**Internal Notes:**
- Strategy: Limited edition collabs are the highest-urgency promotional email type because the scarcity is real and verifiable. The "only 1,000 bags" number and the "no restock" promise create authentic FOMO. The co-founder quote from the collab partner adds credibility and cross-brand social proof. The "numbered every bag" detail adds collectibility.
- A/B test suggestion: Test a "blind drop" approach (announce 1 hour before launch via SMS, then follow with email) vs. a "hype build" approach (teaser email 3 days before, then launch email). For brands with engaged communities, blind drops often create more organic social sharing.
- Send timing: Launch day, 10 AM EST. Limited edition drops perform best at a single, announced time. If possible, send a "dropping tomorrow" teaser email the evening before to prime the audience.
- Segmentation note: Priority send to VIP customers (3+ orders) and subscribers who engage with brand collaborations or spicy products. Use purchase history to identify customers who've bought the spiciest existing flavor (Chili Mango Tango) — they're the highest-intent audience for this collab. Suppress subscribers who haven't opened an email in 60+ days — limited edition emails to cold subscribers have low ROI.
- KPI to watch: Sell-through velocity (time to sell all 1,000 units) and social sharing metrics. If the run sells out in under 24 hours, the next collab should have a larger run. If it takes more than 7 days, the audience may not be responding to this collab partner — test a different category next time.

---

### Variant Summary

| Variant | Type | Urgency Level | Key Hook | Target Word Count | Primary KPI |
|---|---|---|---|---|---|
| A | Product Launch | Moderate | Newness + community demand | 100-200 | CTR, first-day revenue |
| B | Sale / Discount | High | 20% off with deadline | 100-200 | RPE, AOV |
| C | Restock | High | Sold out before, limited restock | 100-200 | CVR, time-to-sellout |
| D | Limited Edition / Collab | Highest | 1,000 bags, never restocked | 100-200 | Sell-through velocity |

**General promotional email best practices:**
- Send promotional emails to engaged segments (opened or clicked in last 60-90 days). Sending to your full list, including inactive subscribers, damages deliverability and inflates send costs.
- Every promotional email should include an unsubscribe link that works. Never hide it or make it difficult. Customers who want to leave should leave easily — keeping them hurts your metrics.
- Track revenue per email sent (RPE) as your north star metric for promotional emails. Open rate and CTR are leading indicators, but RPE is what matters.
- Limit promotional emails to 2-4 per month for most DTC brands. More than that and you risk list fatigue. Each send should feel like an event worth the subscriber's attention.
- Always send a plain-text test version to yourself before launching. If the email doesn't make sense without images (many email clients block images by default), rewrite until the text alone is compelling.

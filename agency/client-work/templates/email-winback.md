# Email Winback Sequence (3-Email Series)

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | A complete 3-email winback sequence for lapsed DTC customers (60-90+ days inactive), including subject lines, preview text, body copy, CTAs, and escalating re-engagement strategy |
| **Turnaround** | 30-45 minutes per sequence |
| **Quality bar** | Production-ready copy that acknowledges the gap without guilt-tripping, makes the brand feel alive and worth returning to, and offers a genuine incentive in the final email that feels exclusive rather than desperate |
| **Best for** | DTC brands with significant lapsed customer segments (60+ days since last purchase), brands preparing for seasonal re-engagement campaigns, clients launching new products who want to re-activate dormant buyers |

---

## Client Brand Variables

Fill in every variable before pasting the prompt into Claude. If a variable is not applicable, write "N/A" — do not leave it blank.

```
[BRAND_NAME] — The brand's name exactly as it appears in customer-facing copy
[BRAND_VOICE] — 3-5 adjectives describing how the brand sounds (e.g., "warm, inviting, sophisticated but not stuffy, grounded")
[TARGET_AUDIENCE] — Demographics + psychographics (e.g., "women 28-45 who invest in home ambiance and daily rituals")
[PRODUCT_SERVICE] — What the brand sells, in plain language (e.g., "hand-poured soy candles in signature and seasonal scents")
[PRICE_RANGE] — Lowest to highest price point for core products (e.g., "$32-58")
[KEY_DIFFERENTIATOR] — The one thing that makes this brand different from every competitor (e.g., "100-hour burn time, scent profiles designed by a former fine fragrance perfumer")
[COMPETITOR_NAMES] — 2-4 competitors the brand is positioned against (e.g., "Yankee Candle, Boy Smells, Diptyque")
[WORDS_TO_USE] — Brand-approved vocabulary (e.g., "handcrafted, warm, intentional, ritual, small-batch")
[WORDS_TO_AVOID] — Words that are off-brand or off-limits (e.g., "cheap, bargain, basic, mainstream, fake")
[TONE_SCALE] — Where the brand sits on a 1-10 scale: 1 = ultra-corporate/formal, 10 = unhinged meme brand (e.g., "5 — warm and conversational but elegant")
[CAMPAIGN_GOAL] — Primary goal for this sequence (e.g., "reactivate 8-12% of lapsed customers within 30 days")
[ADDITIONAL_CONTEXT] — Anything else: new products since they left, seasonal scents, subscription options, loyalty program, typical repurchase cycle, average order value, preferred winback incentive (% off, free shipping, free gift), etc.
```

### Dynamic Tokens for Winback Sequences

These tokens will be replaced by the ESP's dynamic content engine. Use them exactly as written in the copy:

```
[CUSTOMER_FIRST_NAME] — The customer's first name
[LAST_PURCHASE_PRODUCT] — The product from their most recent order
[LAST_PURCHASE_DATE] — Approximate time since their last order (e.g., "a few months ago")
[NEW_PRODUCT_NAME] — A new product launched since their last purchase
[NEW_PRODUCT_IMAGE] — Image of the new product
[NEW_PRODUCT_URL] — Link to the new product page
[WINBACK_DISCOUNT_CODE] — Exclusive winback discount code
[WINBACK_DISCOUNT_AMOUNT] — The discount percentage or dollar amount
[WINBACK_CODE_EXPIRY] — When the discount code expires
[SHOP_URL] — General link to shop
```

---

## The Prompt

Copy everything between the `---START PROMPT---` and `---END PROMPT---` markers. Replace all bracketed variables with the client's actual information before pasting into Claude.

---START PROMPT---

You are a senior DTC email strategist who specializes in customer reactivation. You understand the psychology of lapsed customers: they liked the brand enough to buy once (or more), but something caused them to drift away. Maybe they forgot. Maybe their routine changed. Maybe they found an alternative. Maybe nothing — life just happened. Your job is to reconnect without desperation, guilt, or cringe. You write winback emails that make the brand feel alive, relevant, and worth returning to. You never beg, you never guilt-trip, and you never use "we miss you" as a subject line. You understand that the best winback email makes the customer feel like they are missing out on something genuinely good — not that the brand is sad without them.

**Your task:** Write a complete 3-email winback sequence for the following brand.

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

Write exactly 3 emails following this re-engagement escalation:

**Email 1 — "A Lot Has Changed" (Send: Day 60 after last purchase)**
- Purpose: Reconnect with the lapsed customer by showing them what's new. Make the brand feel alive and evolving — not frozen in time from when they last interacted. Acknowledge the gap without making it awkward.
- Body length: 100-200 words
- Tone: Confident, warm, forward-looking. Like running into a friend you haven't seen in a while — the conversation should be about what's new, not about the absence.
- Must include: A casual acknowledgment that it's been a while (not guilt-driven), 2-3 specific things that are new since they last purchased (new products, new scents, new features, brand milestones), a reference to their previous purchase using [LAST_PURCHASE_PRODUCT] to make it personal, a light CTA to browse what's new
- Must NOT include: Guilt language ("we miss you," "where did you go," "we noticed you've been away"), heavy discounts or incentives (save these for Email 3), passive-aggressive tone, desperation
- Emotional target: Curiosity + "oh, I should check that out" ("this brand has been busy")

**Email 2 — Value-First Content (Send: Day 75 after last purchase)**
- Purpose: Provide genuine value without a hard sell. Share content — a tip, a customer story, a use case, or a seasonal idea — that reminds the customer why they liked the brand in the first place. The goal is engagement (open, click, read) not necessarily purchase.
- Body length: 100-200 words
- Tone: Helpful, warm, content-focused. This email should read more like a newsletter than a promotional email. The brand is giving, not asking.
- Must include: A piece of genuinely useful or interesting content related to the product category, a customer story or testimonial that demonstrates the brand's value through someone else's experience, a natural (not forced) product mention, a light CTA that leads to content or browsing — not a purchase page
- Must NOT include: Discounts, incentives, urgency, or any "buy now" language. This email earns re-engagement through value.
- Emotional target: Warmth + nostalgia + value ("I forgot how good this brand is")

**Email 3 — Exclusive Offer / Last Call (Send: Day 90 after last purchase)**
- Purpose: Make a genuine, exclusive offer to re-activate the customer. This is the final email in the winback sequence and the last attempt before the customer is moved to a dormant segment. The offer should feel exclusive and real — not like a mass discount.
- Body length: 100-200 words
- Tone: Direct, genuine, respectful. Like a brand saying "we'd love to have you back, and we're putting our money where our mouth is." Not "LAST CHANCE!!!" — more like a thoughtful offer from someone who values the relationship.
- Must include: An exclusive discount or incentive using [WINBACK_DISCOUNT_CODE] and [WINBACK_DISCOUNT_AMOUNT], a specific expiration date using [WINBACK_CODE_EXPIRY], a clear reason why this offer is exclusive (not available to general list), a brief reminder of what they loved (reference [LAST_PURCHASE_PRODUCT]), risk reversal (return policy, satisfaction guarantee), a clear and direct CTA
- Must NOT include: Fake urgency, "this is your last email" threats (even if it is — don't weaponize it), language that implies the customer owes the brand something, multiple competing offers or CTAs
- Emotional target: Exclusivity + smart decision ("this is a genuinely good deal and it's just for me")

### Formatting Requirements for EVERY Email

For each of the 3 emails, provide exactly this structure:

```
### Email [NUMBER]: [DESCRIPTIVE TITLE]
**Send timing:** [When this email triggers relative to last purchase date]
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
- Purpose: [What this email accomplishes in the re-engagement arc]
- A/B test suggestion: [One specific test to run]
- Segmentation note: [Conditional logic or exclusion rules]
- KPI to watch: [Primary metric]
- Fallback plan: [What happens if this email doesn't convert]
```

### Writing Rules

1. **No guilt, no cringe.** This is the most important rule. Winback emails that say "we miss you," "where have you been?," "it's been lonely without you," or "your cart is gathering dust" are tired, manipulative, and ineffective. Acknowledge the gap casually and move forward with something interesting.
2. **The brand has been living.** Email 1 should make the brand feel like it's been doing exciting things since the customer left. New products, new milestones, new customer stories. The customer should feel like they've been missing out on a brand that's thriving — not a brand that's been waiting by the phone.
3. **Reference their history.** Use [LAST_PURCHASE_PRODUCT] to make the emails personal. "Since you picked up your [LAST_PURCHASE_PRODUCT]..." is infinitely better than "Since your last order..." Generic winback emails feel mass-produced. Personalized ones feel like a friend reaching out.
4. **Escalate slowly.** Email 1 is curiosity (no incentive). Email 2 is value (no incentive). Email 3 is the offer. If you put a discount in Email 1, you're training customers to go dormant for a discount. The escalation must be strict.
5. **Email 3 exclusivity must feel real.** The offer in Email 3 should explicitly state that it's only available to the recipient — not the general email list. Use language like "this code was generated just for you" or "not available on our site or in any other email." If the customer perceives this as a generic promo, it loses its re-activation power.
6. **Short paragraphs.** 2-3 sentences max per paragraph. White space. Mobile-first. These are customers who are already disengaged — a wall of text will guarantee they stay that way.
7. **Respect the customer's choice.** If someone hasn't bought in 60-90 days, they have reasons. The winback sequence should make returning feel easy and appealing, not obligatory. Every email should feel like it would be fine if the customer didn't come back — no neediness.
8. **Tone warmth progression.** Email 1 is confident and forward-looking. Email 2 is warm and generous. Email 3 is direct and respectful. The tone shifts subtly across the sequence — from "look what's new" to "here's something valuable" to "we'd genuinely love to see you again."
9. **Dynamic token usage.** Use [CUSTOMER_FIRST_NAME] naturally (not in every email). Always use [LAST_PURCHASE_PRODUCT] to personalize. In Email 1, use [NEW_PRODUCT_NAME] and [NEW_PRODUCT_IMAGE] to showcase what's new. In Email 3, use [WINBACK_DISCOUNT_CODE], [WINBACK_DISCOUNT_AMOUNT], and [WINBACK_CODE_EXPIRY] for the offer.
10. **Know when to let go.** After Email 3, if the customer doesn't engage, they should be moved to a suppression or dormant list. Do not send additional winback emails. Respect the unspoken "no." This should be noted in the Email 3 internal notes.

---END PROMPT---

---

## Output Format

The output should be structured exactly as follows:

- **Total emails:** 3
- **Per email:** Subject lines (3), preview text (1), body copy with dynamic tokens and formatting cues, CTA button text (1), internal notes (5 sub-items including fallback plan)
- **Word counts per email body:** 100-200 words each
- **Total deliverable word count:** Approximately 600-1,200 words of copy, plus internal notes
- **Formatting:** Markdown with clear headers, bracketed formatting cues, and dynamic tokens in exact ESP format
- **Naming convention:** Each email should have a descriptive title reflecting its role in re-engagement (e.g., "Email 1: A Lot Has Happened")

---

## Quality Checks Before Sending

Run through every item before delivering to the client:

1. **Guilt language audit.** Read every email and search for guilt, desperation, or passive aggression. Key phrases to flag and remove: "we miss you," "where have you been," "it's been a while since we heard from you," "your account is still active," "don't forget about us," "we've been waiting." If any of these appear, rewrite the section entirely.
2. **Escalation integrity.** Confirm the incentive structure is correct: Email 1 has NO discount or incentive. Email 2 has NO discount or incentive. Email 3 has the exclusive offer. If any incentive appears before Email 3, remove it. Premature discounting trains customers to go dormant for deals.
3. **Dynamic token accuracy.** Verify every token is correctly formatted: [CUSTOMER_FIRST_NAME], [LAST_PURCHASE_PRODUCT], [LAST_PURCHASE_DATE], [NEW_PRODUCT_NAME], [NEW_PRODUCT_IMAGE], [NEW_PRODUCT_URL], [WINBACK_DISCOUNT_CODE], [WINBACK_DISCOUNT_AMOUNT], [WINBACK_CODE_EXPIRY], [SHOP_URL]. Typos or missing brackets will break ESP integration.
4. **Exclusivity test for Email 3.** Does the offer in Email 3 genuinely feel exclusive? If you removed the customer's name and sent this email to your entire list, would it work as a generic promo? If yes, it's not exclusive enough. Add language that makes clear this is only for this customer.
5. **Brand aliveness check.** Does Email 1 make the brand feel like it's been thriving? Read it from the customer's perspective — after 60 days of not thinking about this brand, does this email make you curious about what you've been missing? If the email could have been sent 6 months ago with no changes, it doesn't feel alive enough.
6. **Value authenticity in Email 2.** Is the content in Email 2 genuinely useful or interesting, independent of the brand? Would this tip, story, or idea be worth reading even if the customer never buys again? If the content is just a thin wrapper around a product pitch, rewrite it with more genuine value.
7. **Word count compliance.** Each email must be 100-200 words. Winback emails need to be concise — lapsed customers will not read long emails from a brand they've drifted from. Respect their time and attention.

---

## Example Output

Below is a complete example output using the fictional brand **Ember & Oak** to demonstrate the quality bar and format expected from every deliverable.

**Brand variables used for this example:**
- Brand name: Ember & Oak
- Brand voice: Warm, inviting, sophisticated but not stuffy, grounded, intentional
- Target audience: Women 28-45 who invest in their living spaces, appreciate craftsmanship, and see candles as part of a daily ritual — not just background decor
- Product/service: Hand-poured soy candles in signature and seasonal scents (Fireside Amber, Cedar & Vanilla, Wild Honeysuckle, Smoked Fig, Coastal Morning)
- Price range: $32-58
- Key differentiator: 100-hour burn time, scent profiles designed by a former fine fragrance perfumer, hand-poured in small batches in Portland
- Competitors: Yankee Candle, Boy Smells, Diptyque, Voluspa
- Words to use: Handcrafted, warm, intentional, ritual, small-batch, slow down, glow
- Words to avoid: Cheap, bargain, basic, mainstream, fake, synthetic, mass-produced
- Tone scale: 5 — warm and conversational with an elegance to it
- Campaign goal: Reactivate 10% of lapsed customers (60-90+ days since last purchase) within a 30-day window
- Additional context: Since most lapsed customers last purchased, Ember & Oak has launched 2 new seasonal scents (Autumn Orchard and Evergreen & Frost), hit 2,000 five-star reviews, been featured in Architectural Digest, and launched a "Candle of the Season" subscription ($44/quarter). The typical winback incentive is 15% off next order (code: WELCOMEBACK15). Average repurchase cycle for active customers is 45 days. Free shipping on orders over $50. 30-day satisfaction guarantee on all candles.

---

### Email 1: A Few Things You've Missed

**Send timing:** 60 days after last purchase
**Purpose:** Re-introduce the brand by showcasing what's new and interesting since the customer's last order. Make Ember & Oak feel alive and thriving. No incentive, no selling — just genuine "here's what's been happening."

**Subject Line Options:**
1. A lot's happened since your last candle — Best (references their personal history, creates curiosity gap, warm tone without guilt)
2. Two new scents just dropped (and one sold out already) — Good (newness + scarcity as social proof, specific detail, forward-looking)
3. [CUSTOMER_FIRST_NAME], this one's worth a peek — Test (personal, intriguing, casual — lower specificity but high open potential)

**Preview Text:** New scents, a big feature, and 2,000 five-star reviews. (57 characters)

**Body Copy:**

[HERO IMAGE: Flat-lay of the two new seasonal scents — Autumn Orchard and Evergreen & Frost — in a warm lifestyle setting with seasonal elements]

[CUSTOMER_FIRST_NAME] —

It's been a minute since you picked up your **[LAST_PURCHASE_PRODUCT]**. We've been busy.

Here's a quick update on what's happened at Ember & Oak since you were last here:

**New seasonal scents:**
- **Autumn Orchard** — warm apple, cinnamon bark, a hint of bourbon. Like October in a jar.
- **Evergreen & Frost** — fresh pine, eucalyptus, cool mint. Our fastest seller this year.

**A couple milestones:**
- We hit **2,000 five-star reviews** (still can't believe that one)
- Architectural Digest featured our Fireside Amber in their "Best Candles for Cozy Homes" roundup

**Something new:**
We launched a **Candle of the Season subscription** — a new handcrafted scent delivered to your door every quarter. It's become our most-loved offering.

The same small-batch, 100-hour burn candles you know. A lot of new reasons to come back.

[BUTTON: See What's New at Ember & Oak]

**CTA Button Text:** See What's New at Ember & Oak

**Internal Notes:**
- Purpose: This email makes Ember & Oak feel like a brand that has been thriving, not waiting around. The specific milestones (2,000 reviews, Architectural Digest feature) build social proof. The new products give the customer a reason to return that didn't exist when they last purchased. The reference to [LAST_PURCHASE_PRODUCT] personalizes the email and acknowledges the relationship. Zero selling, zero guilt — just "look what you've been missing."
- A/B test suggestion: Test subject line 1 (personal history reference) vs. subject line 2 (new product-led) to see whether personal or product-driven subjects drive higher opens from lapsed customers
- Segmentation note: Only send to customers whose last purchase was 55-65 days ago (allow a window). Exclude anyone who has opened an email or visited the site in the last 30 days — they're not truly lapsed. If the customer's [LAST_PURCHASE_PRODUCT] has been discontinued, replace the reference with a general "since your last order."
- KPI to watch: Open rate. For winback Email 1, a healthy open rate is 15-25% (lower than engaged list benchmarks, which is normal for lapsed segments). If below 10%, test more aggressive subject lines or send from a personal name (e.g., "Sarah from Ember & Oak") instead of the brand name.
- Fallback plan: If the customer opens but doesn't click, they advance to Email 2 as scheduled. If they don't open Email 1 at all, consider resending with a different subject line 3 days later before moving to Email 2. Track whether resends improve open rate for this segment.

---

### Email 2: The Ritual That Changed Her Evenings

**Send timing:** 75 days after last purchase (15 days after Email 1)
**Purpose:** Provide genuine value through a customer story that demonstrates the brand's impact. Remind the lapsed customer why candles matter — not through product pitching, but through a relatable human experience. Light CTA to browse, no incentive.

**Subject Line Options:**
1. "I stopped scrolling and started being present." — Best (quote format grabs attention, emotional resonance, curiosity about who said it and why)
2. A 10-minute ritual that changed her entire evening — Good (specific time = tangible, "changed" implies transformation, curiosity about what it is)
3. Something worth slowing down for — Test (brand-aligned language, philosophical, emotional — lower specificity but high brand resonance)

**Preview Text:** One customer's evening ritual. No screens. One candle. (54 characters)

**Body Copy:**

[HERO IMAGE: Warm, lifestyle photograph — a woman in a cozy setting, candle lit, book in hand or simply sitting in soft light. Aspirational but authentic.]

We recently asked our customers a simple question: **"What does your candle ritual look like?"**

One answer stopped us in our tracks.

**Meet Danielle, a Fireside Amber loyalist:**

*"I used to end every day on the couch, doom-scrolling until my eyes hurt. A few months ago I decided to change one small thing: I'd light my Ember & Oak candle, put my phone in another room, and just sit for 10 minutes. No screen. No podcast. Just the flicker and the scent.*

*It sounds so small. But those 10 minutes became the most grounding part of my day. My husband noticed. My sleep improved. I started protecting that time like an appointment.*

*It's just a candle. But it became the signal that the busy part of my day was over."*

We hear stories like Danielle's more often than you'd think. A candle isn't just a candle when it becomes the anchor of an intentional moment.

If it's been a while since you've lit one, maybe tonight's the night.

[BUTTON: Find Your Next Ritual Candle]

**CTA Button Text:** Find Your Next Ritual Candle

**Internal Notes:**
- Purpose: Value-first content that sells through story, not promotion. Danielle's story is relatable to the target audience (busy women, screen fatigue, desire for intentionality) and demonstrates the brand's value in a way that a product description never could. The email doesn't ask the customer to buy — it invites them to reconnect with the feeling the brand represents. This is the emotional bridge between "what's new" (Email 1) and "here's an offer" (Email 3).
- A/B test suggestion: Test this customer story version vs. a "5 ways to use your candle beyond ambiance" tip-based version. Stories tend to perform better for emotional brands, but tips can outperform for utility-focused audiences. The test will reveal which content type resonates with this brand's lapsed segment.
- Segmentation note: Send to all customers who received Email 1, regardless of whether they opened it. Value-first content emails sometimes re-engage subscribers that promotional or update emails don't. Exclude any customer who has made a purchase since Email 1 — they're reactivated and should be in the post-purchase flow.
- KPI to watch: Open rate and click-through rate. This email's primary job is engagement (getting the customer to interact with the brand again), not conversion. A strong open rate (20%+) indicates the subject line and brand still resonate. A strong CTR (3-5%) indicates the content reconnected them emotionally. Forward rate is a bonus metric — stories get shared.
- Fallback plan: If the customer engages with Email 2 (opens or clicks) but doesn't purchase, they're prime candidates for Email 3's exclusive offer. If they don't engage with Email 1 or Email 2, Email 3 should still be sent as the final attempt, but expectations for conversion should be lower. Consider a subject line variant for Email 3 that leads with the offer amount rather than the relationship angle.

---

### Email 3: Something Just For You (15% Off, This Week Only)

**Send timing:** 90 days after last purchase (15 days after Email 2)
**Purpose:** Make a genuine, exclusive offer to reactivate the customer. This is the final touchpoint before they move to the dormant segment. The offer must feel personal and exclusive — not like a mass promotion. Direct, respectful, and honest.

**Subject Line Options:**
1. 15% off — just for you, just this week — Best (specific offer, personal exclusivity, clear time frame — high clarity, high urgency)
2. [CUSTOMER_FIRST_NAME], we made this code for you — Good (personal, exclusive feel, curiosity about what "this code" is)
3. One more reason to come back to Ember & Oak — Test (warm, inviting, implies value — lower urgency but high brand alignment)

**Preview Text:** Code WELCOMEBACK15 — exclusive to you. Expires [WINBACK_CODE_EXPIRY]. (69 characters)

**Body Copy:**

[HERO IMAGE: A single beautiful candle — the customer's [LAST_PURCHASE_PRODUCT] if possible, or the brand's bestseller — lit, warm light, inviting setting]

[CUSTOMER_FIRST_NAME] —

We'll keep this simple.

It's been a while since your **[LAST_PURCHASE_PRODUCT]**, and we'd genuinely love to see you back. So we're doing something we don't do for our general email list:

**15% off your next order. Exclusively for you.**

Code: **[WINBACK_DISCOUNT_CODE]**
Expires: **[WINBACK_CODE_EXPIRY]**

This code isn't on our website. It's not in our newsletter. It was generated for your account specifically because you've been part of the Ember & Oak community, and we'd rather offer you something real than watch you drift away.

**A few things worth knowing:**
- Free shipping on orders over $50
- New seasonal scents: Autumn Orchard and Evergreen & Frost
- 30-day satisfaction guarantee — if you don't love it, we'll make it right
- The same 100-hour burn time. Still hand-poured in Portland.

No pressure. Truly. But if you've been meaning to restock, this is the best reason we can offer.

[BUTTON: Use Your 15% Off Now]

**CTA Button Text:** Use Your 15% Off Now

**Internal Notes:**
- Purpose: This is the closer and the final attempt. The offer is framed as exclusive (not available to the general list, generated for their account) which makes it feel personal and valuable rather than like a desperate mass discount. The "we'll keep this simple" opening signals respect for their time. The bullet points serve as a rapid-fire value summary for customers who need a reminder of what makes the brand worth it. The "no pressure" closing is deliberate — it respects the customer's autonomy and paradoxically makes the offer more compelling by removing neediness.
- A/B test suggestion: Test 15% off vs. free shipping (no minimum) as the winback incentive. For premium brands, free shipping sometimes outperforms percentage discounts because it doesn't lower the perceived value of the product. Also test subject line 1 (offer-led) vs. subject line 2 (personal/curiosity) to determine whether lapsed customers respond more to incentive clarity or emotional connection.
- Segmentation note: Send to all customers who received Emails 1 and 2, regardless of engagement. This is the final attempt — even unopened subscribers deserve one last shot with a strong offer. However, create two subject line variants: one for customers who opened at least one previous email (relationship-focused subject) and one for customers who opened neither (offer-first subject to maximize opens). Exclude anyone who has purchased since the sequence began. After this email, move non-responders to a suppressed/dormant list.
- KPI to watch: Conversion rate and revenue recovered. This email should drive the highest conversion of the 3-email sequence. Benchmark: 2-5% conversion rate for engaged recipients (opened Email 1 or 2), 0.5-1% for non-engaged recipients. Track the total reactivation rate for the full sequence against the 10% target.
- Fallback plan: Customers who do not open, click, or purchase from any of the 3 winback emails should be moved to a dormant/suppressed segment. Do NOT send additional winback emails. Respect the non-response. These customers can be reactivated through other channels (retargeting ads, direct mail) or re-entered into the winback flow if they visit the website organically in the future. Suppression protects deliverability and list health — keeping unengaged subscribers on the active list damages inbox placement for engaged subscribers.

---

### Sequence Summary

| Email | Day | Purpose | Incentive | Target Word Count | Primary KPI |
|---|---|---|---|---|---|
| 1 — A Few Things You've Missed | 60 | Reconnect, show what's new | None | 100-200 | Open rate (15-25%) |
| 2 — The Ritual That Changed Her Evenings | 75 | Value content, emotional re-engagement | None | 100-200 | Open rate, CTR (3-5%) |
| 3 — Something Just For You | 90 | Exclusive offer, reactivation | 15% off (exclusive code) | 100-200 | Conversion rate (2-5%) |

**Total expected reactivation rate:** 8-12% of lapsed customers returning to purchase within 30 days of sequence start

**Recommended ESP setup notes:**
- Define the entry trigger precisely: customer last purchased 58-62 days ago AND has not opened or clicked any email in the last 30 days AND has not visited the website in the last 30 days. This ensures you're targeting genuinely lapsed customers, not customers who are engaged but haven't purchased.
- Add an exit condition at every step: if the customer makes a purchase, immediately exit them from the winback flow and enter them into the post-purchase sequence.
- Email 3's discount code should be unique per customer (not a generic code). Generic codes get shared on coupon sites and undermine the exclusivity positioning. Most ESPs (Klaviyo, Omnisend) support unique code generation in flows.
- After Email 3, if no engagement occurs across all 3 emails (zero opens), move the customer to a suppressed segment. Do not continue emailing them — it damages deliverability and sender reputation.
- For customers who open or click but don't purchase, consider one final "code expires tomorrow" SMS message if the brand has SMS consent. SMS winback reminders for engaged-but-not-converted subscribers can recover an additional 1-3%.
- Run this sequence as an evergreen flow (not a one-time campaign) so every customer enters it automatically when they hit the 60-day lapse threshold. Review the flow performance quarterly and refresh the copy if open rates decline below benchmarks.
- Tag all customers reactivated through this flow as "winback-converted" for cohort analysis. Track their 60-day and 90-day retention rates to determine whether winback customers become long-term repeat buyers or one-time reactivations.

# SMS Marketing Template

## Quick Reference

| Detail | Info |
|---|---|
| **What it produces** | 10 complete SMS messages covering the full customer lifecycle: welcome, abandoned cart, flash sale, new product launch, back in stock, shipping confirmation, review request, VIP/loyalty exclusive, birthday/anniversary, and winback |
| **Turnaround** | Same-day delivery |
| **Quality bar** | Every SMS must be under 160 characters, sound like a text from a friend (not a brand), front-load value, include a clear CTA, use one emoji maximum, and comply with SMS marketing regulations |
| **Best for** | DTC brands building or optimizing their SMS marketing flows across platforms like Klaviyo, Postscript, Attentive, or similar |

---

## Client Brand Variables

Fill these in before running the prompt. Replace each bracketed variable with the client's actual information.

```
[BRAND_NAME] = The brand's name (keep it short — character count matters in SMS)
[BRAND_VOICE] = How the brand sounds (e.g., "Smart, approachable, slightly sarcastic — like your friend who's a skincare scientist")
[TARGET_AUDIENCE] = Who they're texting (e.g., "Skincare-obsessed Gen Z and young millennials aged 18-30 who opted into SMS")
[PRODUCT_SERVICE] = What they sell (e.g., "Minimalist 3-product skincare routine — cleanser, serum, moisturizer")
[PRICE_RANGE] = Price point (e.g., "$22-$38 per product, $75 for the set")
[KEY_DIFFERENTIATOR] = What makes them different (e.g., "5 or fewer ingredients per product, founded by a cosmetic chemist")
[COMPETITOR_NAMES] = Key competitors (for context — never mention in SMS messages)
[WORDS_TO_USE] = Brand vocabulary (e.g., "simple, real, bare, routine, ingredients, works")
[WORDS_TO_AVOID] = Off-limits language (e.g., "miracle, anti-aging, flawless, perfect skin, transformation, luxury")
[TONE_SCALE] = Where they fall: Casual 1-----5 Formal | Playful 1-----5 Serious | Bold 1-----5 Understated
[CAMPAIGN_GOAL] = What SMS should accomplish (e.g., "Drive first purchases, recover abandoned carts, increase repeat purchase rate, build loyalty")
[ADDITIONAL_CONTEXT] = Any relevant details (e.g., "Promo codes, specific product names, loyalty program details, subscription model, shipping policies, current offers, brand personality details")
```

---

## The Prompt

Paste the following prompt into Claude after replacing all brand variables above.

---

You are an SMS marketing specialist who writes text messages for DTC brands. You understand that SMS is the most personal marketing channel — it lives in the same app where people text their friends, family, and partners. That means every brand SMS must earn its place. It must feel welcome, not intrusive. It must sound human, not automated. And it must deliver value in under 160 characters.

I need you to write 10 SMS messages covering the full customer lifecycle for the following brand:

**Brand:** [BRAND_NAME]
**Brand Voice:** [BRAND_VOICE]
**Target Audience:** [TARGET_AUDIENCE]
**Product/Service:** [PRODUCT_SERVICE]
**Price Range:** [PRICE_RANGE]
**Key Differentiator:** [KEY_DIFFERENTIATOR]
**Competitors:** [COMPETITOR_NAMES] (DO NOT mention in any message)
**Words to Use:** [WORDS_TO_USE]
**Words to Avoid:** [WORDS_TO_AVOID]
**Tone Scale:** [TONE_SCALE]
**Campaign Goal:** [CAMPAIGN_GOAL]
**Additional Context:** [ADDITIONAL_CONTEXT]

### The 10 SMS Scenarios

Write one message for each of the following scenarios:

1. **Welcome SMS** — Sent immediately after a customer opts into SMS. First impression. Should make them glad they signed up. Include the welcome offer if one exists.

2. **Abandoned Cart SMS** — Sent 30-60 minutes after a customer leaves items in their cart. Should create gentle urgency without being pushy. Reference the product casually.

3. **Flash Sale SMS** — Announces a limited-time sale (24-48 hours). Should create urgency with a specific deadline. The deal should be the first thing the reader sees.

4. **New Product Launch SMS** — Announces a new product to the SMS list first (making them feel like insiders). Should generate excitement and make subscribers feel like they're getting early or exclusive access.

5. **Back in Stock SMS** — Notifies a customer that a previously sold-out product is available again. Should convey urgency (it sold out once, it will again) without being manipulative.

6. **Shipping Confirmation SMS** — Sent when the order ships. Should feel exciting, not transactional. Include tracking info placeholder.

7. **Review Request SMS** — Sent 7-14 days after delivery. Should ask for a review in a way that feels personal and easy, not like a corporate survey request.

8. **VIP/Loyalty Exclusive SMS** — Sent to high-value customers or loyalty program members with an exclusive offer or early access. Should make the recipient feel special and recognized.

9. **Birthday/Anniversary SMS** — Sent on the customer's birthday or subscription anniversary. Should feel celebratory and personal, with a gift or offer attached.

10. **Winback SMS** — Sent to customers who haven't purchased in 60-90 days. Should re-engage without guilt-tripping. Acknowledge the absence casually and offer a reason to return.

### Writing Rules You Must Follow

1. **Write like a text from a friend.** Every SMS should pass the test: "Could I imagine receiving this from someone I know?" No corporate language. No "Dear valued customer." No "We at [Brand] are excited to." Just talk like a person.

2. **Front-load the value or hook.** People see the first 40-50 characters in their notification preview. That preview must convey the most important information — the discount amount, the product name, or the reason they should open the full message. Never start with the brand name or a greeting.

3. **Keep every message under 160 characters.** This is the standard single-segment SMS limit. Going over 160 characters splits the message into multiple segments, which costs more and often delivers out of order. Count characters precisely. The 160-character limit includes the link placeholder, any emoji, and any required opt-out text (if the opt-out is included in the character count for the platform). For this template, write the core message under 160 characters and include a separate compliance note below.

4. **One emoji maximum per message.** Emojis can add personality but they also consume character space and can feel overdone in SMS. Use exactly one emoji per message if it adds warmth or emphasis. Never use more than one. Choose emojis that match the brand tone — no random fire emojis or strings of hands clapping.

5. **Use abbreviations only if natural.** Do not force abbreviations to save characters. "ur" and "2nite" feel forced for most brands. But "$10 off" instead of "ten dollars off" or "w/" instead of "with" can feel natural depending on the brand voice. Match the audience's texting style.

6. **Include a clear CTA in every message.** Every SMS must have a clear next step: click a link, use a code, reply to the text, or visit the site. The CTA should be specific ("Shop the set" or "Grab yours") rather than generic ("Learn more" or "Click here").

7. **Include a link placeholder.** Use [LINK] as a placeholder for the shortened URL. Position it naturally within or at the end of the message. The link should feel like a helpful next step, not an afterthought.

8. **Include a compliance note.** After each SMS message, add a separate compliance line: "Reply STOP to opt out." This is legally required for commercial SMS in the US (TCPA compliance). In the character-count template, this line is kept separate from the 160-character message body, as most SMS platforms append it automatically. Note this for the client.

9. **Never guilt-trip or manipulate.** Especially for abandoned cart, winback, and flash sale messages — create genuine urgency without pressure tactics. "Your cart misses you" is playful. "Don't miss out on the deal of a lifetime!!!" is manipulative. Keep it light.

10. **Personalization placeholders.** Where appropriate, use standard merge tag placeholders: {first_name} for the customer's first name, {product_name} for the abandoned/purchased product, {order_number} for order references. These get replaced by the SMS platform automatically.

### Output Format for Each SMS

```
### [NUMBER]. [SCENARIO NAME]

**Trigger:** [When this SMS is sent]
**Goal:** [What this message should accomplish]

**Message:**
[The complete SMS message — under 160 characters]

**Character Count:** [Exact count]
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
[Any setup notes for the SMS platform — timing, segmentation, merge tags used, automation flow placement]
```

Now write all 10 SMS messages. Every message should feel like a welcome text in someone's inbox — not an interruption.

---

## Output Format

The complete deliverable should contain:

- 10 SMS messages, one for each lifecycle scenario
- Every message under 160 characters (verified character count included)
- One emoji maximum per message
- Clear CTA and [LINK] placeholder in every message
- Compliance note ("Reply STOP to opt out") listed separately for each message
- Trigger timing and goal for each message
- Platform setup notes for each message
- Personalization merge tags ({first_name}, {product_name}, etc.) used where appropriate
- All messages sounding conversational and human, not corporate

---

## Quality Checks Before Sending

Run through every single check before delivering to the client:

1. **Character count verification:** Count every single character in every message — including spaces, punctuation, emoji, [LINK] placeholder (count as 6 characters since most URL shorteners create 20-25 character links, but the placeholder itself is 6), and merge tags (count the placeholder text as-is since it gets replaced). No message may exceed 160 characters.

2. **Notification preview test:** Read only the first 40 characters of each message. Does the preview convey enough value to make someone tap and read the full message? If the first 40 characters are wasted on a greeting or brand name, restructure the message to front-load the hook.

3. **Friend test:** Read each message aloud as if you received it from a friend. Does it sound natural? If any message sounds like it came from a corporate marketing department, rewrite it. Every SMS should feel personal.

4. **Emoji audit:** Verify each message has exactly one emoji. Verify the emoji matches the tone and is not generic or overused (avoid fire emoji, 100 emoji, or praying hands unless they genuinely fit the brand voice).

5. **CTA clarity test:** For each message, identify the CTA. Is it specific? Does the reader know exactly what to do next? "Shop now" is generic. "Grab the set" is specific. "Check it out" is vague. "See what's new" is slightly better. Make every CTA as specific and action-oriented as possible.

6. **Words-to-avoid scan:** Search every message for any word or phrase from the client's "Words to Avoid" list. Remove and replace any that appear.

7. **Urgency ethics check:** Review the abandoned cart, flash sale, back-in-stock, and winback messages. Is the urgency genuine or manufactured? Remove any pressure tactics, false scarcity claims, or guilt-tripping language. Urgency should come from real deadlines, real stock limitations, or genuine value — not emotional manipulation.

---

## Example Output

**Brand used for this example:**

```
[BRAND_NAME] = Bare Route
[BRAND_VOICE] = Smart, approachable, slightly sarcastic — like your friend who happens to be a skincare scientist. Warm but honest. Never preachy.
[TARGET_AUDIENCE] = Skincare-obsessed Gen Z and young millennials (18-30) who opted into SMS, likely from the website or a social media ad. They've tried tons of products and are intrigued by the "fewer ingredients" angle.
[PRODUCT_SERVICE] = Minimalist skincare line — Gel Cleanser ($22), Barrier Repair Serum ($38), Daily Moisturizer ($28). The Full Routine Set is $75 (saves $13). Every product has 5 or fewer ingredients.
[PRICE_RANGE] = $22-$38 per product, $75 for the set
[KEY_DIFFERENTIATOR] = 5 or fewer ingredients per product. Founded by Priya, a cosmetic chemist with 12 years of industry experience. No fragrance, no filler, no BS.
[COMPETITOR_NAMES] = CeraVe, The Ordinary, Drunk Elephant, Glossier, Versed
[WORDS_TO_USE] = simple, real, bare, routine, ingredients, skin barrier, works, fewer, enough
[WORDS_TO_AVOID] = miracle, anti-aging, flawless, perfect skin, transformation, luxury, glow up
[TONE_SCALE] = Casual 1/5 | Playful 2/5 | Bold 2/5
[CAMPAIGN_GOAL] = Drive first purchases (convert browsers to buyers), recover abandoned carts, increase repeat purchases, build a loyal SMS subscriber base that feels like an insider community.
[ADDITIONAL_CONTEXT] = Welcome offer is 20% off first order with code BARE20. The Barrier Repair Serum is the newest and most popular product. The brand just restocked the serum after a 2-week sellout. Loyalty program is called "The Inner Circle" and offers early access + free shipping. Standard shipping is free over $50. The brand's personality on SMS should feel like getting a text from a smart friend who's looking out for your skin.
```

---

### 1. Welcome SMS

**Trigger:** Immediately after SMS opt-in (via website popup, checkout, or social ad)
**Goal:** Deliver the welcome offer, set the tone for the SMS relationship, and drive first purchase

**Message:**
Hey {first_name}! Your 20% off code: BARE20. Fewer ingredients, happier skin. Grab the routine set and save even more. [LINK]

**Character Count:** 131
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Set as the first message in the SMS welcome flow
- Merge tag: {first_name} pulls from sign-up form or Shopify customer data
- If the subscriber already has a purchase history, suppress this message and route to a "welcome back" variant
- Delay: Send immediately upon opt-in (within 60 seconds)

---

### 2. Abandoned Cart SMS

**Trigger:** 45 minutes after cart abandonment (product left in cart, checkout not completed)
**Goal:** Recover the sale with a gentle, non-pushy reminder that feels helpful, not desperate

**Message:**
Still thinking about it? Your {product_name} is waiting. No pressure — just didn't want you to forget. [LINK]

**Character Count:** 112
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Merge tag: {product_name} pulls the specific product left in cart (e.g., "Barrier Repair Serum")
- Timing: 45 minutes is the sweet spot — long enough to not feel stalkerish, short enough that the intent is still warm
- If the cart contains the Full Routine Set, consider a variant: "Your routine set is still in your cart. Free shipping included. Just saying. [LINK]"
- Suppress if purchase is completed before send time
- Do not include a discount in the first abandoned cart SMS — save the discount for a second follow-up at 24 hours if needed

---

### 3. Flash Sale SMS

**Trigger:** Sent to full SMS list at the start of a flash sale event
**Goal:** Drive immediate traffic and purchases with a time-limited offer

**Message:**
25% off everything for 24 hours. Code: BARE25. The routine set drops to $56. Today only. [LINK]

**Character Count:** 101
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Send to full SMS subscriber list
- Best send time: 10:00-11:00 AM local time on a weekday (Tuesday-Thursday perform best for flash sales)
- Set up a follow-up reminder SMS 4 hours before the sale ends: "Last call — BARE25 expires at midnight. Just a heads up. [LINK]"
- Segment out customers who already purchased during the sale window to avoid the reminder
- Update the dollar amount ($56) to reflect the actual discounted price of the current set

---

### 4. New Product Launch SMS

**Trigger:** Sent to SMS list 1-2 hours before or simultaneously with public launch
**Goal:** Make SMS subscribers feel like insiders with early or exclusive access, drive launch-day sales

**Message:**
You're seeing this before everyone else. The Barrier Repair Serum is live. 5 ingredients. Your skin barrier will thank you. [LINK]

**Character Count:** 131
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Send 1-2 hours before the product goes live on social media or the website publicly
- The "before everyone else" framing is key for SMS — subscribers need to feel the channel gives them something they cannot get elsewhere
- Optionally segment VIP/high-value customers for even earlier access (see VIP message below)
- Consider a follow-up SMS 24 hours post-launch with early sales data or social proof: "The Barrier Repair Serum sold 500 units in the first 12 hours. Grab yours before it's gone. [LINK]"

---

### 5. Back in Stock SMS

**Trigger:** Sent to customers who viewed or wishlisted a sold-out product, within 1 hour of restock
**Goal:** Convert high-intent customers immediately before the product sells out again

**Message:**
It's back. The Barrier Repair Serum restocked and it won't last long (it sold out in 11 days last time). [LINK]

**Character Count:** 113
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Send only to customers who triggered a "back in stock" notification, visited the sold-out product page, or added it to a wishlist
- Timing is critical: send within 1 hour of restock going live
- The "sold out in 11 days" detail creates genuine urgency based on real data — update this with actual sellout timeline
- Suppress if the customer has already purchased since restock
- Consider a smaller follow-up to the broader SMS list 4-6 hours later if stock allows

---

### 6. Shipping Confirmation SMS

**Trigger:** Sent when the order ships and a tracking number is generated
**Goal:** Build excitement for delivery, reduce "where's my order" support tickets, reinforce the brand experience

**Message:**
Your Bare Route order just shipped! Track it here: [LINK]. Your skin is about to have a really good week.

**Character Count:** 110
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Integrate with Shopify or fulfillment platform to trigger on shipping confirmation event
- [LINK] should point to the tracking page (AfterShip, Route, or carrier tracking)
- This message is transactional (order-related), which means it has higher legal latitude than promotional SMS, but keep the tone consistent with the brand
- If the brand uses a delivery experience platform (like Route or Malomo), link to the branded tracking page rather than a generic carrier page

---

### 7. Review Request SMS

**Trigger:** 10 days after delivery confirmation (enough time to try the product)
**Goal:** Generate product reviews for social proof on the website and in ads

**Message:**
Hey {first_name}, how's the routine treating you? Quick review would mean the world to a small brand like us. [LINK]

**Character Count:** 119
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Delay 10 days after delivery (not after shipping — after confirmed delivery via tracking data)
- Merge tag: {first_name} for personalization
- [LINK] should go directly to the review submission page for the specific product purchased, not a generic review page
- If the customer purchased multiple products, link to a page where they can review all items
- Suppress if the customer has already left a review or if they contacted support with a complaint (route those to customer service instead)
- Consider a follow-up 5 days later for non-responders: "No pressure — but if you've got 30 seconds, a review really helps us out. [LINK]"

---

### 8. VIP/Loyalty Exclusive SMS

**Trigger:** Sent to "Inner Circle" loyalty members or customers with 3+ purchases, for exclusive offers or early access
**Goal:** Reward loyalty, make high-value customers feel recognized, drive repeat purchases

**Message:**
Inner Circle perk: free shipping + early access to our spring drop. Live for you now, everyone else gets it Friday. [LINK]

**Character Count:** 127
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Segment: Only send to customers tagged as "Inner Circle" members or with 3+ lifetime purchases
- The key value proposition is exclusivity — the offer or access must genuinely be unavailable to the general list at the time of sending
- "Everyone else gets it Friday" creates a specific, real exclusivity window
- Update the offer details (spring drop, free shipping) to match the actual VIP perk being offered
- Track conversion rate from VIP SMS separately to demonstrate the ROI of the loyalty program

---

### 9. Birthday/Anniversary SMS

**Trigger:** Sent on the customer's birthday (if collected) or on the anniversary of their first purchase
**Goal:** Celebrate the customer, drive a purchase with a personal offer, reinforce brand affinity

**Message:**
Happy birthday, {first_name}! Here's 30% off on us. Code: BDAYBARE. Treat yourself to something your skin actually needs. [LINK]

**Character Count:** 130
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Trigger: Customer birthday (from profile data) or first-purchase anniversary if birthday is not collected
- Merge tag: {first_name}
- Birthday discount should be higher than standard promos (30% vs. the usual 20%) to feel special
- Code "BDAYBARE" should be unique or time-limited (expires in 7 days) to prevent sharing/abuse
- Send at 9:00 AM local time on the birthday for maximum delight
- For anniversary variant: "It's been a year since you simplified your routine. Here's 30% off to celebrate. Code: BARE365. [LINK]"

---

### 10. Winback SMS

**Trigger:** Sent 75 days after last purchase (no activity, no site visits, no email opens in 60+ days)
**Goal:** Re-engage lapsed customers with a low-pressure, generous offer that acknowledges the gap without guilt-tripping

**Message:**
Been a minute, {first_name}. Your skin barrier might be missing us. 25% off to come back: BAREBACK. [LINK]

**Character Count:** 111
**Compliance Note:** Reply STOP to opt out.

**Platform Notes:**
- Trigger: 75 days since last purchase AND no site visit or email engagement in 60+ days
- This is the most sensitive SMS in the lifecycle — the customer has gone quiet and one wrong message pushes them to unsubscribe
- The tone must be light and no-pressure. "Been a minute" acknowledges the gap casually without saying "We miss you!" or "Where'd you go?"
- 25% off is intentionally higher than standard offers — lapsed customers need a stronger incentive to return
- Code "BAREBACK" should expire in 14 days to create soft urgency
- If no conversion after 14 days, suppress the customer from promotional SMS for 30 days before trying one final winback attempt
- If no conversion after the second attempt, consider moving the customer to email-only communication to preserve the SMS relationship for customers who are actually engaged

---

### Compliance and Legal Notes (Include for Client)

**Important: SMS Marketing Compliance Reminders**

All SMS marketing in the United States must comply with the Telephone Consumer Protection Act (TCPA) and carrier guidelines. The following are standard requirements:

- **Opt-in required:** Only send messages to customers who have explicitly opted in to receive SMS marketing. Double opt-in is recommended.
- **Opt-out in every message:** Every promotional SMS must include opt-out instructions ("Reply STOP to opt out" or similar). Most SMS platforms (Klaviyo, Postscript, Attentive) append this automatically.
- **Quiet hours:** Do not send promotional SMS before 8:00 AM or after 9:00 PM in the recipient's local timezone. Transactional messages (shipping confirmations) are exempt.
- **Frequency cap:** Recommended maximum of 4-6 promotional SMS messages per month per subscriber. Over-messaging is the fastest path to opt-outs.
- **Transactional vs. promotional:** Shipping confirmations and order updates are transactional. Flash sales, new launches, and winbacks are promotional. Different rules apply — consult your SMS platform's compliance documentation.
- **Record-keeping:** Maintain records of opt-in consent, message timestamps, and opt-out requests for a minimum of 5 years.

These messages are templates. Before deploying, have the client's legal team or SMS platform compliance team review them for full regulatory compliance in their jurisdiction.

---

*End of SMS marketing package for Bare Route.*

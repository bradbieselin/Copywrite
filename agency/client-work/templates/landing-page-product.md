# Product Landing Page Copy Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | Full product landing page copy for a single hero product or product line — hero through final CTA, every section written and formatted for handoff to design/dev |
| **Turnaround** | 30-45 minutes with Claude, plus 15-20 minutes for QA and client-specific tweaks |
| **Quality bar** | Ready to drop into a Shopify page, Webflow build, or Figma mockup without rewriting. Copy should read like it was written by a senior DTC copywriter who has spent a week inside the brand. |
| **Best for** | New product launches, hero product pages, flagship SKU pages, seasonal product pushes, reformulated/relaunched products |

---

## Client Brand Variables

Fill in every variable below before pasting into Claude. If a variable is not applicable, write "N/A" — do not delete the line.

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
[TONE_SCALE] = (1 = very casual/playful, 10 = very formal/clinical)
[CAMPAIGN_GOAL] =
[ADDITIONAL_CONTEXT] =
```

### Variable Guidance

- **BRAND_VOICE**: Go beyond one word. Instead of "friendly," write "friendly like a knowledgeable hiking buddy — not a personal trainer yelling at you."
- **TARGET_AUDIENCE**: Include demographics, psychographics, and the moment they are in when they land on this page. Example: "Weekend athletes aged 30-50 who feel fine during the activity but pay for it on Monday. They are not gym bros. They have jobs, families, and two days a week to do the thing they love."
- **KEY_DIFFERENTIATOR**: The one thing this product does that competitors do not, stated in plain language. Not a feature list — a positioning statement.
- **WORDS_TO_USE**: Brand-approved vocabulary. Include any proprietary ingredient names, trademarked phrases, or preferred terminology.
- **WORDS_TO_AVOID**: Blacklisted words, competitor names that should not appear, industry jargon the brand considers off-putting, and any regulatory no-go terms.
- **TONE_SCALE**: This controls formality. A 3 gets contractions, sentence fragments, and conversational rhythm. A 7 gets complete sentences, measured claims, and a more editorial feel.
- **ADDITIONAL_CONTEXT**: Anything else. Regulatory constraints (FDA, FTC), specific claims that have been approved, existing taglines to incorporate, seasonal tie-ins, upcoming PR or influencer campaigns that the page should align with.

---

## The Prompt

Paste the filled-in variables above this prompt, then paste the prompt below into Claude.

---

```
You are a senior direct-to-consumer copywriter with 10+ years of experience writing high-converting product landing pages for DTC brands. You write copy that sounds like a real person — not a marketing department. You understand that landing pages are not brochures; they are sales conversations that happen in a specific order.

Using the brand variables I have provided above, write a complete product landing page for [PRODUCT_SERVICE] by [BRAND_NAME].

Follow this exact section order. Do not skip any section. Do not combine sections. Label each section with a clear heading so the design team can map copy to layout.

---

### SECTION 1: HERO

Write two (2) headline options. Each headline must be:
- 8 words maximum
- Active voice (subject does the action)
- Front-loaded with the most compelling benefit — the thing that makes a customer stop scrolling
- Free of cliches ("game-changer," "revolutionary," "next-level")

For each headline, write:
- A subheadline (15-25 words) that adds specificity. The subheadline answers the question "what does that actually mean for me?"
- CTA button text (2-5 words, action-oriented, first person preferred — e.g., "Start My Recovery" not "Buy Now")
- One supporting detail line (under 15 words) — this sits near the CTA and handles a micro-objection. Examples: "Free shipping over $50" or "30-day no-questions guarantee" or "Arrives in 2-3 days"

Write a brief note suggesting what type of image or video should accompany this hero section. Be specific — not "product image" but "hero product shot on a natural background with the product in use, showing [specific scenario relevant to the target audience]."

---

### SECTION 2: PROBLEM / AGITATION

Write 3-4 sentences that identify the pain point the target audience experiences. Rules:
- Start with the customer's experience, not the product
- Use specific, concrete details — not vague pain ("feeling tired" is vague; "dragging yourself to the coffee maker at 6am on Monday when your legs still burn from Saturday's trail" is specific)
- Match the emotional register of the target audience. If they are pragmatic people, do not overdramatize. If they are aspirational, lean into the gap between where they are and where they want to be.
- Do NOT mention the product yet. This section is entirely about the customer.
- Keep paragraphs to 2-3 sentences maximum.

---

### SECTION 3: SOLUTION INTRO

Write 2-3 sentences that bridge from the problem to the product. This is the pivot — the moment the page shifts from "I see you" to "here is what we built for you." Rules:
- Name the product naturally, as if recommending it to a friend
- Connect the product directly to the pain point from Section 2
- Do not list features yet. This is the emotional bridge, not the spec sheet.

---

### SECTION 4: BENEFITS

Write 3-5 benefits. For each benefit:
- A bold headline of 5 words maximum. The headline should name the outcome, not the feature. ("Sleep Through the Night" not "Contains Magnesium")
- A 2-sentence explanation. Sentence one states the benefit in customer terms. Sentence two supports it with a specific detail — an ingredient, a design choice, a process — that makes the benefit credible.

Order the benefits from most compelling to least compelling. The first benefit should be the one that, if the customer read nothing else, would make them consider buying.

---

### SECTION 5: SOCIAL PROOF BLOCK

Write this section with the following components:
1. A short introductory line that frames the social proof (e.g., "Join 12,000+ weekend warriors who recovered smarter" or "Rated 4.8 stars by people who actually use this"). Use a specific number if provided in the brand variables; if not, use a plausible placeholder and flag it with [INSERT ACTUAL NUMBER].
2. One complete sample testimonial (3-5 sentences) written in the voice of the target audience. The testimonial should:
   - Reference a specific use case or scenario
   - Mention a before/after experience
   - Sound like a real person, not a copywriter (include minor imperfections, conversational language)
   - End with a name, age range, and location or activity type (e.g., "— Sarah M., 38, trail runner")
3. Placement notes for the design team: recommend how many testimonials to display, whether to use star ratings, whether to include photos, and where to source UGC (reviews platform, social media, etc.)

---

### SECTION 6: HOW IT WORKS / WHAT'S IN IT

Write a 3-step "How It Works" section OR an ingredients/materials breakdown — choose whichever is more appropriate for the product type.

If How It Works:
- Each step gets a number, a short headline (4-6 words), and a 1-2 sentence explanation
- Steps should be dead simple. If a customer cannot understand the process in 10 seconds, simplify it.
- Include a note for any supporting visual (icon, illustration, photo) for each step

If Ingredients / What's In It:
- List 3-5 key ingredients or materials
- For each: name, amount/concentration if relevant, and a plain-English explanation of what it does and why it matters
- Include a note about any certifications (organic, vegan, cruelty-free, etc.) if provided in brand variables
- Do NOT use pseudo-scientific language. Write like you are explaining to a smart friend, not writing a product label.

---

### SECTION 7: COMPARISON SECTION

Write a "Why [PRODUCT_SERVICE] vs. [alternative]" section. The alternative can be a competitor category (not a named competitor unless specified in brand variables), a DIY approach, or the "do nothing" option.

Write 3-4 conversational comparison points. Each point should:
- Be framed from the customer's perspective ("Most recovery supplements load you up with caffeine. [Product] works while you sleep.")
- Avoid directly bashing competitors. Instead, highlight the structural difference in approach.
- Feel like a friend explaining why they switched, not a brand dunking on the competition.

Format as short paragraphs, not a comparison table. Comparison tables feel clinical. This should feel like a conversation.

---

### SECTION 8: FAQ SECTION

Write 5 Q&As covering these five topics:
1. Shipping (how long, where, cost)
2. Returns / guarantee
3. Ingredients / materials / what's in it
4. Sizing / dosage / how to use
5. One objection-handling question (identify the most likely objection for this product and audience, and answer it directly)

Rules:
- Questions should be written in the customer's voice, not the brand's voice. ("How long until I feel a difference?" not "What is the recommended usage period?")
- Answers should be in brand voice, 2-4 sentences each
- Answers should be honest and specific. Vague answers ("results may vary") erode trust. Specific answers ("most customers report noticeable differences within 7-10 days of consistent use") build it.
- If you do not have specific information (e.g., exact shipping times), write a plausible answer and flag it with [CONFIRM WITH CLIENT].

---

### SECTION 9: FINAL CTA SECTION

Write an urgency-driven closing section with:
- A headline (8 words max) that reframes the core benefit or introduces a time-sensitive element
- A subheadline (1-2 sentences) that summarizes the offer and reduces risk
- CTA button text (match or complement the hero CTA)
- 2-3 trust badge suggestions (e.g., "30-Day Guarantee," "Free Shipping," "10,000+ Sold") — use real data from brand variables or flag as [CONFIRM WITH CLIENT]

Include a note on whether this section should include a product image, a lifestyle image, or a minimal/text-focused design.

---

### GENERAL RULES FOR ALL SECTIONS:
- Keep paragraphs to 2-3 sentences maximum throughout the entire page.
- Write in active voice wherever possible.
- Front-load the most important information in every sentence.
- Include notes for images, videos, or UGC placements in brackets like [IMAGE NOTE: ...] or [VIDEO NOTE: ...]
- Do not use exclamation marks more than twice on the entire page.
- Do not use the word "just" as a minimizer.
- Every claim should be supportable. Do not invent clinical studies or statistics. If a claim needs substantiation, flag it with [NEEDS SUBSTANTIATION].
- Write at a 7th-8th grade reading level. Short sentences. Common words. No jargon unless it is industry-standard terminology the audience already uses.
```

---

## Output Format

The output should follow this exact structure:

```
## SECTION 1: HERO

### Option A
**Headline:** [8 words max]
**Subheadline:** [15-25 words]
**CTA Button:** [2-5 words]
**Supporting Detail:** [under 15 words]

### Option B
**Headline:** [8 words max]
**Subheadline:** [15-25 words]
**CTA Button:** [2-5 words]
**Supporting Detail:** [under 15 words]

[IMAGE/VIDEO NOTE: description]

---

## SECTION 2: PROBLEM / AGITATION

[3-4 sentences, 2-3 sentence paragraphs max]

---

## SECTION 3: SOLUTION INTRO

[2-3 sentences]

---

## SECTION 4: BENEFITS

**[Benefit 1 Headline — 5 words max]**
[2-sentence explanation]

**[Benefit 2 Headline — 5 words max]**
[2-sentence explanation]

**[Benefit 3 Headline — 5 words max]**
[2-sentence explanation]

[Repeat for up to 5 benefits]

---

## SECTION 5: SOCIAL PROOF

[Introductory line]

> "[Testimonial text, 3-5 sentences]"
> — [Name], [Age], [Activity/Location]

[Design/placement notes]

---

## SECTION 6: HOW IT WORKS / WHAT'S IN IT

**Step 1: [Headline]**
[1-2 sentence explanation]
[ICON/IMAGE NOTE: description]

**Step 2: [Headline]**
[1-2 sentence explanation]
[ICON/IMAGE NOTE: description]

**Step 3: [Headline]**
[1-2 sentence explanation]
[ICON/IMAGE NOTE: description]

---

## SECTION 7: WHY [PRODUCT] VS. [ALTERNATIVE]

[3-4 conversational comparison paragraphs]

---

## SECTION 8: FAQ

**Q: [Question in customer voice]**
A: [Answer in brand voice, 2-4 sentences]

[Repeat for all 5 Q&As]

---

## SECTION 9: FINAL CTA

**Headline:** [8 words max]
**Subheadline:** [1-2 sentences]
**CTA Button:** [2-5 words]
**Trust Badges:** [2-3 badges]

[Design note]
```

### Word Count Targets

| Section | Target Word Count |
|---|---|
| Hero (both options combined) | 80-120 words |
| Problem / Agitation | 60-90 words |
| Solution Intro | 40-60 words |
| Benefits (all combined) | 150-250 words |
| Social Proof | 100-150 words |
| How It Works / What's In It | 100-175 words |
| Comparison | 120-180 words |
| FAQ (all combined) | 250-400 words |
| Final CTA | 40-70 words |
| **Total page copy** | **940-1,495 words** |

---

## Quality Checks Before Sending

Run through every item below before delivering to the client. If any check fails, revise before sending.

1. **Headline word count**: Confirm both hero headlines are 8 words or fewer. Count them manually — contractions count as one word.
2. **Active voice audit**: Read every headline and the first sentence of every section. If any sentence buries the subject after the verb or uses passive construction ("is designed to," "was created for"), rewrite it.
3. **Brand voice match**: Read the copy aloud. Does it sound like the brand described in the variables, or does it sound like generic DTC copy? Check specifically for words on the WORDS_TO_AVOID list and confirm that WORDS_TO_USE appear at least 2-3 times naturally.
4. **Benefit vs. feature check**: In Section 4, confirm that every bold headline names an outcome the customer experiences, not a product feature or ingredient. "Recover Faster" is a benefit headline. "Contains Tart Cherry Extract" is a feature headline.
5. **Specificity sweep**: Scan for vague language — "high-quality," "premium," "best-in-class," "cutting-edge," "innovative." Replace every instance with a concrete detail. If you cannot replace it with a concrete detail, delete it.
6. **CTA consistency**: Confirm that the hero CTA and the final CTA work together. They should feel like the same ask, stated differently. If the hero says "Start My Recovery" the final CTA should not say "Buy Now."
7. **Flag check**: Search the output for all bracketed flags ([CONFIRM WITH CLIENT], [INSERT ACTUAL NUMBER], [NEEDS SUBSTANTIATION]). List them in a delivery note so the client knows exactly what needs their input.

---

## Example Output

The following is a complete example output using the fictional brand below. This demonstrates the expected quality, length, and format for every section.

**Brand variables used for this example:**

```
[BRAND_NAME] = Basecamp Nutrition
[BRAND_VOICE] = Knowledgeable and encouraging, like a friend who happens to know a lot about sports nutrition. Grounded, not hype-y. We sound like the person at the trailhead who shares their snacks and actually knows what's in them. Never condescending, never bro-science.
[TARGET_AUDIENCE] = Weekend athletes aged 30-55 — hikers, skiers, mountain bikers, trail runners. They are not bodybuilders or gym rats. They have full-time jobs and families, and they spend their weekends doing the things that make them feel alive. They push hard on Saturday, feel it on Monday, and are searching for something that actually works without a cabinet full of supplements.
[PRODUCT_SERVICE] = Summit Recovery — a post-activity recovery supplement (powder, mixed with water) designed for endurance and outdoor athletes. Tart cherry extract, magnesium glycinate, turmeric curcumin, electrolytes, and adaptogenic herbs. No caffeine, no artificial sweeteners, no proprietary blends.
[PRICE_RANGE] = $45 for a 30-serving tub (about $1.50/serving)
[KEY_DIFFERENTIATOR] = Built specifically for outdoor/endurance athletes — not repurposed bodybuilder supplements. Clean label, full transparency on ingredients and dosages, works overnight so you wake up ready instead of wrecked.
[COMPETITOR_NAMES] = N/A (do not name competitors)
[WORDS_TO_USE] = trail-tested, clean label, full transparency, real ingredients, weekend warrior, recover smarter, overnight recovery, wake up ready
[WORDS_TO_AVOID] = gains, shredded, beast mode, crush it, no pain no gain, hack, biohack, proprietary blend, revolutionary, game-changer
[TONE_SCALE] = 4 (conversational, warm, knowledgeable — but not sloppy)
[CAMPAIGN_GOAL] = Drive first-time purchases of Summit Recovery. Primary conversion is single-tub purchase. Secondary conversion is subscribe-and-save.
[ADDITIONAL_CONTEXT] = The brand launched 8 months ago. They have about 1,200 customers and a 4.7-star average rating across 340 reviews. They are not making any FDA claims — keep copy compliant. The subscribe-and-save option is 20% off. Free shipping on orders over $50.
```

---

### EXAMPLE OUTPUT BEGINS HERE

---

## SECTION 1: HERO

### Option A

**Headline:** Wake Up Ready for Monday's Mountains

**Subheadline:** Summit Recovery is the overnight recovery drink built for weekend athletes who push hard and need to bounce back by Monday morning.

**CTA Button:** Start My Recovery

**Supporting Detail:** Free shipping on orders over $50. 30-day guarantee.

### Option B

**Headline:** Your Weekend Shouldn't Wreck Your Week

**Subheadline:** Summit Recovery uses tart cherry, magnesium, and turmeric to help your body repair overnight — so Saturday's trail doesn't ruin Monday's meeting.

**CTA Button:** Try Summit Recovery

**Supporting Detail:** $1.50/serving. Cancel your subscribe-and-save anytime.

[IMAGE NOTE: Hero shot of the Summit Recovery tub on a rough-hewn wooden surface — a kitchen counter or cabin table — with hiking boots slightly out of focus in the background. The setting should feel like "end of a good day outdoors," not a supplement store. If video, consider a 10-second loop: someone pouring the powder into a glass of water in the evening, then a morning cut of them lacing up boots and heading out the door.]

---

## SECTION 2: PROBLEM / AGITATION

You know the feeling. Saturday was perfect — miles of trail, cold air in your lungs, the kind of tired that actually feels earned. But by Sunday afternoon, your legs have turned to concrete. Your lower back aches every time you stand up from the couch.

Monday morning rolls around and you are moving like someone twice your age. You love what you do on the weekends, but the recovery tax is getting harder to pay. And the supplement aisle is not helping — it is a wall of neon labels designed for people who deadlift for fun, not for people who ski for joy.

---

## SECTION 3: SOLUTION INTRO

That is exactly why we made Summit Recovery. It is a clean, no-nonsense recovery drink designed for people who spend their weekends outside — not in a gym. Mix a scoop with water before bed, and let your body do what it already knows how to do, with the right ingredients to help it along.

---

## SECTION 4: BENEFITS

**Recover While You Sleep**
Summit Recovery works overnight, supporting your body's natural repair processes while you rest. The combination of tart cherry extract and magnesium glycinate helps reduce muscle soreness and supports deeper, more restorative sleep — so you wake up feeling like a person again.

**Every Ingredient, Fully Transparent**
There are no proprietary blends here — every ingredient and its exact dosage is printed right on the label. You will find tart cherry extract (500mg), magnesium glycinate (400mg), turmeric curcumin with black pepper extract (300mg), a full electrolyte profile, and adaptogenic herbs including ashwagandha and rhodiola.

**Built for Trails, Not Treadmills**
Most recovery supplements are designed for bodybuilders and gym-goers — high-stim, loaded with artificial flavors, and focused on muscle growth. Summit Recovery was formulated from day one for endurance and outdoor athletes who need joint support, inflammation management, and overnight restoration.

**No Junk, No Surprises**
Zero caffeine, zero artificial sweeteners, zero dyes. Summit Recovery is sweetened with monk fruit, flavored with real tart cherry, and free from the long list of unpronounceable ingredients you have learned to side-eye. Clean label means you actually understand what you are putting in your body.

**One Scoop, One Glass, Done**
Recovery should not be complicated. One scoop in 8-10 ounces of water before bed. That is it. No stacking four different supplements, no timing windows, no complicated protocols. Simple works.

---

## SECTION 5: SOCIAL PROOF

**Rated 4.7 stars across 340+ reviews from people who actually spend their weekends outside.**

> "I have tried a bunch of recovery stuff over the years and most of it either tastes terrible or is clearly made for 22-year-old CrossFitters. Summit Recovery is different. I take it Sunday night after a long day of skiing and Monday morning I actually feel human. My knees still know I skied, but the full-body concrete feeling is gone. I have been using it for about three months now and it is the one supplement I actually re-order."
> — Kevin R., 44, backcountry skier, Colorado

[DESIGN NOTES: Display 3-4 testimonials in a carousel or stacked layout. Include star ratings with each testimonial. If UGC photos are available from customers (trail photos, activity shots — not selfies with the product), pair one photo with each testimonial. Source reviews from the Shopify reviews app and cross-reference with any testimonials shared on Instagram or in customer emails. If available, include a small "Verified Buyer" badge on each testimonial.]

---

## SECTION 6: HOW IT WORKS

**Step 1: Finish Your Day Outside**
Ski the mountain. Ride the trail. Hike the ridge. Whatever your weekend looks like, go do the thing you love and push as hard as you want to.

[ICON NOTE: Simple line illustration of a mountain or trail — active, not restful. This should feel aspirational.]

**Step 2: Mix a Scoop Before Bed**
One scoop of Summit Recovery in 8-10 ounces of cold water. It tastes like tart cherry — because it is tart cherry. Drink it 30-60 minutes before you hit the pillow.

[ICON NOTE: Simple line illustration of a glass with powder being poured in, or a scoop next to a glass. Evening/night setting cue — maybe a moon or window with stars.]

**Step 3: Wake Up Ready**
While you sleep, the tart cherry, magnesium, turmeric, and adaptogens get to work — supporting muscle repair, managing inflammation, and helping your body bounce back. Morning you is going to be pleasantly surprised.

[ICON NOTE: Simple line illustration of a sunrise or someone stretching in the morning. The feeling should be "fresh start," not "alarm clock dread."]

---

## SECTION 7: WHY SUMMIT RECOVERY VS. THE USUAL OPTIONS

Most recovery supplements are built for a different kind of athlete. They are loaded with creatine, BCAAs, and stimulants designed to support heavy lifting and muscle growth. That is great if you are training for a bodybuilding show. It is not so great if you spent six hours on a mountain bike and your primary goal is to walk down the stairs without wincing tomorrow.

Then there is the "just take ibuprofen" approach. It works in the short term, but relying on NSAIDs after every weekend outing is not a long-term strategy — and most weekend athletes know it. Your body deserves actual nutritional support, not a band-aid.

Some people try to piece it together themselves — a magnesium pill here, a turmeric capsule there, some electrolyte tabs from the running store. It works, sort of, but it is expensive, inconvenient, and you are guessing on dosages. Summit Recovery puts the full stack in one scoop, dosed at levels that actually do something, in a form your body can absorb.

The bottom line: Summit Recovery was built from scratch for people like you. Outdoor athletes. Weekend warriors. People who work hard Monday through Friday so they can play hard Saturday and Sunday. Every ingredient choice, every dosage, every flavor decision was made with you in mind — not someone else.

---

## SECTION 8: FAQ

**Q: How fast will my order arrive?**
A: Most orders ship within 1-2 business days from our warehouse in Denver. Standard shipping takes 3-5 business days depending on where you are. If you are in the mountain west, it is usually closer to 2-3 days. Orders over $50 ship free — a single tub of Summit Recovery is $45, so adding anything else to your cart gets you there. [CONFIRM WITH CLIENT: exact shipping times and carrier]

**Q: What if it does not work for me?**
A: We have a straightforward 30-day guarantee. If you try Summit Recovery and it is not making a noticeable difference in your recovery, email us and we will refund your purchase. No hoops, no "send back the unused portion" games. We stand behind this product because we use it ourselves — but we understand that every body is different.

**Q: What is actually in this stuff?**
A: Everything is right on the label — no proprietary blends, no mystery ingredients. The key players are tart cherry extract (500mg) for muscle soreness and sleep support, magnesium glycinate (400mg) for muscle relaxation and recovery, turmeric curcumin with black pepper extract (300mg) for inflammation, a full electrolyte blend to replenish what you sweat out, and adaptogenic herbs (ashwagandha and rhodiola) for stress recovery and energy balance. Zero caffeine, zero artificial sweeteners, sweetened with monk fruit. Full ingredient list and third-party test results are available on the product page.

**Q: How do I take it? Does timing matter?**
A: One scoop in 8-10 ounces of cold water, 30-60 minutes before bed. The timing matters because several of the key ingredients — especially magnesium and tart cherry — support your body's overnight repair processes. Taking it before bed lets the ingredients work in sync with your natural recovery cycle. You can take it after water, milk, or your preferred liquid, but cold water with a quick stir or shake works best for taste.

**Q: I am not a serious athlete — will this still help me?**
A: Absolutely. You do not need to be running ultramarathons to benefit from Summit Recovery. If you hike a few miles on the weekend, take a ski trip a few times a season, or ride your bike on Saturday mornings, you are putting your body through real work — and you deserve real recovery support. Most of our customers are not professional athletes. They are people with jobs and families who want to feel good on Monday after doing the things they love on Saturday. That is exactly who we built this for.

---

## SECTION 9: FINAL CTA

**Headline:** This Weekend, Recover Smarter

**Subheadline:** One scoop before bed. Real ingredients at real dosages. Wake up ready to do it all again — backed by our 30-day guarantee and free shipping on orders over $50.

**CTA Button:** Start My Recovery

**Trust Badges:** 30-Day Money-Back Guarantee | Free Shipping Over $50 | 340+ Five-Star Reviews

[DESIGN NOTE: Keep this section clean and focused. A single product image — the tub with a scoop leaning against it — on one side, with the headline, subheadline, CTA, and trust badges on the other. Consider including a secondary "Subscribe & Save 20%" link below the primary CTA button. Background should be warm and grounded — no neon, no aggressive energy. This is the quiet confidence close, not the hard sell.]

---

### EXAMPLE OUTPUT ENDS HERE

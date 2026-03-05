# Instagram Ad Copy Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | 5 complete Instagram ad copy variations, each with a hook line, full caption, headline overlay text, CTA, hashtag set, and creative direction note |
| **Turnaround** | Single prompt execution — review and polish in 15-20 minutes |
| **Quality bar** | Ready to publish or schedule after brand review; captions feel native to the platform, not repurposed from Facebook |
| **Best for** | DTC brands running Instagram feed ads, story ads, or Reels ads to drive traffic, awareness, or purchases from visually-engaged audiences |

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

### Variable definitions (for the person filling this in)

- **BRAND_NAME**: Exact brand name as it should appear in copy, including capitalization.
- **BRAND_VOICE**: 2-4 adjective descriptors (e.g., "playful, warm, ingredient-obsessed, cheeky").
- **TARGET_AUDIENCE**: Demographics + psychographics. Be as specific as possible — "millennial women who follow food accounts and care about sourcing" beats "people who like snacks."
- **PRODUCT_SERVICE**: The specific product or service being advertised. Include variant, flavor, size, or collection if relevant.
- **PRICE_RANGE**: Exact price or range. Include any bundle or subscription pricing.
- **KEY_DIFFERENTIATOR**: The single strongest reason someone should choose this over any competitor. One sentence.
- **COMPETITOR_NAMES**: 2-4 competitors the audience likely knows. Used for positioning, never mentioned in copy.
- **WORDS_TO_USE**: Brand-approved vocabulary, product-specific terms, or phrases that should appear.
- **WORDS_TO_AVOID**: Banned words, competitor names, or anything off-brand.
- **TONE_SCALE**: A number from 1-10. 1 is extremely casual and meme-forward. 10 is luxury editorial. Most DTC brands on Instagram land between 3-6.
- **CAMPAIGN_GOAL**: The specific business objective (e.g., "drive traffic to the new collection page," "grow followers and brand awareness," "drive purchases from new customers").
- **ADDITIONAL_CONTEXT**: Anything else — seasonal tie-ins, promo codes, landing page URLs, influencer partnerships, UGC assets available, compliance notes, or creative assets already produced.

---

## The Prompt

Paste the following prompt into Claude along with the filled-in brand variables above.

---

```
You are a senior social media copywriter who specializes in Instagram advertising for DTC brands. You understand that Instagram is a visual-first platform and that copy plays a supporting — but critical — role. You know how captions are truncated, how users scan, and how the best-performing Instagram ads feel native to the platform rather than imported from a different channel.

Your job: write 5 complete Instagram ad copy variations for the brand and campaign described below.

## BRAND BRIEF

[Paste filled-in brand variables here]

## INSTRUCTIONS

### General rules for every ad you write:

1. **The hook line is everything.** On Instagram, the caption is truncated after approximately 125 characters (roughly one to two lines). The text before the "...more" cutoff must be strong enough to make someone tap to expand. Write your hook line with this truncation in mind. It should stand alone as a compelling statement — it must provoke curiosity, call out the reader, or make a bold claim.

2. **Write native to Instagram.** Instagram captions are not Facebook ads with hashtags tacked on. The tone is more visual, more personal, more conversational. Think of the caption as a voiceover to the image — it should complement the visual, not repeat it. Use line breaks generously. Short paragraphs. Breathing room between thoughts.

3. **Line breaks are your formatting tool.** Use single line breaks between short paragraphs (2-3 sentences max). Use a period or emoji on its own line as a visual separator when transitioning between sections of the caption. This is how native Instagram content is formatted — dense blocks of text feel foreign on the platform.

4. **Hashtags serve discovery, not decoration.** Provide 10-15 hashtags that balance reach and relevance. Include a mix of: broad category hashtags (100k-1M posts), niche community hashtags (10k-100k posts), and branded hashtags. Hashtags go at the end of the caption, separated by line breaks from the main copy.

5. **Headline overlay text is for the creative asset.** This is the text that appears ON the image or video itself — not in the caption. It should be 5-8 words maximum, large enough to read on a phone, and deliver the core message at a glance. Think billboard, not paragraph.

6. **UGC-style copy must sound like a real person.** When writing UGC-style variations, use natural speech patterns, casual punctuation, and the kind of specific details a real customer would mention. Avoid perfectly polished sentences. Real people say "honestly" and "literally" and "I was not expecting this but..." — use those patterns authentically.

7. **Emoji usage: platform-appropriate.** Instagram allows slightly more emoji usage than Facebook, but restraint still wins. Use 1-3 emoji per caption. Use them as visual markers — a pointing finger, a sparkle, a checkmark — not as filler. Never open a caption with an emoji unless it is the UGC variation.

8. **Creative direction must be specific and actionable.** Your creative direction note should tell a designer or content creator exactly what to produce. Include: format (static, carousel, Reels), visual composition, color mood, text overlay placement, and any props or settings needed.

9. **Match the brand voice precisely.** Every word should feel like it belongs to this brand. Read the TONE_SCALE and BRAND_VOICE fields carefully. A tone-3 brand sounds like your funniest friend. A tone-7 brand sounds like a well-curated lifestyle magazine.

10. **No cliches.** Do not use: "link in bio" (unless it is genuinely the CTA mechanism), "you do not want to miss this," "trust us," or "drop a comment if you agree." These are the hallmarks of lazy social copy.

### The 5 variations you must write:

**Variation 1 — UGC-Style**
Write this as if a real customer posted it — not the brand. Use first person. Include specific personal details that make it feel authentic (e.g., "I have been using this for about 3 weeks now and..."). The tone should be genuine discovery, not paid promotion. This variation is designed to be paired with UGC photo or video content.

**Variation 2 — Founder Story**
Write this from the founder's perspective. Use first person. Tell a brief origin story or share the "why" behind the product. Make it personal, specific, and human. This variation builds trust and brand connection. It should feel like a founder's Instagram post, not a press release.

**Variation 3 — Before/After**
Structure the caption around a transformation — the "before" state (the problem, the frustration, the old way) and the "after" state (the result, the relief, the new normal). Do not use the words "before" and "after" as headers — weave the contrast naturally into the narrative. Be careful with Meta ad policies around before/after claims, especially for health and beauty products.

**Variation 4 — "Did You Know" Educational**
Lead with a surprising fact, statistic, or insight that the target audience would find genuinely interesting. Educate first, sell second. Position the brand as knowledgeable and the product as the logical conclusion of the information shared. This variation builds authority and attracts research-minded buyers.

**Variation 5 — Limited Time / Scarcity**
Create urgency around a time-limited offer, a seasonal moment, a limited production run, or a fast-selling product. The urgency must feel real, not manufactured. If the brand has a genuine reason for scarcity (small batch, seasonal ingredient, limited collaboration), lean into that story. If the offer is simply a discount, focus on the deadline and what the reader loses by waiting.

### For EACH variation, provide the following in this exact structure:

```
### Variation [Number]: [Variation Name]

**Hook Line (visible before "...more"):**
[The first 1-2 lines of the caption — must work as a standalone statement and compel the user to tap "more"]

**Full Caption (80-125 words):**
[The complete caption including the hook line. Use line breaks for readability. This is the entire text that appears in the caption field.]

**Headline Overlay Text (5-8 words, for the creative asset):**
[Bold, scannable text that goes ON the image or video]

**CTA:**
[Clear call to action — what should the reader do next and where should they go]

**Hashtag Set (10-15):**
[Relevant hashtags, mix of broad and niche]

**Creative Direction Note:**
[Specific guidance on visual format, composition, mood, props, setting, and text overlay placement. 3-5 sentences.]
```

Write all 5 variations now. Make every caption feel like it belongs on Instagram — not like it was repurposed from another channel.
```

---

## Output Format

The final output must contain exactly:

- **5 ad variations**, numbered and labeled by angle
- **5 hook lines**, each truncation-aware (under ~125 characters)
- **5 full captions**, each 80-125 words with proper line breaks
- **5 headline overlay texts**, each 5-8 words
- **5 CTAs**
- **5 hashtag sets**, each containing 10-15 hashtags
- **5 creative direction notes**, each 3-5 sentences

Formatting: Use markdown headers and bold labels exactly as shown in the prompt structure. Captions should use line breaks as they would appear on Instagram — not dense paragraphs.

---

## Quality Checks Before Sending

Run through every item on this list before delivering to the client. If any check fails, revise before sending.

1. **Hook truncation test.** Copy each hook line into a character counter. Instagram truncates at roughly 125 characters. If the hook exceeds this and the compelling part is cut off, rewrite it shorter. The hook must deliver its punch before the "...more" fold.

2. **Caption word count.** Each full caption should be 80-125 words. Under 80 feels thin for a paid ad. Over 125 risks losing the reader on a visual-first platform. Count every caption.

3. **Headline overlay brevity.** Each headline overlay must be 5-8 words. Read it aloud — can you say it in one breath while glancing at a phone screen? If not, cut words.

4. **Hashtag relevance and count.** Verify 10-15 hashtags per variation. Remove any hashtag that the target audience would never search for or follow. Remove any hashtag with fewer than 1,000 posts (too niche to matter) or more than 10M posts (too broad to rank).

5. **UGC authenticity check.** Read Variation 1 aloud. Does it sound like a real person talking to a friend, or does it sound like a copywriter pretending to be a real person? If you can hear the marketing, rewrite it. Real people use filler words, incomplete thoughts, and specific details about their personal situation.

6. **Brand voice consistency.** Read all 5 captions in sequence. Do they all feel like they come from the same brand universe? Check against the TONE_SCALE. A tone-3 brand should feel casual and playful across all variations. A tone-8 brand should feel elevated and curated.

7. **Platform nativity.** Would each caption feel normal if you saw it on your personal Instagram feed? If any ad "feels like an ad" in a way that would make you scroll past, rewrite it to feel more organic. The best Instagram ads are the ones you engage with before you realize they are ads.

---

## Example Output

The following is a complete example using the fictional brand below. This demonstrates the exact format, depth, and quality expected from every template run.

### Example Brand Variables

```
[BRAND_NAME] = Wild Bites
[BRAND_VOICE] = Playful, warm, ingredient-obsessed, a little cheeky
[TARGET_AUDIENCE] = Women aged 25-38, health-conscious but not restrictive, follow food and wellness accounts, care about sourcing and ingredient quality, snack frequently, shop online, household income $50k-$100k. They want snacks that taste amazing AND have clean ingredients — they are tired of choosing one or the other.
[PRODUCT_SERVICE] = Wild Bites Sampler Box — a curated box of 8 snack bars (2 each of 4 flavors: Tahini Dark Chocolate, Mango Turmeric, Almond Cardamom, Blueberry Lemon). Each bar is plant-based, gluten-free, no refined sugar, made with whole food ingredients.
[PRICE_RANGE] = $29.99 for the Sampler Box (8 bars), $3.75/bar
[KEY_DIFFERENTIATOR] = Every bar is made with 7 or fewer whole food ingredients — you can pronounce and recognize every single one. No protein isolates, no sugar alcohols, no "natural flavors" hiding behind vague labels.
[COMPETITOR_NAMES] = RXBAR, Larabar, GoMacro
[WORDS_TO_USE] = "real ingredients," "whole food," "7 or fewer ingredients," "actually delicious," "snack without the guilt trip"
[WORDS_TO_AVOID] = "guilt-free" (we say "without the guilt trip" instead), "superfood," "detox," "clean eating" (too diet-culture), "cheat day"
[TONE_SCALE] = 4 (playful, warm, conversational — like a friend who happens to be really into food but is not preachy about it)
[CAMPAIGN_GOAL] = Drive traffic to the Wild Bites website (Sampler Box product page) from Instagram
[ADDITIONAL_CONTEXT] = The brand has strong UGC from customers — lots of unboxing content and "taste test" videos. The founder is a former pastry chef who left restaurant work to create a snack brand with zero compromises on taste or ingredients. Free shipping on orders over $35. No active promo code. The Sampler Box is the #1 gateway product for new customers.
```

---

### Variation 1: UGC-Style

**Hook Line (visible before "...more"):**
okay I need to talk about these bars because I have literally tried every "healthy" snack bar on the market and nothing has come close

**Full Caption (112 words):**
okay I need to talk about these bars because I have literally tried every "healthy" snack bar on the market and nothing has come close

I grabbed the sampler box from Wild Bites like two weeks ago because I kept seeing them and honestly I was skeptical. "7 ingredients" okay sure.

But the tahini dark chocolate one? I am not exaggerating when I say it tastes like dessert. Like actual dessert.

And I flipped the box over and the ingredients are just... almonds, dates, tahini, dark chocolate, sea salt, vanilla, coconut oil. That is it.

No weird fillers. No protein powder aftertaste.

I already ordered two more boxes.

Link is in their bio if you want to try them.

**Headline Overlay Text (6 words):**
Finally a bar worth eating

**CTA:**
Tap the link in bio to grab the Sampler Box — try all 4 flavors for $29.99.

**Hashtag Set (13):**
#WildBites #SnackBar #HealthySnacks #PlantBasedSnacks #CleanIngredients #WholeFood #GlutenFreeSnacks #RealFoodSnacks #SnackReview #HealthyEating #WhatIEatInADay #FoodFinds #SnackTime

**Creative Direction Note:**
Film this as a casual, phone-shot UGC video or use existing customer UGC footage. The creator should be at home — kitchen counter or couch — holding the bar, showing the ingredients on the back of the wrapper, and taking a bite with a genuine reaction. Lighting should be natural, not studio. No brand graphics overlaid — the only text on screen should be the headline overlay in a simple sans-serif font at the top or bottom third. The feel is "real person, real opinion."

---

### Variation 2: Founder Story

**Hook Line (visible before "...more"):**
I left a career as a pastry chef because I got tired of making food I would not feed to my own family.

**Full Caption (118 words):**
I left a career as a pastry chef because I got tired of making food I would not feed to my own family.

I spent years perfecting flavor in professional kitchens. But every packaged snack I grabbed on my way home had an ingredient list I could not even read.

So I made a deal with myself: create a snack bar that a pastry chef would be proud of — but with 7 or fewer whole food ingredients.

No protein isolates. No sugar alcohols. No "natural flavors" that are anything but natural.

Just real food that actually tastes like someone who loves food made it.

Because someone who loves food did make it.

The Wild Bites Sampler Box is our most popular starting point. 8 bars, 4 flavors, $29.99.

**Headline Overlay Text (7 words):**
Made by a pastry chef. Seriously.

**CTA:**
Visit wildbites.com to try the Sampler Box — all 4 flavors, free shipping over $35.

**Hashtag Set (12):**
#WildBites #FounderStory #SmallBusiness #WholeFoodSnacks #PastryChef #CleanLabel #PlantBased #MadeWithLove #FoodEntrepreneur #IngredientsMatter #RealIngredients #DTCBrand

**Creative Direction Note:**
A polished but warm photo or short video of the founder in a kitchen setting — not a restaurant kitchen, but a bright, inviting home or studio kitchen. She should be shown working with real ingredients (whole almonds, dates, dark chocolate) with the finished bars nearby. The mood is artisanal and personal. Headline overlay should appear in the lower third in a warm, slightly imperfect font (think hand-lettered style) that matches the brand's warmth. If video, the founder speaks directly to camera for 10-15 seconds telling a condensed version of the story.

---

### Variation 3: Before/After

**Hook Line (visible before "...more"):**
Three weeks ago I was spending $6 on snack bars that tasted like cardboard wrapped in a marketing budget.

**Full Caption (108 words):**
Three weeks ago I was spending $6 on snack bars that tasted like cardboard wrapped in a marketing budget.

You know the ones. Twelve-line ingredient list. Some kind of protein isolate that leaves a chalky film. "Natural flavors" doing heavy lifting for taste that the actual ingredients could not deliver.

I ate them because I thought those were my options.

Then someone handed me a Wild Bites bar and I actually looked at the back.

Seven ingredients. All of them real food. Almonds. Dates. Tahini. Dark chocolate. Sea salt. Vanilla. Coconut oil.

And it tasted like something a baker made, not a lab.

I have not gone back.

**Headline Overlay Text (7 words):**
Read the label. Taste the difference.

**CTA:**
Try the Sampler Box at wildbites.com — 8 bars, 4 flavors, $29.99. Free shipping over $35.

**Hashtag Set (14):**
#WildBites #SnackBarReview #CleanIngredients #WholeFood #GlutenFree #PlantBasedSnacks #HealthySwap #IngredientList #RealFood #BetterSnacking #NoJunk #FoodLabel #SnackSmarter #HealthyLiving

**Creative Direction Note:**
A split-screen static image or a two-slide carousel. Left side (or Slide 1): a generic snack bar with a long, dense ingredient list visible — slightly desaturated, cold lighting, sterile feel. Right side (or Slide 2): a Wild Bites bar broken in half showing real ingredients (visible chunks of almond, chocolate), warm lighting, with the short ingredient list visible on the wrapper. The headline overlay text should span across both sides or appear on Slide 2. The contrast should be immediate and visual — no explanation needed.

---

### Variation 4: "Did You Know" Educational

**Hook Line (visible before "...more"):**
The average snack bar has 15-20 ingredients. Most of them are not food.

**Full Caption (104 words):**
The average snack bar has 15-20 ingredients. Most of them are not food.

Maltodextrin. Soy lecithin. "Natural flavors." Sugar alcohols. Protein isolates. Cellulose gum.

These are not things your body recognizes as nutrition. They are fillers, binders, and lab-created flavors designed to make cheap ingredients taste acceptable.

Here is a different approach.

Wild Bites bars are made with 7 or fewer whole food ingredients. Every ingredient is something you could buy at a farmers market.

No fillers. No isolates. No hiding behind the word "natural."

Just real food, made by a former pastry chef who actually cares what goes into every bar.

The Sampler Box is $29.99. Try all 4 flavors.

**Headline Overlay Text (8 words):**
7 ingredients or fewer. Every single bar.

**CTA:**
Visit wildbites.com to see every ingredient for yourself. Sampler Box ships free over $35.

**Hashtag Set (13):**
#WildBites #IngredientsMatter #ReadTheLabel #CleanLabel #WholeFoodIngredients #FoodEducation #NutritionFacts #PlantBased #HealthySnacking #FoodTransparency #KnowYourFood #RealIngredients #GlutenFreeSnacks

**Creative Direction Note:**
A clean infographic-style static image or short animated Reel. Show a generic snack bar ingredient list (long, dense, full of chemical names) on one side and a Wild Bites ingredient list (short, simple, recognizable words) on the other. Use a neutral background — white or light cream. Typography should be clean and easy to read. The headline overlay should be positioned at the top. If animated, have the generic ingredient list scroll quickly (overwhelming) while the Wild Bites list appears slowly with each ingredient landing one at a time. The educational tone should feel empowering, not shaming.

---

### Variation 5: Limited Time / Scarcity

**Hook Line (visible before "...more"):**
Our Sampler Box is back in stock — but last time we sold out in 9 days.

**Full Caption (97 words):**
Our Sampler Box is back in stock — but last time we sold out in 9 days.

Here is what is inside: 8 bars, 4 flavors. Tahini Dark Chocolate, Mango Turmeric, Almond Cardamom, Blueberry Lemon.

Every bar made with 7 or fewer real, whole food ingredients. No fillers. No weird stuff.

This is our most popular box for first-time customers — it is the easiest way to find your favorite flavor before you commit to a full case.

$29.99 with free shipping over $35.

We are not running a countdown timer on you. But we are telling you: these move fast.

Grab yours before they are gone again.

**Headline Overlay Text (5 words):**
Back in stock. For now.

**CTA:**
Head to wildbites.com now to grab the Sampler Box while it is available.

**Hashtag Set (11):**
#WildBites #BackInStock #SamplerBox #SnackBar #LimitedStock #PlantBasedSnacks #WholeFood #CleanIngredients #HealthySnacks #TryTheFlavors #NewSnack

**Creative Direction Note:**
A product-focused flat lay or styled shot of the Sampler Box contents — all 8 bars arranged neatly with the box visible, on a warm wooden surface or marble counter. One bar should be unwrapped and broken in half to show texture. Lighting is warm and inviting. The headline overlay "Back in stock. For now." should appear at the top in bold, slightly urgent typography — sans-serif, medium weight. No countdown timers or flashing graphics. The urgency comes from the copy, not the design. The visual should feel appetizing and premium, not promotional.

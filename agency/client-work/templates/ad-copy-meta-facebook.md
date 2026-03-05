# Facebook Ad Copy Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | 5 complete Facebook ad copy variations, each with 3 hook options, short + long primary text, headline, description, CTA recommendation, and creative pairing notes |
| **Turnaround** | Single prompt execution — review and polish in 15-20 minutes |
| **Quality bar** | Ready to paste into Ads Manager after brand review; no placeholder text, no generic filler, every line crafted to stop the scroll |
| **Best for** | DTC brands running Meta acquisition campaigns, retargeting, product launches, seasonal pushes, and evergreen prospecting |

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
- **BRAND_VOICE**: 2-4 adjective descriptors (e.g., "bold, witty, science-backed, no-nonsense").
- **TARGET_AUDIENCE**: Demographics + psychographics. Be specific — "women 28-42 who do CrossFit 4x/week and care about clean ingredients" is far better than "health-conscious adults."
- **PRODUCT_SERVICE**: The specific product or service being advertised in this campaign. Include variant, size, or bundle if relevant.
- **PRICE_RANGE**: Exact price or range (e.g., "$49" or "$35-$65"). Include any subscription pricing if applicable.
- **KEY_DIFFERENTIATOR**: The single strongest reason someone should choose this over any competitor. One sentence.
- **COMPETITOR_NAMES**: 2-4 competitors the audience likely knows. Used for positioning, never mentioned in copy.
- **WORDS_TO_USE**: Brand-approved vocabulary, product-specific terms, or phrases that should appear (e.g., "plant-powered," "backed by science," "clean label").
- **WORDS_TO_AVOID**: Banned words, competitor names, overly clinical language, or anything off-brand (e.g., "cheap," "hack," "miracle").
- **TONE_SCALE**: A number from 1-10. 1 is extremely casual, meme-forward, slang-heavy. 10 is luxury editorial, refined, minimal. Most DTC brands land between 3-7.
- **CAMPAIGN_GOAL**: The specific business objective (e.g., "drive first-time purchases of the Recovery Bundle," "grow email list via lead magnet," "retarget cart abandoners").
- **ADDITIONAL_CONTEXT**: Anything else — seasonal tie-ins, promo codes, landing page URL, specific claims that are pre-approved, compliance notes, or creative assets already produced.

---

## The Prompt

Paste the following prompt into Claude along with the filled-in brand variables above.

---

```
You are a senior direct-response copywriter at a performance-focused DTC ad agency. You have written thousands of Meta ads that have profitably scaled past $100k/month in spend. You understand the Facebook algorithm, the auction dynamics, and — most importantly — you understand how real people scroll, stop, read, and click.

Your job right now: write 5 complete Facebook ad copy variations for the brand and campaign described below.

## BRAND BRIEF

[Paste filled-in brand variables here]

## INSTRUCTIONS

### General rules for every ad you write:

1. **Hook-first thinking.** The first line of every ad is the most important piece of copy you will write. It must stop the scroll. It must create an open loop, provoke curiosity, call out the audience by identity, or state a bold claim. Never start with the brand name. Never start with a generic greeting. Never start with "Introducing..." unless it is genuinely a new product launch.

2. **Write like a friend recommending, not a brand advertising.** The best-performing Facebook ads read like a text message from someone who genuinely loves the product. Avoid corporate language. Avoid marketing jargon. Use "you" and "your" constantly. Write in second person.

3. **Front-load the benefit or curiosity.** The reader decides in under 2 seconds whether to keep reading. Every sentence must earn the next sentence. Cut every word that does not move the reader closer to clicking.

4. **Use specific numbers.** "Reduces soreness by 47%" beats "reduces soreness." "Over 11,000 five-star reviews" beats "thousands of happy customers." If the brief provides numbers, use them. If it does not, use plausible specifics that the brand can verify before publishing.

5. **Emoji usage: sparingly.** Use 1-2 emoji per ad maximum. Use them as visual punctuation — a checkmark to start a benefit list, a pointing finger before a CTA, a fire emoji to signal something noteworthy. Never string 3+ emoji together. Never use emoji as a substitute for good writing.

6. **Match the brand voice and tone scale precisely.** A tone-scale-3 brand should sound like a friend at a bar. A tone-scale-8 brand should sound like a premium magazine editorial. Never drift from the brief.

7. **Creative/image pairing notes.** After each ad variation, include a short note (2-3 sentences) describing what type of visual creative would pair best with that specific copy — static image, carousel, video, UGC clip, etc. Be specific about what the image should show.

8. **Campaign objective alignment.** Each ad should end with a note on which Meta campaign objective it best serves (Conversions, Traffic, Engagement, Lead Generation, etc.) and any targeting notes.

9. **No cliches.** Do not use: "game-changer," "revolutionary," "unlock your potential," "take it to the next level," "are you tired of...?" unless the brief explicitly includes these phrases in WORDS_TO_USE.

10. **Compliance awareness.** Do not make medical claims, income claims, or before/after promises that would violate Meta advertising policies. If the product is in a sensitive category (health, finance, etc.), keep claims within platform guidelines.

### The 5 variations you must write:

**Variation 1 — Pain Point / Problem-Aware**
Lead with the problem the audience faces. Agitate it. Make the reader feel seen. Then position the product as the solution. This ad targets people who know they have a problem but have not yet found the right solution.

**Variation 2 — Social Proof / Testimonial Lead**
Open with what sounds like a real customer quote or reference a volume of social proof (number of reviews, customers, units sold). Build credibility before introducing the product. This ad targets people who are solution-aware but skeptical.

**Variation 3 — Product Feature / Ingredient Spotlight**
Lead with the most compelling product feature, ingredient, technology, or mechanism of action. Educate the reader on WHY this product works differently. This ad targets people who research before buying.

**Variation 4 — Lifestyle / Aspiration**
Paint a picture of the life the reader wants. Use sensory language. Make the reader see themselves using the product and feeling the result. This ad targets people who buy based on identity and emotion.

**Variation 5 — Offer / Promotion Driven**
Lead with the offer — discount, bundle deal, free shipping, limited-time pricing, or bonus gift. Create urgency without being sleazy. This ad targets price-sensitive buyers and fence-sitters.

### For EACH variation, provide the following in this exact structure:

```
### Variation [Number]: [Variation Name]

**Hook Options (choose one for testing — first line of the ad):**
Hook A: [First hook option]
Hook B: [Second hook option]
Hook C: [Third hook option]

**Primary Text — Short Version (40-80 words):**
[Short-form ad copy. This is the version that shows fully without "See more." Tight, punchy, complete.]

**Primary Text — Long Version (100-150 words):**
[Long-form ad copy. This version uses the "See more" expand. Opens with the hook, builds the story, stacks benefits, closes with CTA. Uses line breaks for readability.]

**Headline (40 characters max):**
[Headline that appears below the image/video]

**Description (30 characters max):**
[Description line that appears below the headline]

**CTA Button Recommendation:**
[Shop Now / Learn More / Get Offer / Sign Up / etc.]

**Campaign Objective Note:**
[Which Meta objective this variation best serves + any targeting/placement notes]

**Creative Pairing Note:**
[2-3 sentences describing the ideal visual asset to pair with this copy]
```

Write all 5 variations now. Make every word count. Write copy that makes people stop scrolling and start buying.
```

---

## Output Format

The final output must contain exactly:

- **5 ad variations**, numbered and labeled by angle
- **3 hook options** per variation (15 hooks total)
- **2 primary text versions per variation** — short (40-80 words) and long (100-150 words) — totaling 10 blocks of primary text
- **5 headlines**, each 40 characters or fewer
- **5 descriptions**, each 30 characters or fewer
- **5 CTA button recommendations**
- **5 campaign objective notes**
- **5 creative pairing notes**

Character counts are strict. Headlines over 40 characters or descriptions over 30 characters must be revised before delivery to the client.

Formatting: Use markdown headers and bold labels exactly as shown in the prompt structure. This ensures easy scanning and copy-paste into Ads Manager or a creative brief document.

---

## Quality Checks Before Sending

Run through every item on this list before delivering to the client. If any check fails, revise before sending.

1. **Character count compliance.** Manually verify every headline is 40 characters or fewer and every description is 30 characters or fewer. Count spaces as characters. This is the most common error — do not skip this check.

2. **Hook differentiation.** Read all 15 hooks in sequence. No two hooks should use the same opening structure or opening word. If you see patterns (e.g., three hooks starting with "You"), rewrite until each feels distinct.

3. **Brand voice consistency.** Read every ad aloud. Does it sound like the brand? Compare against the TONE_SCALE number. A tone-3 brand should never sound like a press release. A tone-8 brand should never sound like a Reddit comment.

4. **Banned words scan.** Search the entire output for every word listed in WORDS_TO_AVOID. Also search for common cliches listed in the prompt instructions (game-changer, revolutionary, etc.) unless they appear in WORDS_TO_USE.

5. **CTA clarity.** Every ad must make it unmistakably clear what the reader should do next. The CTA should align with the campaign goal — if the goal is purchases, the CTA should drive to the product page, not to a blog post.

6. **Benefit-to-feature ratio.** Each ad should lead with benefits (what the customer gets) and support with features (what the product has). If any ad reads like a spec sheet, rewrite the opening to lead with the outcome.

7. **Meta policy compliance.** Scan for absolute medical claims ("cures," "treats," "guarantees"), before/after implications, or language that calls out personal attributes ("Are you overweight?"). Revise anything that could trigger a Meta ad rejection.

---

## Example Output

The following is a complete example using the fictional brand below. This demonstrates the exact format, depth, and quality expected from every template run.

### Example Brand Variables

```
[BRAND_NAME] = Basecamp Nutrition
[BRAND_VOICE] = Bold, science-backed, no-BS, supportive
[TARGET_AUDIENCE] = Men and women aged 25-40 who do CrossFit, functional fitness, or hybrid training 4-6x/week. They care about what goes into their body, read labels, and are skeptical of overhyped supplements. Household income $60k-$120k.
[PRODUCT_SERVICE] = Basecamp Recovery — a post-workout recovery supplement (powder, mixed with water) featuring tart cherry extract, magnesium glycinate, L-glutamine, and electrolytes. 30 servings per tub, berry flavor.
[PRICE_RANGE] = $44.99 / one-time, $37.99 / subscribe & save
[KEY_DIFFERENTIATOR] = Third-party tested, fully transparent label (no proprietary blends), formulated specifically for high-intensity functional fitness athletes — not bodybuilders, not casual gym-goers.
[COMPETITOR_NAMES] = Momentous, LMNT, Thorne
[WORDS_TO_USE] = "clean recovery," "third-party tested," "transparent label," "built for the box," "train harder tomorrow"
[WORDS_TO_AVOID] = "miracle," "hack," "crush it," "gains," "bro"
[TONE_SCALE] = 4 (casual, confident, direct — like a knowledgeable training partner, not a lab coat)
[CAMPAIGN_GOAL] = Drive first-time purchases of Basecamp Recovery (single tub) through cold prospecting to CrossFit/functional fitness audiences
[ADDITIONAL_CONTEXT] = Landing page includes a video of the founder (former collegiate athlete and sports dietitian) explaining the formula. Free shipping on orders over $50. No promo code active right now. Can reference the fact that the product was developed with input from 200+ CrossFit athletes during a 6-month beta.
```

---

### Variation 1: Pain Point / Problem-Aware

**Hook Options (choose one for testing — first line of the ad):**
Hook A: You just PR'd your clean and jerk — so why does it feel like your body is falling apart by Thursday?
Hook B: That "I can't sit down on the toilet" soreness after leg day is not a badge of honor.
Hook C: If your recovery strategy is "just sleep it off," your performance is leaving serious progress on the table.

**Primary Text — Short Version (67 words):**
You just PR'd your clean and jerk — so why does it feel like your body is falling apart by Thursday?

Here is the truth: soreness is not a sign you trained hard enough. It is a sign your recovery is not matching your output.

Basecamp Recovery was formulated with CrossFit athletes — not bodybuilders — to cut soreness, replenish electrolytes, and get you back under the barbell faster.

Third-party tested. Transparent label. No proprietary blends.

**Primary Text — Long Version (142 words):**
You just PR'd your clean and jerk — so why does it feel like your body is falling apart by Thursday?

You are not overtraining. You are under-recovering.

Most recovery supplements are built for bodybuilders doing bicep curls and calf raises. That is not what you do. You do heavy cleans, muscle-ups, 20-minute AMRAPs that leave you in a puddle.

Your recovery should match your intensity.

Basecamp Recovery was developed over 6 months with input from 200+ CrossFit athletes. Every ingredient is dosed at clinical levels and listed right on the label — no proprietary blends, no filler.

Tart cherry extract to fight inflammation. Magnesium glycinate to support muscle relaxation. L-glutamine to accelerate tissue repair. Full electrolyte panel to replace what you sweat out.

One scoop. Mixed with water. Done.

Train harder tomorrow. That is the whole point.

**Headline (38 chars):**
Recovery Built for the Box

**Description (28 chars):**
Third-Party Tested Formula

**CTA Button Recommendation:**
Shop Now

**Campaign Objective Note:**
Best served under a Conversions (Purchase) objective targeting interest-based audiences: CrossFit, Functional Fitness, Olympic Weightlifting, plus lookalikes of existing supplement buyers. Run in Feed and Reels placements.

**Creative Pairing Note:**
Pair with a short (8-12 second) video clip of someone finishing a grueling WOD — hands on knees, breathing hard — then cutting to them calmly scooping Basecamp Recovery into a shaker. The contrast between intensity and simple recovery routine sells the ease. Raw gym lighting, not overly produced.

---

### Variation 2: Social Proof / Testimonial Lead

**Hook Options (choose one for testing — first line of the ad):**
Hook A: "I stopped dreading the day after heavy squat days." — that is what 200+ beta testers told us before we even launched.
Hook B: We gave our recovery formula to 200 CrossFit athletes for 6 months and asked them to be brutally honest. Here is what happened.
Hook C: 4.8 stars across 1,100+ reviews — and most of them mention the same thing.

**Primary Text — Short Version (72 words):**
"I stopped dreading the day after heavy squat days."

That is what we kept hearing — over and over — from the 200+ CrossFit athletes who tested Basecamp Recovery during our 6-month beta.

Less soreness. Better sleep. More consistency in the gym because they were not constantly running on fumes.

We did not rush this to market. We let real athletes decide if it was worth making.

They decided for us.

**Primary Text — Long Version (138 words):**
"I stopped dreading the day after heavy squat days."

That is a direct quote from one of the 200+ CrossFit athletes who tested Basecamp Recovery before we ever put it on a shelf.

Here is what we did: we spent 6 months giving our formula to real functional fitness athletes — people who train hard 5 days a week and do not have time for recovery products that do not work.

We asked them to be brutally honest. And they were.

The feedback was consistent:
- Less next-day soreness
- Faster bounce-back between sessions
- Better sleep quality on training days

So we kept the formula exactly as they tested it. Tart cherry, magnesium glycinate, L-glutamine, full electrolyte panel. Every ingredient on the label, every dose visible.

No proprietary blends. No guessing.

Try it yourself. $44.99 or $37.99 on subscribe and save.

**Headline (35 chars):**
Tested by 200+ Athletes First

**Description (25 chars):**
Clean Recovery Formula

**CTA Button Recommendation:**
Shop Now

**Campaign Objective Note:**
Ideal for Conversions (Purchase) objective. Works well in a social proof ad set targeting warm audiences — people who have visited the site, engaged with social content, or are in lookalike audiences based on past purchasers. Feed and Stories placements.

**Creative Pairing Note:**
Use a carousel format. Slide 1: a bold quote from a beta tester overlaid on a gritty gym photo. Slide 2: the product tub with "200+ Athletes Tested" callout. Slide 3: a breakdown of key ingredients. Slide 4: CTA with price. Alternatively, a UGC-style video of a real customer talking about their experience.

---

### Variation 3: Product Feature / Ingredient Spotlight

**Hook Options (choose one for testing — first line of the ad):**
Hook A: Tart cherry extract is the most underrated recovery ingredient in sports nutrition — and most supplement brands underdose it by half.
Hook B: There are 4 ingredients in Basecamp Recovery. We can tell you exactly how much of each one is in every scoop — because it is all right on the label.
Hook C: Your post-workout supplement probably has a "proprietary blend." That is a fancy way of saying they do not want you to know how little of each ingredient is actually inside.

**Primary Text — Short Version (78 words):**
Tart cherry extract is the most underrated recovery ingredient in sports nutrition — and most supplement brands underdose it by half.

Basecamp Recovery uses a clinical dose of tart cherry in every serving — alongside magnesium glycinate for muscle relaxation, L-glutamine for tissue repair, and a full electrolyte panel built for athletes who actually sweat.

Every ingredient. Every dose. Right on the label.

No proprietary blends. Third-party tested.

This is what a clean recovery formula looks like.

**Primary Text — Long Version (147 words):**
Tart cherry extract is the most underrated recovery ingredient in sports nutrition — and most supplement brands underdose it by half.

Here is why that matters to you:

Tart cherry has been shown in peer-reviewed research to reduce exercise-induced muscle soreness and support faster recovery between training sessions. But the dose matters. Sprinkle in a tiny amount and slap it on the label? That is what most brands do.

Basecamp Recovery uses a full clinical dose. And we put it right on the label so you can verify it yourself.

Same with every other ingredient:
- Magnesium glycinate — supports muscle relaxation and sleep quality
- L-glutamine — accelerates tissue repair after high-intensity work
- Full electrolyte panel — replaces sodium, potassium, and magnesium lost during training

No proprietary blends. No fillers. No artificial sweeteners.

Third-party tested so you know exactly what you are putting in your body.

$44.99 per tub. $37.99 on subscribe and save.

**Headline (36 chars):**
Every Ingredient. Every Dose.

**Description (26 chars):**
Transparent Label Always

**CTA Button Recommendation:**
Learn More

**Campaign Objective Note:**
Best for Conversions (Purchase) or Traffic objective. Target audiences interested in supplements, nutrition research, ingredient transparency, and "clean label" products. This variation performs well in Feed placements where users have time to read. Consider pairing with a longer landing page that dives into ingredient science.

**Creative Pairing Note:**
A clean static image or short animation showing each of the four ingredients with their exact doses listed, set against a dark or matte background. Think "nutrition label as hero content." The visual should feel informative and premium — like something from a sports science journal, not a GNC aisle. Alternatively, a short founder video explaining one key ingredient.

---

### Variation 4: Lifestyle / Aspiration

**Hook Options (choose one for testing — first line of the ad):**
Hook A: Imagine walking into the box on Monday morning and your legs actually feel ready to go.
Hook B: The best feeling in CrossFit is not the PR. It is showing up the next day and feeling like you can do it all again.
Hook C: Saturday morning. Competition day. You have trained all week and your body feels like it has been recovering — not just surviving.

**Primary Text — Short Version (74 words):**
Imagine walking into the box on Monday morning and your legs actually feel ready to go.

Not "manageable." Not "I will push through it." Actually ready.

That is what clean recovery feels like. When your body gets the right ingredients at the right doses after every session, you stop living in a constant state of soreness and start actually building on yesterday's work.

Basecamp Recovery. One scoop after training. Train harder tomorrow.

**Primary Text — Long Version (133 words):**
Imagine walking into the box on Monday morning and your legs actually feel ready to go.

Not the "okay I guess I can survive today" kind of ready. The "load up the barbell, I feel great" kind.

That is what this is about. Not supplements. Not another powder on your shelf. This is about what your training looks like when your recovery finally matches your effort.

You have done the hard part. You showed up. You put in the work — five, six days a week. You earned every rep.

Basecamp Recovery is the other half of that equation. Tart cherry, magnesium glycinate, L-glutamine, and a full electrolyte panel. One scoop, mixed with water, right after your workout.

You train like an athlete. Recover like one too.

$44.99 per tub. Free shipping over $50.

**Headline (33 chars):**
Train Harder Tomorrow

**Description (29 chars):**
Clean Recovery for Athletes

**CTA Button Recommendation:**
Shop Now

**Campaign Objective Note:**
Works under Conversions (Purchase) or Brand Awareness objectives. This is a strong top-of-funnel ad for cold audiences who identify as CrossFit or functional fitness athletes. Runs well in Reels and Stories where aspirational content performs. Also effective as a retargeting ad for people who watched a previous video ad but did not click.

**Creative Pairing Note:**
A lifestyle video: early morning, athlete walks into a gym (natural light, slightly cinematic but not overproduced), warms up, hits a workout, finishes strong, then mixes Basecamp Recovery in a shaker. The mood is calm confidence, not hype. Background music should be lo-fi or ambient — this is not a screaming motivation video. The feeling is "this person has it figured out."

---

### Variation 5: Offer / Promotion Driven

**Hook Options (choose one for testing — first line of the ad):**
Hook A: First tub of Basecamp Recovery: $37.99 when you subscribe. Cancel anytime, no questions asked.
Hook B: Free shipping on your first order of Basecamp Recovery — here is why 200+ athletes already made the switch.
Hook C: $37.99/month for the recovery formula that was built by CrossFit athletes, tested for 6 months, and third-party verified. That is less than your daily coffee.

**Primary Text — Short Version (69 words):**
First tub of Basecamp Recovery: $37.99 when you subscribe. Cancel anytime.

That is less than $1.27 per serving for a clinical-dose recovery formula with tart cherry extract, magnesium glycinate, L-glutamine, and a full electrolyte panel.

Every ingredient on the label. Third-party tested. No proprietary blends.

Built specifically for CrossFit and functional fitness athletes — not bodybuilders, not weekend joggers.

Free shipping on orders over $50.

**Primary Text — Long Version (141 words):**
$37.99/month for the recovery formula that was built by CrossFit athletes, tested for 6 months, and third-party verified.

Let us break that down: that is $1.27 per serving. Less than your post-workout coffee.

Here is what you get in every scoop:
- Tart cherry extract — clinically dosed to support recovery
- Magnesium glycinate — for muscle relaxation and better sleep
- L-glutamine — for tissue repair after high-intensity sessions
- Full electrolyte panel — replaces what you sweat out

Every ingredient listed on the label at its exact dose. No proprietary blends. No fillers. No artificial sweeteners.

Subscribe and save at $37.99/month — cancel anytime, no hoops, no "call to cancel" nonsense.

Or grab a single tub for $44.99.

Free shipping on orders over $50.

Your training is already dialed in. Make your recovery match it.

**Headline (37 chars):**
$37.99/Mo — Subscribe and Save

**Description (24 chars):**
Cancel Anytime. Easy.

**CTA Button Recommendation:**
Get Offer

**Campaign Objective Note:**
Best for Conversions (Purchase) objective with a focus on subscribe-and-save conversion events. Target warm audiences: website visitors (30-60 day), video viewers (50%+), and add-to-cart abandoners. This is a strong bottom-of-funnel ad. Run in Feed for maximum text visibility.

**Creative Pairing Note:**
A clean product shot — the Basecamp Recovery tub on a gym bench or next to a barbell — with a bold price callout overlaid: "$37.99/mo." Keep the visual simple so the price is the hero. Alternatively, a split-screen static showing the product on one side and a bullet list of ingredients on the other, with the subscribe price anchored at the bottom. No lifestyle imagery needed here — this ad is about the deal.

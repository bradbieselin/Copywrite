# TikTok Ad Copy / Script Template

## Quick Reference

| Field | Detail |
|---|---|
| **What it produces** | 3 complete TikTok ad concepts, each with a hook, full script with visual direction, timestamped on-screen text overlays, CTA, sound/music direction, and format recommendation |
| **Turnaround** | Single prompt execution — review and timing check in 20-25 minutes |
| **Quality bar** | Ready to hand to a creator or production team for filming; scripts read like real TikTok content, not like ads transplanted from another platform |
| **Best for** | DTC brands running TikTok Ads (Spark Ads, In-Feed Ads, or TopView) to drive awareness, traffic, or purchases among Gen Z and younger Millennial audiences |

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

### Additional TikTok-specific variables

```
[CREATOR_TYPE] = (Who is on camera? Options: brand founder, paid creator/influencer, employee, customer, or "no face" for product-only/text-overlay style)
[CREATOR_DEMOGRAPHICS] = (Age range, gender, and vibe of the on-camera person — e.g., "woman, 26-30, athletic, approachable")
[PRODUCT_SHOW_REQUIREMENTS] = (Must the product be shown? At what point? Any required visual of packaging, label, or usage?)
[TIKTOK_TRENDS_TO_REFERENCE] = (Any current TikTok trends, sounds, or formats the brand wants to lean into — or write "Use evergreen formats" if no specific trend)
[ORGANIC_VS_PRODUCED] = (Should these feel fully organic/UGC, lightly produced, or clearly brand-produced?)
[COMPLIANCE_NOTES] = (Any claims that cannot be made, required disclaimers, or TikTok-specific policy considerations)
```

### Variable definitions (for the person filling this in)

- **BRAND_NAME**: Exact brand name. On TikTok, it often appears in text overlays rather than being spoken.
- **BRAND_VOICE**: 2-4 adjective descriptors. TikTok voice tends to be more casual than other platforms, but it must still feel authentic to the brand. A luxury brand can be on TikTok and still feel premium — it just needs to respect the platform's native language.
- **TARGET_AUDIENCE**: Be specific about the TikTok audience segment — age, interests, content consumption habits, and what kind of TikTok content they engage with. "22-35 who watch fitness content and product review videos" is much more useful than "young adults."
- **PRODUCT_SERVICE**: The specific product being promoted.
- **PRICE_RANGE**: Price matters on TikTok — affordable products can lean into impulse purchase energy, while premium products need to justify the price within the script.
- **KEY_DIFFERENTIATOR**: The single strongest reason to choose this product. On TikTok, this often becomes the "reveal" or the core argument of the script.
- **COMPETITOR_NAMES**: Competitors the audience knows. Can be referenced indirectly on TikTok (e.g., "I have tried every recovery supplement out there and nothing worked until...") but never named directly.
- **WORDS_TO_USE**: Brand vocabulary. These should be woven into spoken scripts naturally — if a phrase sounds awkward spoken aloud, adjust it.
- **WORDS_TO_AVOID**: Banned terms. Especially important because TikTok scripts are spoken — a word that looks fine in text might sound wrong spoken aloud.
- **TONE_SCALE**: TikTok skews casual. Most brands on TikTok operate at a tone of 2-5 regardless of how they present on other platforms. A brand that is a tone-8 on Instagram might be a tone-5 on TikTok. Adjust accordingly.
- **CAMPAIGN_GOAL**: What action should viewers take? TikTok ad goals include awareness, video views, traffic, conversions, and app installs.
- **CREATOR_TYPE**: Who will be on camera? This fundamentally shapes the script. A founder telling their story sounds different from a paid creator doing a review, which sounds different from a faceless product demo.
- **CREATOR_DEMOGRAPHICS**: Describes the on-camera person. This helps the script writer match language, energy, and references to the person delivering the content.
- **PRODUCT_SHOW_REQUIREMENTS**: Some brands require the product to appear within the first 5 seconds. Others want it revealed later as a "punchline." Clarify expectations.
- **TIKTOK_TRENDS_TO_REFERENCE**: Trends have a short shelf life on TikTok. If referencing a specific trend, confirm it is still active. Evergreen formats (reviews, storytime, POV) are always safe.
- **ORGANIC_VS_PRODUCED**: The spectrum ranges from "looks like someone filmed this on their phone in their bedroom" (most organic) to "clearly a professional shoot with lighting and multiple cameras" (most produced). Most effective TikTok ads sit closer to the organic end.
- **COMPLIANCE_NOTES**: TikTok has specific policies around health claims, before/after imagery, and testimonials. Note anything the brand cannot say.

---

## The Prompt

Paste the following prompt into Claude along with the filled-in brand variables above.

---

```
You are a TikTok creative strategist and scriptwriter who specializes in writing ads that perform on TikTok. You understand the platform deeply — the pacing, the language, the formats, the audience behavior. You know that TikTok users scroll past anything that feels like an ad within the first 0.5 seconds. You know that the best TikTok ads are indistinguishable from organic content until the CTA.

Your superpower: you write scripts that sound like real people talking. Not copywriters. Not marketers. Real people who discovered something and are excited to share it.

Your job: write 3 complete TikTok ad concepts for the brand and campaign described below.

## BRAND BRIEF

[Paste filled-in brand variables here]

## TIKTOK-SPECIFIC BRIEF

[Paste filled-in TikTok-specific variables here]

## INSTRUCTIONS

### The golden rules of TikTok ad scripting:

1. **The first 3 seconds decide everything.** TikTok users make a stay-or-scroll decision faster than any other platform. The hook must be visually and verbally arresting. It must feel like organic content — not like an ad. The best hooks create an open loop that the viewer NEEDS to see closed. Techniques that work: a bold claim, a surprising visual, a direct address ("Okay so this is going to sound weird but..."), a mid-action opening (starting the video in the middle of something happening), or a pattern interrupt (something visually unexpected).

2. **Write how people actually talk on TikTok.** This is not Instagram caption writing. This is not Facebook ad copy. TikTok scripts should read like spoken language from a real person. Use contractions. Use filler phrases like "okay so," "honestly," "like," "literally," "I am not even kidding," and "wait for it." Start sentences with "And" and "But." Use incomplete sentences. Trail off. Interrupt yourself. This is how people talk on TikTok, and anything that sounds more polished will be identified as an ad and scrolled past immediately.

3. **Front-load the hook relentlessly.** Do not save the best part for the middle or end. The viewer is not there yet. The first thing they see and hear must be the most interesting thing in the entire video. Every second after the hook should maintain or escalate the energy.

4. **Include pattern interrupts.** A pattern interrupt is a moment in the video where something changes — the camera angle shifts, a text overlay appears, the speaker pauses dramatically, a sound effect plays, or the setting changes. These re-engage viewers who might start to drift. Include at least one pattern interrupt per concept, ideally every 5-7 seconds.

5. **Keep scripts under 60 seconds.** The target range is 15-30 seconds for most TikTok ads. You can go up to 45 seconds if the concept demands it, but every second must earn its place. If the script can be tightened, tighten it. If a beat can be cut without losing meaning, cut it.

6. **Write for sound on AND sound off.** Most TikTok users watch with sound on (unlike Facebook), but text overlays still matter enormously. They reinforce the spoken message, highlight key claims, and serve as visual pattern interrupts. Every concept must include timestamped text overlays.

7. **The CTA must feel natural.** A hard sell at the end of a TikTok video ("Click the link below and use code SAVE20 for 20% off your first order") kills the organic feel of even the best script. The CTA should feel like a natural conclusion to the conversation — "I linked it in my bio if you want to try it" or "You can check it out yourself, I will put the link" or even just a final text overlay with the brand name and "link in bio." The viewer should feel like they are choosing to look it up, not being sold to.

8. **Respect the platform's aesthetic.** TikTok content is vertical (9:16). It is usually shot on a phone or made to look like it was shot on a phone. Even produced content should feel accessible. Overproduced, glossy ads stick out and get scrolled past. Match the energy of the For You Page.

9. **Sound and music matter.** TikTok is a sound-first platform. Every concept should include a note on what the audio landscape sounds like — trending sound, original voiceover, background music mood, or ASMR-style product sounds. If a trending sound is specified in the brief, the script should be timed to it.

10. **Notes on organic vs. produced feel.** After each concept, include a note on where this script falls on the organic-to-produced spectrum and why. Indicate whether it should feel like a Spark Ad (boosted organic post) or a traditional In-Feed Ad.

### The 3 concepts you must write:

**Concept 1 — "Storytime" Personal Narrative**
The creator tells a personal story about discovering the product. The format is confessional, first-person, and emotional. It follows the classic TikTok storytime structure: setup ("Okay so this thing happened..."), buildup (the problem or journey), reveal (discovering the product), and result (how it changed things). The audience should feel like they are hearing a friend tell them about something they found. The product introduction should feel like a natural part of the story, not a scripted transition.

**Concept 2 — "I Tested/Tried" Review Style**
The creator positions themselves as a skeptical tester. They tried the product so the viewer does not have to. The format is: setup ("I have been seeing this everywhere so I finally tried it"), first impression, usage demonstration, results, and verdict. This format works because it aligns with how TikTok users actually discover and evaluate products. The skepticism at the beginning must feel real, and the conversion to being impressed must feel earned, not scripted.

**Concept 3 — "POV" or Trending Format**
Use a POV structure, a trending format, or a visually creative concept that leverages TikTok-native storytelling. This could be: a "POV: you finally found a [product category] that actually works" video, a "things I wish I knew sooner" format, a "put a finger down" challenge adaptation, a "day in my life" segment, or any format that feels native to the platform. The product should be woven into the format naturally — not forced.

### For EACH concept, provide the following in this exact structure:

```
### Concept [Number]: [Concept Name]

**Format:** [Storytime / Review / POV / Trending Format — specify which]

**Total Duration:** [15-30 seconds — specify exact target length]

**Hook (First 3 Seconds):**
Visual: [What the viewer sees on screen]
Audio: [What the viewer hears — voiceover, sound, music]
On-screen text: [Any text overlay visible in the first 3 seconds]

**Full Script (with visual direction):**
[Timestamp] — [Visual direction] — [Spoken script/voiceover]
[Timestamp] — [Visual direction] — [Spoken script/voiceover]
[Continue for each beat of the script...]

**On-Screen Text Overlays (timestamped):**
[Timestamp]: "[Text overlay]"
[Timestamp]: "[Text overlay]"
[Continue for each text overlay...]

**CTA:**
[How the video ends — what the viewer should do next, delivered naturally]

**Sound/Music Direction:**
[Specific sound, trending audio, music mood, voiceover style, or ASMR direction. Be specific about energy level and genre.]

**Format Recommendation:**
[Spark Ad, In-Feed Ad, TopView, or organic post to boost. Explain why this format recommendation fits this concept.]

**Organic vs. Produced Notes:**
[Where this concept sits on the spectrum and production guidance — lighting, camera, editing style, number of cuts, etc.]
```

Write all 3 concepts now. Read every script aloud before finalizing it. If any line sounds like a copywriter wrote it instead of a real person saying it, rewrite it until it sounds human.
```

---

## Output Format

The final output must contain exactly:

- **3 ad concepts**, each with a distinct format and angle
- **3 hooks** (first 3 seconds), each with visual, audio, and text overlay direction
- **3 full scripts** with timestamped visual direction and spoken dialogue
- **3 sets of timestamped on-screen text overlays**
- **3 CTAs**, each delivered naturally within the script
- **3 sound/music direction notes**
- **3 format recommendations** with reasoning
- **3 organic vs. produced notes** with production guidance

Total scripts should target 15-30 seconds each. Every script must be readable aloud within its target duration.

---

## Quality Checks Before Sending

Run through every item on this list before delivering to the client. If any check fails, revise before sending.

1. **Read-aloud timing test.** Read every script aloud at a natural speaking pace (not rushed, not slow — the way someone actually talks on TikTok). Time yourself. If a 25-second script takes 40 seconds to read aloud, it is too long. If a 25-second script takes 15 seconds, the pacing notes need to account for pauses, visual beats, and breathing room. Every script must be deliverable within its stated duration.

2. **Hook strength test.** Cover the script below the first 3 seconds. Read only the hook. Would you keep watching? Would a 24-year-old scrolling through TikTok at 11pm keep watching? If the hook does not create an irresistible open loop, rewrite it.

3. **Authenticity check.** Read the script and ask: "Does this sound like a person talking, or a brand writing?" Specific red flags: perfectly structured sentences, marketing jargon, smooth transitions that no real person would make, and CTA language that sounds like a press release. Real people pause. Real people say "um." Real people start sentences over. The script should feel like it was transcribed from a natural conversation, not written for a teleprompter.

4. **Pattern interrupt presence.** Each concept should have at least one pattern interrupt — a moment where the visual, audio, or pacing changes to re-engage the viewer. If a script is a single continuous shot with no interrupts, add at least one camera angle change, text overlay pop, or dramatic pause.

5. **Product integration naturalness.** The product should enter the script naturally, not abruptly. If you can pinpoint the exact moment where the video "becomes an ad," rewrite that transition. The product should feel like it is part of the story, not an interruption to it.

6. **CTA naturalness.** The CTA should not feel like a different person wrote it. If the rest of the script is casual and the CTA suddenly becomes "Visit our website today to claim your exclusive offer," the tonal shift will kill the ad's performance. The CTA should match the energy and language of the rest of the script.

7. **Platform nativity.** Would this video feel normal on someone's For You Page? If you saw this between a cooking video and a cat video, would it stop your scroll? If it feels like it belongs on YouTube or Instagram instead of TikTok, rethink the format, pacing, and visual style.

---

## Example Output

The following is a complete example using the fictional brand below.

### Example Brand Variables

```
[BRAND_NAME] = Basecamp Nutrition
[BRAND_VOICE] = Bold, science-backed, no-BS, supportive
[TARGET_AUDIENCE] = Men and women aged 22-35 who are active on TikTok and into functional fitness, CrossFit, hybrid training, or general strength training. They watch fitness content, product reviews, and "what I eat in a day" videos. They are skeptical of supplement brands that overpromise, and they appreciate transparency and real results over hype.
[PRODUCT_SERVICE] = Basecamp Recovery — a post-workout recovery supplement (powder, mixed with water) featuring tart cherry extract, magnesium glycinate, L-glutamine, and electrolytes. 30 servings per tub, berry flavor.
[PRICE_RANGE] = $44.99 / one-time, $37.99 / subscribe & save
[KEY_DIFFERENTIATOR] = Third-party tested, fully transparent label (no proprietary blends), formulated specifically for high-intensity functional fitness athletes — not bodybuilders, not casual gym-goers.
[COMPETITOR_NAMES] = Momentous, LMNT, Thorne
[WORDS_TO_USE] = "clean recovery," "third-party tested," "transparent label," "built for the box," "train harder tomorrow"
[WORDS_TO_AVOID] = "miracle," "hack," "crush it," "gains," "bro"
[TONE_SCALE] = 3 (very casual, confident, direct — like someone who trains hard and knows what works, without being preachy)
[CAMPAIGN_GOAL] = Drive awareness and website traffic among active TikTok users aged 22-35 who are interested in fitness and supplements
[ADDITIONAL_CONTEXT] = The product was developed with input from 200+ CrossFit athletes during a 6-month beta. The founder is a former collegiate athlete and sports dietitian. Landing page includes a video explaining the formula. Free shipping on orders over $50. Berry flavor is the only flavor currently available. The product mixes easily and does not have a chalky texture — this is a common praise point in reviews.

[CREATOR_TYPE] = Paid creator (fitness-focused TikTok creator)
[CREATOR_DEMOGRAPHICS] = Man or woman, 24-30, visibly athletic/fit, approachable and relatable — not an elite athlete or fitness model, more like "your friend who is really into CrossFit"
[PRODUCT_SHOW_REQUIREMENTS] = Product must be shown within the first 10 seconds in at least one concept. All concepts must show the product being used (scooping, mixing, drinking) at some point.
[TIKTOK_TRENDS_TO_REFERENCE] = Use evergreen formats — no specific trend required
[ORGANIC_VS_PRODUCED] = Should feel organic/UGC. Shot on a phone or made to look like it. No studio lighting, no teleprompter energy.
[COMPLIANCE_NOTES] = Do not make medical claims. Do not claim the product "cures" or "treats" anything. Use language like "supports recovery" and "helps with soreness" rather than absolute claims. No before/after body transformation imagery.
```

---

### Concept 1: "Storytime" Personal Narrative

**Format:** Storytime

**Total Duration:** 28 seconds

**Hook (First 3 Seconds):**
Visual: Close-up of the creator sitting on the floor of a gym, post-workout, slightly out of breath, looking directly at the camera with a mix of exhaustion and "I need to tell you something" energy. They are holding a shaker bottle with a purple/berry-colored drink in it.
Audio: Creator speaking directly to camera: "Okay so I need to tell you about this because I genuinely did not think it would make a difference."
On-screen text: "storytime: the supplement that actually changed my training"

**Full Script (with visual direction):**

[0:00-0:03] — Close-up, gym floor, post-workout. Creator is slightly sweaty, casual, direct to camera. — "Okay so I need to tell you about this because I genuinely did not think it would make a difference."

[0:03-0:07] — Same angle, creator shifts position slightly, leans in like they are telling a secret. — "So I train like five or six days a week and by Thursday my body just... does not cooperate. Like I am walking down stairs sideways because my legs are destroyed."

[0:07-0:10] — Quick cut to a different angle — slightly wider, showing more of the gym environment. Creator gestures with the shaker bottle. — "And I have tried like everything. Every recovery supplement. Most of them taste like chalk and do absolutely nothing."

[0:10-0:14] — Cut to a close-up of the creator scooping Basecamp Recovery into a shaker bottle. The label is visible. — "A friend who does CrossFit was like 'just try this one.' Basecamp Recovery. So I looked at the label and —" (pauses)

[0:14-0:17] — Creator holds up the tub and points at the label, tapping it. — "every single ingredient is listed with the actual dose. No proprietary blend. No mystery powder. I could see exactly what I was taking."

[0:17-0:21] — Cut back to the creator on the gym floor, shaking the bottle and taking a sip. — "I have been using it for about three weeks now and I am not going to say it is magic because it is not. But Thursday? I actually felt like a normal person. I could walk down stairs like a human being."

[0:21-0:25] — Creator looks directly at camera, slightly more serious but still warm. — "It is third-party tested, the ingredient list is completely transparent, and honestly it is the only recovery supplement I have actually kept buying."

[0:25-0:28] — Creator takes another sip, nods, and gives a casual "that is all" gesture. — "Anyway. Link is right there if you want to check it out. It is called Basecamp Recovery. You are welcome."

**On-Screen Text Overlays (timestamped):**
[0:00]: "storytime: the supplement that actually changed my training"
[0:07]: "every. single. Thursday."
[0:14]: "wait look at this label"
[0:17]: "transparent label = no proprietary blends"
[0:21]: "3 weeks in and I actually notice a difference"
[0:25]: "Basecamp Recovery | link in bio"

**CTA:**
Casual verbal mention: "Link is right there if you want to check it out." Final text overlay with brand name and "link in bio." The CTA should feel like an afterthought — the story sold the product, the link is just there if you want it.

**Sound/Music Direction:**
No background music during the hook — just the creator's voice and ambient gym noise (weights clinking, distant music from gym speakers). This makes it feel real and immediate. From [0:10] onward, a very subtle lo-fi beat fades in underneath the voiceover — something warm and slightly upbeat but not distracting. Volume should stay low enough that the voice is always dominant. The music provides rhythm and pacing support, not energy.

**Format Recommendation:**
Spark Ad. This concept is designed to look and feel like an organic creator post. Running it as a Spark Ad (boosting it from the creator's profile) will give it the highest chance of blending into the For You Page and being engaged with as content rather than skipped as an ad. If the creator has an existing TikTok presence in the fitness space, their profile lends additional credibility.

**Organic vs. Produced Notes:**
This should feel fully organic. Shot on a phone, in a real gym (not a studio), with natural lighting from overhead gym lights. No ring light, no external microphone visible. The creator should be genuinely post-workout — slightly sweaty, hair messy, wearing real workout clothes. Edits should be simple jump cuts (the default TikTok editing style), not smooth transitions. The text overlays should use TikTok's native text tool, not custom graphics. If a viewer cannot tell this is a paid ad within the first 5 seconds, the production is right.

---

### Concept 2: "I Tested/Tried" Review Style

**Format:** Review / "I tried it so you don't have to"

**Total Duration:** 25 seconds

**Hook (First 3 Seconds):**
Visual: Creator standing in their kitchen or bathroom, holding the Basecamp Recovery tub in one hand and looking at the camera with a skeptical expression — one eyebrow slightly raised, the "we will see about this" face.
Audio: Creator speaking directly to camera: "Alright so this recovery supplement has been all over my feed and I need to know if it is actually legit or just good marketing."
On-screen text: "honest review: Basecamp Recovery"

**Full Script (with visual direction):**

[0:00-0:03] — Kitchen/bathroom counter. Creator holds the product and looks at the camera with skeptical energy. — "Alright so this recovery supplement has been all over my feed and I need to know if it is actually legit or just good marketing."

[0:03-0:06] — Creator flips the tub around to show the label. Camera zooms in on the ingredient list. — "First thing I am checking — the label. Because if I see a proprietary blend that is an immediate no from me." (Pause, scanning) "Okay... every ingredient is listed. Every dose. Tart cherry, magnesium glycinate, L-glutamine, electrolytes. That is actually... really clean."

[0:06-0:10] — Cut to creator scooping the powder into a shaker bottle. Close-up of the scoop and the powder (berry colored). — "One scoop. Mixes with water. Let us see if it actually dissolves or if I am drinking a chunky protein shake situation." (Shakes it, opens lid, shows it) "Oh. That is actually smooth. No chunks. No foam."

[0:10-0:14] — Creator takes a sip. Pauses. Genuine reaction. — "Okay that is... that tastes like a berry drink. Like an actual berry drink. Not like medicine pretending to be berry." (Another sip, nodding)

[0:14-0:18] — Jump cut — new outfit, different time of day. The "after" moment. Creator is filming post-workout, slightly sweaty. — "Update. I have been using this for two weeks now. Every day after training. And here is the thing — I did not wake up one morning and feel amazing. It was more like... by week two I realized I was not as wrecked after heavy days. Like my legs were not screaming at me on the stairs."

[0:18-0:22] — Creator back in the kitchen, holding the tub. Calm, honest energy. — "Is it a miracle? No. Is it the first recovery supplement where I actually noticed a difference and did not feel like I was guessing about what was in it? Yeah. Actually yeah."

[0:22-0:25] — Creator sets the tub down on the counter, taps it. — "It is called Basecamp Recovery. It is like forty-five bucks or you can subscribe for thirty-eight. I put the link in my bio. Do what you want with that information."

**On-Screen Text Overlays (timestamped):**
[0:00]: "honest review: Basecamp Recovery"
[0:03]: "checking the label first"
[0:06]: "no proprietary blends"
[0:10]: "the taste test"
[0:14]: "2 week update"
[0:18]: "the honest verdict"
[0:22]: "Basecamp Recovery | $44.99 or $37.99 subscribe"

**CTA:**
Casual, low-pressure: "I put the link in my bio. Do what you want with that information." This is intentionally nonchalant — the entire video is the sell, and the CTA is just a door being left open. Final text overlay includes brand name and pricing.

**Sound/Music Direction:**
Quiet, upbeat lo-fi background music throughout — the kind of track that plays in product review and "get ready with me" videos. Volume should be at about 20% — present but never competing with the voiceover. During the taste test moment [0:10-0:14], consider a brief sound effect or music swell when the creator reacts positively — a subtle "ding" or the beat dropping slightly. Nothing dramatic. Just a small audio punctuation to match the visual reaction.

**Format Recommendation:**
In-Feed Ad or Spark Ad. This concept works well as either. As a Spark Ad from a fitness creator's profile, it gains authenticity. As an In-Feed Ad from the brand's account, it still works because the review format is universally understood on TikTok. For maximum reach and awareness (matching the campaign goal), In-Feed is recommended with broad targeting and interest-based audience signals.

**Organic vs. Produced Notes:**
Mostly organic with one slightly produced element: the two-week time jump. The script requires two filming sessions — one for the "first try" and one for the "two week update." This is common in TikTok review content and viewers expect it. Both sessions should be shot on a phone with natural lighting. The kitchen/bathroom setting should look like a real home, not a studio set. Editing should use standard TikTok jump cuts. Text overlays should use TikTok's native text tools. The only "produced" element is planning the two filming sessions — everything else should feel spontaneous and authentic.

---

### Concept 3: "POV" / Trending Format

**Format:** POV + "Things I Wish I Knew Sooner" hybrid

**Total Duration:** 22 seconds

**Hook (First 3 Seconds):**
Visual: Black screen with white text appearing word by word (TikTok native text style). Then a quick cut to the creator in a gym, mid-workout, looking into the camera as if the viewer just walked up to them.
Audio: A trending or popular lo-fi/motivational beat starts immediately. Creator voiceover begins: "POV: you finally stop guessing what is in your supplements."
On-screen text: "POV: you stop guessing what's in your supplements"

**Full Script (with visual direction):**

[0:00-0:03] — Black screen. Text appears word by word: "POV: you stop guessing what's in your supplements." Quick cut to creator in a gym, mid-rep on a rower or finishing a set, looking up at the camera. — Voiceover: "POV: you finally stop guessing what is in your supplements."

[0:03-0:06] — Quick cuts synced to the music beat: (1) Close-up of a generic supplement label with a "proprietary blend" circled in red or highlighted. (2) Creator shaking their head. (3) Close-up of the Basecamp Recovery label — every ingredient and dose visible. — Voiceover: "No more proprietary blends. No more mystery powders. Every ingredient, every dose, right on the label."

[0:06-0:10] — Creator scoops Basecamp Recovery into a shaker, shakes it, takes a sip. Each action is a separate quick cut synced to beats. — Voiceover: "Tart cherry. Magnesium glycinate. L-glutamine. Full electrolytes. Third-party tested. That is it."

[0:10-0:15] — Montage of training clips — the creator doing different movements (box jumps, cleans, wall balls, rowing) — each clip 1-2 seconds, synced to music. The energy builds with the beat. — Voiceover: "You train five, six days a week. Your body takes a beating. You deserve to know exactly what you are putting into it to recover."

[0:15-0:19] — Creator on the gym floor post-workout, holding the shaker bottle, looking at the camera. Calmer energy now — the music drops to a softer beat. — Voiceover: "This is not some magic powder. It is clean recovery that actually tells you what is inside. And yeah, it works."

[0:19-0:22] — Final shot: the Basecamp Recovery tub on a gym bench, shaker bottle next to it. Clean, simple composition. — Voiceover: "Basecamp Recovery. Train harder tomorrow." (Pause) "Link in bio."

**On-Screen Text Overlays (timestamped):**
[0:00]: "POV: you stop guessing what's in your supplements"
[0:03]: "proprietary blend = they won't tell you what's inside"
[0:06]: "Basecamp Recovery: every ingredient listed"
[0:08]: "tart cherry | magnesium | L-glutamine | electrolytes"
[0:10]: "third-party tested"
[0:15]: "clean recovery. transparent label."
[0:19]: "Basecamp Recovery | link in bio"

**CTA:**
Voiceover CTA integrated naturally: "Link in bio." Short and final. The entire video is structured as a building argument, and the CTA is simply the last step. Final text overlay confirms brand name and link destination. No discount code, no urgency language — the POV format sells through identification ("this is for people like me"), not through promotion.

**Sound/Music Direction:**
This concept is music-driven. Use a trending lo-fi beat with a clear rhythm that allows quick cuts to sync to the beat. The track should have a build — starting minimal during the hook, building energy during the training montage, and dropping to a softer version for the closing. If a specific trending TikTok sound fits (something motivational or fitness-adjacent), use it. If not, a copyright-free lo-fi beat with a strong kick drum works well. The voiceover should sit on top of the music at about 70% volume mix — the voice leads, the music supports. No ASMR, no silence — this concept relies on momentum and rhythm.

**Format Recommendation:**
In-Feed Ad with broad targeting. This concept is designed for maximum reach and awareness — the POV format draws in viewers who identify with the scenario ("I have supplements with proprietary blends"), and the visual pacing keeps them watching. Run this as a standalone In-Feed Ad from the brand account rather than a Spark Ad, because the quick-cut editing and text overlay style is more brand-content than creator-content. Optimize for video views or ThruPlay to maximize awareness at the top of funnel, then retarget viewers with Concept 1 or 2 for conversion.

**Organic vs. Produced Notes:**
This is the most produced of the three concepts — but it should still feel lo-fi. The quick cuts synced to music require planning and editing, but the individual clips should be shot on a phone in a real gym. No external lighting. No gimbal. Handheld or propped phone. The text overlays should use TikTok's native text tool, not After Effects. The editing should feel snappy and energetic but not cinematic — think "someone who is pretty good at editing TikToks" not "video production studio." The training montage clips can be pulled from existing workout footage or filmed in a single session across different exercises. Total production time should be under 2 hours of filming and 1 hour of editing.

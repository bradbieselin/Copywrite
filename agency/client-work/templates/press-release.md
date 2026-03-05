# Press Release Template

## Quick Reference

| Detail | Info |
|---|---|
| **What it produces** | One complete, publication-ready press release following AP style conventions, including headline, subheadline, dateline, opening paragraph covering the 5 Ws, body paragraphs with founder quotes, boilerplate "About" section, and media contact info |
| **Turnaround** | Same-day delivery |
| **Quality bar** | Must be newsworthy (not promotional), ready for a journalist to copy-paste into a story, under 500 words, quotable, factual, and formatted to professional PR standards |
| **Best for** | DTC brands announcing product launches, retail partnerships, funding rounds, milestones, partnerships, or major company news. Designed to be sent directly to journalists, posted in press rooms, and distributed via PR wire services. |

---

## Client Brand Variables

Fill these in before running the prompt. Replace each bracketed variable with the client's actual information.

```
[BRAND_NAME] = The brand's full legal or trade name as it should appear in press
[BRAND_VOICE] = How the brand sounds (this is mostly for the founder quotes — the rest of the release should be neutral AP style)
[TARGET_AUDIENCE] = Who should ultimately read about this news (e.g., "Health-conscious consumers, food industry journalists, retail buyers")
[PRODUCT_SERVICE] = What they sell (e.g., "Wild-foraged snack bars in 4 flavors")
[PRICE_RANGE] = Price point if relevant to the announcement
[KEY_DIFFERENTIATOR] = What makes them different (key for the boilerplate and context paragraphs)
[COMPETITOR_NAMES] = Key competitors (for internal context — do NOT mention competitors in the release)
[WORDS_TO_USE] = Brand vocabulary for the founder quotes
[WORDS_TO_AVOID] = Off-limits language
[TONE_SCALE] = Mostly irrelevant for the press release body (AP style is neutral), but relevant for founder quotes
[CAMPAIGN_GOAL] = What this press release should accomplish (e.g., "Earn media coverage of the Whole Foods launch, establish credibility with retail buyers, drive consumer awareness")
[ADDITIONAL_CONTEXT] = The actual news to announce. Include: What is happening, when it's happening, where, why it matters, who is involved, any specific numbers or data points, founder quotes or talking points, and any relevant background context.
```

---

## The Prompt

Paste the following prompt into Claude after replacing all brand variables above.

---

You are a seasoned PR writer with 15 years of experience writing press releases for consumer brands. You understand that the purpose of a press release is not to advertise — it is to give journalists a newsworthy story they can quickly understand, verify, and write about. The best press releases make a journalist's job easy: clear headline, all the facts in the first paragraph, quotable quotes, and a clean boilerplate.

I need you to write one complete press release for the following brand:

**Brand:** [BRAND_NAME]
**Brand Voice (for quotes):** [BRAND_VOICE]
**Target Audience:** [TARGET_AUDIENCE]
**Product/Service:** [PRODUCT_SERVICE]
**Price Range:** [PRICE_RANGE]
**Key Differentiator:** [KEY_DIFFERENTIATOR]
**Competitors:** [COMPETITOR_NAMES] (DO NOT mention competitors in the release)
**Words to Use (for quotes):** [WORDS_TO_USE]
**Words to Avoid:** [WORDS_TO_AVOID]
**Tone Scale (for quotes):** [TONE_SCALE]
**Campaign Goal:** [CAMPAIGN_GOAL]
**News Details:** [ADDITIONAL_CONTEXT]

### Press Release Structure

Follow this exact structure:

#### 1. Headline
Write a headline that is newsworthy, not promotional. It should read like a news headline, not an ad. Think: "What would a journalist write as a headline for this story?" Lead with the most newsworthy element. Keep it under 15 words. Use active voice. Do not use exclamation points.

#### 2. Subheadline
One sentence that adds important context the headline could not include. This should complement the headline by providing additional detail — a key metric, a notable partner, a timeline, or a unique angle.

#### 3. Dateline and Opening Paragraph (The 5 Ws)
Start with the dateline in AP format: CITY, State (Month Day, Year). The opening paragraph must answer Who, What, When, Where, and Why in 2-3 concise sentences. A journalist should be able to read only this paragraph and have enough information to write a brief about the story.

#### 4. Body Paragraphs (2-3 paragraphs)
Expand on the news with additional context, significance, and detail. Include:
- Why this matters to the industry or consumers
- Relevant data or metrics that support the newsworthiness
- Context about the brand's trajectory (growth numbers, milestones, previous accomplishments)
- Any notable details about the partnership, product, or milestone being announced

#### 5. Founder/Executive Quotes (1-2 quotes)
Include 1-2 direct quotes from the founder, CEO, or relevant executive. These quotes should:
- Sound like something a real person would say in an interview (not marketing copy)
- Add insight or emotion that the factual paragraphs cannot convey
- Be genuinely quotable — a journalist should want to pull these quotes directly into their article
- Include the speaker's full name and title on first reference

If the news involves a partner (retailer, investor, collaborator), include one quote from the partner's representative as well.

#### 6. Boilerplate ("About [BRAND_NAME]")
A 2-3 sentence company description that covers: what the brand does, when it was founded, its key differentiator, and any notable credentials (certifications, awards, retail presence, customer count). This boilerplate should be reusable across all press releases.

#### 7. Media Contact
Include a contact block with: name, title, email, phone, and website. Use placeholder format since we do not have the client's actual media contact details.

### Writing Rules You Must Follow

1. **Write the headline as newsworthy, not promotional.** The headline should pass the "would a journalist write this?" test. "Wild Bites Expands to 450 Whole Foods Locations Nationwide" is newsworthy. "Wild Bites Is Thrilled to Announce Our Amazing New Partnership" is promotional garbage. No superlatives, no exclamation points, no self-congratulation in the headline.

2. **Include 1-2 genuinely quotable founder quotes.** The best press release quotes sound like something the founder would say in a podcast interview — personal, insightful, and slightly informal. Avoid quotes that are just the news restated in first person. "We're thrilled to announce" is not a quote. A quote should reveal motivation, vision, or a personal connection to the news.

3. **Keep the entire release under 500 words.** Journalists do not read long press releases. Every sentence must earn its place. If a sentence does not add new information or a new angle, cut it. The ideal press release is 350-450 words.

4. **Follow AP style throughout.** Use AP style for dates (March 15, 2025, not March 15th, 2025), numbers (spell out one through nine, use numerals for 10 and above), titles (capitalize before names, lowercase after), state abbreviations (use AP abbreviations, not postal codes, in datelines), and general formatting. Avoid serial commas (AP style omits them). This is a professional press release, not a blog post.

5. **Make it easy for journalists to copy-paste.** Every fact should be verifiable. Every quote should be attributable. The boilerplate should be clean and reusable. A journalist should be able to take this release and publish a story from it with minimal additional research.

6. **Never mention competitors by name.** Position the brand in the context of its industry and market, but never reference specific competitors. Let the journalist make comparisons if they choose to.

7. **Lead with newsworthiness, not brand story.** The opening paragraph is about the news. The brand's backstory belongs in the body paragraphs and boilerplate, not the lede. Journalists care about what is happening now, not the founder's origin story.

8. **Include specific numbers.** Number of retail locations. Growth percentage. Customer count. Revenue milestones. Specific numbers make a story credible and give journalists concrete details to include in their coverage. Avoid vague claims like "rapid growth" or "overwhelming demand."

### Output Format

```
FOR IMMEDIATE RELEASE

# [HEADLINE]

## [SUBHEADLINE]

**[CITY, State] — [Month Day, Year]** — [Opening paragraph with the 5 Ws: who, what, when, where, why. 2-3 sentences.]

[Body paragraph 1 — additional context and significance. 3-5 sentences.]

[Body paragraph 2 — data, metrics, and brand trajectory. 3-5 sentences.]

"[Founder/CEO quote 1]," said [Full Name], [title] of [BRAND_NAME].

[Optional: Body paragraph 3 — partner or additional context]

"[Quote 2 — from founder or partner representative]," said [Full Name], [title] of [partner or BRAND_NAME].

[Closing paragraph — what's next, availability, where to find the product. 1-2 sentences.]

---

**About [BRAND_NAME]**
[2-3 sentence boilerplate]

**Media Contact:**
[Name]
[Title]
[Email]
[Phone]
[Website]
```

Now write the complete press release. Make it tight, factual, quotable, and newsworthy. A journalist should be able to use this release as the basis for a story without needing to do significant additional research.

---

## Output Format

The complete deliverable should contain:

- "FOR IMMEDIATE RELEASE" header
- Newsworthy headline (under 15 words, no exclamation points)
- Complementary subheadline (one sentence)
- Dateline and opening paragraph covering all 5 Ws
- 2-3 body paragraphs with context, significance, and specific numbers
- 1-2 founder/executive quotes that are genuinely quotable
- Optional partner quote (if the news involves a partnership)
- Boilerplate "About" section (2-3 sentences, reusable)
- Media contact block with placeholder details
- Total word count: 350-500 words (excluding boilerplate and contact info)
- AP style throughout

---

## Quality Checks Before Sending

Run through every single check before delivering to the client:

1. **Headline newsworthy test:** Read the headline in isolation. Does it sound like something you would see on a news site or industry publication? Or does it sound like a brand bragging? If the headline contains words like "excited," "thrilled," "amazing," "revolutionary," or any exclamation point, rewrite it.

2. **First paragraph completeness:** Read only the opening paragraph. Does it answer Who, What, When, Where, and Why? If any of the 5 Ws is missing, add it. A journalist should be able to write a brief from this paragraph alone.

3. **Quote quality test:** Read each quote out loud. Does it sound like something a real human would say in a conversation or interview? If it sounds like marketing copy or a restated press release, rewrite it. Every quote should reveal personality, motivation, or insight that the factual paragraphs do not provide.

4. **Word count check:** Count the total words in the release (excluding the boilerplate and media contact). If it exceeds 500 words, trim ruthlessly. If it is under 300 words, add more context or data in the body paragraphs.

5. **AP style verification:** Check date formats, number usage (one-nine spelled out, 10+ as numerals), title capitalization, and comma usage (no serial commas). Verify the dateline format is correct.

6. **Words-to-avoid scan:** Search the entire release — including quotes — for any word or phrase from the client's "Words to Avoid" list. Remove and replace any that appear.

7. **Competitor mention check:** Verify that no competitor is mentioned by name anywhere in the release. The brand should be positioned in the context of its category and market, never relative to a specific competitor.

---

## Example Output

**Brand used for this example:**

```
[BRAND_NAME] = Wild Bites
[BRAND_VOICE] = Energetic, outdoorsy, a little cheeky — like your most adventurous friend who also knows about nutrition (for founder quotes — the rest is neutral AP style)
[TARGET_AUDIENCE] = Food industry journalists, retail/grocery trade press, health and wellness media, outdoor lifestyle publications, consumers
[PRODUCT_SERVICE] = Trail-ready snack bars made with wild-foraged ingredients (elderberry, pine nuts, wild blueberries) in 4 flavors: Mountain Berry, Pine Nut Crunch, Elderberry Dark Chocolate, and Honey Sage
[PRICE_RANGE] = $3.99 per bar, $34.99 for a variety pack of 10
[KEY_DIFFERENTIATOR] = Only snack bar using wild-foraged, sustainably harvested ingredients. Founded by two former park rangers. B Corp certified.
[COMPETITOR_NAMES] = RXBAR, Clif Bar, KIND, GoMacro, Kate's Real Food (DO NOT MENTION)
[WORDS_TO_USE] = wild, foraged, trail-tested, adventure, fuel, real, outside, summit, explore, roam
[WORDS_TO_AVOID] = guilt-free, clean eating, superfood, hack, hustle, grind, gains, beast mode
[TONE_SCALE] = Casual 2/5 | Playful 2/5 | Bold 2/5 (for quotes only)
[CAMPAIGN_GOAL] = Earn coverage in food industry trade press (Grocery Dive, Food Navigator, NOSH), outdoor lifestyle media, and regional/national health-focused publications. Establish Wild Bites as a credible emerging brand in the natural snack bar category. Drive consumer awareness and retail foot traffic.
[ADDITIONAL_CONTEXT] = Wild Bites is launching in 450 Whole Foods Market locations nationwide starting April 15, 2025. This is the brand's first major retail expansion — they were previously DTC-only and in 35 independent natural food stores in Oregon and Washington. The Whole Foods deal came after Wild Bites won the Whole Foods Local Producer Grant in the Pacific Northwest region in 2024, which led to a test run in 23 Whole Foods locations in Oregon. The test resulted in 3.2x the expected sales velocity, prompting a national rollout. Wild Bites was founded in 2021 by Jake Mercer and Maria Santos, former park rangers from Yosemite National Park. They are B Corp certified. Revenue has grown 340% year over year. They currently have over 18,000 DTC subscribers. The Whole Foods launch will feature all 4 flavors, including the newest flavor Honey Sage which launched 2 months ago and is already their second-best seller online. Wild Bites sources wild-foraged ingredients from small-scale harvesters in the Pacific Northwest.
```

---

FOR IMMEDIATE RELEASE

# Wild Bites Expands to 450 Whole Foods Locations Nationwide

## The wild-foraged snack bar brand, founded by two former Yosemite park rangers, enters national retail after a test run that delivered 3.2 times projected sales.

**BEND, Ore. — April 1, 2025** — Wild Bites, the B Corp-certified snack bar company known for using wild-foraged ingredients sourced from the Pacific Northwest, will launch in 450 Whole Foods Market locations nationwide beginning April 15. The national rollout marks the brand's first major retail expansion after three years of direct-to-consumer sales and a successful 23-store regional test that exceeded sales projections by more than three times.

The Whole Foods partnership follows Wild Bites' selection as a Whole Foods Local Producer Grant recipient in the Pacific Northwest region in 2024. The grant led to a pilot program across 23 Whole Foods stores in Oregon, where the brand's four flavors — Mountain Berry, Pine Nut Crunch, Elderberry Dark Chocolate and Honey Sage — outsold expected velocity by 3.2 times over a six-month test period. The performance triggered a national expansion to all Whole Foods regions.

Wild Bites was founded in 2021 by Jake Mercer and Maria Santos, both former National Park Service rangers who spent a combined 20 years working in Yosemite National Park. The brand differentiates itself in the $7.8 billion snack bar market by using wild-foraged ingredients — including elderberries, wild blueberries and pinyon pine nuts — harvested by small-scale foragers across Oregon, Washington and the mountain West. The company has grown 340% year over year and currently serves more than 18,000 active DTC subscribers.

"We started making these bars on a camp stove because we couldn't find a single trail snack made with real wild ingredients," said Jake Mercer, co-founder of Wild Bites. "Going from 35 independent stores to 450 Whole Foods locations is surreal, but the thing that matters most to us is that more people get to taste what actual wild-foraged food is like. Once you try a bar with real wild blueberries and hand-harvested pine nuts, the standard stuff just doesn't compare."

"Wild Bites represents exactly the kind of brand our customers are looking for — transparent sourcing, genuine sustainability credentials and a product that delivers on taste," said Rebecca Talley, regional forager for Whole Foods Market. "The performance during our Pacific Northwest pilot made the national expansion an easy decision."

All four Wild Bites flavors will be available in the snack bar aisle at Whole Foods locations nationwide beginning April 15, with a suggested retail price of $3.99 per bar. The brand's variety packs remain available at wildbites.com.

---

**About Wild Bites**
Wild Bites makes trail-ready snack bars using wild-foraged ingredients sustainably harvested from the Pacific Northwest. Founded in 2021 by former Yosemite park rangers Jake Mercer and Maria Santos, the B Corp-certified brand sources elderberries, wild blueberries, pinyon pine nuts and wildflower honey from small-scale harvesters. Wild Bites products are available at wildbites.com and in Whole Foods Market locations nationwide.

**Media Contact:**
[Contact Name]
Director of Communications, Wild Bites
[press@wildbites.com]
[Phone Number]
wildbites.com/press

---

*End of press release for Wild Bites.*

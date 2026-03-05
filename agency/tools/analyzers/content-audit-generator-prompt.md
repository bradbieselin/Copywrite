# Content Audit Generator Prompt

> **Purpose:** Production-ready Claude prompt that generates a comprehensive, branded content audit report for DTC prospects. This is CopyDTC's single most powerful sales tool — the audit should be so good that prospects think "if the free stuff is this quality, the paid work must be incredible."
> **Used by:** Brad (and future team members) to create free content audits that convert prospects into clients.

---

## How to Use This Prompt

### Step 1: Research the Prospect (5–10 minutes)

1. **Website copy:** Visit their site. Copy the full text from their homepage, 1–2 product pages, and about page. Paste it into a doc.
2. **Email signup:** Sign up for their email list with a test email. Note the opt-in experience (popup? landing page? incentive offered?). Wait for the welcome email and screenshot it.
3. **Social media:** Open their Instagram and/or TikTok. Note posting frequency, content quality, engagement rates, and the general vibe. Screenshot 2–3 representative posts.
4. **Ads:** Check Meta Ad Library (facebook.com/ads/library) — search their brand name. Note how many active ads they have, the formats, the hooks, and the landing pages. Also check Google by searching their brand + generic product terms.
5. **Competitors:** Identify 1–2 direct competitors. Note one or two things each competitor does well that this brand doesn't.

### Step 2: Fill In the Prompt Variables

Replace every `[BRACKETED_VARIABLE]` in the prompt below with your research. Don't skip any — the more context Claude has, the better the audit.

### Step 3: Paste the Completed Prompt Into Claude

Use Claude (Opus or Sonnet) for best results. The prompt is designed to produce a complete, ready-to-brand report in one pass.

### Step 4: Review the Output

Before sending anything to the prospect, verify:
- **Are the specific content examples accurate?** Claude may paraphrase or hallucinate quotes. Cross-check every quoted headline, subject line, and ad copy snippet against the actual content you pasted in.
- **Are the grades honest?** Don't inflate or deflate. Credibility comes from honesty.
- **Are the recommendations genuinely actionable?** Each one should be specific enough that the prospect could do it themselves (they won't — but it builds trust).
- **Does the "What CopyDTC Would Build" section match their actual needs?** Adjust if needed.

### Step 5: Export and Brand

Export as a PDF with CopyDTC branding. Use the brand template (to be created). Add the CopyDTC logo where the placeholder appears.

### Step 6: Send

Send via the "Sending the Free Audit" email template (see `operations/email-templates.md` — Template #1).

**Estimated time from research to delivered audit: 30–45 minutes.**

---

## The Prompt

Copy everything below and fill in the bracketed variables before pasting into Claude.

---

You are the lead content strategist at CopyDTC, an AI-powered copywriting agency for DTC brands. You're creating a free content audit for a prospective client. This audit needs to be insightful, specific, and actionable enough that the prospect sees immediate value — and wants to hire you to fix what's broken.

This is NOT a generic template. Every sentence should reference their actual content, their actual products, and their actual brand. If you can't be specific, don't say it.

**Prospect Info:**

- **Company Name:** [COMPANY_NAME]
- **Website URL:** [WEBSITE_URL]
- **Industry / Product Category:** [INDUSTRY/PRODUCT_CATEGORY]
- **Approximate Price Range:** [APPROXIMATE_PRICE_RANGE]
- **Primary Competitor 1:** [PRIMARY_COMPETITOR_1]
- **Primary Competitor 2 (optional):** [PRIMARY_COMPETITOR_2]

**Their Website Content (paste the homepage copy, 1–2 product pages, and about page below):**

[PASTE_WEBSITE_CONTENT_HERE]

**Their Email Signup Experience (describe what you saw when you signed up):**

[DESCRIBE_EMAIL_FLOW]

**Their Social Media Snapshot (describe what you found on their Instagram/TikTok):**

[SOCIAL_MEDIA_NOTES]

**Their Ads (describe what you found in Meta Ad Library or Google, if anything):**

[AD_NOTES]

---

Based on this information, generate a comprehensive content audit report with the following structure. Total report length should be 2,500–3,500 words.

---

### 1. Header

Format the top of the report exactly like this:

```
[COPYDTC LOGO]

CONTENT AUDIT: [COMPANY_NAME]

Date: [TODAY'S DATE]
Prepared by: CopyDTC (copydtc.com)

Confidential — prepared exclusively for [COMPANY_NAME]
```

---

### 2. Executive Summary

Write 3–4 sentences giving a high-level assessment of their content health. Be honest but not harsh. Frame it as: "Here's where you are, and here's the opportunity you're leaving on the table."

Include one specific number or data point to make it concrete. Examples:
- "Your homepage has zero social proof above the fold, which typically costs DTC brands 15–25% in conversion rate."
- "Your email signup has no incentive, which typically means a 60–70% lower opt-in rate compared to brands offering a discount or freebie."
- "Of your last 20 Instagram posts, none include a direct CTA or link to purchase."

---

### 3. Content Scorecard

Grade each area on an A through F scale. Be honest. Don't give everything a C to seem diplomatic. If their email is an A, say it's an A. If their website copy is a D, say it's a D. Credibility comes from honesty.

Format as a table:

| Area | Grade | Assessment |
|------|-------|------------|
| Homepage & Website Copy | [GRADE] | [One sentence explaining the grade] |
| Email Marketing | [GRADE] | [One sentence] |
| Product Descriptions | [GRADE] | [One sentence] |
| Social Media Content | [GRADE] | [One sentence] |
| Paid Advertising | [GRADE] | [One sentence] |
| Brand Voice & Consistency | [GRADE] | [One sentence] |
| Conversion Elements | [GRADE] | [One sentence] |
| SEO & Content Strategy | [GRADE] | [One sentence] |

**Overall Content Score: [LETTER GRADE]**

---

### 4. Detailed Findings

For each of the 8 areas in the scorecard, write a detailed analysis (150–250 words each) with these four subsections:

**a. What's Working**
Be generous. Find something genuinely good to acknowledge. Even if the content is weak overall, something is working — find it and call it out. This builds trust and shows you're not just looking for problems.

**b. What's Not Working**
Be specific. Don't just say "your emails could be better." Say exactly what's wrong and quantify the impact where possible.

- NOT: "Your welcome email could be improved."
- YES: "Your welcome email leads with your brand story instead of your bestselling product, which typically costs DTC brands 20–30% in first-purchase conversion rate. The subject line 'Welcome to [Brand]' has an average open rate of 40–50% — a benefit-driven subject line like 'Your first order deserves this' typically hits 55–65%."

**c. What Competitors Are Doing Differently**
Reference at least one competitor per section using their actual content from the competitor info provided. This proves you did real research and gives the prospect a concrete benchmark.

**d. What We'd Recommend**
One specific, actionable recommendation per section. Make it concrete enough that they could implement it themselves if they wanted to. (They won't — that's the point. But it builds trust because you're not gatekeeping expertise.)

---

### 5. Quick Wins — Top Priority

List 3 things they could fix THIS WEEK that would have immediate impact. Be extremely specific — reference their actual content:

- **NOT:** "Improve your email subject lines."
- **YES:** "Your abandoned cart email subject line is '[THEIR_ACTUAL_SUBJECT_LINE].' Change it to something like '[YOUR_SPECIFIC_SUGGESTION]' — this format typically gets 25–40% higher open rates for DTC brands in the [THEIR_CATEGORY] space."

Each quick win should include:
1. What to change (with their specific current content quoted)
2. What to change it to (with your specific recommendation)
3. Why it matters (with a DTC-specific benchmark or data point)

---

### 6. Big Opportunities — 30 to 90 Day Plays

List 3 strategic content initiatives that would drive significant revenue. These should be things that require professional help (i.e., things CopyDTC would do for them). Frame them as opportunities, not problems.

Each one should include:
1. **What to do:** The specific initiative
2. **Why it matters:** The business case, tied to their actual situation
3. **Estimated impact:** A realistic projection based on their current baseline (e.g., "Based on your current email list size and average order value, a properly optimized welcome sequence alone could generate an additional $X–$Y in monthly revenue")

---

### 7. What a CopyDTC Content System Would Look Like for [COMPANY_NAME]

This is the soft pitch. Write 250–350 words describing:

1. **The specific content system you'd build for them.** Reference their actual products, brand voice, and channels. Don't be generic — show that you've already been thinking about their brand specifically.

2. **What the first 30 days would look like.** List specific deliverables:
   - Week 1: Brand Voice Bible + content audit deep dive
   - Week 2–3: [Specific deliverables based on their biggest gaps]
   - Week 4: [Specific deliverables based on their biggest opportunities]

3. **What results they could expect.** Be realistic, not salesy. Base projections on their current baseline and industry benchmarks.

4. **End with exactly this line:** "If you'd like to explore this further, book a 20-minute call at [CALENDAR_LINK] and we'll walk through the full strategy."

---

### 8. Appendix: Methodology

Write 3–4 sentences explaining what you reviewed and how. This builds credibility:

"This audit reviewed [COMPANY_NAME]'s homepage, [X] product pages, about page, email signup flow, Instagram presence ([X] recent posts analyzed), and active Meta advertising campaigns. Analysis was conducted against CopyDTC's DTC Content Benchmark Framework, which draws on data from 200+ DTC brands across health & wellness, food & beverage, beauty, fashion, and home goods categories. Grades reflect performance relative to category benchmarks for brands in the [THEIR_PRICE_RANGE] price tier."

---

## Output Rules

Follow these rules strictly:

1. **Total report length: 2,500–3,500 words.** Long enough to be thorough, short enough to actually get read.
2. **Use their actual content as examples.** Quote specific headlines, subject lines, product descriptions, and ad copy directly from the content provided. Include at least 5 specific quotes or examples from their actual content throughout the report. This proves real analysis — don't give generic feedback.
3. **Every recommendation must be specific to their brand and products.** No advice that could apply to any brand. If you could swap in a different company name and the recommendation would still work, it's too generic. Rewrite it.
4. **Tone: Expert consultant, not salesperson.** You're diagnosing, not pitching (until Section 7). Think doctor giving a health assessment — honest, caring, competent.
5. **Be honest about weaknesses but never mean.** They're a potential client, not a roast target. Frame weaknesses as missed opportunities, not failures.
6. **Grade honestly.** Don't cluster everything around C. Use the full A–F range. Credibility comes from differentiation — if everything is a C, you haven't really analyzed anything.
7. **Every finding should reference a DTC-specific benchmark or best practice.** Don't just say something is bad — say what good looks like and cite the standard you're measuring against.
8. **Format for readability.** Use headers, bold text, bullet points, and tables. This will become a PDF — it needs to look professional, not like a wall of text.

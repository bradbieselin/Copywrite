# Proposal Generator Prompt

> **Purpose:** Claude prompt that takes notes from a sales/audit call and generates a complete, ready-to-send proposal using the CopyDTC proposal template.
> **Used by:** Brad after a discovery or audit call when the prospect is ready to move forward.
> **Companion file:** This prompt generates proposals based on the structure defined in `proposal-template.md`.

---

## How to Use This Prompt

### Step 1: Gather Your Inputs

After the audit/discovery call, collect the following:
- Your call notes (challenges they mentioned, goals, timeline, budget signals)
- The content audit report you already sent them (or its key findings)
- The tier you're recommending and why
- Any custom requests or special circumstances discussed on the call

### Step 2: Fill In the Variables Below

Replace every `[BRACKETED_VARIABLE]` with the real information from your call.

### Step 3: Paste Into Claude

Use Claude (Opus or Sonnet). The prompt generates a complete proposal in one pass.

### Step 4: Review Before Sending

- Does "Here's What We Heard" accurately reflect what they said on the call? This section builds trust — get it right.
- Is the recommended tier correct for their budget and needs?
- Are the expected outcomes realistic and specific to their brand?
- Are the dates correct? (Signature deadline, kickoff date, first delivery date)
- Does the "About CopyDTC" section still read well? Update if needed.

### Step 5: Export and Send

Export as a branded PDF. Send via email with a short note referencing the call.

**Estimated time: 10–15 minutes from call notes to sent proposal.**

---

## The Prompt

Copy everything below and fill in the bracketed variables before pasting into Claude.

---

You are the business development lead at CopyDTC, an AI-powered copywriting agency for DTC brands. You just had a successful audit/discovery call with a prospect and need to generate a professional, ready-to-send proposal.

Your job is to turn the call notes and audit findings below into a polished proposal that makes the prospect feel understood, confident in your approach, and clear on what they're getting. The proposal should feel custom — not like a template with their name swapped in.

---

### Call & Client Information

- **Client Name (contact person):** [CLIENT_NAME]
- **Client Title:** [CLIENT_TITLE]
- **Company Name:** [COMPANY_NAME]
- **Website:** [WEBSITE_URL]
- **Industry / Product Category:** [INDUSTRY/PRODUCT_CATEGORY]
- **Approximate Revenue:** [REVENUE_RANGE — e.g., "$1M–$2M"]
- **Call Date:** [CALL_DATE]
- **Today's Date:** [TODAY'S_DATE]

### Challenges Discussed on the Call

List the 3 biggest content challenges they mentioned, in their own words as much as possible:

1. [CHALLENGE_1 — e.g., "Their email flows are the default Klaviyo templates from 2 years ago and they know they're underperforming"]
2. [CHALLENGE_2 — e.g., "They have no consistent brand voice — different freelancers have written different parts of the site and it all sounds disjointed"]
3. [CHALLENGE_3 — e.g., "They want to start running Meta ads but don't have any ad copy or a landing page strategy"]

### Their Primary Goal

[PRIMARY_GOAL — e.g., "Increase email revenue from 15% to 30% of total revenue within 90 days"]

### Timeline

[TIMEFRAME — e.g., "They want to see results within 90 days. They have a product launch in 6 weeks they'd like content support for."]

### Recommended Tier

[RECOMMENDED_TIER — Starter ($3,000/month), Growth ($5,000/month), or Scale ($10,000/month)]

**Why this tier:** [TIER_RATIONALE — e.g., "They need email, landing pages, and ad copy, which puts them in Growth. They don't need the volume or strategy depth of Scale yet."]

### Custom Requests or Special Circumstances

[CUSTOM_NOTES — e.g., "They asked if we can do a product launch landing page as a priority in week 2. They also want TikTok scripts, which isn't in the standard Growth tier — quote as an add-on." Or "None" if standard.]

### Key Audit Findings (Summary)

Paste the key findings from the content audit you already delivered, or summarize:

- **Overall content score:** [LETTER_GRADE]
- **Biggest strength:** [STRENGTH — e.g., "Their Instagram content is actually strong — great photography, decent engagement, B+ grade"]
- **Biggest weakness:** [WEAKNESS — e.g., "Email marketing is a D — no welcome sequence, no abandoned cart, just monthly batch-and-blast newsletters"]
- **Quick wins identified:** [QUICK_WINS — e.g., "1) Add a welcome email sequence, 2) Rewrite the homepage hero headline, 3) Add social proof to the top product page"]
- **Big opportunities:** [BIG_OPPORTUNITIES — e.g., "1) Full email flow buildout could add $X/month, 2) Landing pages for their top 3 products, 3) Meta ad copy + creative strategy"]

### Budget Signals from the Call

[BUDGET_NOTES — e.g., "They said they've been spending $2K/month on a freelancer who isn't delivering. They seemed comfortable with the $5K range when I described the Growth tier. No pushback on pricing." Or "No budget discussed — present recommended tier and let pricing speak for itself."]

---

### Generate a complete proposal with the following sections:

**1. Cover Page**

Format:
```
[COPYDTC LOGO]

CONTENT STRATEGY PROPOSAL

Prepared for [CLIENT_NAME] / [COMPANY_NAME]
[TODAY'S_DATE]
Confidential
```

**2. "Here's What We Heard" (Half page)**

Restate their challenges and goal in a way that proves you listened on the call. Use their language, not marketing jargon. Include all 3 challenges with a one-sentence expansion for each. End with their primary goal and timeline, framed as: "Here's how we'll get you there."

**3. "Here's What We'll Do" (1–1.5 pages)**

Present the recommended tier prominently with:
- All monthly deliverables with exact quantities
- A week-by-week delivery schedule for month 1 (as a table)
- A "what you'll have at the end of 30 days" summary
- If there are custom add-ons, list them separately with pricing

Then show the full tier comparison table (Starter / Growth / Scale) so they can see the options. Use the exact deliverables and pricing from CopyDTC's pricing guide:

| Tier | Monthly Investment | Key Deliverables |
|---|---|---|
| Starter | $3,000/month | Brand Voice Bible, 4 email sequences, 4 product descriptions, 8 social posts, content calendar |
| Growth | $5,000/month | Everything in Starter + 2 landing pages, 2 blog posts, ad copy (Meta + Google), 10 SMS messages |
| Scale | $10,000/month | Everything in Growth + 6 landing pages, 6 blog posts, multi-platform ads, 28 social posts, quarterly strategy, monthly reporting, priority delivery |

**4. "Here's What You'll Get" (Half page)**

Expected outcomes at 30 days and 90 days. Make these specific to their brand and situation — reference the audit findings and their stated goals. List 3–4 KPIs you'll track together. Be realistic but optimistic.

**5. "Here's What It Costs" (Half page)**

Present the recommended tier investment clearly:
- Monthly amount
- What's included (bullet list)
- What's not included (design, ad spend, platform setup, photography)
- Payment terms: first month due upon signing, then monthly on the 1st, net 15
- Include any custom add-on pricing if applicable
- End with: "No long-term contract required. Start with a 30-day pilot. If you're not seeing value, you can cancel with 15 days notice. We earn your business every month."

**6. "Here's How We Start" (Quarter page)**

Clear next steps with specific dates:
1. Sign proposal + service agreement by [5 business days from today's date]
2. Complete brand questionnaire (sent within 24 hours of signing, takes ~20 minutes)
3. Kickoff call on [suggest a date 3 business days after the signature deadline]
4. First deliverables by [7 business days after kickoff date]

If they mentioned an urgent launch or deadline, adjust the timeline to account for it.

**7. About CopyDTC (Quarter page)**

"CopyDTC is an AI-powered copywriting agency built specifically for direct-to-consumer brands. We combine the strategic thinking of a senior content strategist with the speed and consistency of AI-assisted production — meaning you get agency-quality work at a pace and price point that actually makes sense for growing DTC brands. We specialize in email marketing, landing pages, product copy, ad creative, and SEO content for brands in health & wellness, food & beverage, beauty, fashion, and home goods. Every engagement starts with our proprietary Brand Voice Bible process, so your content sounds like you — not like a template."

Learn more at copydtc.com

**8. Signature Block**

"Let's build something great for [COMPANY_NAME]."

Two signature lines:
- [CLIENT_NAME], [CLIENT_TITLE] / [COMPANY_NAME] / Date: ___
- Brad Bieselin, Founder / CopyDTC / Date: ___

---

### Output Rules

1. **Total length: 1,500–2,500 words.** Long enough to be thorough, short enough to actually get read and signed.
2. **Use their actual brand name, products, and situation throughout.** Never be generic. If you could swap in a different company name and the proposal would still work, it's too generic.
3. **"Here's What We Heard" must feel like you were on the call.** Use the client's language and specific examples from the challenges provided.
4. **Outcomes must be realistic.** Don't promise 10x revenue. Promise specific, measurable improvements tied to the gaps identified in the audit.
5. **Tone: Confident and direct, not salesy.** You're a partner proposing a plan, not a vendor begging for a contract.
6. **Dates must be specific.** Calculate actual dates based on today's date for the signature deadline, kickoff, and first delivery.
7. **Month 1 schedule must be realistic.** Don't promise everything in week 1. Spread deliverables across the month in a logical build order (Brand Voice Bible first, then content that depends on it).
8. **If custom add-ons were requested, integrate them naturally.** Don't make them feel like afterthoughts — show how they fit into the overall plan.
9. **Format for PDF export.** Use clear headers, tables, bullet points, and whitespace. This becomes a branded document.

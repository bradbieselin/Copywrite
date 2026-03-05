# CopyDTC Client Onboarding Checklist

---

## Client Information

| Field | Details |
|---|---|
| **Client** | [CLIENT NAME] |
| **Start Date** | [DATE] |
| **Tier** | [ ] Starter ($3K/mo) / [ ] Growth ($5K/mo) / [ ] Scale ($10K/mo) |
| **Primary Contact** | [NAME, EMAIL] |
| **Secondary Contact** | [NAME, EMAIL] |
| **Communication Channel** | [Email / Slack / Google Chat / Other] |
| **Onboarding Owner** | Brad |

---

## Phase 1: Pre-Kickoff (Before Day 1)

Everything in this phase must be completed before the kickoff call is scheduled. No exceptions. This is the foundation -- if anything here is incomplete, the onboarding starts on shaky ground.

- [ ] **Service agreement signed**
  - Owner: Brad
  - Tool: PandaDoc / DocuSign
  - Agreement includes scope of work, deliverables per tier, payment terms, revision policy, and content ownership
  - Confirm the correct tier is reflected in the agreement
  - File signed agreement in client folder under `/brand-guide`

- [ ] **First invoice sent and paid**
  - Owner: Brad
  - Tool: Stripe / QuickBooks
  - Invoice sent within 24 hours of signed agreement
  - Payment confirmed before any work begins
  - Set up recurring billing for Month 2+
  - Note: Net-0 terms. We do not start work until payment clears.

- [ ] **Client folder created**
  - Owner: Brad
  - Tool: Google Drive
  - Duplicate the `client-folder-template` directory
  - Rename to client's brand name
  - Move to `/clients/` in the main CopyDTC drive
  - Verify all subfolders are intact: `/brand-guide`, `/content-calendar`, `/deliverables` (with all 7 subfolders), `/feedback`, `/reports`

- [ ] **Client added to project management system**
  - Owner: Brad
  - Tool: Notion / Asana
  - Create client workspace/project
  - Add all deliverable milestones for Month 1
  - Set up recurring tasks for monthly deliverables
  - Tag with correct tier for workload tracking

- [ ] **Welcome email sent**
  - Owner: Brad
  - Tool: Gmail
  - Send within 2 hours of payment confirmation
  - Include: Personal welcome, what to expect in the first 30 days, link to questionnaire, request for kickoff call scheduling
  - Tone: Warm, confident, professional. Make them feel like they made the right decision.
  - Attach or link the Client Questionnaire

- [ ] **Client questionnaire sent**
  - Owner: Brad
  - Tool: Google Docs / PDF
  - Send as a Google Doc (editable) or clean PDF
  - Include a note: "This takes about 30-45 minutes. The more detail you give us, the better your content will be from Day 1."
  - Set a soft deadline: "Please complete this at least 24 hours before our kickoff call."

- [ ] **Kickoff call scheduled**
  - Owner: Brad
  - Tool: Calendly / Google Calendar
  - Schedule within 3-5 business days of payment
  - Duration: 45-60 minutes
  - Send calendar invite with video link (Zoom/Google Meet)
  - Include kickoff call agenda in the invite description
  - Reminder: Questionnaire must be completed before the call

---

## Phase 2: Day 1 -- Kickoff Call

The kickoff call is not a sales call. The client has already bought. This is a strategy session. The goal is to fill gaps the questionnaire didn't capture, build rapport, and align on priorities.

- [ ] **Kickoff call completed**
  - Owner: Brad
  - Tool: Zoom / Google Meet
  - Duration: 45-60 minutes
  - Record the call (with client permission) for reference

  **Call Agenda:**
  1. **Quick intros and rapport building** (5 min)
     - Casual conversation. Ask how they're doing. Reference something specific about their brand to show you've done your homework.
  2. **CopyDTC process overview** (5 min)
     - Walk through the 30-day onboarding timeline
     - Explain: Brand Voice Bible > Content Calendar > First Deliverables > Feedback Loop > Full Production
     - Set expectations: "Week 1 is strategic. Weeks 2-4 are production. You'll see content fast, but the first few days are about getting it right."
  3. **Questionnaire deep-dive** (20 min)
     - Review their questionnaire answers together
     - Probe deeper on: customer avatar (Q17), objections (Q15), brand voice words (Q18-19), copy they love/hate (Q27-28)
     - Ask: "Is there anything about your brand voice that's hard to put into words but you'd know it if you heard it?"
     - Ask: "What's the one thing your current content gets wrong most often?"
     - Ask: "If I wrote something and it was perfect, what would it feel like to read?"
  4. **Competitive landscape** (10 min)
     - Ask them to name their top 3 competitors
     - Ask: "What do they do well? What do they get wrong?"
     - Ask: "Is there a brand outside your industry whose content you admire?"
  5. **Month 1 priorities** (10 min)
     - Confirm what they want first (Q40)
     - Discuss any upcoming launches, promotions, or deadlines
     - Align on the first batch of deliverables
     - Discuss content calendar preferences
  6. **Access and logistics** (5 min)
     - Confirm communication channel
     - Confirm analytics access
     - Confirm asset sharing method
     - Set expectations for response times (both sides)

- [ ] **Kickoff call recap email sent**
  - Owner: Brad
  - Tool: Gmail
  - Send within 2 hours of the call
  - Include: Summary of key decisions, Month 1 priorities, immediate next steps, timeline for Brand Voice Bible (48 hours), any open items/questions
  - Tone: Organized, action-oriented, reassuring

- [ ] **Questionnaire received and filed**
  - Owner: Brad
  - Tool: Google Drive
  - Confirm all 47 questions have answers (or explicit N/As)
  - Flag any gaps or vague answers for follow-up
  - File completed questionnaire in client folder under `/brand-guide`
  - If questionnaire is still incomplete, send a friendly nudge with specific questions that need answers

---

## Phase 3: Day 2-3 -- Brand Voice Bible

This is the most important phase of onboarding. The Brand Voice Bible determines the quality of everything that follows. Do not rush this.

- [ ] **Questionnaire reviewed in detail**
  - Owner: Brad
  - Tool: Google Docs / Notes
  - Read through the entire questionnaire twice
  - Highlight standout answers, unique customer language, and brand personality signals
  - Cross-reference with kickoff call notes
  - Identify any contradictions or gaps that need clarification

- [ ] **Follow-up questions sent (if needed)**
  - Owner: Brad
  - Tool: Email / Slack
  - If any critical answers are missing or vague, send specific follow-up questions
  - Keep it focused: no more than 3-5 questions
  - Give a 24-hour turnaround request

- [ ] **Brand Voice Bible generated**
  - Owner: Brad
  - Tool: Claude (using brand-voice-generator-prompt.md)
  - Paste the full prompt from `brand-voice-generator-prompt.md`
  - Attach the completed questionnaire
  - Generate the full Brand Voice Bible
  - Review the output critically -- Claude will produce a strong first draft, but the following need manual review:
    - Does the Voice Summary actually sound like this brand, or is it generic?
    - Are the Voice Attributes specific enough that you could catch off-brand copy?
    - Do the sample copy pieces sound like real content for this brand?
    - Is the Customer Language Map using language real humans would use?
    - Are the Language Rules concrete and enforceable?

- [ ] **Brand Voice Bible reviewed and refined**
  - Owner: Brad
  - Tool: Google Docs
  - Edit the Bible based on your review
  - Add insights from the kickoff call that Claude didn't have
  - Adjust any recommendations that don't feel right for this brand
  - Run through the Final Check at the bottom of the generator prompt
  - Format cleanly: consistent headers, clean tables, no broken formatting

- [ ] **Brand Voice Bible sent to client for approval**
  - Owner: Brad
  - Tool: Email / Google Docs
  - Send as a shareable Google Doc or PDF
  - Include a note: "This is your Brand Voice Bible -- the foundation for all content we create. Please review it and let us know if anything feels off. We want this to feel 100% right before we start producing content."
  - Request feedback within 24-48 hours
  - File in client folder under `/brand-guide`

---

## Phase 4: Day 4-5 -- Content Planning

Once the Bible is approved (or approved with minor edits), shift into production planning.

- [ ] **Brand Voice Bible approved by client**
  - Owner: Brad
  - Tool: Email / Slack
  - Confirm the client has reviewed and approved the Bible
  - If revisions are requested, make them within 24 hours and resubmit
  - Once approved, mark it as the official Brand Voice Bible v1.0
  - Note: Do not begin content production until the Bible is approved

- [ ] **Content calendar created for Month 1**
  - Owner: Brad
  - Tool: Google Sheets / Notion
  - Build a full Month 1 content calendar based on:
    - Tier deliverables (Starter: X pieces, Growth: Y pieces, Scale: Z pieces)
    - Client's Month 1 priorities from kickoff call
    - Any upcoming launches, promotions, or seasonal events
    - Logical batching (group similar content types for production efficiency)
  - Include for each deliverable: content type, topic/subject, channel, due date, batch number, status
  - Organize into 4 weekly batches

- [ ] **Content calendar sent to client for approval**
  - Owner: Brad
  - Tool: Email / Google Sheets
  - Send with a note: "Here's your Month 1 content plan. Let us know if you'd like to adjust any topics or priorities. We'll start producing Batch 1 as soon as you approve."
  - Request approval within 24 hours
  - File in client folder under `/content-calendar`

- [ ] **Analytics access received and reviewed**
  - Owner: Brad
  - Tool: Google Analytics, Shopify, Klaviyo, Meta, etc.
  - Confirm access to all platforms the client checked in Q43
  - Review current performance baselines:
    - Email: open rates, click rates, revenue attribution
    - Ads: ROAS, CTR, CPA
    - Website: conversion rate, bounce rate, top pages
    - Social: engagement rate, follower growth
  - Note baseline numbers for the Month 1 report
  - If access is delayed, follow up daily until resolved

- [ ] **Brand assets received**
  - Owner: Brad
  - Tool: Google Drive
  - Confirm receipt of: brand guidelines (if they exist), product photos, lifestyle images, logos, any existing content that performs well
  - Organize in client folder under `/brand-guide`
  - If assets are missing or low-quality, flag it early and discuss solutions

---

## Phase 5: Day 5-7 -- First Deliverables

First impressions matter. The first batch of content sets the tone for the entire engagement. Over-deliver here.

- [ ] **Batch 1 produced**
  - Owner: Brad
  - Tool: Claude + Google Docs
  - Produce the first batch of deliverables from the content calendar
  - Reference the Brand Voice Bible for every piece
  - First batch should include the client's top priority from the kickoff call
  - Quality check every piece against the Voice Attributes and Language Rules
  - Recommended first batch: 3-5 high-impact pieces (e.g., welcome email flow, 2 product descriptions, 3 ad variations)

- [ ] **Batch 1 delivered with strategic context**
  - Owner: Brad
  - Tool: Email / Google Docs
  - Deliver each piece in a clean Google Doc
  - For EACH deliverable, include a brief strategic note (2-3 sentences):
    - Why this content is structured the way it is
    - What customer psychology or objection it addresses
    - What the expected outcome is (higher open rates, more clicks, stronger brand recall, etc.)
  - Include a note: "Please review and share any feedback. We'll incorporate your notes and keep the momentum going."
  - File all deliverables in the appropriate subfolders within `/deliverables`

---

## Phase 6: Day 7-10 -- Feedback & Refinement

The feedback loop is where the real calibration happens. This is normal and expected -- the goal is to get tighter with each batch.

- [ ] **Client feedback received on Batch 1**
  - Owner: Brad
  - Tool: Email / Slack / Google Docs
  - If no feedback received by Day 8, send a friendly follow-up
  - Ask specific questions: "Does this feel like your brand? Is the tone right? Anything feel off?"
  - Document ALL feedback in client folder under `/feedback`

- [ ] **Feedback analyzed and patterns identified**
  - Owner: Brad
  - Tool: Notes / Google Docs
  - Look for patterns in the feedback:
    - Is the tone too casual or too formal?
    - Are there specific words or phrases the client keeps flagging?
    - Is the humor level right?
    - Are they asking for more or less detail?
  - Update the Brand Voice Bible if needed (note changes as v1.1)
  - If feedback suggests a significant voice misalignment, schedule a brief 15-minute call

- [ ] **Revised deliverables sent (if needed)**
  - Owner: Brad
  - Tool: Google Docs
  - Turn around revisions within 24-48 hours
  - Include a note explaining what was changed and why
  - Ask for final approval on revised pieces

- [ ] **Batch 2 production started**
  - Owner: Brad
  - Tool: Claude + Google Docs
  - Begin Batch 2 using updated voice calibration from Batch 1 feedback
  - Apply any Brand Voice Bible updates
  - Batch 2 should show noticeable improvement in brand alignment

---

## Phase 7: Day 10-14 -- Full Production Mode

By now the voice is calibrated, the feedback loop is established, and production should be running smoothly.

- [ ] **Batch 2 delivered**
  - Owner: Brad
  - Tool: Email / Google Docs
  - Same delivery format as Batch 1 (strategic context for each piece)
  - Confirm client sees improvement from Batch 1 feedback
  - File deliverables in appropriate subfolders

- [ ] **Mid-month check-in completed**
  - Owner: Brad
  - Tool: Email / Slack / Quick call
  - Proactive check-in with the client (not waiting for them to reach out)
  - Cover:
    - "How are you feeling about the content so far?"
    - "Is there anything you'd like to adjust for the second half of the month?"
    - "Any upcoming promotions or launches we should plan for?"
    - "How is the communication cadence working for you?"
  - Adjust Month 1 plan if needed based on feedback
  - This can be a quick email exchange or a 10-15 minute call -- read the client's communication preference

---

## Phase 8: Day 14-25 -- Delivery Completion

Head down, producing. The voice is locked in. The feedback loop is smooth. Execute the content calendar.

- [ ] **Batch 3 produced and delivered**
  - Owner: Brad
  - Tool: Claude + Google Docs
  - Maintain quality bar from Batch 2
  - Continue including strategic context with each deliverable
  - File in appropriate subfolders

- [ ] **Batch 4 produced and delivered**
  - Owner: Brad
  - Tool: Claude + Google Docs
  - Final batch of Month 1
  - Ensure all content calendar items are accounted for
  - File in appropriate subfolders

- [ ] **All Month 1 deliverables complete**
  - Owner: Brad
  - Tool: Google Sheets / Notion
  - Cross-reference content calendar with delivered files
  - Confirm every promised deliverable has been produced and delivered
  - Confirm every deliverable has been approved or is in revision
  - No outstanding items should carry into Month 2 unless agreed upon with the client

- [ ] **Deliverables organized and archived**
  - Owner: Brad
  - Tool: Google Drive
  - Verify all files are in the correct subfolders
  - Naming conventions are consistent
  - Final approved versions are clearly labeled
  - Feedback documents are filed

---

## Phase 9: Day 25-30 -- Review & Retention

The end of Month 1 is a critical retention moment. The client is deciding whether to continue. Make it easy for them to say yes.

- [ ] **Monthly performance report created**
  - Owner: Brad
  - Tool: Google Docs / Google Sheets
  - Pull data from all connected analytics platforms
  - Report should include:
    - Summary of all content produced (types, quantities)
    - Performance metrics for any content that has been live long enough to measure
    - Email metrics: open rates, click rates, revenue attributed
    - Ad metrics: CTR, CPA, ROAS (if applicable)
    - Website metrics: conversion rate changes, page performance (if applicable)
    - Comparison to baseline numbers from Day 4-5
    - Top-performing piece of content and why it worked
    - Recommendations for Month 2
  - File in client folder under `/reports`

- [ ] **Month-end review call scheduled and completed**
  - Owner: Brad
  - Tool: Zoom / Google Meet
  - Duration: 30 minutes
  - Schedule proactively -- don't wait for the client to ask

  **Call Agenda:**
  1. **Celebrate wins** (5 min) -- Lead with positive results and momentum
  2. **Review the report** (10 min) -- Walk through key metrics and performance data
  3. **Feedback collection** (5 min) -- "What went well? What could be better? Scale of 1-10, how happy are you?"
  4. **Month 2 planning** (10 min) -- Preview upcoming content plan, discuss new priorities, align on deliverables

- [ ] **Retention confirmed**
  - Owner: Brad
  - Tool: Email
  - After the review call, send a follow-up confirming Month 2 continuation
  - If the client hesitates or raises concerns, address them immediately
  - If the client is at risk of churning, escalate internally and consider:
    - Additional deliverables at no charge to demonstrate value
    - Adjusting the content mix to better align with their priorities
    - A candid conversation about what needs to change

- [ ] **Testimonial requested (if appropriate)**
  - Owner: Brad
  - Tool: Email
  - Only ask if the client is clearly happy (8+ on satisfaction)
  - Keep the ask simple: "Would you be open to sharing a quick testimonial about your experience? A few sentences is perfect."
  - Offer options: written quote, video testimonial, or case study
  - If they say yes, send a short list of prompts:
    - "What was your situation before working with CopyDTC?"
    - "What results have you seen?"
    - "What would you say to someone considering CopyDTC?"

- [ ] **Referral opportunity explored (if appropriate)**
  - Owner: Brad
  - Tool: Email / Call
  - Only after testimonial is secured or if the client proactively expresses satisfaction
  - Keep it natural: "Do you know any other brand owners who could use help with their content? Happy to offer them a call."
  - Do NOT make this feel transactional or pushy
  - Consider implementing a referral incentive (discount on next month, bonus deliverables)

---

## Key Metrics to Track During Onboarding

These metrics help diagnose the health of the onboarding and predict long-term client success.

| Metric | Target | How to Measure |
|---|---|---|
| Time from payment to kickoff call | 3-5 business days | Calendar |
| Time from questionnaire to Brand Voice Bible | 48 hours | Internal tracking |
| Time from Bible approval to first deliverable | 2-3 business days | Internal tracking |
| Client response time (average) | Under 48 hours | Email/Slack timestamps |
| Batch 1 feedback rating | Positive (minimal revisions) | Client feedback |
| Revision rounds per deliverable | 1 or fewer (average) | Revision tracking |
| All Month 1 deliverables complete by Day 25 | Yes | Content calendar status |
| Client satisfaction at Month-end review | 8+ out of 10 | Direct question on call |
| Month 2 retention rate | 90%+ | Billing confirmation |
| Testimonial secured by Day 30 | 50%+ of happy clients | CRM tracking |
| Time spent on onboarding (total hours) | Starter: 15-20h / Growth: 25-30h / Scale: 40-50h | Time tracking |

---

## Red Flags During Onboarding

Watch for these warning signs and address them immediately:

- **Client takes more than 5 days to return the questionnaire.** Follow up directly. Offer to walk through it together on a call.
- **Questionnaire answers are mostly one-word or vague.** Schedule a call to fill in the gaps verbally. Do not build a Brand Voice Bible on thin data.
- **Client is unresponsive for 48+ hours during active production.** Send a clear, friendly check-in. If the pattern continues, address it on the next call.
- **Batch 1 feedback is heavily negative.** Do not take it personally. Schedule a call within 24 hours. Re-calibrate the voice. Consider generating a fresh Brand Voice Bible with the new context.
- **Client requests scope changes or additional deliverables beyond their tier.** Address it honestly: "We'd love to do that -- here's how it fits into our tier structure." Upsell if appropriate, but never give away scope for free.
- **Client contact person changes mid-onboarding.** Request an introduction to the new contact. Re-send the Brand Voice Bible. Consider a brief re-alignment call.
- **Payment for Month 2 is delayed.** Pause production until payment is received. Send a professional reminder on Day 1 of the new month.

---

## Onboarding Complete

When all items above are checked, the client has been successfully onboarded. They should:

1. Have an approved Brand Voice Bible they're excited about.
2. Have received a full month of high-quality, on-brand content.
3. Understand the production process and feedback loop.
4. Feel confident about Month 2 and beyond.
5. Be a potential source of testimonials and referrals.

Transition from onboarding mode to ongoing production mode. Archive this checklist in the client folder under `/reports`.

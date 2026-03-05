# Outreach Personalizer Prompt

> **Purpose:** Claude prompt specifically designed for personalizing outreach emails at scale. Takes a prospect's public information and generates customized copy that feels hand-written.
> **Status:** Scaffold — full content to be built in subsequent prompts
> **Used by:** Brad when personalizing outreach for individual prospects or small batches

## Contents

### The Prompt
- Input: prospect's company name and website URL
- Input: prospect's name and role
- Input: 1-2 specific observations about their brand (from initial research)
- Input: which outreach sequence (A: Audit Offer, B: Competitor Gap, C: Results-Led)

### Output
1. **Personalized Email** — complete email using the selected sequence template, customized with:
   - Their company and product references
   - A specific, genuine observation about their content
   - A relevant hook tied to their industry or situation
2. **Subject Line Options** — 3 personalized subject lines
3. **Follow-Up Angles** — 2-3 different angles for follow-up emails
4. **Conversation Starters** — if they reply, 2-3 ways to advance toward a call

### Personalization Depth Levels
- Level 1 (Quick): name + company + one observation (2 minutes per prospect)
- Level 2 (Standard): name + company + product reference + specific content feedback (5 minutes)
- Level 3 (Deep): all of Level 2 + competitive context + strategic insight (10 minutes)

### Quality Bar
- Email must reference something that shows genuine research
- No generic compliments ("love your brand" = lazy)
- Personalization should connect to CopyDTC's value proposition
- Under 125 words total

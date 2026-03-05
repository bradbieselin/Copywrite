# Batch Outreach Prompt

> **Purpose:** Claude prompt for generating personalized outreach emails in bulk. Input a list of prospects with basic info, get back customized first-touch emails for each one.
> **Status:** Scaffold — full content to be built in subsequent prompts
> **Used by:** Brad when sending outreach at scale (10+ prospects at once)

## Contents

### The Prompt
- Input: CSV or list of prospects (company name, website, niche, contact name, one observation per prospect)
- Input: which outreach sequence to use (A, B, or C)
- Input: any seasonal or timely hooks to include

### Output
- Personalized Email 1 for each prospect
- Subject line customized per prospect
- One specific observation or compliment per prospect
- Scheduling recommendation (best day/time to send)

### Batch Processing Rules
- Each email must feel individually written
- Never reuse the same observation across multiple prospects in the same niche
- Vary sentence structure and opening hooks across the batch
- Include merge-field format for mail merge tools (if applicable)

### Quality Bar
- A prospect should not be able to tell their email was part of a batch
- Every email must include at least one detail that could only come from researching that specific brand
- No email should exceed 125 words

# Feedback Processor Prompt

> **Purpose:** Claude prompt that takes raw client feedback on deliverables and converts it into actionable revision instructions, Brand Voice Bible updates, and process improvements.
> **Status:** Scaffold — full content to be built in subsequent prompts
> **Used by:** Brad after receiving client feedback on any batch of deliverables

## Contents

### The Prompt
- Input: raw client feedback (email, comments, marked-up documents)
- Input: the original deliverable(s) that received feedback
- Input: the client's current Brand Voice Bible

### Output Sections
1. **Feedback Summary** — categorize feedback into: voice/tone issues, factual corrections, structural changes, style preferences, strategic direction changes
2. **Revision Instructions** — specific, line-by-line instructions for revising each deliverable
3. **Brand Voice Bible Updates** — any changes that should be made to the client's Bible based on this feedback (new words to avoid, tone adjustments, etc.)
4. **Pattern Recognition** — recurring themes in the feedback that suggest systemic adjustments
5. **Process Notes** — anything to change about our approach for future deliverables for this client
6. **Client Satisfaction Signal** — read between the lines: is the client happy, neutral, or frustrated? What should we do about it?

### Quality Bar
- Revisions should address every piece of feedback, not just the easy ones
- Brand Voice Bible updates should be specific and actionable
- Process notes should prevent the same feedback from recurring

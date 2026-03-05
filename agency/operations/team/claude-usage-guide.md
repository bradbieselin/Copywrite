# Claude Usage Guide

> **Purpose:** Internal guide for how CopyDTC uses Claude (Anthropic's AI) to produce client content. Covers prompt best practices, template usage, quality control, and common pitfalls.
> **Status:** Scaffold — full content to be built in subsequent prompts
> **Used by:** Anyone on the CopyDTC team who uses Claude to generate content

## Contents

### Getting Started with Claude
- API key setup and access
- Recommended Claude model for content generation (Claude Sonnet for drafts, Claude Opus for complex/strategic pieces)
- Claude Code vs Claude.ai vs API — when to use each

### Using Our Prompt Templates
- Where templates live: /client-work/templates/
- How to fill in Brand Variables from the client's Brand Voice Bible
- Step-by-step workflow: select template → paste variables → run prompt → review output
- When to customize the template vs use it as-is

### Prompt Best Practices
- Always paste the Brand Voice Bible section first
- Be specific about what you want — vague prompts get vague output
- Include examples of what "good" looks like when possible
- Use follow-up prompts to refine specific sections rather than re-running the whole thing
- Save successful prompt variations for future use

### Quality Control
- AI output is a first draft, never a final product
- Always check: brand voice match, factual accuracy, placeholder replacement, character/word counts
- Common AI mistakes to watch for: generic language, corporate-speak, made-up statistics, repetitive sentence structures
- The "read it out loud" test — if it sounds like a robot, revise it

### Advanced Techniques
- Chain prompting: use output from one template as input for another
- Batch processing: running multiple deliverables in sequence
- Voice calibration: using client feedback to improve future outputs
- A/B variant generation: asking Claude for multiple versions

### Cost Management
- Approximate token usage per template type
- When to use Sonnet vs Opus to optimize spend
- Batch efficiency tips

### Troubleshooting
- Output doesn't match brand voice → check that Brand Voice Bible is pasted correctly
- Output is too generic → add more specific context about the product/campaign
- Output is too long/short → specify exact word counts in the prompt
- Output has factual errors → always verify claims and statistics independently

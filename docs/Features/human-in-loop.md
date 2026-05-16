# Human-in-the-Loop Research

The distinguishing feature of ResearchCrew: humans actively guide research direction.

## What is Human-in-the-Loop?

Traditional AI research tools are **one-shot**: you ask a question, get an answer. ResearchCrew is **iterative and collaborative**: human and AI work together across multiple rounds.

### One-Shot Research (Traditional)

```txt
User: "Research AI"
     ↓
AI: Generates report
     ↓
Done (no feedback, no iteration)
```

### Human-in-the-Loop Research (ResearchCrew)

```txt
User: "Research AI"
     ↓
AI: Generate initial findings
     ↓
User: Reviews, identifies gaps
     ↓
User: "Explore safety more, skip history"
     ↓
AI: Iterates with guidance
     ↓
User: Reviews again
     ↓
User: "Add cost analysis, clarify timeline"
     ↓
AI: Refines further
     ↓
Result: Thoroughly researched, human-guided output
```

## Why This Matters

### Problem: AI Research Without Guidance

Without human steering, AI research can:

- Focus on surface-level information
- Miss important nuances your domain expertise catches
- Explore irrelevant tangents
- Repeat the same sources unnecessarily
- Include information that's technically correct but not relevant

### Solution: Human Feedback Loop

By actively guiding the crew:

- You leverage AI's ability to search and synthesize
- Your expertise guides focus and priorities
- Results are aligned with your actual needs
- Quality improves with each iteration
- Research is transparent (you see intermediate outputs)

## How to Guide Research Effectively

### Before Your First Run

Think about your research goal:

- What specific questions do you want answered?
- What should the output be used for?
- Are there areas you're unsure about vs. expert in?

Example: If researching "AI in healthcare," you might be:

- Expert in: regulatory compliance
- Curious about: implementation challenges in small clinics
- Looking for: emerging trends, not history

### During Review (Between Runs)

After each run, review `report.md` and ask:

1. **What's missing?** What topics should be deeper?
2. **What's unnecessary?** What can be skipped?
3. **What's unclear?** Where do sources conflict or lack detail?
4. **What's wrong?** Any factual inaccuracies?

### Providing Feedback

Edit `report.md` and add a "User Feedback" section at the end:

```markdown
## User Feedback - Round 2

### Please Explore More:

1. **Implementation in rural clinics** — Most sources focus on large hospitals. 
   Need more on smaller healthcare providers and resource constraints.

2. **Cost-benefit analysis** — What's the actual ROI? What's the payback period?

3. **Patient data security** — How are patient records handled with AI diagnostics?

### Please Skip:

- General history of AI (already covered well)
- Theoretical discussions about future AI (focus on current/near-term)

### Clarifications Needed:

- The report says "95% accuracy" but for what population? Kids vs adults? 
  Please clarify the context.
```

The crew will:

1. See this feedback
2. Understand your priorities
3. Research the topics you highlighted
4. Skip areas you de-prioritized
5. Verify and clarify conflicts

### Examples of Good Guidance

**Specific topic exploration:**

```markdown
## User Feedback

The report mentions "machine learning algorithms" but doesn't explain which ones.
Please research:
- Specific algorithms used (CNNs for imaging, NLP for text analysis, etc.)
- Why these algorithms over alternatives
- Performance characteristics of each
```

**Narrowing scope:**

```markdown
## User Feedback

The report is 50+ pages and covers many countries. We only care about US market.
Please focus on:
- US regulatory environment only
- US company implementations
- US market adoption rates
```

**Fixing quality issues:**

```markdown
## User Feedback

The "Cost Analysis" section lists prices from 2023. These are outdated.
Please update with 2025 pricing from recent sources.

Also, the report says "All experts agree on X" but we saw conflicting views. 
Please clarify the disagreement and major positions.
```

**Deepening understanding:**

```markdown
## User Feedback

The report explains *that* AI is being used in diagnostics, but I need to understand *how*.
Please research:
- Technical approach (how does the AI make decisions)
- Interpretability (can doctors understand why the AI recommended something)
- Integration with existing workflows (how does a doctor use the tool)
```

## Iteration Strategies

### Conservative Approach (Safe)

1. Run initial research
2. Review thoroughly
3. Provide one set of comprehensive feedback
4. One or two more iterations to refine

**Best for:** Complex topics, high-stakes decisions, where accuracy matters more than speed

### Agile Approach (Fast)

1. Run initial research
2. Quick review, give feedback on biggest gaps
3. Run again, review findings
4. Small refinement iteration

**Best for:** Quick research, exploratory work, topics you're familiar with

### Deep Dive Approach

1. Run initial research
2. Thorough review, detailed feedback
3. Run again
4. Run again with even more detailed feedback
5. Continue until research depth matches your goals

**Best for:** Building authoritative reports, publishing, critical decisions

## When Human Guidance is Most Valuable

**Perfect for:**

- Complex topics with many angles (guide focus)
- Domain expertise you want to apply (verify and deepen)
- Exploratory research (discover and refine)
- Building publishable reports (iterate on quality)

**Less valuable for:**

- Simple factual questions (one-shot is fine)
- Very narrow topics (little to guide)
- Time-critical needs (iteration takes time)

## Collaboration with Teams

If multiple people are researching the same topic:

1. **Person A** runs initial research
2. **Persons A, B, C** review and provide feedback
3. **Consolidate feedback** into research plan (avoid duplicates)
4. **One person** provides consolidated feedback to crew
5. **Persons A, B, C** review updated report together

Share feedback in a structured format:

```markdown
## Consolidated Feedback - Round 2

From Alice:
- Deeper on: Cost analysis
- Skip: Historical background

From Bob:
- Deeper on: Security implications
- Clarify: Expert disagreements

From Carol:
- Deeper on: Timeline predictions
- Verify: All numbers are 2025 data
```

## Monitoring Research Quality

### Red Flags (May Need More Iteration)

- Report is too shallow (surface-level information only)
- Sources are consistently from unreliable domains
- Claims conflict without explanation
- Numbers seem outdated or unrealistic
- Same topics repeated across sections
- Missing key subtopics you know are important

### Green Lights (Research is Good)

- Multiple perspectives included and explained
- Claims trace to credible sources
- Depth matches your expertise level
- Covers topics you identified as important
- Addresses questions you had
- Appropriate nuance and caveats

## Tips for Effective Human Guidance

1. **Be specific** — Name topics, sections, or claims, not just "more research"

2. **Explain your reasoning** — Why do you want to explore topic X? This helps crew prioritize

3. **Provide context** — What will the research be used for? Crew can adjust depth accordingly

4. **Batch feedback** — Collect multiple feedback items before next run (more efficient)

5. **Validate learning** — In round 2+, verify the crew understood your feedback from round 1

6. **Know when to stop** — Most research reaches good quality by round 3-4

## Best Practices

**Do:**

- Review reports thoroughly between runs
- Give clear, specific feedback
- Validate the crew understood your guidance
- Use domain expertise to verify quality
- Iterate until you're satisfied

**Don't:**

- Provide vague feedback ("make it better")
- Change direction completely each round (confuses crew)
- Expect perfect results after 1 run (quality improves with feedback)
- Rush iterations (thoughtful guidance takes time)

## Next Steps

- **[Iterative Research Workflow](../usage/iterative-research.md)** — Step-by-step guide
- **[Examples](../examples/index.md)** — Real multi-round research examples
- **[Reliability Features](reliability.md)** — Quality checks throughout pipeline

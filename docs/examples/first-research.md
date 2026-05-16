# Example: First Research on AI Governance

A complete walkthrough of conducting your first ResearchCrew research.

## The Research Question

We want to understand: **What are the current approaches to AI governance and regulation in 2025?**

## Step 1: Set Up

Already installed ResearchCrew? Great. If not, see [Getting Started](../getting-started.md).

Ensure `.env` is configured:

```env
OPENROUTER_API_KEY=sk-your-key
OPENROUTER_MODEL_NAME=openai/gpt-4-turbo
EXA_API_KEY=your-exa-key
```

## Step 2: Create Research Topic

Create `input.md` in the project root:

```markdown
# Research Topic: AI Governance in 2025

Please research the current state of AI governance and regulation globally.

Focus on:
1. Major regulatory frameworks (EU AI Act, US approaches, etc.)
2. Current regulatory bodies and their mandates
3. Industry self-regulation initiatives
4. Emerging enforcement mechanisms
5. International cooperation efforts

Depth: Comprehensive overview with specific examples and timelines.
```

## Step 3: Run Initial Research

```bash
crewai run
```

Expected runtime: 5-15 minutes depending on LLM and search scope.

Output:

```
Starting ResearchCrew pipeline...

✓ Research Planner: Analyzed topic, identified research plan
✓ Web Crawler: Found 8 relevant sources about AI governance
✓ Content Extractor: Extracted 42 claims with confidence levels
✓ Synthesis Researcher: Synthesized findings into coherent themes
✓ Reporting Analyst: Generated publication-ready report

Output files created:
- report.md (main report)
- 20250516_143000_extraction.json (extracted claims)
- 20250516_143000_synthesis.md (synthesis findings)
```

## Step 4: Review Initial Report

Open `report.md`. You'll see something like:

```markdown
# AI Governance Research Report
*Generated: 2025-05-16*

## Executive Summary

[The AI governance landscape in 2025 is rapidly evolving](https://tech-news.com/ai-governance-2025), 
with [major regulatory frameworks being implemented globally](https://regulation-journal.com/ai-act).

## Major Regulatory Frameworks

### EU AI Act

[The EU AI Act became enforceable in 2024](https://eu-council.com/ai-act),
representing [the first comprehensive AI regulation framework](https://regulatory-update.com/eu-ai).

Key elements:
- [Mandatory impact assessments for high-risk AI systems](https://compliance-guide.com/eu-ai-requirements)
- [Transparency requirements for generative AI](https://tech-policy.com/transparency)
- [Penalties up to 6% of global revenue for violations](https://legal-analysis.com/eu-penalties)

### US Regulatory Approach

Unlike the EU, [the US is taking a sector-specific approach](https://white-house.com/ai-governance),
with [different agencies regulating AI in their domains](https://ftc.gov/ai-oversight).

- [FDA regulates AI in medical devices](https://fda.gov/ai-regulation)
- [NHTSA regulates autonomous vehicles](https://transportation.gov/av-standards)
- [FTC oversees AI in consumer protection](https://ftc.gov/ai-fairness)

## Industry Self-Regulation

[Many tech companies have adopted AI governance frameworks](https://industry-report.com/self-regulation), including:
- [OpenAI's GPT usage policies](https://openai.com/governance)
- [Google's AI Principles](https://google.com/ai-principles)
- [Meta's Responsible AI Initiative](https://meta.com/ai-responsibility)

However, [enforcement of self-regulation remains unclear](https://governance-analysis.com/self-regulation-gaps).

## Gaps in Current Governance

The report notes areas where data is insufficient:

**Insufficient data:** Actual enforcement rates and penalties 
imposed under new regulations. Early 2025 data is limited.

**Insufficient data:** Long-term effectiveness of self-regulation 
vs. formal government regulation. Comparative analysis is limited.

## Key Findings

1. [Global AI governance is moving from voluntary to mandatory](https://policy-brief.com/trend-2025)
2. [Regulatory approaches vary significantly by region](https://international-governance.com/comparison)
3. [Compliance is becoming expensive for smaller companies](https://startup-perspective.com/compliance-costs)
4. [Technical standards are still evolving](https://standards-organization.com/ai-standards)
```

## Step 5: Review What's Good & What's Missing

**Good points:**

- Well-organized by region and framework
- Multiple perspectives included
- Recent information (2024-2025)
- Explicit about gaps
- All claims are cited

**Gaps identified:**

- Limited on enforcement (mentioned as gap)
- Nothing on international cooperation (UN, G7, etc.)
- Lacked cost-benefit analysis for companies
- International enforcement mechanisms unclear

## Step 6: Provide Feedback for Iteration

Edit the end of `report.md` and add:

```markdown
## User Feedback - Round 2

### Please Explore More:

1. **International Cooperation** — I notice the report doesn't cover international 
   coordination efforts (UN, G7, bilateral agreements). Please research:
   - UN initiatives on AI governance
   - G7/G20 AI regulation coordination
   - Bilateral AI agreements between countries

2. **Implementation Costs** — How expensive is compliance with these regulations?
   - Cost for large companies vs. startups
   - Specific examples of compliance investments
   - ROI/payback period

3. **Enforcement Mechanisms** — The report notes enforcement is unclear:
   - What specific penalties have been imposed so far?
   - What are the investigation processes?
   - Case studies of violations and consequences

### Skip Further Research:

- General AI capability discussions (not governance-focused)
- Historical AI policy (pre-2024)

### Clarifications:

- The EU 6% penalty is based on global revenue. 
  What would this be for a $10B company? 
  Please provide calculation examples.
```

## Step 7: Run Iteration

```bash
crewai run
```

The crew will:

1. Remember previous research on regulations and frameworks
2. See your feedback about gaps (international, costs, enforcement)
3. Search specifically for those topics
4. Integrate new findings with prior research
5. Update `report.md`

Updated report now includes:

```markdown
# AI Governance Research Report (Updated)
*Generated: 2025-05-16 (Round 2)*

## [Previous sections unchanged - covering EU, US, industry self-regulation]

## International Cooperation

### UN Initiative

[The UN is developing a framework for global AI governance](https://un.org/ai-governance),
with [member states agreeing on principles for responsible AI](https://un-summit.org/ai-outcomes).

Key outcomes:
- [Commitment to transparency in AI development](https://un-resolution.org/ai-transparency)
- [Collaboration on AI safety research](https://un-program.org/ai-safety)

### G7 AI Governance Compact

[The G7 announced an AI governance framework in 2024](https://g7-summit.org/ai), 
featuring [shared principles for AI regulation](https://international-cooperation.com/g7-ai).

### Bilateral Agreements

[US-EU AI governance dialogues](https://us-eu-agreement.com/ai) established 
[frameworks for coordinated regulation](https://transatlantic-ai.org).

## Compliance Costs & Implementation

### Large Enterprises

[A McKinsey study estimated compliance costs](https://mckinsey.com/ai-compliance-2025):
- [$500K-$2M for initial compliance infrastructure](https://compliance-cost-report.com/enterprise)
- [Annual ongoing costs of $200-500K](https://governance-spending.com/enterprise)
- [For a $10B company, EU 6% penalty = $600M exposure](https://penalty-calculation.com)

### Startups

[Smaller companies face proportional challenges](https://startup-compliance.com/ai-2025):
- [$50-200K for compliance setup](https://early-stage-costs.com)
- [Potential barriers to market entry](https://startup-perspective.com/regulatory-burden)

## Enforcement & Penalties

### Recent Enforcement Actions

[The EU has begun investigations into AI systems](https://eu-enforcement.com/cases),
with [first investigations into ChatGPT's data practices](https://ai-investigation.com/gpt-4).

[Estimated penalties for violations range from 1-6% of global revenue](https://enforcement-guide.com/penalties).

### Investigation Processes

[The EU established a dedicated AI Office](https://eu-ai-office.com) to:
- [Investigate non-compliance](https://regulatory-process.com/investigation)
- [Assess impact assessments](https://compliance-verification.com)
- [Issue enforcement orders](https://eu-enforcement.com/process)

## Updated Key Findings

1. Global AI governance is coordinating through UN, G7, and bilateral channels
2. Compliance is expensive ($500K-$2M for enterprises)
3. Early enforcement has begun in the EU
4. Smaller companies face disproportionate compliance challenges
5. Standards continue to evolve
```

## Step 8: Review & Decide If More Iteration is Needed

The updated report now covers:

- International cooperation (UN, G7, bilateral)
- Implementation costs ($500K-$2M examples)
- Enforcement mechanics and penalties
- Impact on startups vs. enterprises

**Is it complete?** Probably good enough for most purposes. You could:

**Stop here if:**

- Research needs are met
- Quality is sufficient
- Time/budget constraints

**Iterate more if:**

- You need even deeper dive into specific countries
- You want policy recommendations
- You're writing a detailed compliance guide

## Step 9: Export & Use

Copy the report:

```bash
cp report.md AI_Governance_Research_2025_05_16.md
```

Now you can:

- Share with colleagues
- Include in presentations
- Cite in your own writing
- Archive for future reference
- Update with feedback if regulations change

## What Made This Research Effective

**Started with clear question** — "What are current approaches to AI governance?"

**Reviewed and validated** — Checked initial output for quality, gaps, and accuracy

**Provided specific feedback** — Identified gaps and guided crew to fill them

**Iterated once** — One round of feedback was sufficient to get comprehensive coverage

**Validated results** — Checked that new findings answered the gaps

**Used reliable sources** — All claims included citations you can verify

## Tips for Your First Research

1. **Start broad** — Let the crew explore the topic initially

2. **Review thoroughly** — Spend time reading and understanding the initial report

3. **Provide specific feedback** — Name topics, sections, or claims

4. **Iterate 1-2 times** — Most research reaches good quality after 2 rounds

5. **Validate key claims** — Click a few citations to verify they support the claim

6. **Know when to stop** — Diminishing returns after 3-4 iterations

## Next Steps

- **[Iterative Research](../usage/iterative-research.md)** — Learn more about multi-round workflows
- **[Human-in-the-Loop](../features/human-in-loop.md)** — How to guide research effectively
- **[Reliability Features](../features/reliability.md)** — Understanding quality checks

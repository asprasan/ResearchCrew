# Example: Multi-Day Workflow with Feedback

A realistic scenario of conducting research over multiple days with active guidance.

## The Research Challenge

You're writing a **whitepaper on AI adoption barriers in enterprise software development teams**. This is complex and requires:

- Multiple perspectives (technical, organizational, financial)
- Deep dives into specific challenges
- Practical solutions and workarounds
- Case studies and real-world examples

This typically requires 3-4 research iterations over several days.

## Day 1: Initial Exploration

### Morning - Set Research Direction

Create `input.md`:

```markdown
# Research Topic: AI Adoption Barriers in Software Development

Research the current barriers preventing widespread AI adoption in enterprise 
software development teams.

Key areas:
1. Technical barriers (integration, reliability, model quality)
2. Organizational barriers (training, culture, workflow changes)
3. Financial barriers (cost, ROI, resource allocation)
4. Security and compliance barriers
5. Skills and expertise gaps

Goal: Comprehensive overview to inform whitepaper strategy.
```

### Midday - Run Initial Research

```bash
crewai run
```

Runtime: ~10 minutes.

---

## Day 2: First Iteration - Enterprise Perspective

### Morning - Review & Plan

Add formal feedback to `outputs/<yyyymmdd>.md`:

```markdown
## User Feedback

### Areas to Explore More:

1. **Enterprise Security Requirements** — Most sources discuss generic security.
   What are specific enterprise security requirements that conflict with AI adoption?
   - Data governance and compliance (SOC 2, HIPAA, etc.)
   - Model training data requirements (cannot use external data)
   - Audit trails and explainability requirements
   - Specific security concerns vs. theoretical

2. **Real Case Studies** — Include specific companies:
   - Which enterprises successfully adopted AI?
   - What barriers did they overcome?
   - What was their timeline and investment?
   - What failed? What worked?

3. **Solutions Being Used** — Don't just identify barriers.
   How are teams actually working around them?
   - Custom fine-tuned models (vs. using external APIs)
   - On-premises deployments
   - Hybrid approaches
   - Custom tooling and infrastructure

### Areas to De-Prioritize:

- General AI capability descriptions (focus on barriers/adoption)
- Theoretical future scenarios (focus on current 2025 state)
- AI hype (focus on pragmatic, realistic assessment)

### Refinement for Tone:

Please adopt a pragmatic tone. This is for enterprise architects deciding whether to invest.
Focus on: realistic obstacles, proven workarounds, actual timelines.
```

### Midday - Run Iteration

```bash
crewai run
```

The crew:

1. Remembers Day 1 research
2. Sees your feedback about enterprise security, case studies, solutions
3. Searches for: "enterprise AI security requirements", "case studies AI adoption", etc.
4. Integrates findings with prior research
5. Generates new report `outputs/<yyyymmdd>.md`

## Day 3: Second Iteration - Developer Voice

### Feedback

You realized the report lacks **actual developer perspective**. They experience barriers differently than executives. Add feedback:

```md
## User Feedback

### Critical Gap: Developer Perspective

The report discusses barriers but doesn't include developer voices.
What do developers actually say about AI adoption?

Please research:
1. Developer surveys and sentiment on AI tools in their workflow
2. Common developer complaints/concerns
3. What developers find valuable vs. frustrating
4. Willingness to adopt (or resistance) from dev teams
5. Training and onboarding challenges from practitioner perspective

This is essential for a whitepaper aimed at decision-makers.
Decision-makers need to understand both exec barriers AND dev barriers.

### Prioritize:

- Real developer quotes and perspectives (if available)
- Developer community discussions (Stack Overflow, Reddit for discussion not Q&A, GitHub discussions)
- Developer conference talks/panels on AI adoption
- Practitioner blogs and experiences

### Supplementary:

If available, research:
- ROI from developer productivity perspective (not just financial)
- Time savings per developer
- Actual adoption % among developers using the tools
```

**Status after Day 3:**

- Technical barriers (enterprise security, compliance)
- Real case studies and examples
- Practical solutions being used
- Developer perspective and sentiment
- Training and adoption guidance

Report is now comprehensive enough for a whitepaper.

---

## Day 4: Final Polish

You review the comprehensive report. It's good, but a few final tweaks would improve it:

```markdown
## User Feedback

### Minor Additions:

1. **Timeline Expectations** — Summarize typical adoption timelines:
   - Planning phase: 3-6 months
   - Infrastructure/tooling: 3-6 months
   - Rollout: 6-12 months
   - Full adoption: 12-24 months

2. **ROI Calculation** — Help executives justify investment:
   - Cost: X
   - Developer productivity gains: Y
   - Timeline to payback: Z

3. **Decision Checklist** — For executives reading this:
   - Questions to ask before investing
   - Red flags to watch for
   - Success criteria

These additions would make this whitepaper-ready.
```

### Run Final Iteration

```bash
crewai run
```

Final report now includes executive summary, decision framework, and timelines.

---

## Key Learnings from This Multi-Day Workflow

### Iteration Pattern

1. **Initial research** — Get broad coverage
2. **First iteration** — Fill enterprise-specific gaps
3. **Second iteration** — Add practitioner perspective
4. **Final iteration** — Polish and make decision-ready

### Feedback Progression

- Day 1: Identifying gaps
- Day 2: Enterprise perspective gaps
- Day 3: Missing developer voice
- Day 4: Polish for executive consumption

### Memory & Context

The crew remembered:

- Initial research on barriers
- Day 2 feedback about enterprise security and case studies
- Day 3 shift to developer perspective
- All sources and findings from prior days

No information was lost. Each iteration built on prior work.

### Time Investment

Total time: ~2 hours of active review + ~30 minutes of feedback writing
Crew runtime: ~40 minutes total (split across 4 runs)

Result: Comprehensive, well-researched report suitable for publication.

---

## Best Practices Demonstrated

- **Planning phase** — Thought about research direction before running

- **Incremental feedback** — Provided feedback day-by-day, not all at once

- **Specific guidance** — Named topics, provided context for why

- **Iterative refinement** — 4 iterations brought report to polished state

- **Using memory** — Crew built on prior research without re-doing work

- **Quality validation** — Reviewed each round for accuracy and completeness

- **Knowing when to stop** — After 4 rounds, diminishing returns set in

## Next Steps

- **[Iterative Research](../usage/iterative-research.md)** — Detailed guide to multi-round workflow
- **[Human-in-the-Loop](../features/human-in-loop.md)** — How to guide research effectively
- **[Configuration](../usage/configuration.md)** — Optimize for faster runs if needed

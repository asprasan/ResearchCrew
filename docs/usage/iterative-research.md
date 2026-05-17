# Iterative Research: Human-Guided Exploration

The power of ResearchCrew is in iteration. After each round, you review findings and actively steer the next research direction.

## The Iterative Loop

```txt
Round 1: Initial Research
    ↓
Review findings
    ↓
Identify gaps and areas to explore
    ↓
Round 2: Guided Research (with feedback)
    ↓
Review refined findings
    ↓
Request deeper analysis or new angles
    ↓
Round 3+: Continue iterating
```

## Step-by-Step Example

### Round 1: Initial Exploration

Create `input.md`:

```markdown
# Research Topic: The Future of Remote Work

Research the future of remote work post-2025. Include current trends, 
company policies, and predictions from industry experts.
```

Run:

```bash
crewai run
```

You get `<yyyymmdd>.md` with initial findings on remote work trends.

### Round 2: Provide Feedback & New Direction

After reviewing `<yyyymmdd>.md`, add feedback at the end:

```markdown
## User Feedback

Good coverage on company policies and trends. Now explore:

1. **Mental health impact** — Research psychological effects of remote work 
   (isolation, burnout, work-life balance)

2. **Hybrid model adoption** — Focus on companies successfully implementing 
   hybrid (not full remote) models

3. **Tools & infrastructure** — Deep dive into remote work tools and technologies

Please de-prioritize:
- General history of remote work (already covered)
- COVID-era temporary remote mandates (focus on permanent structures)
```

Run again:

```bash
crewai run
```

The crew:

- Remembers your previous research
- Sees your feedback
- Explores the new topics you highlighted
- Skips areas you said to de-prioritize
- Integrates findings from both rounds

You get an updated `<yyyymmdd>.md` with deeper analysis on your chosen angles.

### Round 3: Refine Further

Review the updated report. You notice:

- Mental health section is strong
- Hybrid model section needs more company case studies
- Tools section could include budget considerations

Add new feedback:

```markdown
## User Feedback

Excellent analysis on mental health. The hybrid model section is good but needs:
- Real case studies (which companies, what results)
- Employee satisfaction metrics
- Implementation challenges and solutions

For tools section, add:
- Cost comparisons between platforms
- SMB vs Enterprise tool choices
- Security and compliance considerations

New area to explore:
- How remote work is affecting real estate and office spaces
```

Run again:

```bash
crewai run
```

Continue until the research meets your needs.

## How the Crew Remembers

ResearchCrew uses **LanceDB** to persist memory across runs:

**What it remembers:**

- Previous research outputs
- Your input topic
- Extracted claims and sources
- URLs already crawled

**What it learns:**

- Your feedback patterns (what you want deeper on)
- Topics you want to skip
- The full context of prior investigation

**What it avoids:**

- Re-crawling already-researched URLs
- Repeating topics you've marked as complete
- Redundant searches

This means each iteration builds on prior work rather than starting fresh.

## Feedback Format

### Types of Feedback You Can Provide

**1. Explore deeper:**

```markdown
## User Feedback

The AI ethics section needs more depth:
- Current regulatory approaches (EU, US, etc.)
- Industry self-regulation vs government mandates
- Specific AI governance frameworks
```

**2. New topic area:**

```markdown
## User Feedback

Also research:
- Supply chain risks of outsourced AI
- Labor implications of AI automation
```

**3. De-prioritize topics:**

```markdown
## User Feedback

Good coverage on: history of AI

Skip further research on:
- Ancient history of computing
- Academic theoretical frameworks (unless directly relevant)
```

**4. Fix inaccuracies:**

```markdown
## User Feedback

The report claims "AI adoption is 50% complete" but this seems high. 
Please verify this with recent enterprise adoption surveys.

Also, the section on "AI healthcare applications" missed regulatory barriers.
```

**5. Change focus:**

```markdown
## User Feedback

The report is too academic. Focus more on:
- Practical use cases
- Real-world adoption barriers
- Implementation timelines

De-prioritize:
- Theoretical frameworks
- Historical background
```

### Feedback Best Practices

**Good feedback:**

- Specific (name the topic or section)
- Action-oriented (what to explore)
- Clear scope (what to skip)

**Vague feedback:**

- "Make it better"
- "More research"
- "I didn't like the AI section"

Better: "The AI section focuses on hype. Please research actual production deployments, success rates, and lessons learned from real implementations."

## Multi-Day Research

ResearchCrew remembers context across sessions:

**Day 1:**

```bash
crewai run  # Initial research
```

Review, provide feedback.

**Day 2:**

```bash
crewai run  # Iteration continues from prior context
```

The crew has full history from Day 1, so it knows what was researched and what feedback you gave.

You can distribute feedback and runs across days without losing context.

## When Iteration Helps Most

**Use iterative research when:**

- Topic is complex and requires multiple angles
- You want to steer direction based on findings
- Quality is more important than speed
- You're building a comprehensive report

**Use single-round when:**

- Simple, focused questions ("What is X?")
- You just need quick facts
- Topic doesn't require refinement

## Optimization Tips

### Efficient Iterations

Each iteration is a new full pipeline run. To speed things up:

1. **Batch feedback** — Collect multiple feedback items before next run, rather than running after each small note

2. **Specific topics** — Name specific sections/topics to explore, so the crew doesn't re-research completed areas

3. **Quality over quantity** — 2-3 focused iterations produce better results than 10 scattered ones

### Iteration Limit

A practical approach:

- **Round 1:** Initial exploration (comprehensive)
- **Round 2:** Address major gaps (targeted)
- **Round 3:** Polish and verify (refinement)
- **Round 4+:** Diminishing returns (fine-tuning)

Most research reaches diminishing returns after 3-4 rounds.

## Exporting & Sharing

After you're satisfied with your research:

```bash
cp report.md my_research_2025_05_16.md
```

The report includes full citations, so others can:

- Read your findings
- Verify sources by clicking links
- Trace claims back to original sources

## Next Steps

- **[Configuration](configuration.md)** — Optimize LLM choices and performance
- **[Examples](../examples/index.md)** — See full multi-round workflow examples
- **[Architecture](../architecture.md)** — Understand how feedback is incorporated

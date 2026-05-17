# Basic Workflow

Conduct a single-round research investigation.

## Overview

A basic research workflow is a single end-to-end pipeline run:

1. **Provide topic** → Create `inputs/input.md` with research question
2. **Run crew** → `crewai run`
3. **Get report** → Read `outputs/<yyyymmdd>.md` with citations

This is ideal for one-off research tasks or exploring a topic for the first time.

## Step-by-Step Example

### 1. Create Your Research Topic

Create `input.md` in the project root:

```md
# Research Topic: Quantum Computing in 2025

Research the current state of quantum computing in 2025. Include:
- Recent breakthroughs and milestones
- Current limitations and challenges
- Commercial applications and timelines
- Leading companies and organizations
```

### 2. Run the Crew

```bash
crewai run
```

You'll see progress output:

```
Starting crew execution...
✓ Research Planner: Created research plan
✓ Web Crawler: Found 12 relevant sources
✓ Content Extractor: Extracted 45 claims
✓ Synthesis Researcher: Synthesized findings
✓ Reporting Analyst: Generated report

Output files created:
- outputs/<yyyymmdd>.md (final report)
```

### 3. Review the Output

Open `outputs/<yyyymmdd>.md`:

```markdown
# Research Report: Quantum Computing in 2025

## Executive Summary

Quantum computing has reached a significant inflection point in 2025, with 
[multiple companies reporting quantum advantage in specific applications](https://...).

## Current Breakthroughs

### Error Correction

[IBM announced a breakthrough in error correction](https://...), reducing error rates 
by 50% compared to 2024. [Google's Willow chip demonstrated 10-qubit error correction](https://...).

### Commercial Applications

[Financial institutions are testing quantum algorithms for portfolio optimization](https://...),
with [early pilots showing 30% performance improvements](https://...).

## Current Limitations

However, [quantum computers still require extreme cooling to near absolute zero](https://...),
making widespread deployment challenging. [Estimated timeline for practical quantum advantage: 3-5 years](https://...).

## Leading Organizations

- [IBM Quantum](https://...)
- [Google Quantum AI](https://...)
- [IonQ](https://...)
- [Rigetti Computing](https://...)
```

Every claim includes a citation [text](URL) you can click.

## Output Files

### [yyyymmdd].md

Your final research output. This is what you share with others.

**Format:**

- Markdown with [claim](URL) citations
- Organized by subtopic
- Notes "Insufficient data" where gaps exist
- Publication-ready quality
<!-- 
### [timestamp]_extraction.json

Intermediate output: raw extracted claims.

**Format:**

```json
{
  "extraction_metadata": {
    "timestamp": "2025-05-16T14:30:00Z",
    "total_urls_processed": 12,
    "total_claims_extracted": 45
  },
  "extracted_claims": [
    {
      "url": "https://...",
      "title": "Page title",
      "claims": [
        {
          "claim": "AI systems...",
          "quote": "Verbatim quote from page",
          "confidence": "HIGH",
          "section": "What section of page"
        }
      ]
    }
  ]
}
```

Use this for validation or further analysis.

### [timestamp]_synthesis.md

Intermediate output: synthesized findings before final reporting.

**Format:**

- Grouped by topic
- Includes pattern identification
- Notes contradictions between sources
- Internal reference URLs (not final citations)

Use this to validate synthesis logic or debug quality issues. -->

## Common Patterns

### Shallow First Pass

If you want a quick overview:

```markdown
# Quick Overview: Machine Learning Trends

Provide a 5-minute overview of machine learning trends in 2025, 
focusing on recent news and headlines rather than deep analysis.
```

Run normally. The report will be shorter and faster.

### Deep Dive on One Topic

```markdown
# Research Topic: LLM Safety and Alignment

Focus deeply on AI safety, alignment research, and current approaches to making large language models safer.
Include perspectives from leading researchers and organizations.
```

The crew will produce a more detailed report.

### Comparison Research

```markdown
# Comparison: Vue vs React in 2025

Compare Vue.js and React frameworks. Include:
- Performance characteristics
- Developer experience and learning curve
- Ecosystem and library support
- Production use cases and adoption
- Strengths and weaknesses of each
```

The crew will synthesize comparisons across sources.

## When to Use Single-Round Research

- **Good for:**

  - Initial topic exploration
  - Answering a specific question
  - Quick competitive analysis
  - First-time research on a topic

- **Not ideal for:**

  - Complex, multi-faceted topics (use iterative research)
  - Topics requiring human guidance (use human-in-the-loop)
  - Research where you want to steer direction (see [Iterative Research](iterative-research.md))

## Next Steps

- **[Iterative Research](iterative-research.md)** — Learn how to iterate with feedback
- **[Configuration](configuration.md)** — Customize LLM, tools, and outputs
- **[Architecture](../architecture.md)** — Understand the 5-agent pipeline

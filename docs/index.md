# ResearchCrew Documentation

Welcome to ResearchCrew — an AI-powered research system built for **integrity, guidance, and transparency**.

## What is ResearchCrew?

ResearchCrew is a multi-agent research automation platform that:

- **Conducts guided research** — Humans steer the investigation after each round, exploring specific topics in depth
- **Maintains citation integrity** — Every claim is traceable to a source URL; no hallucinations
- **Validates reliability** — Web crawler filters unreliable sources, and the pipeline includes checks at each stage
- **Remembers context** — Long-term memory avoids redundant searches and preserves research history

Unlike generic AI summarization tools, ResearchCrew treats research as an iterative, human-guided process where you actively steer the investigation and trust the output.

## Core Workflow

```md
1. User provides research topic
        ↓
2. Crew runs 5-stage pipeline
   (Planner → Crawler → Extractor → Synthesis → Reporter)
        ↓
3. User reviews report and findings
        ↓
4. User provides guidance (explore X deeper, ignore Y)
        ↓
5. Crew iterates with feedback context
        ↓
6. Refined, cited research output
```

## Key Features

### Human-in-the-Loop Research

After each iteration, you review the findings and actively guide the next round. The system learns your feedback and refines accordingly. This isn't a one-shot summarization—it's a collaborative investigation.

### Citation Integrity

Every claim in the final report is backed by a source URL. The crew extracts verbatim quotes from pages, preserves source context through synthesis, and outputs publication-ready citations.

### Multi-Stage Reliability

- **Web Crawler** applies quality filters (excludes Medium, Reddit, unreliable domains)
- **Content Extractor** records confidence levels for each claim
- **Synthesis** flags contradictions between sources
- **Reporter** notes "Insufficient data" where gaps exist

### Persistent Memory

The system uses LanceDB to store and learn from past research. This enables:

- Deduplication across runs (avoid re-crawling the same sources)
- Context preservation (remember what was already researched)
- Multi-day workflows (continue research across sessions)

## Get Started

- **[Quick Start](getting-started.md)** — 5-minute setup and first run
- **[Architecture](architecture.md)** — How the 5-agent pipeline works
- **[Usage Guides](usage/index.md)** — Single-round and multi-round research workflows
- **[Features in Depth](features/index.md)** — Human guidance, reliability, citations

## Examples

Want to see it in action?

- **[First Research Example](examples/first-research.md)** — Complete walkthrough of a research topic
- **[Multi-Day Workflow](examples/multi-day-workflow.md)** — How to iterate with feedback

## FAQ & Glossary

- **[FAQ](faq.md)** — Common questions and troubleshooting
- **[Glossary](glossary.md)** — Key terms explained

## Philosophy

**Research integrity over speed.** Every finding must be verifiable. Every source must be reliable. Every iteration should be guided by human judgment.

ResearchCrew is for researchers, analysts, and teams who need transparent, well-sourced research outputs.

# ResearchCrew

**AI-powered research with human guidance and citation integrity.**

ResearchCrew is a multi-agent research system that conducts thorough, well-sourced investigations with active human steering. Unlike generic AI summaries, every claim is traceable to a source URL, and every research round is guided by human feedback.

## What Makes ResearchCrew Different

- **Human-Guided Research** — After each round, you review findings and steer the crew toward specific topics. The system learns your feedback and refines accordingly.

- **Citation Integrity** — Every claim includes direct source attribution. No hallucinations, no invented quotes. Full traceability from source to final report.

- **Reliability Filters** — The web crawler avoids unreliable sources, and multiple pipeline checks validate findings at each stage (extraction, synthesis, reporting).

- **Persistent Memory** — The crew remembers past research and feedback across multiple runs, avoiding redundant work and building context.

## Quick Start

### Prerequisites

- Python ≥3.10 < 3.14
- [UV](https://docs.astral.sh/uv/) package manager

### Setup (5 minutes)

1. **Install UV:**

   ```bash
   pip install uv
   ```

2. **Clone and install dependencies:**

   ```bash
   git clone <repo>
   cd researchcrew
   crewai install
   ```

3. **Configure environment:**

   ```bash
   cp .env.example .env
   # Edit .env with your LLM API keys
   ```

4. **Run your first research:**

   ```bash
   crewai run
   ```

   Output: `report.md` in the root folder with your research findings.

## How It Works

ResearchCrew executes a 5-stage research pipeline:

1. **Research Planner** — Analyzes your topic, identifies research gaps, creates search strategy
2. **Web Crawler** — Finds authoritative URLs using semantic search (EXASearch)
3. **Content Extractor** — Retrieves page content and extracts verifiable claims with confidence levels
4. **Synthesis Researcher** — Groups claims by theme, identifies patterns, flags contradictions
5. **Reporting Analyst** — Writes publication-ready markdown with [claim](URL) citations

## The Human-in-the-Loop Workflow

```md
Research Topic
    ↓
[Crew runs 5-stage pipeline]
    ↓
Review Report + Findings
    ↓
Provide Feedback (explore topic X deeper, ignore topic Y, etc.)
    ↓
[Crew iterates with feedback context]
    ↓
Refined Report
    ↓
Provide Feedback (explore topic X deeper, ignore topic Y, etc.)
    ↓
[Crew iterates with feedback context]
    ↓
  ...
```

Each iteration refines the research based on your guidance. The crew remembers prior findings to avoid redundant searching.

## Configuration

**Environment variables** (`.env` file):

- `OPENROUTER_MODEL_NAME` — LLM to use (e.g., `gemini-3-flash`, `gpt-4o-mini`, etc)
- `OPENROUTER_API_KEY` — Your API key
- Other provider-specific keys as needed

See `.env.example` for full configuration.

## Learn More

- **[Getting Started Guide](docs/getting-started.md)** — Detailed setup and first run
- **[Architecture & Design](docs/architecture.md)** — How the 5-agent pipeline works
- **[Usage Guide](docs/usage/)** — Single-round and multi-round workflows
- **[Features](docs/features/)** — Human-in-loop workflow, reliability checks, citations
- **[Examples](docs/examples/)** — Complete research walkthroughs
- **[FAQ](docs/faq.md)** — Common questions and troubleshooting

## Project Philosophy

**Research integrity over speed.** Every finding must be verifiable. Every source must be reliable. Every iteration should be guided by human judgment.

This crew is built for researchers, analysts, and teams who need thorough, transparent, well-sourced research outputs.

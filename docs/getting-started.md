# Getting Started

Get ResearchCrew running in 5 minutes and conduct your first research.

## Prerequisites

- **Python 3.10+** (< 3.14)
- **UV** package manager
- **API Keys** for your LLM provider (OpenRouter, OpenAI, Anthropic, etc.)

## Installation

### 1. Install UV

```bash
pip install uv
```

UV is a fast, reliable Python package manager. If you prefer pip, that works too.

### 2. Clone and Install Dependencies

```bash
git clone https://github.com/yourusername/researchcrew.git
cd researchcrew
crewai install
```

This installs CrewAI and all dependencies listed in `pyproject.toml`.

### 3. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and add your API keys. Example:

```env
OPENROUTER_API_KEY=sk-your-key-here
OPENROUTER_MODEL_NAME=openouter/openai/gpt-4o-mini
```

**Which LLM should I use?**

- **Fast research:** Use Haiku or GPT-4o-mini (cheaper, faster)
- **Accurate research:** Use GPT-4, Claude 3 Opus (more reliable citations)

See [Configuration](usage/configuration.md) for more options.

### 4. Run Your First Research

```bash
crewai run
```

This runs the crew with the default input. You'll see:

```bash
✓ Research Planner completed
✓ Web Crawler completed
✓ Content Extractor completed
✓ Synthesis Researcher completed
✓ Reporting Analyst completed

Report saved to: outputs/<yyyymmdd>.md # in the format yyyymmdd.md
```

Open `<yyyymmdd>.md` to see your research findings with citations!

## File Structure

After running, you'll see these output files:

```
researchcrew/
├── inputs/input.md
└── outputs/<yyyymmdd>.md
```

## Provide Your First Research Topic

Create `input.md` in the root folder:

```markdown
# Research Topic: The Future of AI in Healthcare

Research what are the most significant developments in AI-assisted medical diagnosis in 2024-2025. 
Include emerging trends, specific tools, and expert perspectives.
```

Then run:

```bash
crewai run
```

The crew will:

1. Plan the research strategy
2. Search for authoritative sources
3. Extract verified claims with sources
4. Synthesize findings into coherent insights
5. Generate a cited report

## Iterative Research (Next Round)

After reviewing `<yyyymmdd>.md`, add your feedback to the end of the report:

```markdown
## User Feedback

Please explore more on:
- Real-world implementation challenges in hospitals
- Cost-benefit analysis of AI diagnostic tools

Skip further research on:
- Historical background of AI (already covered)
```

Then run again:

```bash
crewai run
```

The crew will see your feedback, remember previous research, and iterate accordingly.
The next report will be saved as `outputs/<yyyymmdd>.md`.

## Next Steps

- **[Architecture](architecture.md)** — Understand the 5-agent pipeline
- **[Usage Guide](usage/README.md)** — Single-round and multi-round workflows
- **[Features](features/README.md)** — Learn about reliability checks and citations
- **[Examples](examples/README.md)** — See complete research walkthroughs

## Troubleshooting

**"ModuleNotFoundError: No module named 'crewai'"**

Reinstall dependencies:

```bash
crewai install
```

**"API Key is invalid"**

Check your `.env` file and verify your API key is correct for your chosen provider.

**"No output directory found"**

Create an `output/` folder in the root:

```bash
mkdir output
```

**"Crew seems stuck or running slowly"**

- Check your internet connection (web crawler needs it)
- Your LLM provider may be rate-limited; try again in a few minutes
- Check your API key quotas/credits

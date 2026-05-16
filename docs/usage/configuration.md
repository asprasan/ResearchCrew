# Configuration

Customize LLMs, tools, memory, and output behavior.

## Environment Variables

All configuration is managed via `.env` file (copy from `.env.example`).

### Core Configuration

```env
# LLM Selection (required)
OPENROUTER_API_KEY=sk-your-api-key
OPENROUTER_MODEL_NAME=openai/gpt-4-turbo

# Web Search (required)
EXA_API_KEY=your-exa-api-key

# Optional: Embeddings for memory
GOOGLE_API_KEY=your-google-api-key  # For Google Gemini embeddings
```

## LLM Selection

Choose your LLM based on quality vs. cost tradeoff.

### Fast Research (Cost-Optimized)

```env
OPENROUTER_MODEL_NAME=openai/gpt-3.5-turbo
```

- **Speed:** Fast pipeline execution
- **Cost:** Lowest ($0.50-1.00 per run)
- **Quality:** Good for initial exploration, may have more hallucinations
- **Best for:** Quick research, exploratory passes

### Balanced Research

```env
OPENROUTER_MODEL_NAME=openai/gpt-4-turbo
```

- **Speed:** Moderate
- **Cost:** Medium ($2-5 per run)
- **Quality:** Reliable, good citation accuracy
- **Best for:** Most production research

### High-Accuracy Research

```env
OPENROUTER_MODEL_NAME=anthropic/claude-3-opus
```

- **Speed:** Slower
- **Cost:** Higher ($5-10 per run)
- **Quality:** Excellent, minimal hallucinations
- **Best for:** Critical research, high-stakes decisions

### Cutting-Edge Models

```env
OPENROUTER_MODEL_NAME=openai/gpt-4o  # Latest GPT-4 Omni
OPENROUTER_MODEL_NAME=anthropic/claude-3.5-sonnet  # Latest Claude
```

- **Speed:** Varies
- **Cost:** Varies
- **Quality:** State-of-the-art
- **Best for:** Maximum quality requirements

**Find more models:** [OpenRouter models list](https://openrouter.ai/models)

## Memory Configuration

Memory is handled automatically, but you can customize:

### Enable/Disable Memory

In `crew.py`, modify the Crew initialization:

```python
@crew
def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        memory=True,              # Enable long-term memory
        verbose=True,
        embedder={               # Embeddings for memory
            "provider": "google",
            "config": {"model": "models/embedding-001"}
        }
    )
```

**Memory stores:**

- Prior research outputs
- Extracted claims and URLs
- Deduplication history

**Memory benefits:**

- Avoids re-crawling same sources
- Provides context for iterative research
- Improves subsequent run quality

### Memory Database

Memory uses LanceDB (local vector database). Data is stored in:

```
.crew_cache/
├── lancedb/          # Vector store
└── crew_state/       # Agent state
```

No external database needed.

## Web Search Configuration

ResearchCrew uses **EXASearch** for semantic web search.

### Enable Quality Filters

In `tools/ai_tools.py`, quality filters are already enabled:

```python
# Excluded domains (unreliable sources)
EXCLUDED_DOMAINS = [
    "medium.com",
    "reddit.com",
    "stackoverflow.com",  # For research, not coding Q&A
    "twitter.com",
    "linkedin.com",
    "youtube.com",
]
```

Modify this list to add/remove excluded domains.

### Search Results

By default, web crawler returns 3-5 URLs per search query. To customize:

In `tasks.yaml`, modify the web crawler task description:

```yaml
web_crawler_task:
  description: |
    Find 3-5 high-quality URLs using semantic search.
    (Change this number as needed)
  # ...
```

## Output Configuration

### Report Location

By default, reports are saved to:

```
researchcrew/
├── report.md              # Final report
├── [timestamp]_extraction.json
└── [timestamp]_synthesis.md
```

To change output directory, modify in `main.py`:

```python
OUTPUT_DIR = "my_research_output"  # Change this path
```

### Report Format

Reports are generated in markdown. The format is fixed (publication-ready), but you can customize via task descriptions in `tasks.yaml`.

### Timestamp Format

Intermediate files use `YYYYMMDD_HHmmss` format:

```
20250516_143000_extraction.json
20250516_143000_synthesis.md
```

## Agent Customization

All agent behavior is defined in `config/agents.yaml` and `config/tasks.yaml`.

### Modify Agent Instructions

Edit `config/agents.yaml`:

```yaml
research_planner:
  role: Research Planner
  goal: Create comprehensive research plans    # Change goal
  backstory: You are an expert research strategist...  # Change backstory
```

### Modify Task Instructions

Edit `config/tasks.yaml`:

```yaml
research_planner_task:
  description: |
    Create a detailed research plan for: {{ topic }}
    
    Consider: (add custom considerations here)
    - Existing research
    - Knowledge gaps
    - Search strategy
  expected_output: |
    Structured research plan with:
    - Summary of prior research
    - Identified gaps
    - 2-3 search queries (customize this)
  agent: research_planner
```

## Performance Tuning

### Faster Runs

1. **Use faster LLM:**

   ```env
   OPENROUTER_MODEL_NAME=openai/gpt-3.5-turbo
   ```

2. **Reduce search scope** (in tasks.yaml):

   ```yaml
   web_crawler_task:
     description: |
       Find 2-3 high-quality URLs per search query (reduced from 5)
   ```

3. **Skip intermediate files** — Disable synthesis output if not needed

### Better Quality

1. **Use better LLM:**

   ```env
   OPENROUTER_MODEL_NAME=anthropic/claude-3-opus
   ```

2. **Increase search depth** — Find more URLs per query

3. **Use iterative refinement** — Multiple rounds with feedback

## Debugging Configuration

### Verbose Output

Enable detailed logging in `crew.py`:

```python
@crew
def crew(self) -> Crew:
    return Crew(
        # ...
        verbose=True,  # Shows agent thinking and reasoning
    )
```

### Check .env

Verify your `.env` has required keys:

```bash
echo $OPENROUTER_API_KEY
echo $EXA_API_KEY
```

### Test API Keys

```bash
python -c "import os; print(os.getenv('OPENROUTER_API_KEY'))"
```

## Common Configuration Issues

- **"API key is invalid"**

  - Verify `.env` file exists and is readable
  - Check API key format (starts with `sk-`)
  - Verify key is for correct provider

- **"Import error: No module named 'crewai'"**

  - Reinstall: `crewai install`
  - Or: `pip install crewai`

- **"LanceDB connection failed"**

  - Ensure `.crew_cache/` directory exists
  - Check disk space
  - Verify write permissions

- **"Rate limited by API"**

  - Too many requests too quickly
  - Add delays between runs
  - Check your API quota/credits

## Best Practices

- **Do:**

  - Start with GPT-3.5-turbo (cheaper initial testing)
  - Switch to Claude 3 Opus for production research
  - Use iterative feedback for complex topics
  - Save `.env` in `.gitignore` (don't commit API keys!)

- **Don't:**

  - Use free/unknown LLM APIs (quality/reliability unknown)
  - Keep API keys in code or version control
  - Run unlimited research runs without monitoring costs
  - Disable memory for multi-round research

## Next Steps

- **[Usage Guide](basic-workflow.md)** — Single and multi-round workflows
- **[Examples](../examples/)** — See real research examples

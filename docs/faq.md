# FAQ

Frequently asked questions about ResearchCrew.

## Getting Started

**Q: How long does research take?**

A: A single research run typically takes 5-15 minutes depending on:

- Number of search queries (planner decides)
- LLM model speed (GPT-3.5 ~5min, GPT-4 ~10min, Claude ~12min)
- Number of sources crawled (typically 3-5 per query)
- API latency and rate limiting

Each run is independent, so you can run multiple times without waiting.

**Q: What LLM should I use?**

A:

- **For exploration:** Use GPT-3.5-turbo (fast, cheap)
- **For production:** Use GPT-4-turbo or Claude 3 Opus (better quality, cost more)
- **For best quality:** Use Claude 3 Opus (most reliable citations)

Start cheap, upgrade if quality isn't sufficient. See [Configuration](usage/configuration.md).

**Q: Can I run this locally?**

A: Yes, ResearchCrew runs locally on your machine. You only need:

- Python 3.10+
- API keys for LLM and search (obtained from providers)
- Internet connection for web search

No data is stored on external servers except API calls to LLM/search providers.

**Q: Do I need GPU/special hardware?**

A: No. ResearchCrew runs on CPU. It's orchestration + API calls, not model execution.

**Q: How much does it cost to run?**

A: Costs depend on LLM choice:

- **GPT-3.5:** $0.50-$1 per run
- **GPT-4:** $2-5 per run
- **Claude 3 Opus:** $5-10 per run

Plus EXASearch costs (~$0.01-0.05 per search query).

For iterative research with 3-4 runs: $5-30 total per research topic.

---

## Usage & Workflow

**Q: How do I know when to stop iterating?**

A: Stop when:

- You can answer your original research question
- Major gaps are filled
- Quality matches your needs
- Each new iteration adds little new information

Typical sweet spot: 2-4 iterations. After that, diminishing returns.

**Q: Can I use ResearchCrew for real-time research (breaking news)?**

A: ResearchCrew works best for topics with established sources and content. For breaking news:

- May take 12-24+ hours for sources to be published
- May not have enough sources for robust research
- Works once news has had time to be analyzed and covered

For immediate information, ResearchCrew isn't ideal. It's better for research that's a few hours to days old.

**Q: Can I combine research from multiple ResearchCrew runs?**

A: Yes. You can manually:

1. Run research on Topic A
2. Run research on Topic B
3. Manually combine reports
4. Run research iteration asking crew to synthesize both

Or, ask in a single research topic:

```markdown
# Research Topic: Comparison of Topic A vs Topic B

Please research both topics and provide comparative analysis.
```

The crew will handle both in one run.

**Q: What if the crew hallucinated a claim?**

A:

1. Click the citation link — verify it actually supports the claim
2. If wrong, provide feedback:

   ```markdown
   ## User Feedback
   
   The report claims "X" with citation [source]. 
   I read the source and it actually says "Y", not "X".
   Please verify and correct.
   ```

3. Run again — crew will re-verify the citation

This is why human review is essential.

**Q: Can I provide feedback mid-run?**

A: No. You need to wait for a run to complete, then provide feedback for the next run.

---

## Quality & Reliability

**Q: How reliable are the citations?**

A: ResearchCrew enforces:

- Every claim has a source URL
- Extracted using verbatim quotes (not paraphrases)
- Confidence scoring (HIGH/MEDIUM/LOW)
- Cross-source validation where possible

However:

- Sources can be wrong (we filter for authority, not accuracy)
- Sources can be biased (credible ≠ objective)
- Always verify important claims yourself

**Q: What if a source is behind a paywall?**

A: ResearchCrew still fetches and extracts content from paywalled sites, but:

- You won't be able to click and verify yourself
- Consider subscribing to important sources
- Tell crew to focus on open sources if paywalls are problem

**Q: Can the crew access paywalled academic papers?**

A: No. The crew accesses public web content only. For academic papers:

- It can find and cite publicly available papers (arXiv, ResearchGate preprints)
- It cannot access paywalled journals (unless you have a subscription)

**Q: Why is my research shallow?**

A: Common causes:

1. Too few sources found by crawler (widen search, provide more specific queries)
2. LLM is too fast (use better model like GPT-4 or Claude)
3. Topic is niche (fewer sources available)
4. First iteration (provide feedback, iterate)

Solution: Iterate and provide specific feedback about depth desired.

**Q: Can I use ResearchCrew output in academic papers?**

A: Yes, with caveats:

- Every claim is cited, so you can cite original sources
- Methodology is transparent and reproducible
- You should verify citations yourself (as with any source)
- Disclose that AI-assisted research was used (academic honesty)

Best practice: Use ResearchCrew as starting research, verify all citations, cite original sources (not ResearchCrew).

**Q: How do I validate quality before using the research?**

A:

1. **Spot-check citations** — Click 3-5 random links, verify they support claims
2. **Check recency** — Are sources recent enough for your use case?
3. **Look for gaps** — Are there "Insufficient data" flags? Do they seem appropriate?
4. **Cross-reference** — Check if major claims appear in multiple sources
5. **Domain expertise** — Does it align with your knowledge? Flag discrepancies

---

## Technical

**Q: How do I change where output files are saved?**

A: Edit `src/researchcrew/main.py`:

```python
OUTPUT_DIR = "my_custom_path"  # Change this line
```

**Q: Can I exclude certain domains from search?**

A: Yes. Edit the excluded domains in `src/researchcrew/tools/ai_tools.py`:

```python
EXCLUDED_DOMAINS = [
    "medium.com",
    "reddit.com",
    # Add more domains here
]
```

**Q: Can I use a different LLM provider?**

A: Yes. OpenRouter supports multiple providers. Set in `.env`:

```env
OPENROUTER_MODEL_NAME=anthropic/claude-3-opus
OPENROUTER_MODEL_NAME=mistral/mistral-medium
# etc.
```

See [OpenRouter models](https://openrouter.ai/models) for all options.

**Q: How do I debug if something fails?**

A:

1. **Check `.env`** — Verify all required keys are present

   ```bash
   echo $OPENROUTER_API_KEY
   ```

2. **Enable verbose output** — Edit `crew.py`:

   ```python
   return Crew(..., verbose=True)
   ```

3. **Check internet connection** — Web search requires connectivity

4. **Try simpler research** — If it fails on complex topics, try simpler one to isolate issue

5. **Check API quotas** — Verify you have credits/quota with providers

**Q: Why are all claims being extracted with LOW confidence?**

A: Causes:

1. Sources are low-authority (get better sources or adjust crawler filters)
2. Claims are emerging/preliminary (expected for cutting-edge topics)
3. LLM is being conservative (try GPT-4 or Claude for less conservative scoring)

**Q: Can I run multiple research tasks in parallel?**

A: Not in the same project. But you can:

1. Run research in one project
2. While that runs, start different project with different `.env` copy
3. Run research there in parallel

Or run sequentially and don't wait for completion (you'll get results when done).

---

## Collaboration & Sharing

**Q: Can multiple people work on the same research topic?**

A: Yes:

1. Person A creates `input.md` and runs initial research
2. All reviewers examine `report.md`
3. All reviewers provide feedback
4. One person consolidates feedback (avoid duplicates)
5. Person B adds consolidated feedback and runs iteration
6. All reviewers examine updated report

See [Human-in-the-Loop](features/human-in-loop.md#collaboration-with-teams) for example.

**Q: Can I share the output with people who don't have ResearchCrew installed?**

A: Yes! Just share `report.md`. It's a regular markdown file with citations (clickable links). Anyone can read it.

They won't be able to iterate or re-run, but they can read and verify citations.

**Q: What license is ResearchCrew under?**

A: Check LICENSE file in repo. (User should specify — assuming Apache 2.0 or MIT is common for such projects)

---

## Advanced

**Q: Can I integrate ResearchCrew into my application?**

A: Yes. The crew is callable as Python:

```python
from researchcrew.crew import ResearchCrew

crew = ResearchCrew()
result = crew.kickoff(inputs={
    "core_task": "Your research question"
})
```

See docs for API details.

**Q: Can I customize agent behavior?**

A: Yes. Edit:

- `config/agents.yaml` — Agent roles, goals, backstory
- `config/tasks.yaml` — Task descriptions and expectations
- `src/researchcrew/crew.py` — Crew orchestration logic

See [Architecture](architecture.md) for details.

**Q: Can I add custom tools?**

A: Yes. The crew supports CrewAI tools. You can add:

- Custom search tools
- Data processing tools
- External API integrations

See CrewAI documentation for tool creation.

**Q: How do I reset memory/cache?**

A: To clear prior research history:

```bash
rm -rf .crew_cache/
```

This clears all stored research but also removes context from prior runs. Use with caution.

---

## Performance & Optimization

**Q: How can I make research faster?**

A:

1. Use faster LLM (GPT-3.5 instead of GPT-4)
2. Reduce search scope in tasks.yaml (fewer URLs per query)
3. Be specific in feedback (crew doesn't re-research completed topics)
4. Disable memory if not needed (won't help current run, but historical)

Trade-off: Speed vs. quality. Faster usually means less thorough.

**Q: How can I make research more thorough?**

A:

1. Use better LLM (GPT-4 or Claude 3 Opus)
2. Increase search scope (more URLs per query)
3. Provide detailed feedback (guide crew toward depth)
4. Iterate multiple times (each pass adds refinement)

Trade-off: Quality vs. speed and cost. More thorough takes longer and costs more.

**Q: How can I reduce costs?**

A:

1. Use cheaper LLM (GPT-3.5-turbo)
2. Reduce search queries in research plan (fewer topics to explore)
3. Iterate less (settle for "good enough" sooner)
4. Be specific in feedback (avoid re-researching)

---

## Troubleshooting

1. **Q: "API Key is invalid"**

   A:

   1. Check `.env` file exists: `ls .env`
   2. Verify key format: `cat .env | grep OPENROUTER_API_KEY`
   3. Verify key works: Try same key with curl
   4. Ensure no trailing spaces: Edit and save again

2. **Q: "Module not found: crewai"**

   A:

   ```bash
   crewai install
   ```

   Or:

   ```bash
   pip install crewai
   ```

3. **Q: "No such file or directory: .env"**

   A:

   ```bash
   cp .env.example .env
   # Then edit .env with your keys
   ```

4. **Q: "Rate limited by API"**

   A: Too many requests too quickly. Either:

   1. Wait a few minutes before running again
   2. Check your API quota/credits
   3. Use cheaper model (fewer API calls)

5. **Q: "Output directory doesn't exist"**

   A:

   ```bash
   mkdir output
   ```

ResearchCrew should create this automatically, but if not, create it manually.

---

## Not Listed Here?

Didn't find answer? Check:

- **[Getting Started](getting-started.md)** — Setup and first run
- **[Architecture](architecture.md)** — How it works
- **[Usage Guides](usage/index.md)** — Single-round and iterative workflows
- **[Features](features/index.md)** — Detailed feature documentation
- **[Examples](examples/index.md)** — Real research walkthroughs

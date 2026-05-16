# Architecture & Design

## The 5-Agent Pipeline

ResearchCrew executes research as a sequential pipeline of 5 specialized agents. Each agent handles a specific aspect of the research process.

### Pipeline Flow

```txt
Research Topic
    ↓
[1] Research Planner
    ├─ Analyzes the research topic
    ├─ Identifies gaps based on prior research
    └─ Generates 2-3 concrete search queries
    ↓
[2] Web Crawler
    ├─ Searches for authoritative URLs (EXASearch)
    ├─ Applies quality filters
    └─ Deduplicates against previously crawled content
    ↓
[3] Content Extractor
    ├─ Fetches full page content
    ├─ Extracts verifiable claims with quotes
    └─ Records confidence levels per claim
    ↓
[4] Synthesis Researcher
    ├─ Groups claims by theme/subtopic
    ├─ Identifies patterns and contradictions
    └─ Flags conflicting information
    ↓
[5] Reporting Analyst
    ├─ Writes narrative prose
    ├─ Integrates claims into coherent findings
    └─ Generates [claim](URL) citations
    ↓
Publication-Ready Report
```

## Each Agent's Role

### 1. Research Planner

**Input:** Research topic + previous research context (if iterating)

**What it does:**

- Analyzes what has already been researched (by reading prior outputs)
- Identifies gaps and new angles to explore
- Creates 2-3 concrete, specific search queries
- Considers user feedback if this is an iteration

**Output:** Structured research plan with search queries

**Example:**

```
Topic: AI in Healthcare
Prior research: Diagnostic tools, regulatory compliance
Gaps to explore: Implementation in rural hospitals, cost analysis, AI-human collaboration

Search queries:
1. "AI diagnostic tools implementation challenges rural hospitals 2024"
2. "Cost-benefit analysis AI medical imaging systems"
3. "Human-AI collaboration in clinical workflows"
```

### 2. Web Crawler

**Input:** Search queries from Research Planner

**What it does:**

- Uses EXASearch to semantically search for authoritative URLs
- Applies quality filters (excludes Medium, Reddit, low-signal domains)
- Deduplicates against previously crawled URLs (via memory)
- Ranks results by relevance and authority
- Returns 3-5 URLs per topic

**Output:** List of high-confidence URLs with relevance scores

**Reliability Features:**

- Source filtering (skips unreliable domains)
- Deduplication (avoids redundant crawling)
- Authority ranking

### 3. Content Extractor

**Input:** URLs from Web Crawler

**What it does:**

- Fetches the full page content
- Extracts specific claims and supporting quotes
- Records confidence levels: HIGH / MEDIUM / LOW
- Structures output as JSON with metadata

**Output:** JSON file with extracted claims

**Example:**

```json
{
  "url": "https://example.com/ai-healthcare",
  "claims": [
    {
      "claim": "AI diagnostic tools can achieve 95% accuracy in early cancer detection",
      "quote": "Our AI system achieved 95% accuracy...",
      "confidence": "HIGH",
      "source_context": "Published medical journal study"
    }
  ]
}
```

**Reliability Features:**

- Verbatim quotes (not paraphrases)
- Confidence scoring
- Source context preservation

### 4. Synthesis Researcher

**Input:** Extracted claims from Content Extractor

**What it does:**

- Groups claims by theme (e.g., diagnostic tools, implementation barriers, costs)
- Identifies patterns and trends across sources
- Flags contradictions between sources
- Notes areas where data is insufficient
- Preserves URL attribution for traceability

**Output:** Markdown document with synthesized findings

**Example:**

```markdown
## Diagnostic Accuracy

Multiple sources report 90-95% accuracy for AI tools in early detection:
- Study A: 95% accuracy in cancer detection (https://...)
- Study B: 92% accuracy in radiology (https://...)
- Study C: 88% accuracy in pathology (https://...)

Synthesis: Accuracy varies by domain and dataset, but generally 85-95%.
```

**Reliability Features:**

- Cross-source pattern identification
- Contradiction flagging
- Gap identification

### 5. Reporting Analyst

**Input:** Synthesized findings from Synthesis Researcher

**What it does:**

- Writes narrative prose integrating findings
- Creates direct citations using [claim](URL) format
- Preserves source context from synthesis
- Notes "Insufficient data" where gaps exist
- Ensures publication-ready markdown

**Output:** Final research report (report.md)

**Example:**

```markdown
## Current State of AI in Diagnostics

AI diagnostic tools have achieved significant accuracy in recent years. 
[Multiple studies report 90-95% accuracy in early cancer detection](https://...), 
with [pathology being slightly less accurate at 88%](https://...).

However, [implementation challenges remain in rural hospitals](https://...),
particularly around infrastructure and training requirements.
```

**Reliability Features:**

- Direct URL citations (every claim is traceable)
- No invented quotes or sources
- Explicit gap flagging

## Key Design Decisions

### Why Sequential Pipeline?

Each agent builds on the output of the previous agent. This allows for:

- **Specialization:** Each agent focuses on one aspect
- **Quality gates:** Poor outputs from one stage affect the next (visible)
- **Debugging:** Easy to isolate where quality issues arise
- **Transparency:** You can inspect intermediate outputs

### Why Human-in-the-Loop?

Research is iterative and guided. After each run:

- Human reviews findings for accuracy and completeness
- Human identifies gaps or misconceptions
- Human provides guidance for next research round
- System learns from feedback and refines

This prevents:

- Narrow or biased research (humans catch tunnel vision)
- Hallucinations (humans validate against domain knowledge)
- Wasted research (humans redirect effort)

### Why Citations First?

Every claim must be traceable to a source:

- **Anti-hallucination:** Forces facts to come from real sources
- **Credibility:** Readers can verify claims themselves
- **Accountability:** Clear lineage from source to report

This means:

- No invented quotes
- No made-up statistics
- No synthesis without source attribution

### Why Multi-Day Memory?

Research questions are complex and often require multiple rounds:

- **Context preservation:** Remember what was already researched
- **Deduplication:** Avoid re-crawling the same sources
- **Iteration:** Build on prior findings, not restart each time

The system uses LanceDB to store:

- Prior research outputs
- Extracted claims and sources
- Crawler history (to avoid redundant searches)

## LLM Configuration

All agents use a single LLM (configurable via `.env`):

- **Model:** Set `OPENROUTER_MODEL_NAME`
- **Provider:** OpenRouter supports most major LLM providers
- **Trade-off:** Faster models (Haiku) for speed; better models (GPT-4, Claude) for accuracy

Future versions may use different LLMs for different agents based on complexity.

## Reliability Pipeline Summary

```
Research Topic
    ↓
[Planning] Identify gaps and search strategy
    ↓
[Crawling] Quality-filtered source discovery
    ↓
[Extraction] Verbatim claim extraction with confidence
    ↓
[Synthesis] Cross-source pattern identification + contradiction flagging
    ↓
[Reporting] Direct URL citations, gap flagging
    ↓
Publication-Ready, Verified, Cited Report
```

Each stage includes checks to ensure reliability:

1. Source filtering (web crawler)
2. Confidence scoring (extractor)
3. Pattern & contradiction detection (synthesis)
4. Explicit gap identification (reporter)

The result is research output you can trust and cite.

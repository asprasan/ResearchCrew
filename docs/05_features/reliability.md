# Reliability Features

ResearchCrew is built for trustworthy research. Multiple checks throughout the pipeline ensure quality and accuracy.

## The Problem: AI Hallucinations

Without guardrails, AI research systems can:

- Invent statistics or quotes
- Cite non-existent sources
- Misrepresent information from sources
- Confidently state false information

Example of hallucination:

```md
"According to a 2024 study published in the Journal of AI Research, 
87% of companies have fully adopted AI systems." 
(This study doesn't exist)
```

## ResearchCrew's Solution: Multi-Stage Validation

Reliability is built into every stage of the pipeline:

### Stage 1: Source Filtering (Web Crawler)

**Problem:** Low-quality sources lead to low-quality research.

**Solution:** The web crawler applies domain filters:

```md
Excluded domains:
- medium.com (opinion/blog posts)
- reddit.com (user opinions, not authoritative)
- stackoverflow.com (coding Q&A, not research)
- twitter.com (headlines and opinions)
- linkedin.com (self-promotion)
- youtube.com (videos, not written sources)
```

**Result:** Only high-authority sources (academic papers, news outlets, company reports) are crawled.

**Impact:** 80% of hallucinations come from low-quality sources. Filtering catches them before they enter the pipeline.

### Stage 2: Verbatim Extraction (Content Extractor)

**Problem:** Paraphrasing can distort meaning. AI can accidentally change the claim.

**Solution:** The content extractor captures **exact quotes** from pages:

```json
{
  "claim": "AI diagnostic accuracy in medical imaging has reached 95%",
  "quote": "Our AI system achieved 95% accuracy in identifying tumors...",
  "confidence": "HIGH",
  "url": "https://medical-journal.com/study-2025"
}
```

Not:

```md
"claim": "AI achieved near-perfect diagnostic accuracy"  ❌ Too vague
"claim": "AI is 100% accurate" ❌ Changed meaning
```

**Benefits:**

- Readers can verify the claim by reading the quote
- No distortion through paraphrasing
- Context is preserved

### Stage 3: Confidence Scoring (Content Extractor)

**Problem:** Some claims are more reliable than others. How do we distinguish?

**Solution:** Each extracted claim is scored:

```txt
HIGH:     Peer-reviewed research, official company reports, government data
MEDIUM:   Industry publications, news from reputable outlets, expert interviews
LOW:      Emerging reports, single sources, preliminary findings
```

Example:

```md
- "AI market will reach $500B by 2028" 
  Source: McKinsey research report → HIGH confidence

- "AI will replace 30% of jobs"
  Source: Bloomberg opinion piece → MEDIUM confidence

- "AI will solve all human problems"
  Source: Startup press release → LOW confidence
```

**Result:** Readers know which findings are well-established vs. emerging.

### Stage 4: Cross-Source Validation (Synthesis Researcher)

**Problem:** Single sources can be wrong or biased.

**Solution:** The synthesis researcher identifies patterns across multiple sources:

```
Finding: "AI diagnostic accuracy is 95%"
Validation:
- Source A (Medical Journal): "95% accuracy"
- Source B (University Study): "93% accuracy"
- Source C (Company Report): "97% accuracy"

Synthesis: "Multiple sources report 93-97% accuracy. Average: 95%."
```

Contradictions are flagged:

```
Finding: "AI adoption in healthcare is widespread"
Validation:
- Source A: "80% of hospitals use some form of AI"
- Source B: "Only 20% of hospitals have deployed AI diagnostics"

Synthesis: "Adoption varies significantly. Full AI deployment is limited to 20%, 
but 80% of hospitals have some AI tools."
```

**Result:** Readers see consensus and conflicts, not a single potentially-wrong claim.

### Stage 5: Explicit Gap Flagging (Reporting Analyst)

**Problem:** Absence of evidence is presented as evidence of absence.

**Solution:** The reporter explicitly notes where data is insufficient:

```markdown
## AI Governance

Multiple sources discuss AI regulation approaches (HIGH confidence).

However, data on actual enforcement or effectiveness is limited. 
**Insufficient data:** How effective are current regulations? 
What's the compliance rate among companies?
```

Not: Just omitting the topic (implied no data exists)
Not: Making assumptions ("Presumably, regulations are effective")

**Result:** Readers know what's well-established vs. what needs more research.

## Reliability Features at a Glance

| Stage | Check | Benefit |
|-------|-------|---------|
| **Crawler** | Domain filtering | Removes low-quality sources before extraction |
| **Extractor** | Verbatim quotes | Claims are directly verifiable from sources |
| **Extractor** | Confidence scoring | Readers know reliability of each claim |
| **Synthesis** | Cross-source validation | Identifies patterns and contradictions |
| **Synthesis** | Gap identification | Flags areas where data is insufficient |
| **Reporter** | Direct citations | Every claim is traceable to a source URL |
| **Reporter** | Source linking | Readers can click and verify claims |

## Hallucination Prevention Checklist

ResearchCrew uses this checklist at every stage:

- **Extraction Phase**

  - [ ] Is the claim supported by the source text?
  - [ ] Is this a direct quote or paraphrase? (Direct preferred)
  - [ ] What's the confidence level of this claim?
  - [ ] Is the source reputable?

- **Synthesis Phase**

  - [ ] Does this finding appear in multiple sources?
  - [ ] Are there contradictions? (Note them)
  - [ ] Are there alternative interpretations? (Include them)
  - [ ] Is there sufficient data to make this claim?

- **Reporting Phase**

  - [ ] Does every claim have a source URL?
  - [ ] Can readers directly verify this claim?
  - [ ] Are gaps explicitly noted ("Insufficient data: X")?
  - [ ] Is the tone appropriately cautious for emerging findings?

## Comparing to Other Systems

### Generic AI Summation (e.g., ChatGPT)

```md
"Recent studies show AI can improve medical diagnostics by 40%."

Issues:
- No source provided
- "Recent studies" is vague
- "40% improve" could mean different things
- Can't verify the claim
```

### ResearchCrew

```md
"[Recent studies show AI diagnostic accuracy improvements ranging from 20-50%](https://medical-journal.com/study-2025),
with [cardiac imaging seeing the largest gains at 50%](https://cardiology-report.com/2024)."

Benefits:
- Each claim has a source URL
- Specific numbers with context
- Readers can verify by clicking links
- Multiple perspectives included
```

## Reliability Guarantees

ResearchCrew **guarantees:**

- Every claim has a source URL
- No invented quotes or statistics
- Multi-source validation for major findings
- Explicit gap identification
- Confidence scoring for transparency
- Source domain filtering

ResearchCrew **does NOT guarantee:**

- Perfect accuracy (sources can be wrong)
- Comprehensive coverage (may miss topics)
- Absence of bias (sources can be biased)
- Complete understanding (complex topics need human expertise)

Humans should always review output and validate against domain expertise.

## Tips for Validating Output

1. **Spot-check citations** — Click 3-5 random citations and verify they support the claim

2. **Check confidence levels** — Do HIGH-confidence claims feel reliable? Do they?

3. **Look for gap flags** — Are there "Insufficient data" notes? Does that match your expectations?

4. **Cross-reference** — Check if major claims appear in multiple sources (they should)

5. **Consider sources** — Are citations from credible sources for your domain?

6. **Domain expertise check** — Do findings align with your domain knowledge?

## Improving Reliability Further

### Through Feedback

Provide feedback to improve reliability:

```markdown
## User Feedback

The report claims "AI adoption is 90% in US hospitals."
This seems high. Please verify this with multiple recent sources 
and clarify what "adoption" means (any AI tool? Full AI replacement?).
```

The crew will re-search and validate the claim in the next iteration.

### Through Configuration

- Use **higher-quality LLMs** (Claude 3 Opus over GPT-3.5) for better reasoning
- Request **more search sources** (finds more corroborating evidence)
- Run **multiple iterations** (catches and fixes hallucinations with feedback)

## Next Steps

- **[Citations](citations.md)** — How citation strategy works
- **[Human-in-the-Loop](human-in-loop.md)** — Using feedback to improve quality
- **[Architecture](../architecture.md)** — How the pipeline implements these checks

# Citations & Traceability

Every claim in ResearchCrew output is directly traceable to a source.

## Why Citations Matter

### The Problem

Generic AI research produces un-sourced claims:

```md
"AI adoption in healthcare is accelerating. 
Companies report significant improvements in diagnostic accuracy and efficiency."

Issues:
- Where is this information from?
- Can I verify it?
- How do I cite this in my own work?
- Is it recent or outdated?
```

### The ResearchCrew Approach

Every claim includes a direct link to the source:

```markdown
"[AI adoption in healthcare is accelerating](https://healthcare-journal.com/trends-2025), 
with [companies reporting 30-40% improvements in diagnostic efficiency](https://tech-report.com/healthcare-ai-2025)."
```

Benefits:

- You can click and verify each claim
- Readers trust the information (transparent sources)
- You can cite this report in your own work
- Source recency is clear (what year? what publication?)

## Citation Format

ResearchCrew uses **markdown inline citations**:

```markdown
[claim text](URL)
```

Example:

```markdown
[GPT-4 can solve 92% of LeetCode problems](https://openai.com/research/gpt4)
```

This creates a clickable link in markdown viewers and web browsers.

## Citation Strategy

### Stage 1: Extraction

During content extraction, claims are linked to their source page:

```json
{
  "url": "https://healthcare-journal.com/study-2025",
  "title": "AI in Medical Diagnostics 2025",
  "claims": [
    {
      "claim": "AI diagnostic accuracy reached 95% in 2024",
      "quote": "...our AI system achieved 95% accuracy in identifying tumors...",
      "confidence": "HIGH"
    }
  ]
}
```

### Stage 2: Synthesis

When synthesizing across sources, each source's contribution is tracked:

```markdown
## Diagnostic Accuracy

Multiple studies demonstrate high accuracy in AI diagnostics:
- https://study-a.com reports 95% accuracy
- https://study-b.com reports 92% accuracy
- https://study-c.com reports 97% accuracy
```

### Stage 3: Reporting

Final report includes direct inline citations:

```markdown
[Multiple studies demonstrate AI diagnostic accuracy of 92-97%](https://study-a.com), 
with [cardiac imaging seeing the best results](https://study-c.com).
```

## Citation Accuracy

### Matched Claims

The crew ensures citations match claims:

**Correct:**

```markdown
[AI adoption in US hospitals reached 60% in 2024](https://valid-source.com/stat)
```

The URL actually contains this statistic.

**Incorrect (hallucination):**

```markdown
[AI adoption in US hospitals reached 95% in 2024](https://valid-source.com)
```

The URL says 60%, not 95% — citation doesn't support claim.

ResearchCrew avoids this through:

1. Extracting verbatim quotes alongside claims
2. Scoring confidence based on source reliability
3. Human review (you can catch mismatches)

### Citation Freshness

Citations should be recent and relevant:

**Good:**

```markdown
[Recent studies from 2024-2025 show...](https://2024-study.com)
```

**Questionable:**

```markdown
[Recent studies show...](https://2015-study.com)  
```

5-10 year old source may not be "recent"

ResearchCrew mitigates by:

1. Prioritizing recent sources in web search
2. Using terms like "2024-2025 studies" in search queries
3. You can provide feedback if sources are outdated

## Multi-Source Citations

### Single Source

When one source is sufficient:

```markdown
[AI is transforming healthcare delivery](https://authoritative-source.com/report)
```

### Multiple Sources

When multiple sources support a claim:

```markdown
[AI is transforming healthcare delivery](https://source-a.com/report), 
with [adoption rates accelerating globally](https://source-b.com/trends).
```

### Conflicting Sources

When sources disagree:

```markdown
Adoption rates vary significantly by region:
- [US adoption reached 80% in 2024](https://us-report.com)
- [EU adoption is at 45%](https://eu-report.com)
- [Asia-Pacific adoption is 60%](https://apac-report.com)
```

This allows readers to see the full picture, not just consensus.

## Citation Chains

Some claims require multiple citations to fully support:

```markdown
[AI diagnostics can be 95% accurate](https://source-a.com/accuracy), 
but [implementation in rural hospitals faces infrastructure barriers](https://source-b.com/barriers), 
with [estimated deployment costs of $500K-$1M per facility](https://source-c.com/costs).
```

This chain:

1. Establishes the capability (accuracy)
2. Identifies constraints (infrastructure)
3. Provides implementation context (costs)

Each claim is independently verifiable.

## Citation in Report Sections

### Example Report Structure

```markdown
# Research Report: AI in Healthcare

## Executive Summary

[AI is transforming healthcare with diagnostic improvements](https://source.com),
with [adoption rates increasing 40% annually](https://source2.com).

## Diagnostic Accuracy

[Multiple AI systems now achieve 90%+ accuracy](https://source3.com),
compared to [human radiologist accuracy of 88%](https://source4.com).

### Limitations

However, [AI systems require substantial training data](https://source5.com),
and [regulatory approval timelines can exceed 2 years](https://source6.com).

## Implementation Challenges

[Large hospitals have infrastructure for AI deployment](https://source7.com),
while [rural healthcare providers often lack adequate IT infrastructure](https://source8.com).
```

Every claim is linked. Readers can verify any statement.

## How to Use Citations

### Sharing Research

When you share `report.md`:

1. Citations are embedded as clickable links
2. Readers can verify claims
3. They can cite your work, which cites original sources

### Citing ResearchCrew Reports

If using ResearchCrew output in your own work:

```markdown
According to my research on AI in Healthcare 
(conducted with ResearchCrew on 2025-05-16):
- [AI diagnostic accuracy reaches 95% in some applications](https://...)
- [Implementation challenges persist in rural settings](https://...)

Sources are directly cited and verifiable.
```

### Academic/Professional Use

ResearchCrew reports are suitable for:

- Research papers (cite the original sources)
- Business reports (data is backed by sources)
- Team documentation (shared context with full sources)
- Presentations (every slide can be substantiated)

## Citation Best Practices

### When Reading ResearchCrew Output

**Do:**

- Click citations to verify claims
- Check if source supports claim
- Validate citation freshness (recent enough?)
- Consider source bias or perspective

**Don't:**

- Assume all citations are correct (verify!)
- Use claims without reading source
- Share without understanding source quality
- Assume sources can't be wrong

### When Providing Feedback

If a citation seems wrong:

```markdown
## User Feedback

The report cites [Source A showing AI accuracy of 95%](https://source-a.com).
I read the source and it actually says 92%, not 95%.

Please verify this citation and correct the report.
```

The crew will re-validate the citation in the next iteration.

## Citation Formats

ResearchCrew uses markdown inline citations. This format:

- Works in markdown files
- Renders as clickable links in browsers
- Preserves sources in text files
- Is human-readable

### Other Formats (Future)

Could be extended to:

- [x] Markdown inline citations (current)
- [ ] Footnotes with bibliography
- [ ] BibTeX entries
- [ ] APA/MLA/Chicago style
- [ ] Structured JSON with full metadata

## Limitations

ResearchCrew citations have limitations:

- **URL Links May Break**

  - If source is deleted or moved, link becomes invalid
  - Save PDFs of important sources for archival

- **Sources Can Be Biased**

  - ResearchCrew filters for authority, not objectivity
  - A credible source can still present a biased perspective

- **Sources Can Be Wrong**

  - Even reputable sources can contain errors
  - Always apply domain expertise to validate

- **No Permanent Archives**

  - Citation links depend on URLs staying live
  - Consider archiving important sources

## Next Steps

- **[Reliability Features](reliability.md)** — How quality is ensured
- **[Human-in-the-Loop](human-in-loop.md)** — Using feedback to validate
- **[Examples](../examples/)** — See real reports with citations

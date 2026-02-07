---
chapters: [9]
primary_chapter: 9
narrative_role: "Benchmark showing frontier LLMs compute fewer than 1/3 of tax returns correctly"
---

# TaxCalcBench

**Paper**: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task"
**Authors**: Michael R. Bock, Kara Molisee, Zachary Ozer, Sumit Shah (Column Tax)
**Date**: July 2025 (arXiv: 2507.16126)
**Code**: github.com/column-tax/tax-calc-bench

## What It Tests

51 synthetic Tax Year 2024 federal-only personal income tax returns. Covers various filing statuses, income sources, and features (CTC, EITC). Only models with 2025 knowledge cutoff tested (complete information about TY2024 rules).

## Results (strict accuracy — fully correct returns)

| Model | Best Strict Accuracy |
|---|---|
| Gemini 2.5 Pro | 32.35% |
| Claude Opus 4 | 27.45% |
| Gemini 2.5 Flash | 25.98% |
| Claude Sonnet 4 | 23.04% |

Tested across thinking budget levels: Lobotomized (minimal), Low (1024 tokens), Medium (2048), High (4096), Ultrathink (maximum). Four runs per model per level.

## Key Error Patterns

1. **Tax table misuse** (15-20% of cases): Models used percentage/bracket-based calculations instead of proper IRS tax tables, causing $3-5 discrepancies per return
2. **Eligibility errors**: Incorrectly determined credit eligibility (e.g., CTC)
3. **Calculation errors**: Particularly on supplementary forms like Form 8962 (Premium Tax Credit)

## Significance

Even the best-performing model got fewer than 1/3 of returns right. This is worse than the Blair-Stanek SARA benchmark (67% on true/false), because TaxCalcBench requires computing complete returns, not just answering questions.

The authors conclude: additional infrastructure needed to apply LLMs to personal income tax calculation. This directly supports the Cosilico thesis.

## Connection to Book

Updates the "AI accuracy" story from Ch 9 and the introduction:
- Blair-Stanek 2023: GPT-4 gets 67% on true/false tax questions
- TaxCalcBench 2025: Best model gets 32% on complete returns
- The accuracy gap hasn't closed with better models — it's a structural limitation

## Relationship to Column Tax

Column Tax (the authors' company) also built Iris, an AI tax development agent that reads tax law and generates code. They've filed 1M+ returns and processed $1B+ in refunds. Their conclusion: LLMs need deterministic tools, not just better prompts.

Column Tax was acquired by Aiwyn in November 2025.

## Sources

- [arXiv paper](https://arxiv.org/abs/2507.16126)
- [Column Tax blog](https://www.columntax.com/blog/taxcalcbench)

## Links

- [[ai-integration-philosophy]]
- [[cosilico]]

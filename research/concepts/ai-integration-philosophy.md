# AI Integration Philosophy

## The Insight That Addresses Priya's Critique

The book's framing shouldn't be **deterministic vs AI**. It should be **deterministic AS infrastructure FOR AI**.

## The Core Principle

From Cosilico thesis:
> "Deterministic tools will always be faster, auditable, and legally citable; LLMs will call tools."

This isn't about competing with AI. It's about building what AI needs to be reliable.

## How PolicyEngine Uses AI

### Claude for Explanations
- Claude 3.5 Sonnet explains complex tax-benefit calculations
- The engine does the math; Claude translates to natural language
- "Explain with AI" buttons in US and UK apps

### Multi-Agent Research Workflows
- Claude Code orchestrates data fetching, script writing, report generation
- Handles routine distributional analyses (poverty rates, Gini coefficients)
- Struggles with complex multi-program interactions (still needs human expertise)

### GPT-4 for Policy Narratives
- Auto-generated policy analysis from reform data
- Three audience modes: ELI5, Normal, Wonk

### LLMs for Behavioral Research
- Using Claude/GPT to simulate taxpayer behavioral responses
- Comparing LLM responses to empirical literature (NTA 2024 study)

## How Cosilico Uses AI

### Agentic Rule Encoding
AI agents learn to encode rules from statute text:

```
Statute Text → Claude → Generated Code → Oracle (PolicyEngine, TAXSIM) → Reward → Iterate
```

Two-level reward function:
1. **Structural**: Does code parse? Valid DSL? Has citations?
2. **Semantic**: Does code match oracle outputs?

Target: ≥95% accuracy through iterative refinement.

### AI as Tool-Caller, Not Calculator
The vision: Every AI assistant needs reliable policy calculations. Cosilico provides the backend.

- Anthropic MCP integration
- API for tool-calling models
- "Society is hard to optimize because nobody has a shared model to reason against... Cosilico is the shared substrate."

## The Reframe for the Book

**Old framing** (what Priya critiqued):
> "GPT-4 gets 67% accuracy, so we need deterministic tools instead of AI"

**New framing**:
> "GPT-4 gets 67% accuracy *on its own*. That's why AI needs reliable tools to call. Microsimulation isn't competing with AI—it's the infrastructure that makes AI trustworthy for policy."

### Key Quotes to Use

From Cosilico: "LLMs will call tools."

From PolicyEngine: "AI handles communication and routine analysis; the deterministic engine ensures accuracy."

## Implications for Each Part

**Part I (Origins)**: The history of building reliable calculation infrastructure—now relevant because AI agents need it.

**Part II (Building)**: Not just democratizing access to humans, but creating the API layer that AI systems call.

**Part III (Future)**: AI agents with tool-use capabilities (Claude 3+, GPT-4 function calling) will be the primary users. The "democratic moment" is partly about AI making these tools accessible via natural language.

## The Stronger Argument (per Priya)

Even if LLMs improve to 99% accuracy, you'd still want:
1. **Auditability**: Traceable to statute citations
2. **Reproducibility**: Same inputs → same outputs
3. **Legal citability**: "The model said so" vs "26 USC §32(a)(1)"
4. **Speed**: Deterministic calculations are faster than inference
5. **Cost**: API calls cheaper than LLM inference for high volume

The case for deterministic tools doesn't depend on AI being bad. It depends on policy domains requiring these properties.

## The Diversity Problem (HiveSight Insight)

LLMs have a fundamental limitation for simulating human populations: they predict the "most likely" response, not the distribution of responses.

**Temperature is not the answer**: Adding random noise via temperature creates unstructured variation. But real human diversity is structured—opinions correlate with demographics, experiences, circumstances.

**Microdata is the answer**: HiveSight uses PolicyEngine/Cosilico microdata to construct representative demographic profiles. This grounds LLM-generated opinions in actual population distributions.

This is analogous to quantile regression forests in microimpute: modeling not just the mean but the full conditional distribution. The microdata provides the "shape" of human variation that LLMs can't learn from RLHF.

**The integration pattern**:
```
Representative Microdata (deterministic) → Persona Conditioning → LLM Response → Aggregated Distribution
```

Without the microdata layer, you're just getting the LLM's modal prediction N times with noise. With it, you're sampling from a distribution that reflects actual human heterogeneity.

## Updated AI + Tax Developments (2025-2026)

### TaxCalcBench (July 2025)
Column Tax's benchmark: even the best frontier model (Gemini 2.5 Pro) computes only 32.35% of full tax returns correctly. See [[taxcalcbench]] for details. The accuracy gap hasn't closed with better models.

### Column Tax's Iris Agent
AI tax development agent that reads tax law and generates code. Custom orchestration: topological sorting of tax form dependencies, embeddings + vector DB over IRS forms, code generation, testing. The computation graph has 100,000+ nodes. Filed 1M+ returns, $1B+ in refunds. Column Tax acquired by Aiwyn Nov 2025.

### IRS AI Adoption
- Deployed Salesforce Agentforce across Office of Chief Counsel, Taxpayer Advocate, Office of Appeals (document search, case summaries)
- Replaced Discriminant Analysis System (DAS) with Line Anomaly Recommender (LAR) for corporate audit selection
- AI now used in both audit selection and execution

### Intuit Agentic AI
Intuit's agentic platform can pre-prepare up to 80% of simple tax situations for TY2025. Paired with 13,000 human experts.

### AI Financial Regulation
- SEC "AI washing" enforcement priority — fined Nate Inc ($42M fraud), Presto Automation
- CFPB requires specific reasons in AI-driven credit denials
- EU AI Act (fully applicable Aug 2026): AI in credit scoring, insurance, complex tax = "High-Risk"
- No comprehensive US federal AI governance framework

## Sources

- PolicyEngine blog posts (policyengine-app-v2/app/src/data/posts/articles/)
- Cosilico THESIS.md
- Cosilico AI_ENCODING.md
- Cosilico agent.py implementation
- [TaxCalcBench](https://arxiv.org/abs/2507.16126)
- [Column Tax Iris](https://www.columntax.com/blog/introducing-iris-our-ai-tax-development-agent)
- [IRS AI adoption](https://www.eisneramper.com/insights/tax/ai-irs-transforming-0126/)

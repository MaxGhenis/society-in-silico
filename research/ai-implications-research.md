# AI Implications for Policy Simulation: Research Findings

Research compiled: December 23, 2025
For: Part III of "Society in Silico"

## Executive Summary

This research explores three critical dimensions of AI's role in policy simulation:

1. **LLM Accuracy Limitations**: Large language models struggle with mathematical reasoning and numerical tasks, showing 20-65% performance drops when even slight changes are made to problems. They rely on pattern matching rather than genuine logical reasoning.

2. **AI Agents Need Reliable Tools**: Tool augmentation (calculators, APIs, databases) can improve accuracy dramatically—from 16% to 88% in medical calculations, and to 98-99% for arithmetic tasks—by grounding AI outputs in verifiable computation.

3. **Open vs. Closed Systems**: Government adoption of proprietary "black box" AI raises accountability concerns, while open-source approaches enable transparency, auditability, and democratic oversight—critical for tax-benefit policy analysis.

---

## I. LLM Accuracy Limitations

### The Core Problem: Pattern Matching vs. Reasoning

Research shows that LLMs do not perform genuine logical reasoning; instead, they replicate reasoning steps from training data. The landmark GSM-Symbolic study ([Apple/Meta, ICLR 2025](https://arxiv.org/abs/2410.05229)) demonstrates this through carefully controlled experiments.

**Key Finding**: When only numerical values in math problems are altered, model performance drops by **up to 65%**—despite the logical structure remaining identical.

> "Current LLMs cannot perform genuine logical reasoning; they replicate reasoning steps from their training data. When evaluating models on GSM-Symbolic, researchers observed that performance could drop by up to 65% compared to the original GSM8K, even when only numerical values were altered in otherwise identical problems."
> — [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2410.05229)

### Specific Accuracy Numbers by Task Type

#### Mathematical Reasoning Benchmarks

**GSM8K (Grade School Math):**
- GPT-4: ~92% (few-shot), up to 97% with strategies
- GPT-4o: 96.1%
- o1 model: 96.13%
- Open-source SOTA: ~80-90%

Sources: [GSM8K Benchmark](https://klu.ai/glossary/GSM8K-eval), [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)

**MATH (Higher Difficulty):**
- GPT-4o: 76.6%
- o1 model: 93.12%

**AIME (Competition-Level Math):**
- GPT-4o: Only 12% (1.8/15 problems)
- o1: 74% (11.1/15) single sample, 83% with consensus, 93% with reranking

> "On the 2024 AIME exams, GPT-4o only solved on average 12% (1.8/15) of problems. o1 averaged 74% (11.1/15) with a single sample per problem."
> — [Scheherazade: Evaluating Chain-of-Thought Math Reasoning](https://arxiv.org/pdf/2410.00151)

The gap between GPT-4o and o1 demonstrates that reasoning capabilities can be significantly improved, but even o1 shows degradation on more complex variants.

### Hallucination Rates and Factual Accuracy

**Reported Hallucination Rates Across Models:**
- GPT-4: Below 5% (near-perfect on simple evaluations)
- LLaMA 2: 20-25% factual hallucination rate
- DeepSeek: 20-25% factual hallucination rate

Source: [Survey on Hallucination in Large Language Models](https://pmc.ncbi.nlm.nih.gov/articles/PMC12518350/)

**Critical Limitation**: On more challenging evaluations and in real-world use, accuracy is capped below 100% because:
- Some questions' answers cannot be determined due to unavailable information
- Models have limited thinking abilities
- Ambiguities exist in natural language

> "While evaluations themselves do not directly cause hallucinations, most evaluations measure model performance in a way that encourages guessing rather than honesty about uncertainty."
> — [Why Language Models Hallucinate](https://openai.com/index/why-language-models-hallucinate/)

### Sensitivity to Irrelevant Information

The GSM-NoOp dataset tests how models handle extraneous information. When irrelevant numbers are added to problems (e.g., "five kiwis were smaller than average" in a counting problem), models consistently incorporate them into calculations.

**Performance Drop**: Phi-3-mini experienced over **65% drop in accuracy** when problems included irrelevant information.

Source: [GSM-Symbolic Paper](https://arxiv.org/pdf/2410.05229)

### Medical Context: The 67% Accuracy Benchmark

The often-cited 67% accuracy figure comes from medical AI:

> "Fine-tuned transformers (like Google's Med-PaLM, a PaLM model fine-tuned on medical Q&A) reached ~67% accuracy (close to passing) in 2022. This was on the MedQA benchmark, which is derived from USMLE (United States Medical Licensing Exam) questions."
> — [LLM Benchmarks in Life Sciences](https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview)

For context:
- Random guessing on MedQA: 25%
- Traditional models (pre-2022): ~40%
- GPT-4 (zero-shot): 71.6%

This demonstrates the rapid progress in specialized domains, but also highlights that even state-of-the-art models make significant errors on expert-level knowledge tasks.

### Common Error Patterns

Research identifies recurring error types in LLM mathematical reasoning:

1. **Calculation errors**: Arithmetic mistakes
2. **Counting errors**: Incorrect enumeration
3. **Formula confusion**: Misapplying mathematical formulas
4. **Question misinterpretation**: Misunderstanding problem requirements
5. **Missing solution steps**: Incomplete reasoning chains
6. **Conceptual confusion**: Fundamental misunderstanding of concepts
7. **Nonsensical outputs**: Logically incoherent responses

Source: [Mathematical Computation and Reasoning Errors](https://arxiv.org/html/2508.09932)

### Implications for Policy Simulation

**Why This Matters**: Tax-benefit calculations require:
- Precise arithmetic (income thresholds, phase-out rates)
- Multi-step logical reasoning (eligibility chains, interaction effects)
- Numerical accuracy (budget projections, distributional impacts)

LLMs alone cannot reliably perform these tasks. A model that drops from 90% to 25% accuracy when problem parameters change cannot be trusted with calculating household tax liability or program eligibility.

---

## II. AI Agents Need Reliable Tools

### The Solution: Grounding in External Tools

While LLMs struggle with precise computation, they excel at orchestration and natural language understanding. The solution is **tool augmentation**—connecting LLMs to reliable calculators, databases, and APIs.

### What is Grounding?

> "In generative AI, grounding is the ability to connect model output to verifiable sources of information. If you provide models with access to specific data sources, then grounding tethers their output to these data and reduces the chances of inventing content."
> — [Google Cloud: Grounding Overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)

**Key Techniques:**
1. **Retrieval-Augmented Generation (RAG)**: Fetching real-time data from databases or web search
2. **Tool Use / Function Calling**: Calling external tools or APIs (calculators, databases, CRMs)
3. **Code Execution**: Having LLMs write code that is executed by interpreters

### Dramatic Accuracy Improvements with Tools

#### Medical Calculations: 5.5x to 13x Reduction in Errors

Study comparing LLM performance on medical calculations with and without tools:

**Without Tools:**
- LLaMA-based models: 16% correct
- GPT-based models: 4.8% correct

**With Task-Specific Tools (OpenMedCalc):**
- LLaMA-based models: 88% correct (**5.5x improvement**)
- GPT-based models: 64% correct (**13x improvement**)

> "Large language models (LLMs) can answer expert-level questions in medicine but are prone to hallucinations and arithmetic errors. Models with access to task-specific tools showed the greatest improvement, with LLaMa and GPT-based models demonstrating a 5.5-fold (88% vs 16%) and 13-fold (64% vs 4.8%) reduction in incorrect responses."
> — [Large language model agents can use tools to perform clinical calculations](https://www.nature.com/articles/s41746-025-01475-8)

#### Arithmetic Tasks: 98-99% Accuracy with Integrated Calculators

The Integrated Gated Calculator (IGC) approach embeds calculator functionality directly:

> "When finetuned with a Llama model, it beats the State of the Art on the BigBench Arithmetic benchmark, outperforming models almost two orders of magnitude larger. It is computationally efficient, interpretable, and avoids side-effects on tasks that do not require arithmetic operations. It reliably achieves **98% to 99% accuracy** across multiple training runs."
> — [IGC: Integrating a Gated Calculator into an LLM](https://arxiv.org/abs/2501.00684)

#### RAG for Medical AI: From 77.5% to 83.1% Accuracy

Incorporating RAG significantly enhanced GPT-4's medical diagnosis accuracy:

- GPT-4 alone: AUC 0.79, accuracy 77.5%
- GPT-4 + RAG: AUC 0.82, accuracy 81.3%
- GPT-4 + RAG + ML probabilities: AUC 0.87, accuracy 83.1%

Source: [Enhancing medical AI with RAG](https://pmc.ncbi.nlm.nih.gov/articles/PMC12059965/)

### Agentic RAG: The Next Evolution

Traditional RAG systems have static workflows. **Agentic RAG** adds autonomous agents that can:

1. **Refine queries iteratively**: Improving semantic similarity
2. **Self-grade retrieved information**: Assessing quality through feedback loops
3. **Adaptive retrieval**: Determining optimal moments and content for retrieval
4. **Multi-step reasoning**: Complex task management with tool orchestration

> "RAG has emerged as a solution, enhancing LLMs by integrating real-time data retrieval to provide contextually relevant and up-to-date responses. However, traditional RAG systems are constrained by static workflows and lack the adaptability required for multistep reasoning and complex task management. Agentic RAG transcends these limitations by embedding autonomous AI agents into the RAG pipeline."
> — [Agentic RAG: A Survey](https://arxiv.org/abs/2501.09136)

**Key Research Finding**: Hallucinations in RAG systems may be due to insufficient context. Selective generation (abstaining when context is insufficient) can mitigate this issue.

Source: [Deeper insights into RAG: The role of sufficient context](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) (Google, ICLR 2025)

### Why This Matters for Microsimulation

**Microsimulation models are ideal grounding tools for AI agents**:

1. **Precise computation**: Tax-benefit rules encoded in code (not LLM approximations)
2. **Verifiable outputs**: Every calculation can be traced and audited
3. **Representative data**: Population microdata grounds analysis in real distributions
4. **Reproducible results**: Same inputs always produce same outputs

An AI agent that can:
- Understand natural language policy questions
- Query microsimulation APIs (like PolicyEngine)
- Explain results in accessible language

...combines the strengths of LLMs (language understanding, explanation) with microsimulation's strengths (numerical accuracy, policy fidelity).

---

## III. Open vs. Closed Systems

### The Government AI Transparency Debate

As governments increasingly adopt AI for policy analysis and public services, a critical debate has emerged: Should these systems be open-source and auditable, or is proprietary AI acceptable?

### The Case for Open Source in Government

#### Legislative Movement

**Federal AI Governance and Transparency Act (2024)**:
Bipartisan House bill introduced by Chairman James Comer (R-KY) and Ranking Member Jamie Raskin (D-MD):

> "The bill aims to codify governance of agency AI systems, establish new mechanisms for transparency and accountability, and consolidate and streamline other existing AI laws. The legislation emphasizes 'transparency in publicly disclosing relevant information regarding the use of artificial intelligence to appropriate stakeholders, to the extent practicable and in accordance with any applicable law and policy.'"
> — [Federal AI Governance and Transparency Act](https://federalnewsnetwork.com/federal-newscast/2024/03/new-house-bill-specifies-how-agencies-should-use-artificial-intelligence/)

#### Open-Source AI Foundation (O-SAIF)

Launched in February 2025 to advocate for open-source AI in civilian government:

> "Awarding a closed source software vendor to develop and train a proprietary AI in civilian govtech represents a serious misuse of public resources. These proprietary systems lack transparency and accountability, effectively wasting taxpayer funds while enriching private companies. This approach undermines public oversight and creates long-term dependencies that jeopardize government operations."
> — [O-SAIF Launch Announcement](https://www.prnewswire.com/news-releases/open-source-ai-foundation-o-saif-launched-to-fight-for-transparency-and-accountability-in-civilian-government-ai-contracts-302382045.html)

**O-SAIF Partnership**: OpenTeams partnered with O-SAIF to promote safety and transparency of AI in U.S. government, advocating for:
- Public auditability
- Enhanced security
- Prevention of wasteful spending
- Avoidance of vendor lock-in

Source: [OpenTeams Partners with O-SAIF](https://www.businesswire.com/news/home/20250228100105/en/OpenTeams-Proudly-Partners-with-the-Open-Source-AI-Foundation-O-SAIF-to-Promote-Safety-and-Transparency-of-AI-in-U.S.-Government)

### The Black Box Problem

#### Real-World Consequences: Dutch Benefits Scandal

The "Toeslagenaffaire" (benefits affair) in the Netherlands led to the **entire Dutch government resigning in 2021**:

> "This case underscores a core issue with black box algorithms in governance: lack of transparency can enable severe injustice. It fueled European resolve to regulate algorithmic transparency – providing a real-world backdrop to the EU's AI Act."
> — [Black Box AI Exposed](https://ts2.tech/en/black-box-ai-exposed-hidden-algorithms-risks-and-breakthroughs-in-2025/)

The scandal involved an opaque algorithm wrongly flagging thousands of families for welfare fraud, causing financial devastation. Families couldn't understand or challenge the decisions because the system was a black box.

#### Houston Teacher Evaluation Case

Houston Federation of Teachers sued over an AI-powered teacher evaluation tool (EVAAS):

> "The union sued the school district over its use of an AI-powered teacher evaluation tool (EVAAS), arguing that the algorithm was opaque and lacked sufficient explanations for its outputs. The case was ultimately settled, with the district agreeing to provide more transparency and due process protections."
> — [Transparency and accountability in AI systems](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2024.1421273/full)

### International Governance Frameworks

#### European Union AI Act

The EU's landmark legislation mandates:
- Rigorous standards for high-risk AI systems
- Explainability and accountability requirements
- Becoming a global benchmark for AI regulation

Source: [Black Box AI: Risks and Breakthroughs](https://ts2.tech/en/black-box-ai-exposed-hidden-algorithms-risks-and-breakthroughs-in-2025/)

#### Canada's Directive on Automated Decision-Making

Canada's framework ties AI use to:
- Algorithmic Impact Assessment (required)
- Risk tiers with corresponding safeguards
- For high-impact systems:
  - Human-in-the-loop escalation
  - Public notice to affected individuals
  - Layperson-readable explanations
  - Clear routes to challenge outcomes

Source: [AI governance in the public sector](https://pmc.ncbi.nlm.nih.gov/articles/PMC7164913/)

### The Explainability Trade-off

A tension exists between performance and transparency:

> "With machine learning in general and neural networks or deep learning in particular, there is often a trade-off between performance and explainability. The larger and more complex a model, the harder it will be to understand, even though its performance is generally better. For complex situations with many interacting influences—which is true of many key areas of policy—machine learning will often be more useful the more of a black box it is."
> — [The tensions between explainable AI and good public policy](https://www.brookings.edu/articles/the-tensions-between-explainable-ai-and-good-public-policy/)

**However**, for policy simulation:
- The underlying model (microsimulation) can be fully transparent
- The AI layer provides natural language interface and explanation
- This preserves both accuracy and interpretability

### PolicyEngine as an Open-Source Model

PolicyEngine exemplifies the open-source approach to policy analysis:

**Core Mission**:
> "PolicyEngine is a nonprofit with the mission to compute the impact of public policy for the world. Their free, open-source software models the tax and benefit systems in the US and UK, using a microsimulation framework based on OpenFisca."
> — [PolicyEngine GitHub](https://github.com/PolicyEngine)

**Key Features**:
1. **Fully open-source**: All code is publicly available and auditable
2. **Multiple interfaces**: Python packages, APIs, web apps
3. **Policy reform analysis**: Budget, poverty, inequality impacts
4. **Household-level calculations**: Tax liability and benefit eligibility
5. **Government transparency**: UK government publishes Algorithmic Transparency Record for PolicyEngine

> "The tool aims to enhance the accuracy of household survey data used for microsimulation modeling of tax-benefit policy changes by addressing sampling error (particularly the under-sampling of high-income households) and measurement error (such as under-reporting of specific income sources)."
> — [HMT: Policy Engine UK](https://www.gov.uk/algorithmic-transparency-records/hmt-modelling-policy-engine)

### Open Source Benefits for Policy AI

1. **Public Trust**: Citizens can verify how calculations are made
2. **Democratic Accountability**: Elected officials can audit policy models
3. **Scientific Validation**: Researchers can reproduce and verify results
4. **Collaborative Improvement**: Community contributions enhance accuracy
5. **No Vendor Lock-in**: Government retains independence
6. **Cost Efficiency**: No proprietary licensing fees

> "As government agencies explore AI-based services, the transparency and accountability of open source software become essential. Public trust hinges on clear decision-making processes—something open source models support inherently."
> — [How AI Enhances Open Source Software Compliance for Government](https://openteams.com/how-ai-enhances-open-source-software-compliance-for-government/)

---

## IV. Policy Simulation with AI: Current Research

### Traditional Microsimulation Models

Major institutions using microsimulation for tax-benefit policy:

**United States:**
- Congressional Budget Office (CBO)
- Joint Committee on Taxation (JCT)
- Treasury's Office of Tax Analysis (OTA)
- Urban-Brookings Tax Policy Center (TPC)
- The Budget Lab at Yale

**International:**
- EUROMOD (EU-wide tax-benefit model)
- Institute for Fiscal Studies (UK)
- Centre for Microsimulation and Policy Analysis (University of Essex)

**Key Limitation**: These models produce first-order effects only—assuming household composition, work hours, and incomes remain unchanged. They don't model behavioral responses.

> "Simulation models can analyze who will gain and who will lose from a tax change, and estimate the aggregate budget effects of tax and benefit changes. However, models will only give the first-order effect of a tax change, because household composition, work hours and incomes are assumed unchanged. This is both a strength and weakness—it's easy to understand what the model does and no controversial assumptions are needed."
> — [Microsimulation and Policy Analysis](https://www.sciencedirect.com/science/article/abs/pii/B978044459429700025X)

### AI-Driven Approaches: The AI Economist

Salesforce Research's "AI Economist" uses deep reinforcement learning for tax policy design:

**Innovation**: Instead of assuming fixed behavioral rules, agents learn optimal behaviors through interaction. The system finds tax policies that maximize social welfare compared to traditional progressive, regressive, or no-tax baselines.

**Methodology**:
- Agent-based modeling (ABM) with AI-learned behaviors
- Two-level deep multiagent reinforcement learning
- Millions of simulated agents

**Limitations and Ethical Considerations**:
> "Future research can scale up AI-driven simulations and calibrate them to real-world data, along with learning AI policies that are explainable and robust to simulation-to-reality gaps. The researchers encourage anyone using the AI Economist to describe the ethical considerations of trained AI-driven tax models to increase transparency and trust in the system. Furthermore, they believe that any future application or policy built on economic simulations should be built on inspectable code and subject to full transparency."
> — [The AI Economist: Taxation policy design via RL](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067926/)

### Risks of AI in Policy Analysis

Research identifies critical challenges:

**1. Distribution Shifts**: Models trained on historical data may fail when conditions change

**2. Label Bias**: Training data reflects past decisions, which may encode biases

**3. Competing Objectives**: Public policy involves multiple, sometimes conflicting goals

**4. Pattern Recognition Risks**:
> "Algorithms are vulnerable to biases in the original data and to making decisions on arbitrary grounds. Unexpected implications of 'pattern recognition' can be complicated to safeguard against."
> — [Machine Learning in Public Policy: Perils and Promise](https://www.rand.org/pubs/perspectives/PEA828-1.html)

### RAND Recommendations for Policymakers

> "Recommendations for policymakers include: (1) improve data through coordinated investments; (2) approach ML expecting interpretability, and be critical; and (3) leverage interpretable ML to understand policy values and predict policy impacts."
> — [RAND: Machine Learning in Public Policy](https://www.rand.org/pubs/perspectives/PEA828-1.html)

### The Human-Centered Approach

> "AI in policymaking should be conceived as an assistive tool, an empowering exoskeleton for policymakers that aids in navigating complex decisions, envisioning desirable futures, raising patterns in data to investigate, and assessing the risks and impacts of simulated policies. Such an approach to AI integration can be defined as human-centred."
> — [Bridging the gap: AI-driven decision-making in the public sector](https://www.sciencedirect.com/science/article/pii/S0740624X24000686)

**Critical Principle**:
> "While AI has the potential to enhance policymaking, it is crucial to exercise rigorous oversight and stringent risk assessments when integrating AI. AI systems, though powerful, can perpetuate biases, misinterpret data, and/or provide recommendations that are not aligned with the public good. Policymakers must ensure that AI tools are used transparently and ethically, with a strong emphasis on human oversight and intervention at every stage. AI should serve as a supportive tool rather than a decision-maker."
> — [AI in Public Policy - The Decision Lab](https://thedecisionlab.com/reference-guide/computer-science/ai-in-public-policy)

---

## V. Implications for "Society in Silico"

### Chapter Content Ideas

#### Chapter: "The 67% Problem" or "When AI Meets Arithmetic"

**Opening hook**: LLMs can write poetry and pass the bar exam, but ask one to calculate a household's EITC eligibility, and you're playing Russian roulette with policy analysis.

**Core narrative**:
1. Show a simple tax calculation that GPT-4 gets wrong
2. Explain why: pattern matching vs. computation
3. The GSM-Symbolic revelation: change the numbers, lose the pattern
4. Why this matters for policy: precision requirements in tax-benefit systems

**Key tension**: The same technology that can explain complex policy in plain English cannot reliably add up the costs.

#### Chapter: "Grounding the Oracle" or "AI Agents Need Calculators"

**Opening hook**: In 1997, Deep Blue beat Kasparov at chess not by thinking like a human, but by calculating like a machine. Today's AI needs to rediscover that lesson.

**Core narrative**:
1. The tool-augmentation revolution: from 16% to 88% accuracy
2. RAG and agentic systems as "exoskeletons for thought"
3. Microsimulation as the ultimate grounding tool
4. Vision: AI agents that query PolicyEngine for accurate analysis

**Historical parallel**: Guy Orcutt's insight that simulation needs micro-level precision, not aggregate approximation

#### Chapter: "Black Box Democracy" or "The Open-Source Imperative"

**Opening hook**: In 2021, the entire Dutch government resigned because an algorithm they couldn't explain destroyed thousands of families. The black box had become a black hole.

**Core narrative**:
1. The Dutch benefits scandal: opacity enables injustice
2. The case for open-source policy tools
3. PolicyEngine as exemplar: transparent, auditable, democratic
4. AI regulation catching up: EU AI Act, Canadian framework, U.S. legislation

**Key argument**: Democratic policy analysis requires democratic tools. Proprietary black boxes are incompatible with public accountability.

### Synthesis: The Vision

**AI + Microsimulation = The Future of Policy Analysis**

The optimal system combines:
1. **LLM strengths**: Natural language understanding, explanation generation, pattern recognition in unstructured data
2. **Microsimulation strengths**: Precise computation, rule encoding, distributional analysis
3. **Open-source philosophy**: Transparency, auditability, democratic accountability

**What this looks like in practice**:
- A policymaker asks: "What would a $3,000 child allowance cost, and who benefits most?"
- An AI agent understands the question, queries PolicyEngine's API, receives precise calculations
- The agent explains results in natural language: "This reform would cost $110 billion annually, reduce child poverty by 3.2 million, and provide the largest percentage gains to families in the bottom income quintile"
- Every number is traceable to open-source code that anyone can audit

### The Max Ghenis Arc

This connects to your personal journey:
- **Economist**: Understanding the limitations of black-box models and the importance of transparent analysis
- **Builder**: Creating PolicyEngine as an open-source alternative
- **Visionary**: Seeing how AI can amplify microsimulation's impact while preserving its rigor

### Avoiding Hype, Embracing Honesty

**What to avoid**:
- "AI will revolutionize everything!" breathlessness
- Overselling current capabilities
- Ignoring real limitations and risks

**What to emphasize**:
- Specific numbers: 65% accuracy drops, 5.5x improvement with tools
- Real-world consequences: Dutch scandal, Houston teachers
- Honest trade-offs: Performance vs. explainability
- Concrete vision: AI as interface to microsimulation, not replacement

### The Uncertainty Principle

> "While evaluations themselves do not directly cause hallucinations, most evaluations measure model performance in a way that encourages guessing rather than honesty about uncertainty."

**Book principle**: Be honest about uncertainty. Don't let AI guess when calculation is needed. Ground in tools that can say "I don't know" or "this requires more data."

---

## VI. Key Sources by Topic

### LLM Mathematical Reasoning Limitations
- [GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs](https://arxiv.org/abs/2410.05229) - Apple/Meta, ICLR 2025
- [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/) - OpenAI
- [Mathematical Computation and Reasoning Errors by LLMs](https://arxiv.org/html/2508.09932)
- [Why Language Models Hallucinate](https://openai.com/index/why-language-models-hallucinate/) - OpenAI
- [Survey on Hallucination in LLMs](https://pmc.ncbi.nlm.nih.gov/articles/PMC12518350/)
- [Hallucinations Leaderboard](https://huggingface.co/blog/leaderboard-hallucinations) - Hugging Face

### Tool Use and Grounding
- [IGC: Integrating a Gated Calculator into an LLM](https://arxiv.org/abs/2501.00684)
- [Large language model agents can use tools to perform clinical calculations](https://www.nature.com/articles/s41746-025-01475-8)
- [Grounding overview - Google Cloud](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)
- [Agentic RAG: A Survey](https://arxiv.org/abs/2501.09136)
- [Deeper insights into RAG: The role of sufficient context](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) - Google, ICLR 2025

### Open Source vs. Proprietary AI in Government
- [Federal AI Governance and Transparency Act](https://www.congress.gov/bill/118th-congress/house-bill/7532/text)
- [O-SAIF Launch Announcement](https://www.prnewswire.com/news-releases/open-source-ai-foundation-o-saif-launched-to-fight-for-transparency-and-accountability-in-civilian-government-ai-contracts-302382045.html)
- [Transparency and accountability in AI systems](https://www.frontiersin.org/journals/human-dynamics/articles/10.3389/fhumd.2024.1421273/full)
- [Black Box AI Exposed](https://ts2.tech/en/black-box-ai-exposed-hidden-algorithms-risks-and-breakthroughs-in-2025/)
- [The tensions between explainable AI and good public policy](https://www.brookings.edu/articles/the-tensions-between-explainable-ai-and-good-public-policy/) - Brookings

### Microsimulation and Policy Modeling
- [The AI Economist: Taxation policy design via RL](https://pmc.ncbi.nlm.nih.gov/articles/PMC9067926/)
- [Machine Learning in Public Policy: Perils and Promise](https://www.rand.org/pubs/perspectives/PEA828-1.html) - RAND
- [The Use of Microsimulation Models to Inform US Tax Policymaking](https://www.microsimulation.pub/articles/00314)
- [Tax Microsimulation at The Budget Lab](https://budgetlab.yale.edu/research/tax-microsimulation-budget-lab)
- [PolicyEngine GitHub](https://github.com/PolicyEngine)
- [HMT: Policy Engine UK - Algorithmic Transparency Record](https://www.gov.uk/algorithmic-transparency-records/hmt-modelling-policy-engine)

### AI Safety and Governance
- [Towards Guaranteed Safe AI](https://arxiv.org/html/2405.06624v2)
- [AI governance in the public sector](https://pmc.ncbi.nlm.nih.gov/articles/PMC7164913/)
- [Bridging the gap: AI-driven decision-making in the public sector](https://www.sciencedirect.com/science/article/pii/S0740624X24000686)
- [AI in Public Policy - The Decision Lab](https://thedecisionlab.com/reference-guide/computer-science/ai-in-public-policy)

---

## VII. Statistics Quick Reference

For quick citation in writing:

**LLM Limitations:**
- Up to 65% performance drop when numerical values change (GSM-Symbolic)
- GPT-4: <5% hallucination rate on simple tasks, 20-25% for LLaMA 2/DeepSeek
- GPT-4o: 12% on AIME competition math, o1: 74%
- Medical context: 67% accuracy (Med-PaLM, 2022)

**Tool Augmentation Improvements:**
- Medical calculations: 16% → 88% (LLaMA), 4.8% → 64% (GPT)
- Arithmetic tasks: 98-99% with integrated calculator
- Medical AI with RAG: 77.5% → 83.1% accuracy

**Government & Transparency:**
- Dutch government resigned 2021 (benefits scandal)
- EU AI Act: global benchmark for transparency requirements
- O-SAIF founded 2025 for open-source government AI
- PolicyEngine: open-source microsimulation model (UK govt uses)

---

## Conclusion

The research reveals a clear path forward for AI in policy simulation:

1. **Acknowledge limitations**: LLMs cannot reliably perform precise numerical reasoning
2. **Leverage tool augmentation**: Grounding in calculators, APIs, and microsimulation models dramatically improves accuracy
3. **Demand transparency**: Open-source approaches enable democratic accountability and public trust
4. **Combine strengths**: AI for natural language understanding + microsimulation for precision = powerful policy analysis

The vision is neither utopian nor dystopian—it's practical. Build on microsimulation's 70-year tradition of rigorous computation, add AI's natural language capabilities, and maintain open-source transparency. This is how we compute the impact of public policy for the world.

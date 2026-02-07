---
chapters: [9]
primary_chapter: 9
narrative_role: "Salesforce RL system that learned tax policies outperforming classical optimal taxation"
---

# AI Economist

**Paper**: "The AI Economist: Taxation policy design via two-level deep multiagent reinforcement learning"
**Published**: Science Advances, Vol 8, Issue 18, May 4, 2022
**Authors**: Stephan Zheng, Alexander Trott, Sunil Srinivasa, Nikhil Naik, Melvin Gruesbeck, David C. Parkes (Harvard), Richard Socher
**Affiliations**: Salesforce Research + Harvard
**Preprint**: arXiv:2004.13332 (April 2020)
**Code**: github.com/salesforce/ai-economist

## What It Does

Two-level deep reinforcement learning system where:
1. **Economic agents** (workers) learn optimal strategies in a simulated economy
2. **Social planner** (government) learns tax policies that optimize a welfare objective

The key innovation: both levels co-adapt. The government learns tax policy while agents simultaneously learn how to respond to that policy. This captures the strategic interaction that static optimal taxation theory misses.

## Key Results

- AI-derived tax policies improved the equality-times-productivity metric by **>12%** over the Saez optimal taxation framework
- For utilitarian objectives: improvements exceeded **8%**
- The 2020 preprint reported **≥16%** improvement over prominent baselines (varies by configuration)

## Baselines Compared

1. Saez Optimal Taxation — the analytical framework from economic theory
2. U.S. Federal Tax — stylized 2018 progressive schedule
3. Free Market — no taxation

## Key Behaviors Learned

AI-derived policies set higher top tax rates and higher net subsidies for low incomes. The system proved effective against emergent tax-gaming strategies developed by the AI agents.

Human experiments on Amazon Mechanical Turk validated that AI tax policy provided equality-productivity trade-offs similar to Saez while achieving higher social welfare.

## Successor: TaxAgent (Wang et al., 2025)

**Paper**: "TaxAgent: How Large Language Model Designs Fiscal Policy" (arXiv:2506.02838, June 2025)
**Authors**: Jizhou Wang, Xiaodan Fang, Lei Huang, Yongfeng Huang

Replaces the RL social planner with an LLM-based agent. Key difference: the planner reasons in natural language about economic conditions rather than relying purely on reward signals. Uses 50 heterogeneous household agents in 120-month simulations. Outperformed baselines (including AI Economist) on equality-productivity index in long-term (80-120 months).

## Why It Matters for the Book

The AI Economist represents a fundamentally different approach to AI in policy:
- **Tool-use paradigm** (Ch 9 focus): AI calls microsimulation as a tool
- **AI Economist paradigm**: AI *learns* policy directly through simulation

These are complementary. The AI Economist shows AI can discover non-obvious policy designs. But it operates in simplified economies (4 agents, simple production). Real policy requires the precision of deterministic microsimulation for implementation.

The progression: AI Economist (learns policy in simulation) → TaxAgent (LLM reasons about policy) → Cosilico (LLM encodes rules from statute text). Each moves closer to real-world applicability.

## Sources

- [Science Advances publication](https://www.science.org/doi/10.1126/sciadv.abk2607)
- [arXiv preprint](https://arxiv.org/abs/2004.13332)
- [GitHub](https://github.com/salesforce/ai-economist)
- [TaxAgent arXiv](https://arxiv.org/abs/2506.02838)

## Links

- [[ai-integration-philosophy]]
- [[cosilico]]
- [[taxcalcbench]]

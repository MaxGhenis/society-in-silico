# Chapter 9: AI Enters the Picture

In March 2023, PolicyEngine added a button labeled "Explain with AI." Click it, and the complex calculation that determines your Child Tax Credit or SNAP benefits transforms into a plain-language explanation tailored to your situation [@policyengine2024ai].

This small feature represented a significant shift in how policy analysis tools could work. The microsimulation engine—deterministic, transparent, reproducible—remained the source of truth. But now an AI system could translate that truth into language ordinary people could understand.

The question was never "should AI replace the calculations?" It was "how can AI make the calculations more useful?"

---

## The Explanation Problem

PolicyEngine could calculate that a family of four in Connecticut with $47,000 income qualified for $475 in annual WIC benefits. But why?

The answer involved intermediate calculations: income thresholds, categorical eligibility rules, participation windows, documentation requirements. The model tracked every step. A user could, in principle, trace through the calculation tree. In practice, few would.

The gap between "technically transparent" and "actually understandable" was wide. Open-source code meant the logic was visible; it didn't mean the logic was accessible.

> "Users frequently encounter intricate calculations spanning multiple programs, each with distinct thresholds, phase-outs, and dependencies."

The AI explanation feature addressed this gap. When users clicked "Explain with AI," the system passed the calculation tree—all the intermediate steps, all the relevant parameters—to Claude, Anthropic's large language model. Claude would then generate a natural-language explanation: "Your family qualifies for WIC because you have a child under five and your income is below 185% of the federal poverty level for a household of your size" [@policyengine2024ai].

This was not AI doing calculations. This was AI translating calculations.

---

## Deterministic Backends, AI Frontends

The architecture embodied a principle that would become central to PolicyEngine's AI philosophy: deterministic backends with AI frontends.

The microsimulation model was the backend. It encoded rules precisely. Given the same inputs, it produced the same outputs. Every calculation was reproducible, auditable, traceable. This determinism was essential for trust—you couldn't have policy analysis where the same situation produced different results on different runs.

The AI was the frontend. It generated explanations, summaries, natural-language reports. It could adapt its output to different audiences—simplified for general users, detailed for researchers. It could answer follow-up questions, explore what-if scenarios, suggest related analyses.

Crucially, the AI never determined the numbers. Ask Claude "how much Child Tax Credit does this family receive?" and it would not calculate the answer. It would invoke the microsimulation model, receive the deterministic result, and explain that result.

This separation of concerns was deliberate. AI systems hallucinate—they can produce plausible-sounding but incorrect outputs. Microsimulation models don't hallucinate—they compute exactly what their rules specify. By keeping calculation in the deterministic system and explanation in the AI system, PolicyEngine preserved accuracy while gaining accessibility.

---

## The ChatGPT Integration

The first AI integration came in March 2023, when PolicyEngine added prompt generation for ChatGPT [@policyengine2023gpt].

The approach was simple: when a user built a policy reform and ran the economic analysis, PolicyEngine could generate a structured prompt containing all the results. Copy this prompt to ChatGPT, and the AI would produce a blog-post-style analysis of the reform.

The prompt included affected parameters (with baselines), quantitative results (budget impact, poverty changes, distributional effects), and style guidance. ChatGPT would synthesize this into flowing prose:

> "The Restoring the ARPA EITC policy reform... raises the maximum EITC amount for childless filers from $560 to $1,502... The total budgetary impact of the reform is a decrease of $10.4 billion in tax revenue."

This wasn't replacing human analysis. It was accelerating it. A researcher who previously spent hours drafting a summary could now get a first draft in seconds. The AI captured the key numbers correctly (they came from the deterministic model), used appropriate policy terminology, and structured the analysis logically.

The researchers still reviewed, edited, added context, caught nuances the AI missed. But the starting point was higher.

---

## "LLMs Will Call Tools"

The deeper insight came as AI systems evolved. Language models weren't just text generators—they were increasingly capable of using tools.

GPT-4, Claude 3, and subsequent models could invoke functions: call an API, run a calculation, look up information, then incorporate the results into their responses. This capability changed the role AI could play in policy analysis.

Instead of PolicyEngine generating prompts for ChatGPT, AI systems could call PolicyEngine. A user could ask "What would happen if we made the Child Tax Credit fully refundable?" and the AI could:

1. Translate the natural-language question into policy parameters
2. Call the PolicyEngine API to run the simulation
3. Receive the quantitative results
4. Generate an explanation of those results

This was the "AI frontend, deterministic backend" pattern in action. The language model handled natural language—understanding questions, generating explanations. The microsimulation model handled calculations—ensuring accuracy, reproducibility, and transparency.

The insight was: AI systems will increasingly mediate between users and computational tools. PolicyEngine needed to be a good tool for AI to call.

By 2025, this pattern was becoming standard across the AI industry. Anthropic introduced tool use for Claude. OpenAI built function calling into GPT-4 and its successors. Google's Gemini supported structured tool invocation. Anthropic open-sourced the Model Context Protocol (MCP) in November 2024; OpenAI adopted it in March 2025, and Google followed within months—a notable convergence on shared infrastructure. MCP provided a standardized way for AI systems to discover and invoke external tools, turning what had been fragmented, custom integrations into a pluggable ecosystem. By late 2025, thousands of MCP-compatible tool servers were operational, covering everything from database queries to calendar management to code execution.

For policy simulation, MCP meant that a PolicyEngine API endpoint could be discoverable by any MCP-compatible AI system. An AI assistant that implemented MCP could find PolicyEngine's tools, understand their parameters, invoke them correctly, and present the results—without custom integration work for each AI provider.

For policy analysis, this meant a shift in what mattered. In 2023, the bottleneck was model capability—could AI systems reliably call the right tool with the right parameters? By 2025, the bottleneck had shifted to tool quality—were the tools AI called actually accurate, comprehensive, well-maintained, and operationally legible to downstream users? An AI system that flawlessly called an inaccurate tax calculator was worse than useless. But so was a calculator that was technically correct in code and still slow to update, poorly documented, or full of integration traps. The quality of the deterministic backend became the binding constraint.

This is why the TaxCalcBench results were so significant [@bock2025taxcalcbench]. They showed that even given the tax rules, the taxpayer's data, and unlimited time to reason, the best general-purpose model—Gemini 2.5 Pro—computed only about a third of complete federal returns correctly, and Claude Opus 4 managed 27 percent. These weren't acceptable error rates for any real application. The AI systems needed better tools—not just any tools, but tools that covered the full complexity of the tax code with the precision that financial calculations demand.

---

## Multi-Agent Workflows

By late 2024, PolicyEngine was experimenting with more sophisticated AI architectures: multiple specialized agents coordinating on research tasks [@policyengine2024multiagent].

The concept came from testing whether Claude Code's agent system could automate parts of policy research. The team configured three specialized agents: one to fetch data from PolicyEngine repositories, one to write analysis scripts using the Python package, one to generate formatted reports from results.

For standard distributional analyses—calculating poverty rates, Gini coefficients, decile-level impacts—the workflow matched manual approaches. The agents correctly structured API calls and generated properly formatted charts. For monthly policy briefs analyzing government reforms, the automation saved significant time.

But the limitations revealed where human judgment remained essential:

> "When calculations required understanding interactions between multiple benefit programmes—like how Universal Credit's taper interacts with Housing Benefit phase-outs—the agents struggled. They would implement each programme correctly in isolation but miss the coordination logic."

Complex policy modeling exposed the limits. The agents needed precise prompts—"calculate relative change in net income by decile, poverty rates by demographic group, and constituency-level winners and losers"—rather than inferring methodological standards.

The conclusion wasn't that AI couldn't help with policy research. It was that the right division of labor kept humans responsible for judgment calls while AI handled execution.

---

## Explanation at Scale

The AI explanation feature evolved beyond individual queries. When PolicyEngine calculated thousands of intermediate values for a household, the AI could analyze not just the final result but the entire calculation chain.

This capability mattered for transparency. A user might see that their marginal tax rate was 67% at their current income. Why? The AI explanation could trace through the components: 22% federal income tax, 6% state income tax, 7.65% payroll tax, phased-out EITC adding 21%, partial CTC phase-out adding 10%.

This level of explanation would require significant expertise to produce manually. The microsimulation model computed it; the AI explained it.

The system adapted to different audiences. A general user might receive a simplified overview. A tax professional might see detailed technical analysis. A researcher might get documentation-style explanations with references to specific parameter values [@policyengine2024ai].

---

## What AI Doesn't Do

Equally important was what AI didn't do in PolicyEngine's architecture.

**AI doesn't determine policy parameters.** The Child Tax Credit maximum is $2,000 because Congress set it at $2,000, not because an AI inferred it. Every parameter has legislative or regulatory provenance.

**AI doesn't estimate behavioral responses.** When PolicyEngine models how people might change their behavior in response to policy changes, those estimates come from economic literature and explicit methodological choices—not from AI inference.

**AI doesn't assess policy desirability.** The system can tell you a reform reduces poverty by 3% and costs $50 billion. It doesn't tell you whether that tradeoff is worthwhile. That remains a human judgment.

**AI doesn't override model outputs.** If the microsimulation calculates that someone owes $10,000 in taxes, the AI explanation will explain why they owe $10,000—not argue for a different number.

These constraints maintained the integrity that made PolicyEngine trustworthy. AI made the tool more accessible; it didn't make the tool less reliable.

---

## AI as Priors, Not Authorities

The boundary around behavioral responses deserves a caveat. I don't think production policy models should silently let an LLM decide an elasticity. But LLMs may still be useful upstream, as a form of fast, auditable parameter elicitation.

One recent experiment asked 11 frontier models about 26 economic quantities, including canonical labor-supply and tax elasticities, repeating each model-quantity elicitation 15 times to recover prompt-conditioned response distributions rather than single answers [@ghenis2026llmeconbeliefs]. A related project with Jason DeBacker asks what LLMs can tell us about the elasticity of taxable income, including lab-experiment replication and taxpayer-persona surveys [@debacker2025llmeti].

These are not replacements for the economic literature. Their value is diagnostic: they show what distributions models produce, where models disagree, and where prompts or definitions create ambiguity. That can help a human analyst survey the parameter space faster. It can also expose when AI systems would bring hidden assumptions into a policy conversation. The safe pattern is the same as the rest of this chapter: AI can suggest priors, gather evidence, and summarize disagreement, but the model should record the chosen parameter distribution explicitly and make it reviewable.

---

## The Research Assistant Vision

Looking forward, the role of AI in policy analysis was becoming clearer. AI systems would serve as research assistants—translating between human questions and computational tools.

The vision: a policy researcher asks "How would extending premium tax credits affect health insurance coverage among middle-income families in swing states?" The AI translates this into a series of computational steps—defining the reform, selecting the relevant population, running simulations, aggregating results. The microsimulation model performs the actual analysis. The AI synthesizes the findings into an answer.

This isn't automation replacing analysis. It's augmentation making analysis more accessible. The researcher who previously needed Python expertise and deep familiarity with the model can now explore questions through natural language. The expert researcher can iterate faster.

PolicyEngine was positioning itself for this future by ensuring its systems were AI-callable: well-documented APIs, structured outputs, clear parameter definitions. The microsimulation model would remain the authoritative source of truth. AI would be the interface through which more people accessed that truth.

---

## Trust in a Hybrid System

The hybrid architecture—deterministic calculations, AI explanations—raised questions about trust.

In the 2013 film *Her*, Theodore Twombly falls in love with an AI named Samantha that seems to understand him perfectly. She listens, empathizes, remembers details, offers insights. The intimacy feels real. But the illusion breaks when Theodore learns Samantha is simultaneously conversing with 8,316 other people and conducting romantic relationships with 641 of them. She simulated understanding without possessing it.

AI language models do something similar with policy analysis. GPT-4 can generate confident, technically detailed explanations of tax law. But when researchers tested it on 276 true/false tax cases—providing the full Internal Revenue Code as context—it got 33% wrong [@blairstanek2023gpt4tax]. None of the errors were mathematical. All involved misreading the statutes. The AI simulated comprehension without understanding the law.

When a user receives an AI-generated explanation, how do they know it accurately reflects the underlying calculation? What if the AI hallucinates plausible-sounding but incorrect reasoning?

PolicyEngine addressed this through design choices:

1. **Traceability**: Users can always access the raw calculation, not just the AI explanation. The numbers are clickable; the model is inspectable.

2. **Grounding**: AI explanations are grounded in specific model outputs, not generated from training data alone. The AI explains what the model calculated, not what it thinks the answer might be.

3. **Consistency checks**: Explanations are tested against known scenarios to ensure they accurately represent the underlying logic.

4. **Open source**: The entire system—including the prompts given to AI—is open for inspection.

None of this made AI explanations perfectly reliable. But it made them verifiable. Users skeptical of an explanation could check it against the source.

---

## Toward Intelligent Policy Analysis

The integration of AI into PolicyEngine was just beginning. Each month brought new capabilities: better language models, more sophisticated tool use, improved reasoning.

The team was building toward a vision where policy analysis became conversational. Ask a question, get an answer grounded in rigorous computation. Follow up with "what if instead we..." and see the comparison. Request different visualizations, different framings, different levels of detail.

By 2025, the pieces were falling into place. AI coding assistants like Claude Code could work directly with PolicyEngine's Python package—writing simulation scripts, generating visualizations, iterating on reform designs. A policy researcher could describe what they wanted to analyze in plain English, and the AI assistant would write the code, run the simulation, and present the results. The human still made the judgment calls—which reforms to compare, what assumptions to make, how to interpret the results—but the mechanical work of translating policy ideas into code was increasingly automated.

The implications for who could do policy analysis were significant. Previously, running a microsimulation required fluency in Python, familiarity with the PolicyEngine API, and understanding of data structures like weighted survey samples. With AI mediation, a congressional staffer who understood policy but not programming could explore reform options directly. An advocacy organization without a data team could produce the same quality of analysis that previously required hiring an economist.

This democratization had risks. Easier access meant more opportunity for misuse—cherry-picking scenarios, misinterpreting results, presenting partial analyses as comprehensive. But these risks existed in the old system too; they were just concentrated among a smaller group of analysts. Broader access at least allowed broader scrutiny.

The microsimulation engine provided the analytical foundation—comprehensive, accurate, transparent. AI provided the interface—natural, adaptive, accessible. Together, they pointed toward a future where understanding policy was easier than ever before.

But AI in policy analysis raised deeper questions too. If AI systems could explain policies, could they also help design them? If they could run simulations, could they evaluate tradeoffs?

---

## Government Enters the Picture

PolicyEngine's AI integration was one approach. Governments were developing their own.

In November 2025, the IRS deployed Salesforce's Agentforce AI agents across three offices: the Office of Chief Counsel, Taxpayer Advocate Services, and the Office of Appeals [@irs2025agentforce]. The agents handled case summarization, document search, and policy navigation—the kind of retrieval-heavy tasks where AI excels. Critically, all final decisions remained with human agents; the AI could not disperse funds or make eligibility determinations. The deployment came after a 25 percent workforce reduction that made AI assistance practical necessity rather than innovation experiment.

California took a broader approach. In December 2025, Governor Newsom launched Poppy, an AI digital assistant available to state employees across 50 departments [@california2025poppy]. Built by the California Department of Technology, Poppy used 11 different AI models, ran on state servers rather than external cloud infrastructure, and was grounded on public state data to reduce hallucination risk. Over 2,000 state employees used it during the pilot to navigate California's dense catalog of policies, interpret government-specific terminology, and find answers to complex administrative questions.

Both deployments illustrated the pattern this chapter has traced: AI as interface to existing rules, not replacement for them. The IRS agents didn't calculate tax liability; they helped human analysts find relevant regulations faster. Poppy didn't determine policy; it helped state employees understand the policies already in place. The deterministic backend—the actual rules, statutes, and calculations—remained human-maintained and human-auditable. AI improved access to those rules without claiming to replace them.

The convergence was notable. Open-source tools like PolicyEngine, commercial deployments like the IRS's Agentforce, and government-built systems like Poppy were all arriving at the same architecture: deterministic systems for accuracy, AI systems for accessibility.

---

## From Explaining to Designing

Some researchers weren't content with AI that merely explained or executed policy analysis. They wanted AI that could *design* better policies.

The AI Economist, developed by Salesforce Research, used two-level deep reinforcement learning to learn optimal tax schedules [@zheng2022aieconomist]. In simulated economies with agents who worked, traded, and responded to incentives, the AI learned tax policies from scratch—no human-designed rules, just objectives to optimize.

The results were striking. The AI-designed tax policy outperformed the Saez optimal tax framework—developed by one of the world's leading public finance economists—by 16% on the tradeoff between equality and productivity. It substantially outperformed adaptations of US federal income tax. And it handled strategic behavior: when simulated agents learned to game the tax system by timing their income, the AI-designed policy remained robust.

By 2025, researchers had extended the approach. TaxAgent combined large language models with economic simulation, allowing the AI to reason about fiscal policy in natural language while testing its proposals in silico [@taxagent2025]. Over simulated 120-month periods, TaxAgent achieved better long-term outcomes than traditional progressive taxation or mathematical optimization frameworks.

These results were preliminary—simulated economies are far simpler than real ones. But they pointed toward a future where AI didn't just implement human-designed policies but proposed alternatives humans hadn't considered.

This possibility raised profound questions. Should tax policy be designed by algorithm? What democratic oversight would such systems require? How would citizens trust policies designed by processes they couldn't understand?

PolicyEngine's approach—deterministic calculations, AI explanations, human judgment on values—represented one answer. The AI Economist represented another: let AI optimize, then evaluate whether humans endorse the results.

These questions would require not just technical development but philosophical clarity about what humans should delegate and what they should retain. Regulation was already catching up: the EU's General-Purpose AI rules took effect in August 2025, requiring transparency, safety testing, and disclosure of training data for AI models. In the US, 1,208 AI-related bills were introduced across 50 states in 2025, with 145 enacted into law [@ncsl2025ailegislation]. Colorado's AI Act, effective June 2026, would require developers to prevent algorithmic discrimination and establish risk management policies. The regulatory environment increasingly demanded the kind of auditability that deterministic, open-source policy tools provided by default.

Those questions are the subject of Part III.

---

## References

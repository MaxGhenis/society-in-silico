# Chapter 7: AI Enters the Picture

In March 2023, PolicyEngine added a button labeled "Explain with AI." Click it, and the complex calculation that determines your Child Tax Credit or SNAP benefits transforms into a plain-language explanation tailored to your situation {cite}`policyengine2024ai`.

This small feature represented a significant shift in how policy analysis tools could work. The microsimulation engine—deterministic, transparent, reproducible—remained the source of truth. But now an AI system could translate that truth into language ordinary people could understand.

The question was never "should AI replace the calculations?" It was "how can AI make the calculations more useful?"

---

## The Explanation Problem

PolicyEngine could calculate that a family of four in Connecticut with $47,000 income qualified for $475 in annual WIC benefits. But why?

The answer involved intermediate calculations: income thresholds, categorical eligibility rules, participation windows, documentation requirements. The model tracked every step. A user could, in principle, trace through the calculation tree. In practice, few would.

The gap between "technically transparent" and "actually understandable" was wide. Open-source code meant the logic was visible; it didn't mean the logic was accessible.

> "Users frequently encounter intricate calculations spanning multiple programs, each with distinct thresholds, phase-outs, and dependencies."

The AI explanation feature addressed this gap. When users clicked "Explain with AI," the system passed the calculation tree—all the intermediate steps, all the relevant parameters—to Claude, Anthropic's large language model. Claude would then generate a natural-language explanation: "Your family qualifies for WIC because you have a child under five and your income is below 185% of the federal poverty level for a household of your size" {cite}`policyengine2024ai`.

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

The first AI integration came in March 2023, when PolicyEngine added prompt generation for ChatGPT {cite}`policyengine2023gpt`.

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

---

## Multi-Agent Workflows

By late 2024, PolicyEngine was experimenting with more sophisticated AI architectures: multiple specialized agents coordinating on research tasks {cite}`policyengine2024multiagent`.

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

The system adapted to different audiences. A general user might receive a simplified overview. A tax professional might see detailed technical analysis. A researcher might get documentation-style explanations with references to specific parameter values {cite}`policyengine2024ai`.

---

## What AI Doesn't Do

Equally important was what AI didn't do in PolicyEngine's architecture.

**AI doesn't determine policy parameters.** The Child Tax Credit maximum is $2,000 because Congress set it at $2,000, not because an AI inferred it. Every parameter has legislative or regulatory provenance.

**AI doesn't estimate behavioral responses.** When PolicyEngine models how people might change their behavior in response to policy changes, those estimates come from economic literature and explicit methodological choices—not from AI inference.

**AI doesn't assess policy desirability.** The system can tell you a reform reduces poverty by 3% and costs $50 billion. It doesn't tell you whether that tradeoff is worthwhile. That remains a human judgment.

**AI doesn't override model outputs.** If the microsimulation calculates that someone owes $10,000 in taxes, the AI explanation will explain why they owe $10,000—not argue for a different number.

These constraints maintained the integrity that made PolicyEngine trustworthy. AI made the tool more accessible; it didn't make the tool less reliable.

---

## The Research Assistant Vision

Looking forward, the role of AI in policy analysis was becoming clearer. AI systems would serve as research assistants—translating between human questions and computational tools.

The vision: a policy researcher asks "How would extending premium tax credits affect health insurance coverage among middle-income families in swing states?" The AI translates this into a series of computational steps—defining the reform, selecting the relevant population, running simulations, aggregating results. The microsimulation model performs the actual analysis. The AI synthesizes the findings into an answer.

This isn't automation replacing analysis. It's augmentation making analysis more accessible. The researcher who previously needed Python expertise and deep familiarity with the model can now explore questions through natural language. The expert researcher can iterate faster.

PolicyEngine was positioning itself for this future by ensuring its systems were AI-callable: well-documented APIs, structured outputs, clear parameter definitions. The microsimulation model would remain the authoritative source of truth. AI would be the interface through which more people accessed that truth.

---

## Trust in a Hybrid System

The hybrid architecture—deterministic calculations, AI explanations—raised questions about trust.

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

The microsimulation engine provided the analytical foundation—comprehensive, accurate, transparent. AI provided the interface—natural, adaptive, accessible. Together, they pointed toward a future where understanding policy was easier than ever before.

But AI in policy analysis raised deeper questions too. If AI systems could explain policies, could they also help design them? If they could run simulations, could they evaluate tradeoffs? These questions would require not just technical development but philosophical clarity about what humans should delegate and what they should retain.

Those questions are the subject of Part III.

---

## References

```{bibliography}
:filter: docname in docnames
```

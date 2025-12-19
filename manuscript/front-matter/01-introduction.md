# Introduction: The Model and the World

<!--
Opening options:

OPTION A - Westworld hook:
Open with Serac and Rehoboam. The French trillionaire who watched Paris burn,
then built an AI to predict and control human behavior. His solution to chaos:
eliminate freedom. "I don't predict the future—I create it."

Then the pivot: This isn't just fiction. We're already building societal models.
The question is whether they'll be Serac's closed system or something democratic.

OPTION B - Policy analyst scene:
A budget analyst running simulations the night before a major vote.
The human moment behind the computational process. Then zoom out to the stakes.

OPTION C - GPT-4 fails at taxes:
Open with the surprising finding: GPT-4 gets only 67% of tax questions right.
The world's most capable AI can't reliably calculate your refund.
This is the problem—and the opportunity.

RECOMMENDATION: Start with Option A (Westworld), transition through C (AI limitations),
end with the democratic alternative vision.
-->

## Draft Opening

In the 2020 third season of Westworld—HBO's science fiction series about artificial consciousness and control—we meet Engerraund Serac, a French trillionaire who watched a thermonuclear incident destroy Paris, then spent decades building an AI called Rehoboam to ensure it never happened again. His system predicted individual human lives: when you'd get sick, lose your job, take your own life. It assigned people to "paths" and manipulated society to make those predictions come true. Those who didn't fit the predictions—the "outliers"—were flagged for "reconditioning."

Serac's philosophy: "I don't predict the future. I create it."

The show had explored this territory before: "A human is just a brief algorithm. 10,247 lines." People reduced to code without their knowledge or consent.

When I first watched this, I recognized the premise. Since 2018, I've built microsimulation systems that model society computationally—tools that predict how policies affect households, that simulate economies with millions of synthetic people. The Westworld writers had taken the same technology and followed it to its darkest conclusion.

But they'd also revealed a fork in the road.

Serac's system was closed: one man decided what "optimal" meant, and everyone else lived inside his model without knowing it. What if the model were open? What if anyone could query it, challenge its assumptions, propose alternatives? What if simulation were infrastructure for democratic deliberation rather than autocratic control?

That's what this book is about.

---

## The Stakes

We don't have Rehoboam. But we're not starting from zero either.

Governments use predictive models to allocate benefits, assess fraud risk, set policy. Insurance companies price your premiums based on algorithms you can't inspect. Banks decide your creditworthiness with models they won't explain. AI assistants confidently give tax advice that's wrong a third of the time—GPT-4 achieves only 67% accuracy on basic tax questions.[^gpt4-tax]

The question isn't whether we'll have computational models of society. We do. The question is:

- **Who builds them?** Closed institutions or open communities?
- **Who can access them?** Only the powerful or everyone?
- **What are they for?** Control or understanding?

## The Alternative

This book traces a different path—from [[guy-orcutt|Guy Orcutt]]'s 1957 vision of simulating individual households, through six decades of institutional models locked inside government agencies, to the open source movement that's making these tools public infrastructure.

I'll trace the story through my own journey: from Google data scientist to MIT economist to founder of [[policyengine|PolicyEngine]] and [[cosilico|Cosilico]]. But it's not my story. It's the story of a technology that's been waiting for its democratic moment.

**Society needs a shared model to reason against.** Congress debates with napkin math. Voters can't see how policies affect their own families. AI hallucinates eligibility rules. We can do better.

What if everyone could:
- See how a proposed tax change would affect their household?
- Understand who gains and loses from a policy reform?
- Test their assumptions about how society works?
- Contribute to making the model more accurate?

That's not Rehoboam. That's the opposite of Rehoboam.

---

## Key Themes

1. **The gap between policy debates (emotional, tribal) and policy analysis (computational, precise)**—and how to bridge it without technocracy

2. **Models as translation devices**—turning raw data and dense legislation into comprehensible impact

3. **The democratization thesis**—simulation tools are becoming public infrastructure, shifting power from institutions to citizens

4. **The AI question**—what LLMs can and can't do, and why deterministic tools matter more than ever

5. **Open source as philosophy**—transparency as democratic value, not just engineering practice

## What's Ahead

**Part I: Origins** traces the intellectual history—from [[guy-orcutt|Orcutt]]'s frustration with aggregate models in 1957, through [[dynasim|DYNASIM]]'s mainframe ambitions, to the [[ifs-taxben|IFS]] and [[taxsim|NBER]] models that shaped policy for decades.

**Part II: Building** follows the open source turn—[[openfisca|OpenFisca]] in France, [[policyengine|PolicyEngine]] spanning US and UK, the reality of encoding law as [[rules-as-code|code]].

**Part III: Future** confronts the AI moment—what changes when language models can help write rules, when agents need reliable tools, when "society in silico" becomes feasible at scale.

The book ends where we started: at the fork in the road. Serac's path or the open one. The choice is being made now, in code and policy and institutional design. This is my case for the democratic alternative.

---

## Research Links

- [[rehoboam-contrast]]
- [[cosilico]]
- [[microsimulation-definition]]
- [[guy-orcutt]]
- [[policyengine]]
- [[dynasim]]
- [[ifs-taxben]]
- [[taxsim]]
- [[openfisca]]
- [[rules-as-code]]

[^gpt4-tax]: Blair-Stanek et al. (2023), "Can GPT-4 Really Do Tax?" Researchers posed 276 true/false tax cases to GPT-4 with the full Internal Revenue Code provided. GPT-4 got 186 correct (67%). None of the errors were mathematical—all involved misreading the statutes. arXiv:2309.09992

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

"I don't predict the future. I create it."

That line comes from Engerraund Serac, the antagonist of Westworld's third season. After watching a thermonuclear incident destroy Paris, Serac built an AI called Rehoboam that predicted individual human lives—when you'd get sick, lose your job, die. The system didn't just forecast; it manipulated society to make its predictions come true. People who deviated from their predicted paths got flagged for "reconditioning."

The show's premise: humans are "just a brief algorithm," reducible to code. The horror: one man controlling that algorithm without anyone else knowing.

When I watched this in 2020, I recognized the technology. I'd been building microsimulation systems since 2018—computational models that predict how tax policies affect households, that simulate entire economies with millions of synthetic people. The Westworld writers had taken the same tools and followed them to their darkest conclusion.

They'd also revealed a choice we're making right now.

Serac's system was closed: he decided what "optimal" meant, and everyone else lived inside his model without consent. But computational models of society don't have to work that way. What if anyone could query the model? Challenge its assumptions? Propose alternatives? What if simulation became public infrastructure for democratic deliberation, not a tool for autocratic control?

That's the fork in the road. That's what this book is about.

---

## The Stakes

We don't have Rehoboam. But we're not starting from zero.

Governments already use predictive models to allocate benefits, assess fraud risk, shape policy. Insurance companies price your premiums with algorithms you can't inspect. Banks decide your creditworthiness with models they won't explain. And AI assistants—including GPT-4, the most capable language model when I started writing this—get only 67% of basic tax questions right.[^gpt4-tax]

These models exist. The question is who controls them.

**Who builds them?** Closed institutions or open communities?

**Who can access them?** Only the powerful or everyone?

**What are they for?** Optimization or understanding?

## The Alternative

Society needs a shared model to reason against. Right now, Congress debates tax policy with napkin math. Voters can't calculate how reforms affect their own households. AI confidently hallucinates benefit eligibility rules.

This book traces a different path—from [[guy-orcutt|Guy Orcutt]]'s 1957 vision of simulating individual households, through six decades of institutional models locked inside government agencies, to the open source movement making these tools public infrastructure.

The democratic alternative looks like this:

- Anyone can see how a proposed policy change affects their household
- Anyone can understand who gains and loses from a reform
- Anyone can test their assumptions about how society works
- Anyone can contribute to making the model more accurate

I'll tell this story through my own path—from learning discrete-event simulation at Berkeley, to building headcount forecasts at Google, to discovering that the same tools could illuminate policy questions that affected my family personally. The thread running through it all: simulation as a way to make complex systems comprehensible. But this isn't my story alone. It's the story of a technology that's been waiting sixty years for its democratic moment.

That's not Rehoboam. That's the opposite of Rehoboam.

---

## Key Themes

**The gap between policy debates and policy analysis.** Political arguments run on emotion and tribal loyalty. Policy analysis runs on computation and precision. Bridging that gap without sliding into technocracy is the central challenge.

**Models as translation devices.** They turn raw administrative data and dense legislation into comprehensible impact. A 300-page tax bill becomes "your family pays $1,200 less next year."

**The democratization thesis.** Simulation tools are becoming public infrastructure. Power is shifting from institutions that guard models to communities that build them in the open.

**The AI question.** What language models can and can't do, and why deterministic tools matter more than ever when AI makes everything else probabilistic.

**Open source as philosophy.** Transparency is a democratic value, not just an engineering practice.

## What's Ahead

**Part I: Origins** traces the intellectual history—from [[guy-orcutt|Orcutt]]'s frustration with aggregate models in 1957, through [[dynasim|DYNASIM]]'s mainframe ambitions, to the [[ifs-taxben|IFS]] and [[taxsim|NBER]] models that shaped policy for decades.

**Part II: Building** follows the open source turn—[[openfisca|OpenFisca]] in France, [[policyengine|PolicyEngine]] spanning US and UK, the reality of encoding law as [[rules-as-code|code]].

**Part III: Future** confronts the AI moment—what changes when language models help write rules, when agents need reliable tools, when simulating society at scale becomes technically feasible.

The book ends where it started: at the fork in the road. The choice between Serac's closed system and the democratic alternative is being made right now, in code and policy and institutional design. This is the case for the open path.

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

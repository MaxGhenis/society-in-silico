# Chapter 15: Society in Silico

We return to where we started: Engerraund Serac standing in his control room, watching Rehoboam's predictions cascade across holographic displays. Individual lives reduced to trajectories. Society optimized according to one man's definition of optimal. "I don't predict the future," he says. "I create it."

That's one vision of society in silico.

This book has traced another.

---

## Two Paths

Both paths start from the same recognition: complex social systems can be modeled computationally. Policies can be simulated before they're enacted. Populations can be represented as millions of synthetic households. Elections can be gamed out in code.

But they diverge immediately after.

**Serac's path:**
- The model is closed. Only he sees it.
- The predictions are hidden. People live inside the model without knowing it.
- Optimization is unilateral. His values, his objective function, his paths.
- Uncertainty is suppressed. Rehoboam speaks in certainties.
- Power concentrates. Those without access are subjects, not participants.

**The open path:**
- The model is public. Anyone can inspect the code.
- The predictions are accessible. People can query their own outcomes.
- Values are contested. Multiple objectives, multiple stakeholders, no single optimizer.
- Uncertainty is quantified. Confidence intervals, not false precision.
- Power distributes. The tools of analysis become public infrastructure.

Every chapter of this book has been about building the second path.

---

## What We've Built

Guy Orcutt imagined simulating the economy household by household in 1957. For decades, that vision was realized only inside government agencies—Congressional Budget Office, Joint Committee on Taxation, Treasury—accessible to the powerful, invisible to citizens.

OpenFisca cracked open the model in France. The code was published. Anyone could run it. Rules as code became a movement: legislation should be readable by machines and humans alike.

PolicyEngine extended this to the US and UK, adding a web interface that lets anyone—not just programmers—see how policies affect their household. The household view: "How does this tax credit affect me?" The society view: "Who gains and who loses across the population?"

Cosilico is building the next layer: infrastructure that lets AI agents encode rules from authoritative sources with empirical validation. Not AI replacing analysis—AI using deterministic tools to ground its reasoning.

HiveSight simulates opinions. Democrasim simulates elections. Squigglepy quantifies uncertainty. Each component addresses a layer of the problem.

Together, they form the beginnings of democratic simulation infrastructure.

---

## What We Haven't Built

Let me be honest about what's incomplete.

**Uncertainty quantification is partial.** PolicyEngine gives point estimates. "This reform costs $50 billion." It should say: "This reform costs $50 billion, 90% CI [$35B, $68B]." We've identified the problem; we haven't solved it everywhere.

**Value forecasting is untested.** Chapter 14 proposed an empirical research program. Train on historical survey data, validate on held-out periods, project to long reflection. The experiment hasn't been run. It might fail.

**Adoption is early.** PolicyEngine has thousands of users, but policy debates still happen mostly without it. The tools exist; the cultural change hasn't fully occurred.

**AI integration is nascent.** Cosilico isn't launched. The vision of AI agents reliably using deterministic microsimulation is closer to prototype than production.

This book describes aspiration as much as achievement. We're partway up the mountain, not at the summit.

---

## The Honest Caveat

There's a version of this book that would claim: "We've solved policy analysis. We've democratized the tools. We've shown AI how to reason about society. The future is bright."

That would be false.

The more honest version: We've demonstrated that open simulation infrastructure is possible. We've built enough to show the concept works. We've identified the gaps that remain. The question now is execution.

Can we add uncertainty quantification before trust erodes? Can we validate value forecasting empirically? Can we scale adoption beyond early adopters? Can we build the AI integrations that let these tools compound?

The answers aren't known. The work is ongoing.

---

## Why It Matters

If society can't reason about itself, it can't govern itself.

The alternative to open simulation isn't human judgment uncorrupted by models. It's:

**Black-box decisions by agencies with proprietary tools.** The government runs simulations you can't see. Experts disagree about their assumptions. You're asked to trust outputs you can't verify.

**Vibes-based policy debate.** Politicians wave hands. Pundits assert confidently. Numbers float by without sources. Anyone with a megaphone claims authority; none provide audit trails.

**AI systems aligned to current values without understanding how values evolve.** LLMs trained on today's preferences, frozen in place, even as humanity's considered views change.

**Power concentrated in those with access to compute and data.** The rich can simulate; the poor guess. Corporations optimize; citizens react. The asymmetry compounds.

Open simulation addresses each failure mode:
- Auditable code instead of black boxes
- Reproducible results instead of vibes
- Value forecasting instead of frozen alignment
- Public infrastructure instead of private advantage

It's not guaranteed to help. But the counterfactual is worse.

---

## The Democratic Argument

The deepest case for open simulation is democratic.

Democracy requires shared understanding. We vote on policies without knowing their effects. We debate taxes without calculating impacts. We judge politicians without auditing claims.

This isn't ignorance by choice—it's ignorance by limitation. The tools to understand policy were, until recently, locked inside institutions. Expert analysis was expensive and inaccessible. Citizens had opinions; experts had models; the two rarely connected.

Open microsimulation changes the equation. Now a voter can ask: "What would this candidate's tax plan do to my family?" and get an answer. Not from a partisan think tank. Not from a cable news pundit. From a transparent model they can inspect.

That's not utopia. Many won't use the tools. Many will distrust them. Many will find reality uncomfortable. But the marginal improvement matters.

A voter with accurate information may still vote against their economic interest for other reasons—values, identity, loyalty. That's their right. But a voter who wants to know can know. The option exists.

And if enough voters use the option, electoral dynamics shift. Politicians can be held to calculable claims. Platforms can be stress-tested against distributional analysis. The signal-to-noise ratio of democratic deliberation improves.

---

## The AI Argument

As AI systems become more capable, they'll increasingly be asked questions about policy.

"What would happen if we expanded the child tax credit?"
"How would a carbon tax affect my family?"
"Which candidate's healthcare plan would benefit me more?"

The AI can respond in two ways:

**Option 1: Make stuff up.** Draw on training data, synthesize plausible-sounding text, perhaps hallucinate eligibility rules or invent statistics. This is what happens today. GPT-4 gets tax questions right 67% of the time—worse than a coin flip for true/false {cite}`blairstanek2023gpt4tax`.

**Option 2: Call reliable tools.** Use PolicyEngine as a backend. Look up actual parameters from Cosilico's validated rules. Calculate instead of guess. Return auditable results.

This is the AI case for open simulation: LLMs need tools to call. Those tools should be accurate, transparent, and well-maintained. Building them is infrastructure investment that compounds as AI capabilities grow.

The alternative is AI confidently wrong about policy—a future where more people have access to information that's less reliable. That's not progress.

---

## The Work Ahead

If I'm still building these tools in five years, what does success look like?

**PolicyEngine covers more countries.** Not just US and UK, but every jurisdiction with sufficient data. Tax-benefit models as global infrastructure.

**Uncertainty is quantified.** Every estimate comes with confidence intervals. Users see ranges, not false precision.

**Cosilico works at scale.** AI agents reliably encode rules from statutes. Validation against authoritative oracles is automatic. The human-AI partnership produces rules faster and more accurately than either alone.

**Value forecasting has been tested.** We know whether historical validation works. We know how far forward projections are reliable. We've integrated (or abandoned) the approach based on evidence.

**Adoption is mainstream.** Policy debates reference open models. Journalists query microsimulations. Voters compare candidates using shared infrastructure. The asymmetry of analysis has flattened.

Some of this will happen. Some won't. The vision adjusts as reality teaches.

---

## An Invitation

This book ends with an invitation.

The work is open. The code is public. The communities are forming. If any of this resonates—the vision of transparent policy analysis, of AI grounded in reliable tools, of democratic deliberation informed by shared models—there's a way to participate.

Use the tools. Calculate your taxes on PolicyEngine. Simulate policy reforms. Find the bugs and report them.

Contribute to the code. Microsimulation models need maintenance. Rules change. Parameters update. The work never ends.

Join the conversation. Policy analysis shouldn't be an insider sport. The debates should include everyone the policies affect.

Build on the infrastructure. HiveSight started as an experiment. Democrasim is a prototype. Value forecasting is a thesis. Each could be developed further by others.

Or challenge the premise. Maybe open simulation is misguided. Maybe the tools entrench technocracy rather than democratizing it. Maybe the assumptions are wrong in ways I can't see. The argument improves through critique.

---

## Closing the Loop

In Westworld, Serac's system ultimately fails. Rehoboam couldn't handle the chaos introduced by Dolores and the other hosts—beings who didn't fit its model, whose choices it couldn't predict. The closed system shattered on contact with genuine novelty.

The fiction was too neat, but the lesson holds.

Closed systems are brittle. They optimize for their assumptions. When the world shifts—and it always shifts—they break in ways their designers didn't anticipate.

Open systems are different. They expose assumptions. They invite correction. They adapt as understanding improves. They're never finished, but they're also never frozen.

Society in silico isn't about predicting the future with certainty. It's about creating tools that help us reason about possible futures with calibrated uncertainty.

Not: "This reform will cost $50 billion and save 10,000 lives."

But: "Our best estimate is $50 billion [90% CI: $35B-$68B] and 10,000 lives [90% CI: 7,000-13,000], based on assumptions you can inspect in the code, with uncertainty that reflects what we don't know."

That's not a prediction machine. It's a reasoning aid.

---

*Can simulation help society realize its goals?*

The question that opened this book has no definitive answer. Simulation can't tell us what to value. It can't guarantee we'll use insights wisely. It can't prevent bad-faith actors from gaming the tools.

What it can do is make the invisible visible. The distributional effects hidden in policy details. The uncertainty masked by point estimates. The values implicit in optimization targets. The trajectories of moral change across generations.

Making these visible doesn't solve politics. It informs it.

And that, in the end, is the aspiration. Not a perfect model of society. Not a machine that optimizes humanity. Just tools—open, transparent, uncertainty-aware—that help us see more clearly what we're choosing and why.

The work continues. The invitation stands.

Welcome to society in silico.


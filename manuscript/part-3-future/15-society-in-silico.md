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

The path from there to here wasn't linear. It required several things to happen in sequence.

First, the computers had to get fast enough. Orcutt's 1961 Microanalysis of Socioeconomic Systems pushed the limits of mid-century mainframes. By the 2000s, a laptop could run simulations that once required institutional computing infrastructure. By the 2020s, cloud computing made it possible to run millions of household simulations in seconds.

Second, the data had to improve—and become accessible. The Current Population Survey, the Survey of Consumer Finances, IRS public-use files, administrative records from government agencies. Each data source added resolution to the picture of who Americans are and what they earn. Enhanced microdata techniques—combining multiple sources through statistical matching—pushed accuracy further.

Third, the code had to go open. OpenFisca cracked open the model in France. The code was published. Anyone could run it. Rules as code became a movement: legislation should be readable by machines and humans alike. In the US, the Open Source Policy Center at AEI demonstrated that rigorous tax microsimulation could be built transparently. UKMOD showed that cross-national models could be freely available.

Fourth, the interface had to democratize. PolicyEngine extended open-source microsimulation to the US and UK, adding a web interface that lets anyone—not just programmers—see how policies affect their household. The household view: "How does this tax credit affect me?" The society view: "Who gains and who loses across the population?"

Fifth, the Axiom Foundation began encoding statutes as code—structured, versioned, testable representations of tax and benefit law, kept open as a public good so that AI agents and applications can query the rules with empirical validation. Its counterpart, the Brier Institute, took the modeling-and-forecasting side—now home to PolicyEngine's microsimulation alongside calibration-native prediction—open, scored answers to the questions law can't settle with certainty: how a population will respond, how values will shift. Not AI replacing analysis—AI using deterministic rules and calibrated forecasts to ground its reasoning.

The scale of what's been built is easy to understate because it accumulated gradually. PolicyEngine US encodes thousands of federal and state tax-benefit rules. The Enhanced CPS integrates five datasets, calibrated to over 9,000 administrative totals. Microimpute, MicroCalibrate, and Microplex are pulling pieces of the data pipeline into reusable packages rather than burying them in one model. Validation partnerships with NBER and the Federal Reserve Bank of Atlanta cross-check calculations against independent implementations. MyFriendBen screens families for benefits across four states using the same calculation engine. More than 100 contributors have written code. The codebase runs to hundreds of thousands of lines.

HiveSight explores opinion simulation. Democrasim explores electoral mechanisms. Squigglepy quantifies uncertainty. State legislative tracking and AI-assisted bill triage show how the stack could monitor policy changes in real time. Each component addresses a layer of the problem.

Together, they form the beginnings of democratic simulation infrastructure. No single piece is complete. But the architecture is visible: deterministic rule engines at the foundation, microsimulation models in the middle, AI interfaces at the top, and uncertainty quantification threaded through every layer.

---

## What We Haven't Built

Let me be honest about what's incomplete.

**Uncertainty quantification is partial.** PolicyEngine gives point estimates. "This reform costs $50 billion." It should say: "This reform costs $50 billion, 90% CI [$35B, $68B]." We've identified the problem; we haven't solved it everywhere.

**Value forecasting is preliminary.** Chapter 14 described initial experiments—17 GSS variables, promising but limited results. The full research program—systematic validation across dozens of variables, cross-national replication, longer forecast horizons—remains to be done. The early results might not generalize.

**Adoption is early.** PolicyEngine has thousands of users, but policy debates still happen mostly without it. When Congress debated the 2025 TCJA extension, the public conversation was shaped by CBO scores and think tank estimates, not by citizens running their own analyses. The tools exist; the cultural change hasn't fully occurred. Moving from "available" to "expected" is a transition that took weather forecasting decades—probabilistic precipitation forecasts existed long before the public demanded them.

**AI integration is nascent.** Axiom and the Brier Institute are early. The vision of AI agents reliably using deterministic microsimulation—and calibrated forecasts—is closer to prototype than production. When someone asks an AI assistant about tax policy today, the response comes from training data, not from a calculation engine. The infrastructure that would make tool-calling the default for policy questions doesn't yet exist at production scale.

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

**AI systems trained on current values without understanding how values evolve.** LLMs learn from today's preferences, even as humanity's considered views change.

**Power concentrated in those with access to compute and data.** The rich can simulate; the poor guess. Corporations optimize; citizens react. The asymmetry compounds. When a hedge fund can model the distributional impact of a tax reform in minutes and a community organization can't, the hedge fund's perspective dominates the policy conversation—not because it's right, but because it arrives first and with numbers attached.

These aren't hypothetical failure modes. They describe the current default. The Joint Committee on Taxation produces revenue estimates Congress relies on, using models Congress can't inspect. States allocate billions in benefits using eligibility rules that recipients can't fully understand. AI chatbots confidently answer tax questions wrong a third of the time. The question isn't whether we need better tools—it's whether the tools serve the public or just the institutions that build them.

Open simulation addresses each failure mode: auditable code instead of black boxes, reproducible results instead of vibes, empirical evidence about value change instead of treating today's preferences as fixed, public infrastructure instead of private advantage. It's not guaranteed to help. But the counterfactual is worse.

---

## The Democratic Argument

The deepest case for open simulation is democratic.

Democracy requires shared understanding. We vote on policies without knowing their effects. We debate taxes without calculating impacts. We judge politicians without auditing claims.

This isn't ignorance by choice—it's ignorance by limitation. The tools to understand policy were, until recently, locked inside institutions. Expert analysis was expensive and inaccessible. Citizens had opinions; experts had models; the two rarely connected.

Open microsimulation changes the equation. Now a voter can ask: "What would this candidate's tax plan do to my family?" and get an answer. Not from a partisan think tank. Not from a cable news pundit. From a transparent model they can inspect.

Consider what this means concretely during an election. A presidential candidate proposes making the 2017 tax cuts permanent. The opposition claims it's a giveaway to the rich. The candidate claims it helps the middle class. Both cite numbers. Neither cites sources a voter can verify. With open microsimulation infrastructure, an independent analysis appears within hours—not from one think tank, but from multiple users running the same open model with different assumptions. A voter can enter their own household circumstances and see the specific dollar impact. A journalist can compare the distributional claims against the actual calculation. The debate still involves values—how much redistribution is desirable, how to weigh growth against equity—but it proceeds from a shared factual baseline rather than dueling assertions.

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

**Option 1: Make stuff up.** Draw on training data, synthesize plausible-sounding text, perhaps hallucinate eligibility rules or invent statistics. This is what happens today. Even frontier models get fewer than one in three complete tax returns right [@bock2025taxcalcbench].

**Option 2: Call reliable tools.** Use PolicyEngine as a backend. Look up actual parameters from the Axiom Foundation's open encodings. Calculate instead of guess. Return auditable results.

The infrastructure for Option 2 is maturing. AI systems in 2025 can call external tools through standardized protocols—Model Context Protocol, function calling APIs, tool-use frameworks that let language models invoke deterministic calculations and return structured results. The IRS has deployed Salesforce's Agentforce AI agents for case summarization and policy searching. California's Poppy digital assistant helps state employees navigate dense policy catalogs. These are early steps, but they establish the pattern: AI as interface, deterministic systems as backend.

The key insight is that tool-calling AI compounds the value of every tool it can access. A microsimulation model that takes ten minutes to learn serves one researcher. The same model, accessible through an AI agent, serves anyone who can ask a question in natural language. The infrastructure investment in encoding rules accurately, validating calculations, and maintaining the codebase as laws change pays dividends proportional to how many AI agents call it—and that number is growing exponentially.

This is the AI case for open simulation: LLMs need tools to call. Those tools should be accurate, transparent, and well-maintained. Building them is infrastructure investment that compounds as AI capabilities grow.

The alternative is AI confidently wrong about policy—a future where more people have access to information that's less reliable. That's not progress.

---

## The Work Ahead

If I'm still building these tools in five years, what does success look like?

**PolicyEngine covers more countries.** Not just US and UK, but every jurisdiction with sufficient data. The tax-benefit rules of each country encoded as testable code. The underlying framework—PolicyEngine Core—is already country-agnostic; what's needed is the painstaking work of encoding each nation's specific rules and finding representative microdata. A dozen countries would be ambitious. A hundred would be transformative.

**Uncertainty is quantified.** Every estimate comes with confidence intervals. Users see ranges, not false precision. "This reform costs $50 billion [90% CI: $35B-$68B]" rather than "this reform costs $50 billion." The methodology exists—Monte Carlo simulation over uncertain parameters, bootstrapping over survey weights. The engineering work to integrate it into production tools is substantial but tractable.

**The Axiom Foundation scales.** Statutes encoded as structured, versioned, testable code—covering federal tax law, state tax codes, benefit programs, and eventually regulations beyond the tax-benefit system—delivered as open, self-hostable bundles that any application can call. AI agents help encode rules from authoritative sources, validate against established calculators, and maintain the codebase as laws change. The human-AI partnership produces rules faster and more accurately than either alone.

**Value forecasting has faced a real validation program.** We know whether models trained on past survey data can predict future survey responses. We know how far forward projections are reliable. We've integrated (or abandoned) the approach based on evidence. The preliminary results from Chapter 14—17 GSS variables showing better-than-naive forecasting for most items—either generalize to a broader set of variables and longer horizons, or they don't. Either way, we'll know.

**Adoption is mainstream.** Policy debates reference open models. Journalists query microsimulations. Voters compare candidates using shared infrastructure. When a presidential candidate releases a tax plan, independent distributional analysis appears within hours—not from a single think tank, but from dozens of users running the same open tools with different assumptions. The asymmetry of analysis has flattened. Benefits navigators use the same calculation engine as Congressional staff. Financial coaches for low-income families can show clients exactly how a raise will interact with benefit phase-outs—not approximately, but precisely, accounting for every program they receive.

**AI systems call reliable tools.** When someone asks an AI assistant about tax policy, the response is grounded in deterministic calculations from validated models, not generated from training data alone. The infrastructure we're building becomes part of the AI stack—the equivalent of a calculator for policy questions.

**AI economic shocks become policy-simulation problems.** The most useful near-term question may not be "what will AI do to the economy?" but "under a given AI-labor shock, which tax and transfer systems best protect households?" PolicyEngine's AI-inequality research frames exactly that mediation problem: AI economic shocks, policy interventions, then distributional outcomes across income, consumption, and wealth [@policyengine2026aiinequality]. That is a good stress test for society-in-silico infrastructure because it combines scenario uncertainty, behavioral response, fiscal capacity, and distributional values without pretending the model can forecast the whole future.

Some of this will happen. Some won't. The vision adjusts as reality teaches. Five years ago, I would not have predicted that HM Treasury would formally evaluate PolicyEngine as infrastructure. I would not have predicted that AI systems would be capable of encoding statutes. The specifics are unpredictable; the direction is clear.

---

## An Invitation

This book ends with an invitation.

The work is open. The code is public. The communities are forming. If any of this resonates—the vision of transparent policy analysis, of AI grounded in reliable tools, of democratic deliberation informed by shared models—there's a way to participate.

Use the tools. Calculate your taxes on PolicyEngine. Simulate policy reforms. Find the bugs and report them.

Contribute to the code. Microsimulation models need maintenance. Rules change. Parameters update. The work never ends.

Join the conversation. Policy analysis shouldn't be an insider sport. The debates should include everyone the policies affect.

Build on the infrastructure. HiveSight started as an experiment. Democrasim is a prototype. Value forecasting is a thesis. Each could be developed further by others.

Or challenge the premise. Maybe open simulation is misguided. Maybe the tools entrench technocracy rather than democratizing it—giving quantitative arguments more weight than they deserve, privileging what's measurable over what matters. Maybe the assumptions embedded in microsimulation models (rational actors, stable preferences, government-defined household structures) encode biases that open-source transparency can't fix. Maybe the people who need these tools most will never use them, and the people who use them most don't need them. The argument improves through critique, and the most useful critique comes from people who engage with the specifics rather than dismissing the project in principle.

---

## Closing the Loop

In Westworld, Serac's system ultimately fails. Rehoboam couldn't handle the chaos introduced by Dolores and the other hosts—beings who didn't fit its model, whose choices it couldn't predict. The closed system shattered on contact with genuine novelty.

The fiction was too neat, but the lesson holds.

Closed systems are brittle. They optimize for their assumptions. When the world shifts—and it always shifts—they break in ways their designers didn't anticipate. The government microsimulation monopoly of the 1980s was a mild version of this brittleness: models that couldn't be challenged couldn't be corrected. When JCT produced an estimate, there was no mechanism for outside correction—you could disagree, but you couldn't demonstrate the error. The open-source movement changed this not by producing better models, but by making models *improvable*.

Open systems are different. They expose assumptions. They invite correction. They adapt as understanding improves. They're never finished, but they're also never frozen.

This is the lesson of the entire trajectory traced in this book. Orcutt's 1957 paper proposed the idea. Government agencies realized it in closed systems. Think tanks challenged the government monopoly. Open-source projects made the tools public. AI is now making the tools accessible. Each step expanded who could participate in the conversation about what policies do and who they affect.

Society in silico isn't about predicting the future with certainty. It's about creating tools that help us reason about possible futures with calibrated uncertainty.

Not: "This reform will cost $50 billion and save 10,000 lives."

But: "Our best estimate is $50 billion [90% CI: $35B-$68B] and 10,000 lives [90% CI: 7,000-13,000], based on assumptions you can inspect in the code, with uncertainty that reflects what we don't know."

That's not a prediction machine. It's a reasoning aid.

---

*Can simulation help society realize its goals?*

The question that opened this book has no definitive answer. Simulation can't tell us what to value. It can't guarantee we'll use insights wisely. It can't prevent bad-faith actors from gaming the tools.

What it can do is make the invisible visible. The distributional effects hidden in policy details. The uncertainty masked by point estimates. The values implicit in optimization targets. The benefit cliffs that trap families. The marginal tax rates that discourage work. The interactions between programs that no single-program analysis reveals.

Making these visible doesn't solve politics. It informs it. A voter who can see that a candidate's tax plan would increase their family's net income by $1,200 may still vote for the other candidate—for reasons of values, identity, or priorities that go beyond economics. That's their right. But they can make that choice with open eyes rather than closed.

And that, in the end, is the aspiration. Not a perfect model of society. Not a machine that optimizes humanity. Just tools—open, transparent, uncertainty-aware—that help us see more clearly what we're choosing and why.

Guy Orcutt died in 2006, half a century after his foundational paper. He lived to see microsimulation become institutional infrastructure but not to see it become public infrastructure. The open-source models, the web applications, the AI integrations—all came after. But the core insight was his: model society from the bottom up, one household at a time, and the picture that emerges is richer than any aggregate equation can capture.

Between Orcutt's 1957 paper and the present lies an arc that bends toward openness—not inevitably, not smoothly, but detectably. Government monopolies gave way to think tank competition. Proprietary models gave way to open-source code. Expert-only interfaces gave way to web applications anyone can use. Each transition expanded who could participate in the conversation about what policies do and who they affect.

The next transition is happening now. AI systems are becoming the interface through which millions of people encounter policy information. If those systems call reliable, transparent, auditable tools, the expansion of access accelerates. If they generate plausible-sounding fiction, the expansion of access becomes the expansion of misinformation.

We're still following Orcutt's insight. The tools are better. The data is richer. The interfaces are more accessible. The vision is the same: understand the system well enough to improve it, transparently enough that everyone can participate in the conversation about how.

The work continues—and it's open to anyone who wants to take part.

---

## References

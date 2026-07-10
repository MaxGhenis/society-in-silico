# Chapter 17: Society in silico

We return to where we began: Engerraund Serac in his control room, watching Rehoboam's predictions cascade across the displays. Individual lives reduced to trajectories. A society optimized to one man's definition of optimal. "I don't predict the future," he says. "I create it." That is one vision of society in silico.

This book has traced another.

## Two paths

Both visions start from the same recognition: that complex social systems can be modeled computationally—that policies can be simulated before they are enacted, that a population can be represented as millions of synthetic households, that the consequences of a choice can be estimated before anyone has to live them. They diverge on everything that comes after.

Serac's path is closed. The model is his alone; the predictions are hidden from the people living inside them; the objective function is singular, chosen by one actor and imposed on the rest. Uncertainty is suppressed, because Rehoboam speaks in certainties. Power concentrates, because those without access to the model are its subjects rather than its authors.

The open path inverts each of these. The model is public, and anyone can read the code. The predictions are queryable, so a person can ask what a policy does to their own household. The objectives are contested—many stakeholders, many goals, no single optimizer. Uncertainty is quantified rather than hidden, reported as intervals instead of false precision. And the capacity to analyze becomes public infrastructure rather than private advantage. Every chapter of this book has been about building the second path.

## What we've built

Guy Orcutt imagined simulating the economy household by household in 1957. For half a century, that vision lived almost entirely inside government agencies—the Congressional Budget Office, the Joint Committee on Taxation, Treasury—available to the powerful and invisible to the public. Rebuilding it in the open took faster computers, better and more accessible data, and code that anyone could inspect and run. Most of that rebuild is no longer a plan. It shipped.

**The open engine.** PolicyEngine encodes thousands of federal and state tax-benefit rules and shows them from two angles: the household view—*how does this policy affect my family?*—and the society view—*who gains and who loses across the population?* Its microdata is calibrated to over 9,000 administrative totals; validation partnerships with the National Bureau of Economic Research and the Federal Reserve Bank of Atlanta cross-check its calculations against independent implementations; and benefit screeners such as MyFriendBen run families across four states on the same underlying engine. <!-- VERIFY: 9,000 totals / four states figures -->

**The rules commons, at scale.** The Axiom Foundation, launching on July 28, 2026 [@axiomfoundation2026], has encoded roughly 3,000 US rule files spanning federal law and 28 states, with companion repositories for the United Kingdom, Canada, New Zealand, and Belgium—the mission stated as encoding all public policy, from federal statute down to a single London borough's council-tax reduction scheme. [VERIFY: ~3,000 US rule files, 28 states] In one week it encoded five African tax-benefit systems and validated them against UNU-WIDER's SOUTHMOD models [@unuwider2026southmod], reporting its findings back to the models' authors. Every monetary amount in an encoding is traced to a quoted excerpt from its governing source; and wherever encodings were compared against a reference model, the mismatches were 100 percent explained. This is the single strongest piece of evidence for the book's thesis, and it happened while the book was being written.

**The data commons.** populace assembles calibrated population data—synthetic households, tuned to administrative totals, that let the model represent anyone in the country rather than only the survey respondents who happened to be sampled. It is the successor to the enhanced survey files the earlier chapters described, and the answer to the permanent asymmetry those chapters diagnosed: outsiders were never handed the government's confidential records, so the open stack synthesizes and calibrates its own.

**The scoreboard.** The Thesis Institute [@thesisinstitute2026] publishes forecasts of government metrics—the first print of an unemployment number, a Medicaid call-center wait time under a policy that may or may not take effect—each carrying an explicit interval, each to be graded when the official figure lands. Its honest status belongs in the record: the scoreboard is live, the grades arrive with reality, and not one forecast has resolved yet.

**The measured boundary.** PolicyBench [@policybench2026] puts today's best language models on a public board and scores them on complete household tax-and-benefit calculations. As of mid-2026, the best model still gets roughly one in six of them wrong by more than a dollar; most models miss a quarter or more; and the errors are not rounding but family-level—a wrong Medicaid eligibility, a wrong SNAP amount. That gap is why the deterministic layer has to exist at all.

These are not five separate projects so much as one structure pulled apart along its natural seams. PolicyEngine keeps its name and its users; underneath, it is being recomposed into two open layers—Axiom, which answers what the law says, and populace, which answers who the people are—with the Thesis Institute as a distinct, third pole answering what will happen. An axiom is an accepted truth; a thesis is a proposition to be tested; and the two are verified in entirely different ways—rules against statute and against reference calculators, forecasts against reality when the number finally arrives. The organization came to mirror the questions it was built to answer.

## What we haven't built

Honesty requires the other ledger.

Adoption is still early. The tools exist, but most policy debates run without them. When Congress passed the One Big Beautiful Bill Act in July 2025 and extended the 2017 tax cuts [@obbba2025], the public argument was shaped by CBO scores and think-tank estimates—not by citizens running their own analyses. Scores mattered enormously; they moved a live, enacted law worth trillions. But they were institutional scores, and the shift from *available* to *expected* is the kind of cultural transition that took weather forecasting decades to complete.

The prediction pole has no track record. This is worth stating flatly, because it is exactly the thing a less careful book would blur: the Thesis Institute has not resolved a single forecast. Its scoreboard is a set of promises with intervals attached, not a record of hits. Until reality grades them, they are predictions, not evidence—and the discipline of saying so, out loud, is the entire reason to build a scoreboard instead of a megaphone.

The AI layer is only half-arrived. The rules and the data now exist at production scale, and an AI assistant can call them today—that part is real and shipped. What has not happened is that calling them becomes the default. Ask most assistants about tax policy right now and the answer still comes from training data rather than a calculation engine. The infrastructure that would make tool-calling automatic is built; the habit of reaching for it is not.

So this book describes as much aspiration as achievement. The rules layer is further up the mountain than the last draft dared claim; the prediction pole is barely off the trailhead. We are partway up, and honest about the altitude.

## Why it matters

If a society cannot reason about itself, it cannot govern itself. And the alternative to open simulation is not human judgment uncorrupted by models—it is the set of failure modes that already constitute the default.

Agencies make black-box decisions with proprietary tools: the Joint Committee on Taxation produces the revenue estimates Congress relies on using models Congress cannot inspect, and you are asked to trust outputs you cannot verify. Debate runs on vibes: politicians assert, pundits assert louder, and numbers float past without sources or audit trails. AI systems answer policy questions from training data, confidently and often wrongly—the family-level errors PolicyBench measures, shipped at the scale of every chatbot. And power concentrates among those with compute and data: a hedge fund can model the distributional impact of a tax reform in minutes while a community organization cannot, so the fund's version of events arrives first and with numbers attached, and sets the terms of the argument regardless of whether it is right.

These are not hypothetical. They describe how policy is analyzed today. Open simulation answers each one in kind—auditable code instead of black boxes, reproducible results instead of vibes, tools an AI can call instead of fiction it invents, public infrastructure instead of private advantage. It is not guaranteed to help. But the counterfactual is worse.

What it buys, concretely, is a shared factual floor. Picture the next time a candidate releases a tax plan. Instead of two campaigns trading unsourced numbers, independent analysis appears within hours—not from a single think tank but from many people running the same open model with different assumptions. A voter enters their own household and sees the specific dollar effect. A journalist checks a distributional claim against the actual calculation. The disagreement that remains is the real one, about values—how much redistribution is fair, how to weigh growth against security—argued from a common set of facts rather than dueling assertions. That is not utopia. Many will never use the tools; many will distrust them. But the option to know now exists, and it did not before.

## Closing the loop

In *Westworld*, Serac's system fails. Rehoboam cannot handle Dolores and the other hosts—beings who do not fit its model, whose choices it cannot predict—and the closed system shatters on contact with genuine novelty. The fiction was too tidy, but the lesson holds.

Closed systems are brittle. They optimize for their own assumptions, and when the world shifts—as it always does—they break in ways their designers never anticipated. The government microsimulation monopoly of the 1980s was a mild version of the same fragility: models that could not be challenged could not be corrected. When the Joint Committee on Taxation produced an estimate, there was no mechanism for outside correction—you could disagree, but you could not demonstrate the error. The open-source movement changed this not by producing better models, but by making models *improvable*.

That is the through-line of everything this book has traced. Orcutt's 1957 paper proposed the idea; government agencies realized it behind closed doors; think tanks broke the monopoly; open-source projects made the tools public; and agents are now making them buildable at a pace that turned last year's aspiration into this year's field report. Each step widened the circle of people who could take part in the argument about what policy does, and to whom. An open system is never finished. But it is also never frozen: it exposes its assumptions, invites correction, and adapts as understanding improves.

## An invitation

So the fork is real, and it is not science fiction. Both paths are open right now, as live institutional choices. One rebuilds the analytic machinery of government behind glass—closed, singular, speaking in certainties. The other rebuilds it in daylight—inspectable, plural, and graded against reality when reality arrives. The difference between them is not the sophistication of the model. Serac's was sophisticated. The difference is whether anyone outside the room can check it, correct it, and build on it.

Which is why the invitation at the end of this book is not a sales pitch. The code is public; the rules are open; the forecasts will be scored where everyone can see them. Anyone can read the encodings, run the models against their own questions, file the bug they find—or reject the premise entirely, and argue that these tools entrench technocracy rather than democratize it, that what is measurable will crowd out what matters. That argument, too, is better conducted in the open, against specifics that can be examined, than as assertion in the dark. The work continues in public, because public is the only place it can be corrected.

Society in silico is not a destination. It's a method.

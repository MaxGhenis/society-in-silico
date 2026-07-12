# Introduction: The model and the world

"For the first time, history has an author."

Engerraund Serac says it with pride. He is the villain of Westworld's third season: after watching Paris burn in a thermonuclear strike, he builds Rehoboam, an AI that models every human life and predicts its course — when you will lose your job, when you will get sick, when you will die. Prediction slides into control. The system starts arranging outcomes to match its forecasts, and people who wander off their assigned trajectories get flagged for "reconditioning." The show's premise is that a person is "just a brief algorithm," compressible to code. Its horror is simpler: history has an author, the author has a model, and no one else knows either exists.

I watched this in 2020 and recognized the machinery. I had been building models of society since 2018 — smaller, tamer ones that predict how a tax change lands on millions of simulated households. The writers had taken tools I used every day and followed them to their darkest terminus.

They had also, without meaning to, posed a design question that this book spends seventeen chapters answering. The dangerous thing about Rehoboam was never the simulation. It was the secrecy, the monopoly, and the absence of anything that could tell the system it was wrong. Governments already score citizens for fraud risk and bail decisions with models no defendant can inspect. Insurers and credit bureaus run the same pattern in private markets — a real fight, under different law, and not this book's; the chapters ahead are about the public machinery, where what the model computes is the policy. That machinery exists and is spreading; the only live question is its architecture. Closed, proprietary, graded by no one? Or open, inspectable, and checked — line by line — against the world it claims to describe?

That fork is the book.

## The AI can't do your taxes

Start with a fact that surprises people who expect artificial intelligence to be good at arithmetic.

In July 2025, the tax-software company Column Tax published TaxCalcBench, a test of whether frontier AI models could complete real federal tax returns [@bock2025taxcalcbench]. The models got everything a preparer would get: the taxpayer's full information, the rules, unlimited time to think. The best performer, Google's Gemini 2.5 Pro, produced a correct return less than a third of the time. Claude Opus 4 managed 27 percent. The errors followed a pattern: the models computed tax from bracket percentages instead of looking up the IRS tax tables, drifting $3 to $5 off on return after return; they fumbled credit eligibility; they lost track of supplementary forms. Software that costs fifty dollars does this flawlessly. The most capable AI systems on Earth could not.

Researchers had seen it coming. In 2023, a Johns Hopkins and Maryland team found GPT-4 answered only 67 percent of true-or-false tax questions correctly — better than a coin, useless for a filing [@blairstanek2023gpt4tax]. The models have improved since, and the improvement is measured, not conceded: on PolicyBench, PolicyEngine's own benchmark of complete household tax-and-benefit calculations, the newest flagships beat their predecessors, generation over generation. What the same board shows is how far there is left to go. As of mid-2026, across two dozen frontier and open models, the best still got roughly one in nine households wrong by more than a dollar, and the typical model missed about one in four [@policybench2026]. A dollar sounds like a rounding slip until you see what the misses are: the wrong Medicaid eligibility, the wrong food-assistance amount.

The limitation is structural. Language models learn patterns from text; tax law is not a pattern, it is a specification. It changes every year, differs across fifty states, and turns on interactions among dozens of provisions that no amount of pretraining can memorize into reliability. More training data does not fix a specification problem.

Tools fix it. AI systems do not memorize multiplication tables; they call calculators. They do not learn orbital mechanics by reading about rockets; they call physics engines. For the same reason, an AI answering a tax question should call a tax engine — software that encodes the rules exactly, cites the statute behind every number, and returns answers that can be checked. When people ask what this book is about technically, this is the one-sentence version: teaching machines to call verified models of society instead of guessing.

The catch, and the reason there was a book's worth of work to do: the tool did not exist. Avalara computes sales tax. ADP runs payroll. TurboTax files returns. Nothing answered the whole question — for this household, in this state, all taxes and all benefits, every interaction, and what changes if the law does. That question has a sixty-nine-year-old name: microsimulation. Its story starts in 1957 and runs straight into the benchmark failures above.

## Why the story turns now

Three developments converged to make this decade different from every previous era of policy analysis.

When someone wonders how much Child Tax Credit they will get, they increasingly ask a chatbot, not IRS.gov: AI became the interface. Whatever the assistant says, someone may act on. The infrastructure those assistants should consult — accurate, current, citable — either exists as public plumbing or every AI company improvises its own, badly.

The rules those assistants must navigate kept compounding. The tax code has roughly doubled in length since 1985 [NEEDS CITATION: tax-code length growth since 1985], and it interlocks with dozens of benefit programs whose rules shift by state and by year. A single parent earning $35,000 faces genuinely different arithmetic in Texas and New York, and the difference can run to thousands of dollars. No unaided human navigates this; the question is only which computer helps, and who can see inside it.

And the answer to both was growing up in public. What began as academic code became working infrastructure: by 2025 PolicyEngine covered federal taxes plus all fifty states, the United Kingdom, and Canada, built by more than a hundred contributors; EUROMOD spanned twenty-seven European countries; OpenFisca ran on four continents. The question stopped being whether open policy simulation could work and became whether it would be the shared foundation — for AI systems, for governments, for citizens — or a curiosity beside the closed models that still decide budgets.

## What a model shows you

Picture a single mother in Ohio earning $45,000 with two kids, offered a promotion to $55,000. Obviously she should take it.

Run the rules and the obvious answer wobbles. Across that income range her Earned Income Tax Credit phases out, her food assistance shrinks, and — depending on her county and her childcare subsidy — a benefit can vanish at a hard threshold. Of each new dollar, the tax-benefit system quietly takes back most of it; cross the wrong line and the raise leaves her family with less than before. Millions of American families sit somewhere on this labyrinth, and none of it is visible in an average. You can only see it by applying every bracket, phase-out, and eligibility test to her household in particular — and then to a few hundred thousand more households, to learn how many share her trap.

That is microsimulation: compute the law on each simulated family, then add up. Guy Orcutt proposed it in 1957 after concluding that models of national aggregates could never answer the questions that mattered, because two economies with identical averages can contain utterly different lives. His idea became the machinery behind every serious answer to "who wins and who loses" — and for fifty years that machinery sat inside the CBO, the Treasury, and a handful of institutions, where you could read its outputs but never check its work.

This book is about what happened when that stopped being true: first slowly, through open source, and then all at once, when AI agents learned to build and verify the models themselves.

## The stakes

When Congress debated extending the 2017 tax cuts in 2025, cost estimates ranged from four to five trillion dollars depending on modeling assumptions [@cbo2025tcja] — a spread wider than most federal agencies' budgets, on the single largest fiscal decision of the decade. The official scorekeepers used models the public cannot inspect. Independent groups produced competing numbers from different data and methods. Members of Congress quoted whichever figure served, and voted; the extension passed that July [@obbba2025]. Nothing in the process could tell a voter which number deserved belief, or why.

It does not have to work like that. Estimates can come from open models, where a disagreement traces to a named assumption instead of dissolving into "methodological differences." Uncertainty can be printed instead of hidden: "$4.5 trillion, plus or minus $700 billion, and here is the assumption doing the work." A family can run the proposal on their own circumstances before their representative votes on it. An AI assistant can cite a calculation instead of hallucinating one, because a public engine exists for it to call. None of this is hypothetical anymore; the chapters ahead describe each piece running.

But "running" is a claim, and this book holds claims to a rule that chapter 3 states and the rest enforce: a simulation is admissible only where its verification chain ends in ground truth. A rule proves itself against the statute and against independent calculators. A synthetic population proves itself against the census. A forecast proves itself when the official number lands and grades it — and until then it is a bet, labeled as one. The alternative to that discipline is Serac's machine with better branding: fluent, confident, and answerable to nothing.

## Four questions

Everything the book covers is machinery for answering four questions, in rising order of difficulty. What does the law say? Who are the people? What will happen? What do we want? The first has exact answers a computer can hold. The second has statistical answers a census can check. The third has probabilistic answers reality eventually grades. The fourth belongs to humans — and the book's final chapters ask, carefully, whether simulation can help us hear ourselves answer it without ever answering it for us.

The five parts follow that ladder:

- **Part I — The closed stack.** Orcutt's idea; the institutional models that ran the country's fiscal arguments from behind closed doors; the question that disciplines everything — how would you know whether any model is right? — and the family arithmetic that turned the question personal.
- **Part II — The open engine.** Building PolicyEngine: what the engine shows one household, what it shows a country, and the three problems every such model must solve.
- **Part III — The agent turn.** AI agents writing verified law-as-code at scale; the gates and oracles that make machine-encoded law trustworthy; five African tax systems encoded and checked in a week; and why the organization rebuilt itself around the epistemology.
- **Part IV — The prediction pole.** The uncertainty point estimates hide, the public scoreboard built to price it, and what language models actually add to opinion research once you benchmark them honestly.
- **Part V — The horizon.** Simulated democracy and simulated values, labeled as the research directions they are, and the return to the fork.

Two warnings before we start. I built many of the tools this book describes — PolicyEngine, the PolicyBench benchmark, the HiveSight and Democrasim experiments of Parts IV and V — and I am not a neutral witness; where the work is mine, I say so, and where it failed, I show the failure. And the boundary between "runs today" and "someday, maybe" moved faster during the writing than in any year of my career — so every chapter marks which side of it each claim sits on, as of the date on the preface.

The technology here will not save democracy or end poverty. What it can do is narrower and worth having: make the invisible visible — the cliff hidden in a benefit formula, the uncertainty behind a confident headline number, the difference between a model someone owns and a model anyone can check. What we do with the visibility is the political question, and it stays ours.

This is the case for the open path.

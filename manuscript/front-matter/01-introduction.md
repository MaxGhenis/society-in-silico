# Introduction: The model and the world

"I don't predict the future. I create it."

That line comes from Engerraund Serac, the antagonist of Westworld's third season. After watching a thermonuclear incident destroy Paris, Serac built an AI called Rehoboam that predicted individual human lives—when you'd get sick, lose your job, die. The system didn't just forecast; it manipulated society to make its predictions come true. People who deviated from their predicted paths got flagged for "reconditioning."

The show's premise: humans are "just a brief algorithm," reducible to code. The horror: one man controlling that algorithm without anyone else knowing.

When I watched this in 2020, I recognized the technology. I'd been building microsimulation systems since 2018—computational models that predict how tax policies affect households, that simulate entire economies with millions of synthetic people. The Westworld writers had taken the same tools and followed them to their darkest conclusion.

They'd also revealed a choice we're making right now.

Serac's system was closed: he decided what "optimal" meant, and everyone else lived inside his model without consent. But computational models of society don't have to work that way. What if anyone could query the model? Challenge its assumptions? Propose alternatives? What if simulation became public infrastructure for democratic deliberation, not a tool for autocratic control?

That's the fork in the road. That's what this book is about.

---

## The AI can't do your taxes

In July 2025, Column Tax released TaxCalcBench—a benchmark testing whether AI could correctly compute complete federal tax returns {cite}`bock2025taxcalcbench`. They gave frontier models everything they needed: the tax rules, the taxpayer's information, and as much time to think as they wanted. The best-performing model, Gemini 2.5 Pro, got fewer than one in three returns right. Claude Opus 4 managed 27%. These are the most capable AI systems in the world, and they can't reliably do what a $50 copy of TurboTax does without breaking a sweat.

The errors weren't random. Models used percentage-based bracket calculations instead of the IRS tax tables, producing returns that were off by $3-5 each time. They miscalculated credit eligibility. They stumbled on supplementary forms. The pattern was consistent across every model tested.

This wasn't a surprise to researchers who'd been tracking the problem. In 2023, researchers at Johns Hopkins and the University of Maryland found GPT-4 answered only 67% of true/false tax questions correctly—better than chance, but nowhere near reliable enough for financial decisions {cite}`blairstanek2023gpt4tax`. Two years and two model generations later, the fundamental limitation remains.

Language models can generate fluent explanations of tax law. They can summarize complex regulations. What they can't do is *calculate*—apply specific rules to specific circumstances and produce a number that's guaranteed to be correct. Tax law changes every year. Fifty states have different rules. Eligibility for benefits depends on dozens of interacting variables. The combinatorial complexity exceeds what pretraining can memorize.

The solution isn't better training. It's better tools—deterministic, auditable computational tools that AI systems can call when they need exact answers.

This is the central technical insight of the book: AI needs tools, and the tools that matter most for policy questions are microsimulation models.

---

## Why now

Three trends are converging to make this moment different from any previous era of policy analysis.

**AI systems are becoming the primary interface for information.** When someone asks "how much would I get from the Child Tax Credit?" they increasingly ask an AI assistant rather than navigating IRS.gov. If the assistant hallucinates an answer, the person may make financial decisions based on fiction. The infrastructure that AI systems call when they need accurate answers doesn't exist as a unified, production-ready service. Each company building AI assistants has to solve the tax-and-benefits problem from scratch—or get it wrong.

**Policy complexity is accelerating.** The US tax code has roughly doubled in length since 1985. The interaction between federal taxes, state taxes, and means-tested benefit programs creates a combinatorial explosion that no individual can navigate without computational tools. A single parent earning $35,000 in Texas faces a different effective tax rate than the same parent in New York—not by a small amount, but potentially by thousands of dollars. The complexity isn't a bug in the system; it's the accumulated result of decades of legislation, each layer addressing a real problem while creating new interactions with existing programs.

**Open-source infrastructure has matured.** A decade ago, the idea of encoding an entire country's tax-benefit system as publicly inspectable code was aspirational. Today, PolicyEngine covers US federal taxes plus all fifty states, the UK, and Canada—maintained by over fifty open-source contributors. EUROMOD covers twenty-seven EU countries. OpenFisca has been deployed on four continents. The question is no longer whether open policy simulation is possible. It's whether it can become the shared infrastructure that AI systems, governments, and citizens all rely on.

These trends create both opportunity and risk. The opportunity: a world where anyone can understand how policy affects them, where AI assistants give accurate answers about taxes and benefits, where policymakers can model proposals against a shared baseline that everyone trusts because everyone can inspect it. The risk: a world where opaque models make decisions about benefits and creditworthiness, where AI systems confidently give wrong answers about financial matters, where the tools of policy analysis remain locked inside institutions while the public debates with anecdotes.

---

## What simulation reveals

Consider a single parent in Ohio earning $45,000 with two children. She's trying to decide whether to accept a promotion that would raise her salary to $55,000.

Without calculation, the answer seems obvious—more money is better. But the tax-benefit system creates a labyrinth of interactions. At $55,000, she loses eligibility for the Earned Income Tax Credit—a cliff worth over $3,000. Her SNAP benefits phase down. Her childcare subsidy may evaporate. Her marginal tax rate—the share of each additional dollar she keeps—might briefly exceed 80%.

The parent who earns $55,000 may take home less than the parent who earns $45,000. This isn't a theoretical curiosity. It affects millions of families every year. And you can't see it without running the numbers through a model that captures the full interaction of taxes and benefits.

That's what microsimulation does. It calculates how policies affect specific households by applying the actual rules—every bracket, every phase-out, every eligibility test—to specific circumstances. Then it aggregates across a representative sample of the population to estimate what a policy does to everyone.

When Congress debates expanding the Child Tax Credit, microsimulation answers: How much would it cost? Which families would benefit? Would it reduce poverty? By how much? These aren't guesses. They're calculations—the product of applying the proposed rules to millions of synthetic households drawn from actual survey data.

The idea goes back to 1957, when an economist named Guy Orcutt proposed modeling society from the bottom up—simulating individual households rather than relying on aggregate equations. For decades, the tools to realize his vision were locked inside government agencies: the Congressional Budget Office, the Joint Committee on Taxation, the Treasury Department. If you wanted to know how a policy would affect you, you had to trust their numbers. You couldn't check their work.

That's changing. Open-source microsimulation models now make it possible for anyone—researchers, journalists, advocates, curious citizens—to run the same kinds of analyses that once required government resources. The code is public. The methodology is inspectable. The results are reproducible.

---

## The stakes

We don't have Rehoboam. But we're not starting from zero.

Governments already use predictive models to allocate benefits, assess fraud risk, and shape policy. Insurance companies price your premiums with algorithms you can't inspect. Banks decide your creditworthiness with models they won't explain. And AI assistants—the primary interface through which many people will encounter policy information—get tax questions wrong a third of the time.

These models exist. The question is who controls them.

**Who builds them?** Closed institutions or open communities?

**Who can access them?** Only the powerful or everyone?

**What are they for?** Optimization or understanding?

The gap between policy debates and policy analysis is vast. Political arguments run on emotion and tribal loyalty. Policy analysis runs on computation and precision. Bridging that gap without sliding into technocracy is the central challenge.

Consider the stakes concretely. When Congress debated extending the 2017 Tax Cuts and Jobs Act in 2025, the ten-year cost estimates ranged from $4 trillion to $5 trillion depending on the assumptions {cite}`cbo2025tcja`—a trillion-dollar range that could fund entire new programs or blow a hole in the deficit. The official scorekeepers at the Joint Committee on Taxation used models the public couldn't inspect. Independent groups like the Tax Policy Center, the Penn Wharton Budget Model, and PolicyEngine produced their own estimates, each with different data and methods. Members of Congress voted based on whichever number supported their position.

This isn't how it has to work. Imagine instead that every estimate was produced by open models—inspectable, reproducible, challengeable. That disagreements could be traced to specific assumptions rather than handwaved as "different methodologies." That a citizen could enter their own household circumstances and see, before a vote, exactly what the proposal would mean for them. Not approximately. Not according to a talking head. Precisely, calculated from the same rules that would govern their taxes.

That infrastructure is closer to reality than most people realize. And building it—making it accurate, accessible, and trustworthy—is the project this book describes.

---

## What's ahead

This book traces the story of microsimulation—from Orcutt's frustration with aggregate models in 1957, through six decades of institutional models locked inside government agencies, to the open-source movement making these tools public infrastructure. It arrives at the present moment, where AI systems need deterministic tools for financial calculations and the boundaries of what we can simulate are expanding.

**Part I: Origins** traces the intellectual history. Chapter 1 follows Guy Orcutt from his engineering background to the invention of microsimulation. Chapter 2 maps the "tax model wars"—the institutional competition between government agencies, think tanks, and open-source projects for analytical authority. Chapter 3 covers the European tradition, from EUROMOD to OpenFisca. Chapter 4 confronts the accuracy question: how good are these models, really?

**Part II: Building** follows the open-source turn. Chapter 5 describes PolicyEngine's development from research tool to public infrastructure. Chapter 6 explains the three ingredients that make microsimulation work. Chapters 7 and 8 explore the household view and society view—individual impact and population-wide analysis. Chapter 9 examines how AI is entering the picture. Chapter 10 describes the infrastructure gap and what it would take to build production-ready simulation for AI systems.

**Part III: Future** confronts the speculative edge. Chapter 11 tackles the uncertainty gap in policy analysis. Chapter 12 explores simulating public opinion. Chapter 13 models democratic processes. Chapter 14 asks whether we can forecast how human values evolve—and what that might mean for AI alignment. Chapter 15 returns to the fork in the road: Serac's closed system versus the democratic alternative.

The book ends where it started: at the choice between models that concentrate power and models that distribute it. That choice is being made right now, in code and policy and institutional design. This is the case for the open path.

---

## References

```{bibliography}
:filter: docname in docnames
```

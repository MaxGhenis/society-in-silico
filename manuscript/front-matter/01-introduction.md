# Introduction: The model and the world

"I don't predict the future. I create it."

That line comes from Engerraund Serac, the antagonist of Westworld's third season. After watching a thermonuclear incident destroy Paris, Serac built an AI called Rehoboam that predicted individual human lives—when you'd get sick, lose your job, die. The system didn't just forecast; it manipulated society to make its predictions come true. People who deviated from their predicted paths got flagged for "reconditioning."

The show's premise: humans are "just a brief algorithm," reducible to code. The horror: one man controlling that algorithm without anyone else knowing.

When I watched this in 2020, I recognized the technology. I'd been building microsimulation systems since 2018—computational models that predict how tax policies affect households, that simulate entire economies with millions of synthetic people. The Westworld writers had taken the same tools and followed them to their darkest conclusion.

They'd also revealed a choice we're making right now.

The fictional version is extreme—a single AI controlling human destiny. But the underlying dynamic is already real. Governments use algorithmic risk scores to allocate child welfare investigations, set bail amounts, and flag potential fraud in benefit claims. Insurance companies use predictive models you can't inspect to set your premiums. Credit agencies reduce your financial life to a three-digit number using methods they won't fully explain. Each of these systems makes predictions about individuals based on computational models of human behavior—and each operates with minimal transparency about its assumptions, its uncertainty, or its error rates.

Serac's system was closed: he decided what "optimal" meant, and everyone else lived inside his model without consent. But computational models of society don't have to work that way. What if anyone could query the model? Challenge its assumptions? Propose alternatives? What if simulation became public infrastructure for democratic deliberation, not a tool for autocratic control?

That's the fork in the road. That's what this book is about.

---

## The AI can't do your taxes

In July 2025, Column Tax released TaxCalcBench—a benchmark testing whether AI could correctly compute complete federal tax returns [@bock2025taxcalcbench]. They gave frontier models everything they needed: the tax rules, the taxpayer's information, and as much time to think as they wanted. The best-performing model, Gemini 2.5 Pro, got fewer than one in three returns right. Claude Opus 4 managed 27%. These are the most capable AI systems in the world, and they can't reliably do what a $50 copy of TurboTax does without breaking a sweat.

The errors weren't random. Models used percentage-based bracket calculations instead of the IRS tax tables, producing returns that were off by $3-5 each time. They miscalculated credit eligibility. They stumbled on supplementary forms. The pattern was consistent across every model tested.

This wasn't a surprise to researchers who'd been tracking the problem. In 2023, researchers at Johns Hopkins and the University of Maryland found GPT-4 answered only 67% of true/false tax questions correctly—better than chance, but nowhere near reliable enough for financial decisions [@blairstanek2023gpt4tax]. And the limitation has survived every model generation since. By mid-2026, PolicyEngine's own benchmark—PolicyBench, which scores some twenty frontier and open-weight models on complete household tax-and-benefit calculations drawn from realistic family circumstances—found the best model still getting roughly one in six households wrong by more than a dollar, and most models missing a quarter or more [@policybench2026]. The errors aren't rounding noise. They're family-level mistakes: the wrong Medicaid eligibility, the wrong SNAP amount, a credit granted to a household that doesn't qualify.

Language models can generate fluent explanations of tax law. They can summarize complex regulations. What they can't do is *calculate*—apply specific rules to specific circumstances and produce a number that's guaranteed to be correct. Tax law changes every year. Fifty states have different rules. Eligibility for benefits depends on dozens of interacting variables. The combinatorial complexity exceeds what pretraining can memorize.

The solution isn't better training. It's better tools—deterministic, auditable computational tools that AI systems can call when they need exact answers.

This is the central technical insight of the book: AI needs tools, and the tools that matter most for policy questions are microsimulation models. The pattern is familiar from other domains. AI systems don't memorize multiplication tables—they call calculators. They don't learn orbital mechanics from scratch—they call physics engines. For the same reasons, they shouldn't try to memorize tax law. They should call a tax engine that encodes the rules exactly, traces each calculation to statute, and produces guaranteed-correct results.

The trouble is that no comprehensive tax-and-benefit engine exists as unified public infrastructure. Avalara handles sales tax. ADP handles payroll. TurboTax handles filing. But nothing answers the full-stack question that matters for policy: given this specific household in this specific state, what are all their taxes and all their benefits, how do they interact, and what happens when you change the rules? That question—the question microsimulation was built to answer—is what connects a 1957 academic paper to a 2025 AI benchmark failure.

---

## Why now

Twenty years ago, if you wanted to know how a tax reform would affect American families, you had two options: read the CBO score (a single number for the nation) or hire a consulting firm to run proprietary models. Ten years ago, open-source tools like Tax-Calculator and EUROMOD existed, but using them required programming expertise and statistical training. Five years ago, PolicyEngine put microsimulation in a web browser, but the audience was still mostly policy professionals.

Three trends are now converging to make this moment different from any previous era of policy analysis.

**AI systems are becoming the primary interface for information.** When someone asks "how much would I get from the Child Tax Credit?" they increasingly ask an AI assistant rather than navigating IRS.gov. If the assistant hallucinates an answer, the person may make financial decisions based on fiction. The infrastructure that AI systems call when they need accurate answers doesn't exist as a unified, production-ready service. Each company building AI assistants has to solve the tax-and-benefits problem from scratch—or get it wrong.

**Policy complexity is accelerating.** The US tax code has roughly doubled in length since 1985. The interaction between federal taxes, state taxes, and means-tested benefit programs creates a combinatorial explosion that no individual can navigate without computational tools. A single parent earning $35,000 in Texas faces a different effective tax rate than the same parent in New York—not by a small amount, but potentially by thousands of dollars. The complexity isn't a bug in the system; it's the accumulated result of decades of legislation, each layer addressing a real problem while creating new interactions with existing programs.

**Open-source infrastructure has matured.** A decade ago, the idea of encoding an entire country's tax-benefit system as publicly inspectable code was aspirational. Today, PolicyEngine covers US federal taxes plus all fifty states, the UK, and Canada—maintained by more than 100 open-source contributors. EUROMOD covers twenty-seven EU countries. OpenFisca has been deployed on four continents. The question is no longer whether open policy simulation is possible. It's whether it can become the shared infrastructure that AI systems, governments, and citizens all rely on.

These trends create both opportunity and risk. The opportunity: a world where anyone can understand how policy affects them, where AI assistants give accurate answers about taxes and benefits, where policymakers can model proposals against a shared baseline that everyone trusts because everyone can inspect it. The risk: a world where opaque models make decisions about benefits and creditworthiness, where AI systems confidently give wrong answers about financial matters, where the tools of policy analysis remain locked inside institutions while the public debates with anecdotes.

---

## What simulation reveals

Consider a single parent in Ohio earning $45,000 with two children. She's trying to decide whether to accept a promotion that would raise her salary to $55,000.

Without calculation, the answer seems obvious—more money is better. But the tax-benefit system creates a labyrinth of interactions. As her earnings rise toward $55,000, the Earned Income Tax Credit she still collected at $45,000 phases out entirely, her SNAP benefits shrink, and—depending on her state and childcare arrangement—a subsidy can vanish at a hard threshold. The share of each additional dollar she actually keeps can stay strikingly low across that range.

For families who hit one of those hard thresholds, the losses can bunch tightly enough that earning more leaves them with less—a true benefit cliff. This isn't a theoretical curiosity. It affects millions of families every year. And you can't see it without running the numbers through a model that captures the full interaction of taxes and benefits.

That's what microsimulation does. It calculates how policies affect specific households by applying the actual rules—every bracket, every phase-out, every eligibility test—to specific circumstances. Then it aggregates across a representative sample of the population to estimate what a policy does to everyone.

When Congress debates expanding the Child Tax Credit, microsimulation answers: How much would it cost? Which families would benefit? Would it reduce poverty? By how much? These aren't guesses. They're calculations—the product of applying the proposed rules to millions of synthetic households drawn from actual survey data.

The same logic applies across the Atlantic. When the UK Chancellor announces changes to Universal Credit taper rates, a microsimulation model can show that a single parent working 25 hours per week at minimum wage keeps an additional £1,000 per year, while a two-earner couple sees a smaller gain. When Scotland sets different income tax rates from the rest of the UK, simulation reveals who wins and who loses across the income distribution. The tool is country-agnostic; the rules are country-specific.

The idea goes back to 1957, when an economist named Guy Orcutt proposed modeling society from the bottom up—simulating individual households rather than relying on aggregate equations. His insight was that you could learn more about how the economy works by tracking what happens to millions of individual families than by studying national averages. A 2% change in GDP tells you nothing about whether the people who need help are getting it. But simulate the change household by household—applying actual tax rules to actual income data—and you see what aggregate numbers hide: the family that falls through the cracks, the benefit cliff that punishes a raise, the interaction between programs that no single-program analysis reveals.

For decades, the tools to realize Orcutt's vision were locked inside government agencies: the Congressional Budget Office, the Joint Committee on Taxation, the Treasury Department. If you wanted to know how a policy would affect you, you had to trust their numbers. You couldn't check their work.

That's changing. Open-source microsimulation models now make it possible for anyone—researchers, journalists, advocates, curious citizens—to run the same kinds of analyses that once required government resources. The code is public. The methodology is inspectable. The results are reproducible.

---

## The stakes

We don't have Rehoboam. But we're not starting from zero.

Governments already use predictive models to allocate benefits, assess fraud risk, and shape policy. Insurance companies price your premiums with algorithms you can't inspect. Banks decide your creditworthiness with models they won't explain. And AI assistants—the primary interface through which many people will encounter policy information—get tax questions wrong a third of the time.

These models exist. The question is who controls them.

**Who builds them?** Closed institutions or open communities?

**Who can access them?** Only the powerful or everyone?

**What are they for?** Optimization or understanding?

The gap between policy debates and policy analysis is vast. Political arguments run on emotion and tribal loyalty. Policy analysis runs on computation and precision. In a typical election, candidates propose tax plans that would affect millions of families by thousands of dollars each—and most voters have no way to know whether they'd come out ahead or behind. They rely on campaign claims, pundit interpretations, and gut feeling. The tools to calculate the actual impact exist, but they're not available to the people the policies affect. Bridging that gap—making analysis accessible without sliding into technocracy—is the central challenge.

Consider the stakes concretely. When Congress debated extending the 2017 Tax Cuts and Jobs Act in 2025—an extension ultimately enacted that July [@obbba2025]—the ten-year cost estimates ranged from $4 trillion to $5 trillion depending on the assumptions [@cbo2025tcja]—a trillion-dollar range that could fund entire new programs or blow a hole in the deficit. The official scorekeepers at the Joint Committee on Taxation used models the public couldn't inspect. Independent groups like the Tax Policy Center, the Penn Wharton Budget Model, and PolicyEngine produced their own estimates, each with different data and methods. Members of Congress voted based on whichever number supported their position.

This isn't how it has to work. Imagine instead that every estimate was produced by open models—inspectable, reproducible, challengeable. That disagreements could be traced to specific assumptions rather than handwaved as "different methodologies." That a citizen could enter their own household circumstances and see, before a vote, exactly what the proposal would mean for them. Not approximately. Not according to a talking head. Precisely, calculated from the same rules that would govern their taxes.

Imagine further that the uncertainty was visible. Not "this reform costs $4.5 trillion" but "this reform costs $4.5 trillion, with a 90% confidence interval of $3.8 to $5.2 trillion, and here are the assumptions that matter most." That AI assistants, when asked about policy, could call these models and return accurate, citable answers instead of hallucinated approximations. That a nonprofit screening families for benefit eligibility could use the same calculation engine as the Congressional Budget Office, producing consistent results because they're running the same code against the same rules.

That infrastructure is closer to reality than most people realize. And building it—making it accurate, accessible, and trustworthy—is the project this book describes.

---

## What's ahead

Every claim anyone makes about public policy decomposes into four questions. **What does the law say?** — a question of rules, answerable exactly, checkable against the statute. **Who are the people?** — a question of data, answerable statistically, checkable against surveys and administrative totals. **What will happen?** — a question of prediction, checkable only when reality arrives. And **what do we want?** — a question of values, the hardest to answer and the easiest to smuggle into the other three. This book is the story of building open computational infrastructure for each question in turn, and of the discipline that keeps such infrastructure honest: every layer verified against ground truth, at the level of the individual unit—one rule, one household, one forecast.

**Part I: The closed stack** traces the history. Chapter 1 follows Guy Orcutt from his engineering background to the invention of microsimulation. Chapter 2 maps the tax model wars—how scoring became institutional authority, and how a confidentiality statute became an analytical moat. Chapter 3 confronts the accuracy question: how good are these models, really—and how would you know? Chapter 4 is the personal origin: the benefit cliff in my own family that turned the question from academic to urgent.

**Part II: The open engine** follows the building of PolicyEngine. Chapter 5 tells the origin story. Chapter 6 shows what the engine reveals—for one household, and for a country. Chapter 7 dissects the three ingredients every microsimulation must solve: rules, data, and dynamics.

**Part III: The agent turn** is where the story changes register. Chapter 8 shows why AI systems can't compute policy unaided—and why the answer is tools, not training. Chapter 9 reports on encoding the law at scale, by agents, under gates. Chapter 10 confronts the question everything depends on: how do you trust law encoded by machines? Chapter 11 takes the method to countries that never had public models at all. Chapter 12 explains why the organizations ended up mirroring the epistemology.

**Part IV: The prediction pole** crosses from calculation to forecasting. Chapter 13 exposes the uncertainty that point estimates hide, and the scoreboard being built to price it. Chapter 14 benchmarks what language models actually add to opinion research.

**Part V: The horizon** is the speculative edge, labeled as such. Chapter 15 models democratic processes. Chapter 16 asks whether we can forecast how human values evolve—and what that might mean for AI alignment. Chapter 17 returns to the fork in the road: Serac's closed system versus the democratic alternative.

The book ends where it started: at the choice between models that concentrate power and models that distribute it. That choice is being made right now, in code and policy and institutional design.

Some warnings before we begin. This is not a neutral survey. I've built many of the tools I describe, and I'll try to be honest about their limitations, but I'm not a disinterested observer. The chapters on systems I've created—PolicyEngine, HiveSight, Democrasim, the institutions of Part III—are marked as such. The speculative chapters are labeled clearly. Where something is early, unproven, or ungraded by reality, I say so—including, more than once, about my own projects.

I've also tried to resist the temptation to oversell. The technology described in this book won't save democracy, eliminate poverty, or solve AI alignment. What it can do is make the invisible visible—the distributional effects hidden in policy details, the uncertainty masked by point estimates, the benefit cliffs that trap families. Whether that visibility translates into better decisions depends on what people do with it.

This is the case for the open path.

---

## References


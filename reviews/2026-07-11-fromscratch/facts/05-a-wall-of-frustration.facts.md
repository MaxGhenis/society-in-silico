# Facts catalog — Chapter 4: A wall of frustration

Source: `manuscript/part-1-closed-stack/04-a-wall-of-frustration.md`
Note: This chapter is first-person memoir. The narrator "I" is the author, Max Ghenis.

## Facts

- In 2008 the author took a course at UC Berkeley: IEOR 131, Discrete-Event Simulation.
- The premise of IEOR 131: model a complex system not as a set of equations but as a collection of individuals moving through states (e.g., simulate an emergency room by tracking each patient's arrival, each nurse assignment, each treatment decision, then change something and watch the system respond).
- The course ran on Excel and Visual Basic for Applications; its examples were operational: healthcare facilities, manufacturing lines, service queues.
- The author's first internship was at Finelite, a lighting-fixture manufacturer in Union City, California, where he used Matlab to simulate production decisions (whether to pre-cut wire to standard lengths or cut to order; how to sequence assembly lines to minimize changeover time).
- After two years in consulting, the author joined Google's People Analytics team in 2010 — a group premised on bringing the same standard of evidence to decisions about people as to decisions about products.
- In 2012 the author and a colleague founded a small data-science team inside People Analytics, working on natural-language processing of employee feedback, social-network analysis of the org chart, and (the author's piece) simulation models for workforce planning.
- Google's staffing group processed between one and two million job applications a year; hundreds of recruiters managed thousands of open roles across divisions with different hiring needs.
- Leadership wanted to project headcount growth against targets, accounting for recruiting capacity, candidate pipeline dynamics, internal mobility, and attrition; the existing tool was a set of spreadsheets.
- The author built a bottoms-up simulation called Project Lorenz, named after Edward Lorenz, whose weather research showed how micro-level dynamics could drive macro-level phenomena.
- Project Lorenz (built on microsimulation principles, though the author didn't yet call them that): modeled candidates entering through different channels; estimated probabilities of moving between hiring stages using survival models (the same machinery health researchers use to predict disease progression); accounted for recruiter-productivity variation, attrition, and transfers between divisions; implemented in R; used Monte Carlo methods to quantify uncertainty; produced a distribution of outcomes rather than a single number.
- Project Lorenz never fully materialized: too many moving parts, unstable once wired together; a small change to one transition probability would ripple through and produce a headcount forecast no one believed. They ran the spreadsheets for another cycle.
- The author's brother, Alex, is the personal motivation for his turn to economic policy.
- In June 2004 — a month after the author's high school graduation, two months before he left the family's Menlo Park home for UC Berkeley — Alex suffered a spinal cord injury in a mountain biking accident. Alex was sixteen; the author was seventeen. Alex became a quadriplegic, dependent on attendant care for daily living (cooking, cleaning, getting in and out of bed).
- Alex went to Berkeley, earning an undergraduate degree and then a master's in public policy.
- When Alex entered the workforce, the family confronted how his benefits would interact with his earnings.
- Medicaid covered Alex's In-Home Supportive Services (IHSS) — attendant care that would otherwise have cost tens of thousands of dollars a year — but Medicaid had an income limit.
- Benefit-cliff numbers (data content): if Alex earned more than roughly $70,000 he would lose Medicaid eligibility; his medical expenses would then become tax-deductible, but he would have had to earn something like $160,000 for the added income to make up for the lost coverage. Across that whole range, the effective marginal tax rate exceeded 100 percent.
- The family modeled scenario after scenario in spreadsheets (tax brackets, benefit phase-outs, deductions, the interaction of state and federal programs), rebuilding repeatedly and always finding earning more would leave Alex worse off.
- This is what economists call means-tested benefit cliffs and implicit marginal tax rates.
- Around the same time, conversation inside Google turned to technological unemployment, to what AI might do to the labor market, and to whether society needed new institutions to guarantee basic needs; some people discussed universal basic income (unconditional cash payments without the means-testing that produces cliffs).
- In 2012, Google.org gave GiveDirectly a $2.4 million Global Impact Award [@givedirectly2012google].
- GiveDirectly made unconditional cash transfers to extremely poor households in Kenya (families living on roughly a dollar a day receiving about a thousand dollars, no strings attached), and its founders ran randomized controlled trials to measure the effects; results were encouraging (gains in earnings, assets, nutrition, educational outcomes).
- The author volunteered with GiveDirectly on the side, helping them use their data more efficiently and hosting their researchers for talks at Google.
- In 2015 the author moved to YouTube's data-science team, working on growth models, experiment analysis, and the launch of YouTube Go (a product built for markets with poor connectivity and lower-end phones, primarily in India and sub-Saharan Africa).
- Senators Michael Bennet and Sherrod Brown had introduced the American Family Act (a Child Tax Credit expansion).
- The author found Tax-Calculator, the open-source model of US federal income and payroll taxes that came out of the American Enterprise Institute — written in Python, maintained by experienced economists, with its code on GitHub (anyone could read the formulas, run the model, check the results).
- In 2018 the author took three months off from Google to work on policy full-time, and enrolled in MIT's MicroMasters program in Data, Economics, and Development Policy (graduate-level coursework that could ladder into a full master's).
- During those three months the author worked with the Open Source Policy Center at AEI, contributed to Tax-Calculator's technical infrastructure, and ran distributional analyses of tax reforms.
- The author returned to YouTube briefly, then left Google in July 2018, after eight years, to commit to independent policy research, supported by savings.
- In 2019 the author founded the UBI Center, an explicitly open-source think tank focused on universal basic income policy, with all code and data public [@ubicenter2019].
- A $1,000-a-month basic income costs something like $3 trillion a year; to fund it you must change taxes or benefits, so modeling UBI honestly requires modeling the entire tax-and-benefit system (to show what would pay for it).
- Without UBI as a lens, low-income families faced implicit marginal tax rates above 50 percent from stacked phase-outs, and cliffs where earning a little more meant losing thousands in benefits.
- Tax-Calculator could handle federal income and payroll taxes but not benefits like SNAP or Medicaid; OpenFisca offered a rule-encoding framework but OpenFisca-US was young and incomplete; neither had an interface for a non-programmer; state-level tools barely existed.
- The first researcher recruited was Nate Golden, a middle-school math teacher in Washington, DC, who cared about fighting poverty with evidence and would later found the Maryland Child Alliance to push child-poverty policy at the state level.
- The second recruit came from the internet: after the author posted on the Basic Income subreddit asking for help, Nikhil Woodruff, a college student in the UK, replied; he had a rare pairing of economic-policy interest and software-engineering skill.
- Footnote/disclosure: as of July 2026, Nikhil Woodruff serves in the UK government at 10 Downing Street [VERIFY with Nikhil: role wording]. Noted as a disclosure because much of the book touches UK policy and the institutions that model it.
- The UBI Center produced analyses of Andrew Yang's Freedom Dividend, carbon-dividend designs, and child allowances — each requiring cobbling partial tools together and working around gaps.
- There was no open-source model of the UK tax-and-benefit system at all; to do comparative US/UK UBI analysis, they had to build the UK model from scratch. ("So we did.")
- By 2020 the UBI Center had grown to ten researchers (its biggest year) and shifted from writing reports to building infrastructure: microdf (for analyzing survey data) and openfisca-uk (for simulating UK policy), with two of their Python packages accepted into the Policy Simulation Library catalog.
- Building openfisca-uk meant encoding an entire national system no one had put in the open before — Universal Credit, the personal allowance, the benefit taper — line by line from the legislation and guidance, tested against every hand-checkable case.
- Nate Golden worked out whether a basic income should target adults, children, or both, finding child allowances the most effective for poverty reduction up to a given budget.
- Nikhil Woodruff built on the UK Family Resources Survey while the author worked on enhancing the US Current Population Survey.
- UBI Center analysis of Yang's proposal (data content): showed a 74 percent reduction in poverty, but also that the plan would cost about $2.8 trillion a year while his five proposed taxes would raise only $1.2 trillion, leaving a $1.6 trillion gap [NEEDS CITATION: UBI Center report].
- UBI Center carbon-dividend work (data content): a £100-per-tonne UK carbon tax would cut poverty by 14 percent and deep child poverty by 33 percent [NEEDS CITATION: UBI Center report].
- All of the UBI Center's work took Python: open-source in principle, inaccessible in practice to the journalists, advocates, and policymakers who needed it most. The code was public; the ability to use it was not.

## Story beats

- **The simulation education.** IEOR 131 at Berkeley (2008, Excel/VBA) teaches modeling individuals-through-states → Finelite internship applies it in Matlab to a factory → the conceptual frame outlasts the syntax.
- **Google → Project Lorenz.** 2010 joins People Analytics; 2012 co-founds a data-science team; builds Project Lorenz (workforce-planning microsimulation named for Edward Lorenz) in R with survival models and Monte Carlo, producing a distribution not a point estimate.
- **Project Lorenz's failure.** Too many interacting moving parts; unstable when integrated; one transition-probability change ripples into an unbelievable forecast; they revert to spreadsheets. The idea was right even where the execution wasn't.
- **The Alex arc (the book's emotional core).** June 2004 mountain-biking accident (Alex 16, author 17), quadriplegia, attendant care → Alex earns a Berkeley undergrad degree and a public-policy master's → entering the workforce triggers the Medicaid/IHSS cliff: $70k eligibility limit, $160k breakeven, >100% effective marginal tax rate → family rebuilds spreadsheets "for an audience of one" → aggregates are silent about the thing reshaping his decision to work → "a wall of frustration."
- **The UBI thread.** Google conversations about technological unemployment/AI/basic income → GiveDirectly's $2.4M Google.org award (2012), Kenya cash transfers, RCTs → author volunteers → UBI reframed as a *benchmark/counterfactual* for the targeting-vs-universality tradeoff, the same "hold one thing constant, vary another" move from the Berkeley course.
- **The policy turn.** 2015 YouTube (YouTube Go) → attention drifts to policy → American Family Act (Bennet/Brown) raises answerable questions → finds Tax-Calculator on GitHub → "So I did": uses it, contributes, works nights/weekends → realizes serious policy analysis can be done open-source, from a laptop, without the machinery behind the curtain. "This was how policy analysis *should* work."
- **Leaving Google.** 2018: three months off, MIT MicroMasters, OSPC/AEI contributions → leaves Google in July 2018 after eight years for independent research on savings and conviction.
- **Founding the UBI Center (2019).** Open-source think tank; immediate discovery that modeling UBI honestly means modeling the whole tax-and-benefit system; tool gaps (Tax-Calculator no benefits, OpenFisca-US immature, no interface, no state tools).
- **Recruiting the team.** Nate Golden (DC middle-school math teacher, later Maryland Child Alliance) first; Nikhil Woodruff (UK college student) second, recruited from the Basic Income subreddit — "a math teacher, a college student from a message board, me."
- **Building UK from scratch.** No open-source UK model exists → they build one ("So we did") → 2020: ten researchers, microdf + openfisca-uk, PSL acceptance; Golden's targeting finding; Nikhil on FRS, author on CPS; honest Yang numbers (74% poverty cut but $1.6T funding gap); carbon-dividend numbers.
- **The wall, scaled up.** The realization that the frustration is "infrastructure-shaped": fragmented tools, all requiring Python, no assembled rules+data+interface a non-programmer could trust — the same wall the family hit around Alex's kitchen table, "scaled up to a country."

## Quotes

None. Chapter 4 is first-person memoir and contains no verbatim external quotations attributable to a named third-party speaker. Its distinctive verbatim material is the author's own voice — see Author-texture. (Author's own phrases such as "So we did." and "This was how policy analysis *should* work." are the author's hand, catalogued under Author-texture rather than as sourced quotes.)

## Arguments

1. You can understand the emergent behavior of a complex system by simulating its individuals rather than modeling its aggregates — and the behavior you get that way is often one you'd never guess from the averages going in (learned in IEOR 131, applied at Finelite and in Project Lorenz).
2. Aggregates are silent about what matters to a specific person: Alex's cliff lived in the interaction of specific programs at a specific income for a specific person, visible only by modeling that person directly. A poverty statistic or average tax rate would show nothing of it.
3. Means-tested benefits create cliffs and effective marginal tax rates above 100 percent; the system offered no way around earning-more-leaving-you-worse-off.
4. UBI works as a benchmark, not necessarily an optimal policy — a clean reference case for the tradeoff between targeting (cheaper but with disincentives and cliffs) and universality (costlier but simple, no cliffs). Setting universality beside means-testing makes the cliffs visible.
5. To model UBI honestly you must model the entire tax-and-benefit system, because you have to show what would pay for a ~$3 trillion/year program.
6. Serious public-policy analysis can be done with open-source software, from a laptop, without joining a think tank or agency — it requires a good model, public data, and the willingness to do the work.
7. But the open-source revolution produced *components* (a tax model here, a benefits framework there), all demanding Python and none with an interface, and nobody had assembled rules + data + interface into one reliable, usable instrument.
8. The gap was infrastructure-shaped: the same wall the family hit at Alex's kitchen table, scaled to a country. Assembling the pieces was nobody's job because each belonged to a different discipline and institution. Someone would have to build the thing that tore it down.

## Author-texture (verbatim, may be reused)

**THE ALEX PASSAGE — the book's emotional core, quoted in full (§ "The personal motivation"):**

> My interest in economic policy became personal through my brother Alex.
>
> In June 2004—a month after my high school graduation, two months before I left our Menlo Park home for UC Berkeley—Alex suffered a spinal cord injury in a mountain biking accident. He was sixteen; I was seventeen. He became a quadriplegic, dependent on attendant care for the daily mechanics of living, from cooking and cleaning to getting in and out of bed.
>
> Like me, Alex went to Berkeley, earning an undergraduate degree and then a master's in public policy. And when he entered the workforce, our family ran headlong into the question of how his benefits would interact with his earnings.
>
> Medicaid covered his In-Home Supportive Services—attendant care that would otherwise have cost tens of thousands of dollars a year. But Medicaid had an income limit. If Alex earned more than roughly $70,000, he would lose eligibility; his medical expenses would then become tax-deductible, but the trade was brutal, and he would have had to earn something like $160,000 for the added income to make up for the coverage he had lost. Across that whole range, the effective marginal tax rate exceeded 100 percent—the arithmetic our spreadsheets kept producing, no matter how many times we rebuilt them looking for a way through. Earning more would leave him worse off, and the system offered no way around it.
>
> We modeled scenario after scenario, and the complexity was overwhelming: tax brackets, benefit phase-outs, deductions, the interaction of state and federal programs, each rule sensible on its own and the combination punishing. The tools to understand how policy actually landed on one person's particular circumstances simply did not exist; we were building them from scratch, badly, in a spreadsheet, for an audience of one.
>
> And none of it was visible from the outside. A poverty statistic or an average tax rate would have shown nothing of what Alex faced; his cliff lived in the interaction of specific programs at a specific income for a specific person, and you could only see it if you modeled that person directly. The aggregates were silent about exactly the thing that was reshaping my brother's decisions about whether to work.
>
> This was my introduction to what economists call means-tested benefit cliffs and implicit marginal tax rates. For the person living inside the system, it was just a wall of frustration.

**"So we did." and its setup (§ before "The UBI Center" close):**

> And there was no open-source model of the UK tax-and-benefit system at all. If Nikhil and I wanted to do comparative UBI analysis across the US and the UK, we would have to build the UK model from scratch.
>
> So we did.

**The kitchen-table-to-country closing image (final paragraph):**

> The frustration, I finally understood, was infrastructure-shaped. The tools were fragmented—tax models that didn't talk to benefit models, federal systems that didn't connect to state ones—and running any of them meant installing software, preparing data, and writing code. The gap was not a missing model. It was that no one had assembled rules, data, and an interface into a single thing that a person without a programming background could sit down and use to ask a real question and get an answer they could trust. Rules, data, and an interface, welded into one instrument and made reliable enough to believe—that was the whole of it, and it had gone unbuilt because each piece belonged to a different discipline and a different institution, and putting them together was nobody's job. That was the wall, and it was the same wall my family had hit around Alex's kitchen table, scaled up to a country. Someone would have to build the thing that tore it down.

**Other first-person moments with real specificity (preserve where useful):**

> So I did. I started using Tax-Calculator, then contributing to it, then spending my evenings and weekends on policy analysis with open-source tools while working full-time at YouTube. … This was how policy analysis *should* work.

> The whole operation, in those first months, amounted to a few people—a math teacher, a college student from a message board, me—working nights and weekends on a model of the American tax-and-benefit system. It did not look like infrastructure. It looked like a hobby with unusually high stakes.

> We weren't advocates. We were modelers, showing the tradeoffs and letting the numbers say what they said.

Nikhil disclosure footnote (carry with its [VERIFY] marker): "As of July 2026, Nikhil Woodruff serves in the UK government at 10 Downing Street [VERIFY with Nikhil: role wording]. I note it here as a disclosure—much of what follows in this book touches UK policy and the institutions that model it—and because the shape of the thing is hard to improve on: the co-founder I recruited from a subreddit now works inside the government whose analytical machinery these tools were built to open up."

## Structural notes

- **Chapter's job in the book.** Closes Part I ("The closed stack"). Pivots from third-person history (Chs 1–3) to first-person origin story. Establishes the author's personal motivation (Alex's cliff), the intellectual continuity (simulating individuals, from IEOR 131 to Project Lorenz to policy), the UBI-as-benchmark frame, the founding of the UBI Center, and the "infrastructure-shaped" gap that the next part (PolicyEngine) is built to fill. Carries the book's emotional core.
- **Cross-references.** Back to Chapter 1 (microsimulation principles — "though I didn't yet know to call them that"); Tax-Calculator/AEI/OSPC and OpenFisca from Chapter 2; the phrase "the machinery behind the curtain" echoes Chapter 2; "an answer they could trust" echoes Chapter 3's verifiability/admissibility rule. Forward: the assembled rules+data+interface instrument is PolicyEngine (next part); Nikhil Woodruff's arc and the UK model seed later UK-policy chapters.
- **Protected lines** (task-flagged, preserve verbatim): "So we did." / the kitchen-table-to-country closing image / "It looked like a hobby with unusually high stakes." Also load-bearing: "For the person living inside the system, it was just a wall of frustration." (the chapter's title line).
- **Disclosure to carry.** The Nikhil Woodruff / 10 Downing Street footnote (July 2026) with its [VERIFY with Nikhil: role wording] marker — a deliberate disclosure, not to be dropped. Consistent with the project rule to disclose Nikhil's No. 10 role in UK-policy contexts.
- **Handoff.** Ends on the mission statement — "Someone would have to build the thing that tore it down" — handing off to the PolicyEngine chapters (Part II).

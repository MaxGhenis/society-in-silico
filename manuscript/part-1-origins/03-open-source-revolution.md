# Chapter 3: The Open Source Revolution

In May 2011, a small team at France Stratégie—the French government's policy analysis agency—released something unusual: the source code for a tax and benefit calculator {cite}`openfisca2024about`.

They called it OpenFisca. The premise was simple but radical: tax and benefit rules should exist not just as legal text but as executable code. Give the system a person's circumstances—income, family structure, location—and it would calculate their taxes and benefits. Change a parameter—a tax rate, an eligibility threshold—and see the effects immediately.

The code was released under an open-source license. Anyone could use it, modify it, extend it. The French government had decided that the logic of its tax-benefit system should be a public good.

This was the beginning of the open source revolution in policy modeling. It would take a decade to spread, and it remains incomplete. But it represents something fundamental: the idea that the rules governing citizens' lives should be not just publicly available but publicly *computable*.

---

## Rules as Code

The concept went by various names: "rules as code," "legislation as code," "machine-consumable rules." The idea was always the same: laws and regulations should be expressed in a form that computers can execute, not just humans can read.

This wasn't new in principle. Tax agencies had been encoding rules in software for decades—that was what George Sadowsky had done at Treasury in the 1960s, what every government tax system did by the 2000s. But those implementations were proprietary, hidden inside agency systems. Citizens experienced the *outputs* of coded rules (a tax bill, a benefit payment) without access to the *logic*.

The open source revolution proposed transparency: publish the code, let anyone run it, enable verification and experimentation.

In 2018, New Zealand's Service Innovation Lab launched "Better Rules"—a collaboration between Inland Revenue, the Ministry of Business, Innovation and Employment, and the Parliamentary Counsel Office {cite}`nz2018betterrules`. The team spent three weeks translating legislation into Python code, demonstrating that rules could be drafted in both human-readable and machine-readable form simultaneously.

Estonia's Chief Information Officer called it "the most transformative idea" he'd seen {cite}`nz2018betterrules`. The OECD took notice, eventually publishing "Cracking the Code: Rulemaking for Humans and Machines" in 2020—a primer for governments on what rules as code could mean {cite}`oecd2020cracking`.

By 2022, OpenFisca had been deployed on four continents {cite}`openfisca2024about`. France used it for Mes Aides, a citizen-facing benefits calculator. New Zealand built a rates rebate application. Tunisia, Senegal, Australia, Canada, and others adapted the framework for their own systems.

The OECD named OpenFisca's approach an "Innovation of the Year" at the World Government Summit. The European Commission recognized it as the most innovative open-source software in their Joinup program {cite}`openfisca2024about`. A small French project had become a global movement.

---

## The Promise and the Gap

The promise was intoxicating. If tax and benefit rules were published as code:

**Citizens could check their own calculations.** Rather than trusting that an agency computed their benefits correctly, anyone could run the same logic themselves.

**Reformers could model alternatives.** Policy proposals wouldn't require access to government systems. Anyone with a laptop could simulate how a new benefit structure would work.

**Errors could be found and fixed.** Open code meant open scrutiny. Bugs in benefit calculations—which affected real people's lives—could be identified by outside researchers.

**Innovation could flourish.** Nonprofits, journalists, and entrepreneurs could build applications on top of official rule logic, creating tools the government never imagined.

But between the promise and reality lay significant gaps.

**Technical barriers.** OpenFisca required Python programming skills. Most citizens—most policy researchers, even—couldn't write code. The rules were technically public but practically inaccessible.

**Data problems.** Microsimulation requires not just rules but data: a representative population to simulate. OpenFisca encoded the rules; it didn't solve the data challenge. Without microdata, you could calculate individual scenarios but not aggregate impacts.

**Trust gaps.** Even with open code, who would trust it? Governments were wary of unofficial calculations contradicting official ones. Citizens didn't know how to evaluate competing estimates.

**Maintenance burdens.** Tax codes change constantly. Someone had to update the models, track legislative changes, fix bugs. Open source meant anyone *could* contribute; it didn't mean anyone *would*.

The gap between OpenFisca's elegant framework and actually usable policy analysis remained wide.

---

## The American Ecosystem

While OpenFisca spread globally, a parallel movement was building in the United States.

In 2016, Matt Jensen launched the Open Source Policy Center at the American Enterprise Institute {cite}`aei2016ospc`. His diagnosis was blunt: "The closed-source approach to estimating the costs and economic impact of policies raises challenges, as there is limited accessibility and transparency in the process, leaving the public and many policymakers in the dark."

Jensen recruited Martin Holmer, who had a PhD from MIT and decades of microsimulation experience, to build Tax-Calculator—an open-source model of US federal income and payroll taxes {cite}`holmer2024profile`. Written in Python with over 200 adjustable parameters, Tax-Calculator could simulate an enormous range of reforms. And unlike the black boxes at JCT and Treasury, anyone could inspect the code.

The project grew into the Policy Simulation Library—a community of open-source policy models sharing transparency standards and interoperability criteria. Jason DeBacker and Richard Evans built OG-USA, an overlapping-generations model for dynamic scoring that complemented Tax-Calculator's static analysis. The Tax Foundation contributed its capital cost recovery model. QuantEcon brought computational economics tools.

By 2023, PSL was hosting monthly "Demo Days" where researchers from the Congressional Budget Office, NOAA, Johns Hopkins, and the City of New York presented their work. The community had developed institutional memory and governance—a leadership council, a fiscal sponsor (the PSL Foundation), and a YouTube channel archiving every presentation.

Even the Federal Reserve joined the movement. FRB/US, the Fed's main macroeconomic model—375 equations describing the entire US economy—had been publicly available since the late 1990s, but in 2022 the Fed released a Python implementation, making the model accessible to anyone who could write code {cite}`frbus2024`. The central bank's primary forecasting tool was now open source.

The American ecosystem differed from OpenFisca's approach. Where OpenFisca provided a unified framework that countries could adapt, PSL was a federation of independent projects. Tax-Calculator handled income taxes; OG-USA handled dynamic macroeconomic effects; each model had its own maintainers, its own governance, its own priorities.

This decentralization had benefits—specialization, diversity, resilience—but also costs. The models didn't always talk to each other. Running a comprehensive analysis meant stitching together multiple tools. And no single organization was responsible for the complete picture.

---

## The Path to PolicyEngine

### Simulation as Tool

In 2008, I took a course at UC Berkeley that would shape my career: IEOR 131, Discrete-Event Simulation. The premise was elegant—model complex systems not as equations but as collections of individuals moving through states. Simulate a hospital emergency room by tracking each patient arrival, each nurse assignment, each treatment decision. Change a parameter—add a nurse, reorganize triage—and watch how the whole system responds.

The course used Excel and Visual Basic for Applications. The applications were operational: healthcare facilities, manufacturing lines, service queues. But the conceptual framework stuck: you could understand emergent behavior by simulating individuals rather than modeling aggregates.

My first internship put the concept into practice. At Finelite, a lighting fixture manufacturer in Union City, California, I used Matlab to simulate production decisions. Should they pre-cut wire to standard lengths or cut to order? How should assembly lines be sequenced to minimize changeover time? The models were simple, but they worked—computational experiments that revealed non-obvious insights about manufacturing operations.

After two years in consulting, I joined Google's People Analytics team in 2010.

### Project Lorenz

Google's Staffing Analytics group dealt with operational complexity at a scale that dwarfed any factory. Between one and two million job applications arrived each year. Hundreds of recruiters managed thousands of open positions across divisions with different hiring needs. The challenge: project headcount growth relative to targets, accounting for recruiting capacity, candidate pipeline dynamics, internal mobility, and attrition.

The existing tool was a series of spreadsheets—functional but limited. I convinced leadership to let me try something different: a bottoms-up simulation model I called Project Lorenz, after Edward Lorenz's pioneering work in weather modeling that showed how micro-level dynamics could explain macro phenomena.

The approach was microsimulation, though I didn't use that term yet. Model candidates entering the system through different channels. Estimate transition probabilities between hiring stages using survival models—the same statistical tools used in health research to predict disease progression, repurposed to predict how candidates moved through Google's hiring process. Account for recruiter productivity variation, attrition patterns, internal transfers between divisions.

The technical implementation was in R, using survival models for transition probabilities, Monte Carlo methods for uncertainty quantification. The goal was flexibility: rather than a single forecast, produce a distribution of outcomes that captured the inherent uncertainty in hiring dynamics.

Project Lorenz never fully materialized. The complexity proved difficult to manage—many moving parts that looked reasonable individually but produced unstable results when integrated. But the conceptual seed was planted: complex social systems could be understood by simulating individuals and their transitions through states.

### The Personal Motivation

My interest in economic policy became personal through my brother Alex.

In 2005, Alex suffered a spinal cord injury in a mountain biking accident when he was sixteen. I was seventeen. He became a quadriplegic—dependent on attendant care for daily activities from cooking and cleaning to getting in and out of bed.

Like me, Alex went to Berkeley, earning both an undergraduate degree and a Master's in Public Policy. When he entered the workforce, our family confronted how benefit programs would interact with his earnings.

Medicaid covered In-Home Supportive Services—essentially attendant care that would cost tens of thousands of dollars annually without coverage. But Medicaid had income limits. If Alex earned more than about $70,000, he would lose eligibility. His medical expenses would become tax-deductible, but the math was stark: he would need to earn roughly $160,000 for the increased income to offset the lost benefits. The effective marginal tax rate in that range exceeded 100%.

We built spreadsheets to model different scenarios. The complexity was overwhelming—tax brackets, benefit phase-outs, deductions, state versus federal programs. The tools didn't exist to easily understand how policy interacted with individual circumstances.

This was my introduction to what economists call "means-tested benefit cliffs" and "implicit marginal tax rates." For someone navigating the system, it was just a wall of frustration.

### The UBI Thread

Around this time, internal discussions at Google were addressing technological unemployment, AI's labor market implications, and whether society needed new institutions to ensure basic needs were met as automation advanced. Some employees were discussing universal basic income—unconditional cash payments that could provide a floor without the means-testing problems that created cliffs like the one Alex faced.

In 2012, Google.org awarded GiveDirectly a $2.4 million Global Impact Award {cite}`givedirectly2012google`. The organization was providing unconditional cash transfers to extremely poor households in Kenya—people living on roughly a dollar a day received about $1,000 per household. As economists, GiveDirectly's founders ran randomized controlled trials to measure effects. The results were positive: improved earnings, assets, nutrition, educational outcomes.

I volunteered with GiveDirectly, helping them use data more efficiently and hosting talks at Google's campus. The cash transfer model felt like a useful thought experiment: instead of targeting programs with complex eligibility rules and implicit taxes on earning more, just provide cash and fund it through explicit taxes.

The idea wasn't necessarily that UBI was the optimal policy. It was that UBI served as a *benchmark*—a way to think clearly about the tradeoffs between targeting (lower cost, but creates disincentives) and universality (higher cost, but simpler and no cliffs).

### YouTube and the Policy Turn

In 2015, I moved to YouTube's data science team, working on growth models, experiment analysis, and the launch of YouTube Go—a product designed for markets with poor internet connectivity and lower-quality phones, primarily in India and sub-Saharan Africa.

But my attention was increasingly on policy. Proposals for expanding the Child Tax Credit were gaining traction. Senators Michael Bennet and Sherrod Brown had introduced the American Family Act. The question: what would a larger child allowance do to poverty rates? Who would benefit?

I found a tool that could answer the question: Tax-Calculator, an open-source microsimulation model from the American Enterprise Institute. Written in Python, maintained by economists with decades of modeling experience, and crucially: the code was on GitHub. Anyone could see the formulas, run the model, check the results.

I started using Tax-Calculator. Then contributing to it. Then spending evenings and weekends on policy analysis using open-source tools while still working full-time at YouTube.

The realization: public policy analysis—affecting millions of people and billions of dollars—could be done with open-source software, without leaving Google to join a think tank or government agency. This was how policy analysis *should* work.

### The Commitment

In 2018, I took three months off from Google to work on policy full-time. I enrolled in MIT's MicroMasters program in Data, Economics, and Development Policy—graduate-level courses that could ladder into a full master's degree if I decided to pursue it.

The three months were clarifying. I worked with the Open Source Policy Center at AEI, contributed to Tax-Calculator's technical infrastructure, and conducted distributional analysis of tax reforms. The work felt more important than anything else available to me.

I decided not to return to YouTube. Instead, I committed to independent policy research, supported by savings and the growing conviction that open-source policy analysis was infrastructure the world needed.

### Founding the UBI Center

In 2019, I founded the UBI Center {cite}`ubicenter2019`—an explicitly open-source think tank focused on universal basic income policy. The mission: produce rigorous research that could inform UBI debates, with all code and data public so anyone could verify the findings.

The challenge emerged immediately. UBI proposals didn't exist in isolation—they interacted with the entire tax and benefit system. A $1,000-per-month basic income would affect federal income taxes, state income taxes, SNAP eligibility, Medicaid thresholds, housing benefits. To model UBI properly required modeling everything.

Tax-Calculator could handle federal income and payroll taxes, but not benefits like SNAP or Medicaid. OpenFisca provided the framework for encoding rules, but OpenFisca-US was nascent and incomplete. Neither had a web interface that would let non-programmers explore policy options.

For state-level analysis—crucial since many UBI proposals targeted specific states—the tools barely existed at all.

The first researcher I recruited was Nate Golden, a middle school math teacher in Washington, DC, passionate about fighting poverty with evidence-based policy. The second came from an unexpected place: I posted on the Basic Income subreddit looking for researchers. Nikhil Woodruff, a college student in the UK, replied. He turned out to have a rare combination—economic policy interest and software engineering skill.

The UBI Center produced reports analyzing Andrew Yang's Freedom Dividend proposal, carbon dividend designs, child allowances. But every analysis required cobbling together partial tools, writing custom code, working around gaps in the existing infrastructure.

I kept hitting walls. I'd want to model a policy and discover that nobody had encoded the relevant benefit program. Or the model existed but hadn't been updated in years. Or it worked but required expertise I didn't have to run it.

The frustration wasn't unique to UBI research. Anyone trying to analyze cross-cutting policy reforms faced the same barriers. The open-source revolution had produced components, but no one had assembled them into something ordinary researchers—let alone citizens—could use.

And critically: there was no open-source model of the UK tax and benefit system at all. If Nikhil and I wanted to do comparative UBI analysis across the US and UK, we would need to build the UK model from scratch.

So we did.

---

## What Was Missing

Looking back, the gaps were clear:

**Integration.** The tools were fragmented. Tax models didn't talk to benefit models. Federal systems didn't connect to state systems. No one had built the comprehensive picture.

**Accessibility.** Running a microsimulation required installing software, preparing data, writing code. The barrier to entry was too high for most potential users.

**Data infrastructure.** Open-source rules were necessary but not sufficient. Without open (or at least accessible) data, you couldn't do population-level analysis.

**Sustainability.** Open-source projects depended on volunteer maintainers who could lose interest, change jobs, or simply burn out. Long-term maintenance was nobody's job.

**Trust and validation.** How did you know if a model was accurate? There were no systematic comparisons to authoritative sources, no uncertainty quantification, no institutional credibility.

The open-source revolution had proved the concept. OpenFisca showed that legislation *could* be code. Tax-Calculator showed that rigorous tax modeling *could* be open. UKMOD showed that major governments *could* use open-source tools.

But the revolution was incomplete. The tools were promising components, not finished products. Using them required expertise that most researchers lacked and all citizens lacked.

For the promise to be fulfilled—for ordinary people to actually be able to model policy and understand how it affected them—someone would need to assemble the pieces.

---

## Toward Part II

The researchers who had built these tools understood the gaps. Holly Sutherland at Essex knew that EUROMOD's accessibility was limited. Matt Jensen at AEI knew that Tax-Calculator served a niche audience. The OpenFisca team knew that encoding rules was only half the battle.

What none of them had done was build the full stack: rules plus data plus interface plus institutional credibility. A platform that could take a researcher's question—or a citizen's question—and return an answer they could trust.

That challenge would require not just technical work but organizational building. Someone would need to fund ongoing maintenance, hire engineers, establish relationships with official data sources, build trust with policymakers.

In 2021, the UBI Center researcher who had been frustrated by the tool gaps decided to address them directly. PolicyEngine was born—first for the UK, then for the US—as an attempt to complete what the open-source revolution had started {cite}`policyengine2024about`.

That story is the subject of Part II. But it only makes sense in the context of what came before: Orcutt's vision of simulating society from the bottom up, the tax model wars that concentrated analytical power in government institutions, and the open-source revolution that began to democratize access without yet completing the job.

The tools were ready. The infrastructure was emerging. The question was whether anyone could put it all together.

---

## References

```{bibliography}
:filter: docname in docnames
```

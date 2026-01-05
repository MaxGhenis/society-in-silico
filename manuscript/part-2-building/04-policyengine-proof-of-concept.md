# Chapter 4: PolicyEngine - Proof of Concept

In September 2021, a website launched that let anyone in the United Kingdom design their own tax and benefit system.

The premise was simple: enter a policy reform—raise income tax, increase child benefits, introduce a carbon dividend—and see the effects. Not just abstract estimates, but specific numbers: the cost to the Treasury, the change in poverty rates, the impact on inequality. And then enter your own household circumstances and see what the reform would mean for you personally {cite}`policyengine2021review`.

PolicyEngine UK was, as its creators claimed, "the world's first product allowing anyone to design policy reforms and see both the effects on specific households, and on UK-wide outcomes like poverty, inequality and the budget" {cite}`policyengine2021review`.

Behind this launch was a frustration that had been building for years.

---

## The UBI Center Problem

I had founded the UBI Center in 2019 to conduct rigorous, open-source research on universal basic income policies {cite}`ubicenter2019intro`. The idea was to bring quantitative analysis to UBI debates—not advocacy, but numbers. How much would different UBI designs cost? Who would gain, who would lose? How would a basic income interact with existing taxes and benefits?

The problem was immediate: UBI is a deceptively simple policy that interacts with everything else. A $1,000-per-month basic income doesn't just add $1,000 to everyone's income. It affects tax liabilities. It changes benefit eligibility. It alters work incentives. To model UBI properly, you needed to model the entire tax-benefit system.

In the United States, Tax-Calculator could handle federal income taxes, but not benefits like SNAP or Medicaid. OpenFisca-US was nascent. And for state-level analysis—crucial since many UBI proposals targeted specific states—the tools barely existed at all.

The first researcher I recruited was Nate Golden, a middle school math teacher in Washington, DC, who was passionate about using evidence to fight poverty. The second came from an unexpected source: I posted on the basic income subreddit looking for researchers interested in UBI policy analysis.

Nikhil Woodruff replied. He was a college student in the UK with an unusual combination: deep interest in economic policy and strong software engineering skills. The collaboration started in early 2020, just as the COVID-19 pandemic was beginning {cite}`policyengine2021review`.

We wanted to analyze UBI policies across both countries: the US where I lived, and the UK where Nikhil lived. But there was no open-source model of the UK tax and benefit system.

So we built one.

---

## Building OpenFisca UK

The foundation was OpenFisca, the French framework that had proven legislation could be encoded as executable code {cite}`openfisca2024about`. But OpenFisca was a framework, not a complete model. Someone still had to encode every benefit rule, every tax bracket, every eligibility threshold.

Woodruff did the work. Over months in 2020 and 2021, he built OpenFisca UK from scratch: Income Tax, National Insurance, Universal Credit, Child Benefit, Council Tax Reduction, dozens of interacting programs. The codebase grew to encode the complex reality of British tax and benefit policy—means tests, tapers, interactions, special cases {cite}`policyengine2021review`.

> "Over the past year, we developed OpenFisca UK, the UK's first open source tax and benefit microsimulation model, and used it to produce four reports and three conference presentations on UBI in the UK."

The model could run simulations, but only for programmers comfortable with Python. That wasn't good enough.

---

## From Model to Product

The leap from research tool to public product was deliberate. The UBI Center had built interactive tools before—visualizations that let users explore different UBI parameters. But PolicyEngine would go further. It would put the full power of the microsimulation model in a web browser, accessible to anyone {cite}`ubicenter2021policyengine`.

The technical architecture reflected this goal. The model ran on Python in the cloud, called through an API. The frontend was a React application that managed complex state: household definitions, policy parameters, simulation results. Users could define reforms without writing code, and see results update in seconds.

In October 2021, we spun PolicyEngine off as a new nonprofit organization. The mission statement evolved: no longer just "Make Everyone a Policymaker," but "Help People Understand and Change Public Policy" {cite}`policyengine2021review`. The second verb mattered. Understanding was passive; changing required agency.

Within months of launch, the public policy community had started using the tool. The UBI Lab Network embedded PolicyEngine in their Resilience UBI proposal. Parliamentary groups experimented with policies in real time during presentations. When the Chancellor announced Autumn Budget changes to Universal Credit, PolicyEngine had analysis published within a day {cite}`policyengine2021review`.

---

## Crossing the Atlantic

In March 2022, PolicyEngine expanded to the United States {cite}`policyengine2022review`.

The US model was different—not just in the policies encoded, but in the data challenges and institutional landscape. The UK has a single national tax system, though Scotland sets its own income tax rates (Wales and Northern Ireland have more limited fiscal powers). The US, by contrast, has fifty states with entirely separate income tax codes, plus a federal system of bewildering complexity.

We started with household impacts: enter your circumstances, see your taxes and benefits. Then in July 2022, we added population impacts using the Current Population Survey—the same microdata foundation that official government estimates relied on {cite}`policyengine2022review`.

State by state, the model grew. Maryland. Massachusetts. Oregon. New York. Pennsylvania. Washington. Each state had its own income tax structure, its own EITC variants, its own quirks.

> "The US is not just one launch: each state has their own benefit program rules, and most have their own income tax as well."

The expansion was exhausting and incomplete. By the end of 2022, PolicyEngine had modeled six states with dozens more to go. The gap between ambition and capacity was palpable.

---

## What "Open" Actually Means

PolicyEngine inherited the open-source ethos of its predecessors, but extended it deliberately. The code was on GitHub—anyone could see the formulas, trace the calculations, identify bugs {cite}`policyengine2024github`. The methodology was documented. The data sources were cited.

But open-source means more than accessible code. It means choices about governance, funding, and sustainability.

The organization was structured as a nonprofit. This wasn't accidental. Tax and benefit analysis is politically charged; an organization funded by ideological donors or structured for profit would face questions about neutrality. The nonprofit structure was a commitment: analysis without advocacy.

Funding came from foundations and individual donors. End Poverty Make Trillions provided early grants for US development. Innovation Network for Communities and Gary Community Ventures followed. The Policy Simulation Library Foundation served as fiscal sponsor, offering tax-deductible status {cite}`policyengine2022review`.

The contributors were largely volunteers, supplemented by a small paid team. Dozens of developers contributed to the various repositories: the US model, the UK model, the web app, the API, the documentation. Open source meant distributed maintenance—anyone could fix a bug, add a benefit program, update a threshold.

---

## The Use Cases Emerge

As PolicyEngine grew, patterns emerged in how people used it.

**Researchers** found a tool that could answer questions they couldn't answer before. The Center for Growth and Opportunity used PolicyEngine to analyze how targeted cash assistance affects work incentives. The Social Market Foundation modeled cost-of-living responses. Academic economists cited PolicyEngine results in papers {cite}`policyengine2022review`.

**Advocates** discovered they could make quantitative arguments without paying consultants. The Maryland Child Alliance used PolicyEngine to analyze child poverty policies. UBI Lab Northern Ireland modeled recovery basic income proposals. Organizations that had previously relied on government estimates or expensive think tank reports could now run their own simulations.

**Journalists** appreciated the speed. When UK Prime Minister Liz Truss announced tax cuts in her short-lived administration, PolicyEngine produced distributional analysis within hours—estimates that appeared in news coverage before official government figures {cite}`policyengine2022review`.

**Policymakers** themselves used the tool. We presented to the US Congressional Budget Office, to UK Parliamentary groups on Universal Basic Income, to the Green Party of England and Wales at their PolicyFest {cite}`policyengine2022review`. Staff members and elected officials ran scenarios, explored alternatives, asked "what if."

And increasingly, **developers** built on the API. The Fund for Guaranteed Income integrated PolicyEngine to show participants how pilot programs would affect their benefits. Gary Community Ventures used the API in their tools. The boundary between PolicyEngine as product and PolicyEngine as infrastructure was blurring.

---

## Recognition and Validation

In April 2023, the Digital Public Goods Alliance—a UN-endorsed initiative involving UNICEF, the Norwegian Agency for Development Cooperation, and others—added PolicyEngine to their registry {cite}`policyengine2023dpg`. The recognition affirmed that PolicyEngine met their standard for digital public goods: open-source, privacy-respecting, do-no-harm, and supporting the UN Sustainable Development Goals.

The specific SDGs cited were telling: ending poverty, achieving gender equality, promoting inclusive economic growth, reducing inequality. PolicyEngine wasn't just a technical achievement; it was infrastructure for the kind of analysis those goals required.

By late 2023, we had grown from two cofounders to a staff of five, with a researcher network and dozens of open-source contributors. The models had expanded to include Canada and Nigeria prototypes. The data science had improved with machine learning-based reweighting that made estimates more accurate than ever before {cite}`policyengine2023enhanced`.

And the vision was evolving. "We've come to see another opportunity," the 2021 review had noted. "The same open source policy simulation models that power our reform analysis can also show people their tax liability and benefit entitlement under current law" {cite}`policyengine2021review`.

It wasn't just about policy reform analysis. It was about helping ordinary people understand the complex systems that governed their financial lives.

---

## The Gaps Remain

Despite the progress, honest assessment revealed limitations.

**Coverage was incomplete.** The US model handled federal taxes and major benefit programs, but not every state, not every local quirk, not every edge case. The UK model was more comprehensive but still had gaps—housing benefit calculations, legacy benefit interactions, Scotland-specific provisions.

**Accuracy varied.** We invested heavily in validation, comparing PolicyEngine results to official calculators and published statistics. But microsimulation is an approximation, and the further you got from typical cases, the more uncertainty crept in {cite}`policyengine2024ukvalidation`.

**Usability challenged non-experts.** The interface was simpler than programming, but modeling a complex reform still required understanding of policy terminology, tax concepts, and the limitations of the tool. The dream of "everyone a policymaker" remained aspirational.

**Resources were thin.** A small team trying to maintain and improve models for multiple countries, respond to user requests, produce original research, and build new features faced constant tradeoffs. Open source meant anyone *could* contribute, but maintaining a production-quality policy analysis tool required sustained professional effort.

The proof of concept had worked. PolicyEngine demonstrated that open-source, accessible, rigorous policy analysis was possible. But the concept was still far from complete.

---

## From Tool to Infrastructure

Within three years of launch, PolicyEngine had evolved from a research tool to production infrastructure.

In April 2024, we solved the problem that had frustrated me at the UBI Center: state-level analysis. PolicyEngine launched comprehensive state income tax modeling for all 50 states and DC. Over 100 open-source contributors had encoded the nation's Byzantine patchwork of tax codes. What we couldn't find in 2019, we built by 2024.

The technical sophistication grew in parallel. In August 2025, we launched the Enhanced Current Population Survey, integrating five datasets using machine learning and calibrating to 9,168 administrative totals. The approach combined Quantile Regression Forests for imputation with gradient descent optimization for reweighting—techniques that cut our deviations from official statistics by 97 percent. We built two new open-source packages to do it: microimpute and microcalibrate.

But the real validation came from who started using it.

### Building a Validation Ecosystem

In September 2025, we signed a memorandum of understanding with the National Bureau of Economic Research to build an open-source emulator of TAXSIM, the tax calculator that has powered academic research since the 1970s. Over 1,200 papers had relied on TAXSIM. Brookings used it extensively for tax policy analysis. The Bureau of Labor Statistics used it for the Consumer Expenditure Survey. The Census Bureau evaluated it for the Supplemental Poverty Measure.

Daniel Feenberg, TAXSIM's creator, joined our advisory board and served as external mentor through our NSF grant. We were building the emulator to ensure researchers maintained access to these capabilities—but also to create something larger: a validation framework where multiple independent models could cross-check each other.

A month later, we signed a second MOU with the Federal Reserve Bank of Atlanta. Their Policy Rules Database covered benefits—SNAP, Medicaid, housing vouchers, childcare subsidies—complementing TAXSIM's focus on taxes. The database powered the Atlanta Fed's CLIFF tools, which Colorado's Workforce Development Council and New Mexico's Caregivers Coalition used to help families understand how earning more income would affect their benefits.

The three-way validation approach was deliberate. When independently developed models agree on a calculation, researchers can trust the result. When they diverge, the differences reveal important questions about policy interpretation or implementation details. Having three models—PolicyEngine, TAXSIM, and the Policy Rules Database—helped isolate where discrepancies originated.

We were no longer just another microsimulation model. We had become the integrator, the platform that validated across Python and R, across taxes and benefits, across academic and government implementations.

And then came the UK.

In March 2025, HM Treasury published an Algorithmic Transparency Record revealing they had piloted PolicyEngine UK as a potential supplement to their official Intra-Governmental Tax and Benefit Microsimulation model. The Times reported that the tool "can more accurately predict the outcome of ministers' decisions and is expected to be used mostly in budget periods."

The Treasury highlighted our machine learning approach to fixing survey data errors—combining multiple years of the Family Resources Survey, using random forest models to impute missing income, employing gradient descent to reweight households. The same techniques we'd developed for the Enhanced CPS, now being evaluated by the UK government to supplement their internal models.

From frustrated researcher cobbling together tools in 2019 to government ministries piloting our models in 2025. Six years.

### The API Becomes Infrastructure

The evolution from tool to platform showed up in unexpected ways. In 2025, MyFriendBen—a benefits screening platform—launched in North Carolina, Illinois, Colorado, and New York using PolicyEngine's API to calculate eligibility and benefit amounts. The tool achieved over 90 percent accuracy in six minutes, available in 12 languages. Colorado users discovered they were eligible for benefits averaging $1,500 per month—money they hadn't known they could access.

This was the vision from 2021: not just researchers using PolicyEngine, but PolicyEngine powering tools that helped people navigate the system. The API had become infrastructure for benefit access.

---

## Toward a Platform

By the end of 2022, we were already thinking about what came next.

"We've been exploring opportunities to leverage the recent explosion of artificial intelligence tools to make policy analysis more robust, accessible, and even delightful," we wrote in our 2022 review {cite}`policyengine2022review`.

The microsimulation engine was the foundation. But the engine could power many things: chatbots that explained policies in plain language, personalized calculators for specific use cases, automated research assistants that could answer policy questions.

The question was whether PolicyEngine would remain a product—a specific tool with a specific interface—or become infrastructure: a platform on which others could build.

That question, and the larger question of what AI would mean for policy analysis, is the subject of later chapters. But first, we need to understand what PolicyEngine actually does—how it works at the level of individual households and entire populations.

---

## References

```{bibliography}
:filter: docname in docnames
```

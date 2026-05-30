# Chapter 5: PolicyEngine - Proof of Concept

## The State of Play, 2019-2021

The years 2019-2021 were transformative for open-source policy modeling, even before PolicyEngine launched.

In September 2019, UKMOD became the UK's first freely available tax-benefit microsimulation model. The UK had proprietary tools—the Institute for Fiscal Studies' TAXBEN since 1983, HM Treasury's IGOTM, the Department for Work and Pensions' PSM—but UKMOD was different. Built on EUROMOD's UK component and funded by the Nuffield Foundation, it was academic-focused but open to anyone.

Then COVID-19 hit, and suddenly everyone needed rapid policy analysis. The CARES Act, unemployment insurance expansions, recovery rebates—policy changed weekly. NBER released TAXSIM35 in 2020 with CARES Act provisions. Tax-Calculator v3.2.1 followed in August 2021 with pandemic updates. The International Microsimulation Association held a dedicated conference in December 2020 on COVID policy responses.

The most significant shift came in December 2020: EUROMOD went fully open source. What had been "open access" became genuinely open, with the JRC European Commission assuming control in January 2021. After decades of proprietary European policy modeling, the code was finally public.

The Policy Simulation Library expanded. The Capital Cost Recovery model joined. The OG-USA overlapping-generations model joined. Demo Day webinars showcased new applications. The open-source ecosystem was growing, but a critical gap remained: none of these tools were accessible to non-programmers.

I had started the UBI Center in 2019 with a simple frustration: I wanted to know what various universal basic income proposals would cost and who they'd help, and no publicly available tool could answer the question with specificity [@ubicenter2019intro]. The UBI Center became a research organization that published open-source analyses of basic income proposals, using whatever microsimulation tools were available—mostly Tax-Calculator and custom Python scripts built on CPS data.

The work taught me two things. First, the tools existed in fragments. Tax-Calculator handled federal income tax beautifully but didn't cover benefits. TAXSIM handled state taxes but required batch processing. No single tool captured the full interaction between taxes and benefits that determined whether a UBI proposal was progressive, regressive, or poverty-reducing.

Second, the audience for policy analysis was far larger than the audience that could use the tools. When I published UBI Center analyses, the response was enormous from people who wanted to explore the ideas themselves—vary the parameters, check different household types, model the proposals their local advocacy group was pushing. They couldn't, because the tools lived in Jupyter notebooks.

By late 2020, Nikhil Woodruff and I had a working microsimulation model of the UK tax and benefit system we'd built at the UBI Center. Nikhil was an undergraduate at UCL studying mathematics and computer science—preternaturally talented at software engineering, with an intuitive grasp of how to translate complex policy rules into clean code. OpenFisca UK could calculate taxes, simulate benefits, estimate policy reform effects. But it lived in Python scripts that only programmers could run.

We'd seen this pattern everywhere—TAXSIM required batch processing, Tax-Calculator needed Python, UKMOD was academic-focused, TAXBEN was proprietary. Powerful tools locked behind technical barriers. The solution was obvious but ambitious: build a web application that put the full power of microsimulation in a browser. Anyone could design a reform, see the costs and distributional effects, understand the impact on their own household. No code required.

We called it PolicyEngine.

---

## Building the Application

The technical challenge was translating microsimulation—a fundamentally computational process—into an interface that felt intuitive. We built the system in layers.

**The model layer** ran in Python on cloud servers. OpenFisca UK encoded the tax and benefit rules as executable code. Feed it a household's circumstances and a policy reform, and it calculated the exact tax liability and benefit entitlement before and after the change.

**The API layer** wrapped the model in HTTP endpoints. The frontend sent requests describing households and reforms; the API ran simulations and returned results. This separation meant we could improve the model without rebuilding the interface, or redesign the interface without rewriting the model.

**The application layer** was a React web app that managed complexity. Users defined households by answering questions—income sources, number of children, housing costs. They specified reforms by adjusting sliders and toggles—income tax rates, benefit levels, eligibility thresholds. The app translated these interactions into API calls, ran simulations, and displayed results: budget impact, poverty changes, inequality effects, household-level impact.

The architecture reflected a key design decision: the model should be usable without the interface. The API was the product; the web app was one consumer of that API. This meant anyone—a researcher, a journalist, another application—could call the same engine that powered the website. At the time, this felt like overengineering. In retrospect, it was the decision that made everything else possible. When developers later wanted to embed PolicyEngine calculations in their own tools, the API already existed.

The first version took months to build. Nikhil handled most of the engineering—API design, React components, state management. I focused on the policy logic—which parameters to expose, how to present results, what comparisons mattered. We debated endlessly about the reform interface. How much complexity should users see? Exposing every parameter in the tax-benefit system would be overwhelming—there are thousands. Hiding too many would limit what users could model. We settled on a compromise: a curated set of frequently-discussed parameters (income tax rates, benefit levels, credit amounts) with the option to adjust any parameter in the model for users who knew what they were looking for.

The output was similarly contested. We wanted to show budget cost, poverty impact, inequality metrics, and distributional effects—but presenting all of that at once risked information overload. The solution was progressive disclosure: headline numbers first (net cost, poverty change), then detailed breakdowns (by income decile, by household type, by region) for users who wanted to dig deeper.

We launched PolicyEngine UK in September 2021 [@policyengine2021review].

The premise was simple: enter a policy reform—raise income tax, increase child benefits, introduce a carbon dividend—and see the effects. Not abstract estimates, but specific numbers. The cost to the Treasury. The change in poverty rates. The impact on inequality. And critically: enter your own household circumstances and see what the reform would mean for you personally.

The response surprised us. Within weeks, advocacy groups were using PolicyEngine to design proposals. Parliamentary groups experimented with policies during presentations. When the Chancellor announced Autumn Budget changes to Universal Credit, we published analysis within a day [@policyengine2021review]. News outlets cited our numbers.

In October 2021, we spun PolicyEngine off as a separate nonprofit organization. The mission statement evolved from "Make Everyone a Policymaker" to "Help People Understand and Change Public Policy." The second verb mattered—understanding was passive, changing required agency.

Incorporation as a 501(c)(3) was itself a design choice. We wanted PolicyEngine to be trusted by all sides of the political spectrum—progressive groups designing basic income proposals and conservative groups analyzing flat tax reforms should both feel confident the model wasn't biased toward the other side. Nonprofit status, combined with open-source code, was our answer to the trust problem. Any user could inspect the calculations. The organization had no shareholders whose interests might distort the analysis. Revenue came from grants and donations, not from clients who might prefer particular results.

The early team was small and overextended. Nikhil remained the primary engineer, joined by a rotating cast of volunteers, interns, and part-time contributors. I handled strategy, fundraising, research output, and increasingly, the communication work that came with media attention. When the Autumn Budget analysis went viral, we weren't a media operation—we were two people with a model and a website, scrambling to respond to interview requests while simultaneously fixing bugs that the attention revealed.

---

## Crossing the Atlantic

In March 2022, we launched PolicyEngine US [@policyengine2022review].

The US model was different—not just in the policies encoded, but in the entire structure of the challenge. The UK has a single national tax system, though Scotland sets its own income tax rates. Universal Credit replaced most legacy benefits, meaning one system handled most means-tested support. The US has fifty states with separate income tax codes, plus a federal system of bewildering complexity. Benefits are fragmented across agencies: SNAP from the USDA, SSI from the Social Security Administration, Medicaid from HHS, housing vouchers from HUD, childcare subsidies from state agencies. Each program has its own definition of income, its own household unit, its own eligibility rules. Modeling the US wasn't just harder than modeling the UK—it was a categorically different kind of problem, with complexity that grew multiplicatively rather than additively.

We started with what we could model: federal income and payroll taxes, major benefit programs like SNAP and the EITC. The household calculator launched first—enter your circumstances, see your taxes and benefits. Then in July 2022, we added population impacts using the Current Population Survey, the same microdata foundation that official government estimates relied on [@policyengine2022review].

But state-level analysis remained incomplete. We began encoding state income taxes one by one: Maryland, Massachusetts, Oregon, New York, Pennsylvania, Washington. Each state had its own structure, its own EITC variants, its own quirks. Some states piggyback on the federal adjusted gross income, making their systems relatively simple to encode once you have the federal model. Others—like New York, with its multiple income tax schedules, city taxes, and supplemental credits—were their own miniature ecosystems. By the end of 2022, we had modeled six states. Forty-four remained.

The gap between ambition and capacity was palpable. We wanted comprehensive coverage; we had a small volunteer team encoding policies in their spare time. We wanted immediate updates when policies changed; we struggled to keep models current. We wanted validation against official estimates; we often discovered discrepancies we couldn't easily resolve. A contributor might encode Oregon's working family household credit, only to discover that the state had amended the eligibility rules in the latest legislative session—and the amendment hadn't been reflected in the official documentation we were working from.

The contributor model was open source in the truest sense: anyone could submit a pull request encoding a state's tax rules, and our team would review it for accuracy and code quality. This worked for states where a local policy expert cared enough to contribute. It didn't work for states where no one volunteered. The result was patchy coverage that correlated with contributor geography rather than policy importance.

The proof of concept worked—people wanted accessible policy analysis—but scaling it would require more than enthusiasm and weekends.

---

## Who Used It

As PolicyEngine grew, we tracked how different groups engaged with the tool. The patterns revealed both what we'd built successfully and what remained aspirational.

Researchers found PolicyEngine could answer questions other tools couldn't. The Center for Growth and Opportunity used it to analyze how targeted cash assistance affects work incentives. The Social Market Foundation modeled cost-of-living responses. Academic economists cited PolicyEngine results in papers [@policyengine2022review]. The academic use case worked because researchers needed flexibility—they wanted to test specific policy variants, compare alternatives, run sensitivity analyses. PolicyEngine provided that.

Advocacy groups discovered they could make quantitative arguments without hiring consultants. The Maryland Child Alliance analyzed child poverty policies. UBI Lab Northern Ireland modeled recovery basic income proposals. Organizations that had previously relied on government estimates or expensive think tank reports could now run their own simulations. This democratization mattered—it meant smaller organizations with limited budgets could participate in policy debates with numbers, not just narratives.

Journalists appreciated the speed. When UK Prime Minister Liz Truss announced tax cuts during her short-lived administration, we produced distributional analysis within hours. News coverage included our estimates before official government figures appeared [@policyengine2022review]. The journalism use case revealed both capability and risk—we could move fast, but speed created pressure to avoid errors that would undermine credibility.

Policymakers themselves used the tool, though more cautiously. We presented to the US Congressional Budget Office, to UK Parliamentary groups, to the Green Party of England and Wales [@policyengine2022review]. Staff members and elected officials ran scenarios, explored alternatives, asked "what if" questions. But official use remained limited—governments had their own models, their own methodologies, their own validation processes. PolicyEngine could inform but not replace official analysis.

The most revealing feedback came from legislative staff. A Congressional aide could use PolicyEngine to quickly test whether a proposed CTC expansion would actually reach the families the member cared about, then use that analysis to shape the legislative language before requesting a formal CBO score. The informal tool didn't replace the formal process—but it changed what questions got asked at the formal stage. Instead of "what does this cost?" as the first question, staff could arrive at CBO with proposals already refined for distributional impact.

And increasingly, developers built on our API. The Fund for Guaranteed Income integrated PolicyEngine to show pilot program participants how their benefits would change. Gary Community Ventures used the API in their tools. We weren't just a product anymore; we were becoming infrastructure.

---

## The Validation Challenge

Open-source meant anyone could inspect our code, but inspection didn't guarantee correctness. We invested heavily in validation, comparing PolicyEngine results to official calculators and published statistics.

The results were mixed. Each model had a test suite comparing outputs to official calculations across hundreds of household scenarios. We tracked discrepancies systematically—was the bug in our code, the official calculator, or our interpretation of ambiguous rules?

Some bugs were straightforward: a phase-out rate coded as 21.06% instead of 21.6%, caught by comparing to IRS published tables. Others were genuinely ambiguous. When a regulation says income is calculated "net of applicable deductions," which deductions apply? Different official sources sometimes gave different answers. We maintained a tracking system for these ambiguities—cases where reasonable interpretations of the same statute produced different numbers. The existence of these ambiguities was itself a finding: the tax-benefit system was so complex that even the agencies administering it sometimes disagreed on the rules.

For the UK model, HM Treasury eventually conducted their own evaluation. They found 60 percent of National Insurance calculations fell within 0.5 percent of their internal model [@hmt2025policyengine]. But income tax validation proved more challenging—they had difficulty identifying comparable variables between our approaches. Edge cases revealed gaps throughout: housing benefit interactions with legacy benefits, Scotland-specific tax provisions, transition rules for households moving between programs. The lesson was that validation against government models is harder than it sounds—not because the math is difficult, but because the two systems may define "income" differently, aggregate at different levels, or handle household composition in incompatible ways.

The US model faced different validation challenges. With fifty state income tax systems, we needed to compare against fifty different official sources—when those sources existed. Some states provided online calculators we could test against. Others had rules buried in legislative text with no official tool to verify our implementation. Federal programs were better documented, but interactions between federal and state systems created combinatorial complexity.

And we openly acknowledged a fundamental limitation: revenue estimates. PolicyEngine used household survey data; governments used administrative tax records. Survey data consistently under-samples high-income households—the CPS might include a few hundred households with incomes above $500,000, while IRS records contain millions. Since high-income taxpayers generate a disproportionate share of revenue, this sampling gap cascaded into aggregate estimates. The result: our revenue projections ran about one-third lower than official government estimates. This wasn't a bug we could fix with better code—it was a structural constraint of survey-based microsimulation that required better data, which arrived later with the Enhanced CPS (Chapter 8).

The revenue gap shaped how we communicated results. We learned to emphasize *relative* impacts (how much does Reform A increase or decrease revenue compared to current law) rather than *absolute* revenue levels. Relative changes were more stable because the survey sampling error affected both the baseline and the reform similarly, partially canceling out. But sophisticated users wanted absolute numbers, and we couldn't always explain why ours differed from CBO's without a lecture on survey methodology.

The validation work was never finished. Policies changed constantly—tax brackets adjusted for inflation, benefit eligibility thresholds updated, new programs launched. Keeping models current required sustained attention. But validation mattered for credibility. If journalists, researchers, or policymakers were going to cite our numbers, those numbers needed to be defensible.

---

## From Tool to Infrastructure

In 2024, the National Science Foundation awarded PolicyEngine a Pathways to Enable Open-Source Ecosystems (POSE) grant to expand access to policy analysis tools—recognition that open-source microsimulation had become infrastructure worth investing in. The grant helped fund what had been a volunteer effort.

By April 2024, we solved the problem that had frustrated me at the UBI Center: state-level analysis. PolicyEngine launched comprehensive income tax modeling for all 50 states and DC. Over 100 open-source contributors had encoded the nation's Byzantine patchwork of tax codes. What we couldn't find in 2019, we built by 2024. The final push required a sustained campaign: identifying the remaining states, finding contributors with local expertise or recruiting engineers willing to parse unfamiliar tax codes, and validating each implementation against whatever official tools or published tables existed. Some states were straightforward—flat tax states with few credits took days. Others—New York, California, Hawaii—took weeks of iterative debugging.

The technical sophistication grew in parallel. In August 2025, we launched the Enhanced Current Population Survey, integrating five datasets using machine learning and calibrating to 9,168 administrative totals. The approach combined Quantile Regression Forests for imputation with gradient descent optimization for reweighting—techniques that cut our deviations from official statistics by 97 percent [@policyengine2022enhanced]. We built two new open-source packages to do it: microimpute and microcalibrate.

But the real validation came from who started using it.

In September 2025, we signed a memorandum of understanding with the National Bureau of Economic Research to build an open-source emulator of TAXSIM, the tax calculator that has powered academic research since the 1970s. Over 1,200 papers had relied on TAXSIM. Brookings used it extensively. The Bureau of Labor Statistics used it for the Consumer Expenditure Survey. The Census Bureau evaluated it for the Supplemental Poverty Measure.

Daniel Feenberg, TAXSIM's creator, joined our advisory board and served as external mentor through our NSF grant. We were building the emulator to ensure researchers maintained access to these capabilities—but also to create something larger: a validation framework where multiple independent models could cross-check each other.

A month later, we signed a second MOU with the Federal Reserve Bank of Atlanta. Their Policy Rules Database covered benefits—SNAP, Medicaid, housing vouchers, childcare subsidies—complementing TAXSIM's focus on taxes. The database powered the Atlanta Fed's CLIFF tools, which Colorado's Workforce Development Council and New Mexico's Caregivers Coalition used to help families understand how earning more would affect their benefits.

The three-way validation approach was deliberate. When independently developed models agree on a calculation, researchers can trust the result. When they diverge, the differences reveal important questions about policy interpretation or implementation details. Having three models—PolicyEngine, TAXSIM, and the Policy Rules Database—helped isolate where discrepancies originated.

We were positioning PolicyEngine as more than another microsimulation model—as an integrator that could cross-validate across Python and R, across taxes and benefits, across academic and government implementations.

And then came the UK.

In March 2025, HM Treasury published an Algorithmic Transparency Record revealing they had piloted PolicyEngine UK as a potential supplement to their official Intra-Governmental Tax and Benefit Microsimulation model—IGOTM, the closed system that had generated government policy estimates for decades. The Times reported that the tool could more accurately predict the outcomes of ministers' decisions and was expected to be used mainly in budget periods.

The Treasury highlighted our machine learning approach to fixing survey data errors—combining multiple years of the Family Resources Survey, using random forest models to impute missing income, employing gradient descent to reweight households. The same techniques we'd developed for the Enhanced CPS, now being evaluated by the UK government to supplement their internal models.

The significance went beyond validation. For decades, government microsimulation models were closed by default—proprietary code, restricted data, results that could be questioned but not reproduced. An outside tool good enough for the Treasury to pilot threatened that default. If an open-source model could even partly reproduce the government's internal estimates—and the Treasury thought it worth testing—the case for keeping those models closed weakened. The Treasury's evaluation wasn't just about PolicyEngine; it was about whether the monopoly on policy analysis infrastructure could hold.

In 2019 I couldn't find a tool to answer a basic question about a universal basic income; by 2025 HM Treasury was piloting one we'd built.

In 2025, MyFriendBen—a benefits screening platform—launched in North Carolina, Illinois, Colorado, and New York using PolicyEngine's API to calculate eligibility and benefit amounts. PolicyEngine's launch note reported that the personalized estimates matched expected amounts more than 90 percent of the time, in about six minutes, across 12 languages—a self-reported figure, not an independent audit [@policyengine2025myfriendben]. In Colorado, MyFriendBen reported that users surfaced an average of $1,500 per month in benefits they appeared eligible for but hadn't claimed [@myfriendben2025pueblo].

This was the vision from 2021: not just researchers using PolicyEngine, but PolicyEngine powering tools that helped people navigate the system. The API had become infrastructure for benefit access.

---

## What We Built, What Remained

By late 2025, PolicyEngine had evolved from a research tool to production infrastructure. We had comprehensive tax and benefit models for the US and UK. We had validation partnerships with NBER and the Atlanta Fed. We had government agencies piloting our models. We had developers building on our API.

But honest assessment revealed what we hadn't solved.

**Accuracy varied by use case.** Household-level calculations were highly accurate, and enhanced microdata dramatically improved aggregate estimates (Chapter 8). But unusual situations revealed limitations, and survey-based revenue estimates consistently ran below official projections—a structural constraint Chapter 8 explores in detail.

**Usability challenged non-experts.** The interface was simpler than programming, but modeling a complex reform still required understanding policy terminology, tax concepts, and the tool's limitations. We could explain that increasing the personal allowance reduces revenue, but users needed to know what a personal allowance was. We could show distributional effects across income deciles, but users needed to understand what that meant for actual families. The dream of "everyone a policymaker" remained aspirational—though "many more people than before" was real progress.

**Resources constrained what we could build.** A team of five staff plus volunteers maintaining models for multiple countries, responding to user requests, producing research, building new features, and keeping everything updated faced constant tradeoffs. Open source meant anyone *could* contribute, but production-quality policy analysis tools required sustained professional attention. We chose what to prioritize and accepted what we couldn't do. Canada, which we launched in 2023, received less attention than the US and UK. Feature requests accumulated faster than we could address them. The tension between being a research organization (producing analyses) and an infrastructure provider (maintaining software) was never fully resolved.

**Sustainability remained uncertain.** Nonprofits building open-source infrastructure face a structural challenge: the users who benefit most—government agencies, think tanks, fintech companies—don't always fund the tools they rely on. Foundation grants supported research but not infrastructure maintenance. Government contracts required more institutional overhead than a small team could manage. The business model question—how to sustain open-source policy infrastructure over decades, not just grant cycles—was the hardest unsolved problem by late 2025.

The proof of concept had worked. We'd demonstrated that open-source, accessible, rigorous policy analysis was possible. But moving from proof of concept to sustainable infrastructure would require thinking differently about what PolicyEngine was and what it could become. That infrastructure question—how to build production-ready simulation that AI systems, governments, and citizens all rely on—is the subject of Chapter 10.

---

## References

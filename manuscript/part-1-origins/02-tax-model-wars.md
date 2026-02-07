# Chapter 2: The Tax Model Wars

In 1983, a small think tank in London did something that would reshape policy analysis for decades: they built a tax-benefit model and used it to critique the government's budget.

The Institute for Fiscal Studies had existed since 1969, founded by four financial professionals frustrated by the opacity of UK tax policy {cite}`ifs2024history`. But TAXBEN—their microsimulation model of British taxes and benefits—gave them something new: the ability to run the numbers themselves. When the Chancellor announced a budget, IFS could simulate its effects on different household types within hours. Their "Green Budget" analyses became essential reading for journalists, politicians, and civil servants alike.

This was a small revolution. For the first time, an independent organization could challenge official government estimates with its own calculations. The asymmetry of information that had always favored those in power was beginning to crack.

But only beginning. Four decades later, that asymmetry persists—and understanding why requires tracing how tax microsimulation spread through governments, think tanks, and eventually into the open.

---

## The American Machinery

While IFS was building TAXBEN in London, American government agencies were constructing their own microsimulation apparatus—but behind closed doors.

The story begins with Alice Rivlin.

In 1974, Congress created the Congressional Budget Office to give itself independent analytical capacity—no longer relying solely on the executive branch for budget projections. Rivlin, an economist at Brookings, became CBO's first director. Her vision was specific: CBO would be nonpartisan, analytical, and unafraid to publish numbers that made both parties uncomfortable {cite}`rivlin1984economics`. She staffed the office with economists, not political operatives, and established a culture of methodological transparency that persists five decades later.

CBO developed microsimulation models for health insurance, Social Security, and tax analysis. For long-term projections—especially the fiscal trajectory of entitlement programs—they built CBOLT, the Congressional Budget Office Long-Term model {cite}`cbo2018overview`. These models gave Congress something it had never had: the ability to independently evaluate the President's budget proposals with its own numbers.

The Joint Committee on Taxation, created in 1926, had long been Congress's official scorekeeper for tax legislation {cite}`jct2024history`. By the 1970s, JCT was developing sophisticated microsimulation models: an Individual Model, a Corporate Model, an International Cross Border Model, an Estate and Gift Model {cite}`jct2024revenue`. When a member of Congress proposed a tax change, JCT's models would estimate its cost. These estimates carried legal weight—the Budget Act of 1974 made JCT the official source of revenue estimates for Congress.

The process was—and remains—remarkably consequential. A senator drafts a tax amendment. JCT's staff feed the proposal into their microsimulation models, which apply the new rules to a representative sample of tax returns drawn from actual IRS data. Within days, sometimes hours, JCT produces a "score"—the projected change in federal revenue over ten years. That number determines whether the amendment is fiscally viable, whether it fits within a budget resolution, whether it can pass under reconciliation rules. A score that comes in too high kills proposals before they reach a vote.

The Treasury's Office of Tax Analysis built parallel capabilities for the executive branch. George Sadowsky's work in the early 1960s had demonstrated what was possible {cite}`sadowsky1991computing`; by the 1980s, Treasury maintained the Individual Income Tax Model (ITM), regularly updated with fresh data from IRS tax returns. Treasury's models served the President—providing revenue estimates for Administration proposals—while JCT's served Congress.

Outside government, the Urban Institute was building its own analytical infrastructure. Karen Smith joined Urban in the 1980s and would spend three decades developing microsimulation models for Social Security, pensions, taxation, and welfare reform {cite}`urban2024karensmith`. She played lead roles in both MINT (the Social Security Administration's retirement income model) and DYNASIM (Urban's flagship dynamic microsimulation). While Urban's models served government clients rather than challenging official estimates, Smith was building expertise that would bridge the mainframe era into the age of open source.

Three major government institutions, plus Urban's adjacent capacity. Billions of dollars in policy decisions riding on their outputs. And almost none of it was visible to the public.

---

## The Asymmetry Problem

Here was the situation by the 1990s: if you wanted to know how a tax proposal would affect federal revenue, you had to trust the government's numbers. You couldn't check their work. You couldn't see their code. You couldn't run alternative scenarios. The models were black boxes, and the keys were held by a small priesthood of government economists.

This created several problems.

**Trust deficits.** When JCT or Treasury produced an estimate that a politician disliked, they could dismiss it as biased without anyone being able to verify. When estimates turned out wrong—as they inevitably sometimes did—there was no way to understand why.

**Limited debate.** Policy discussions were constrained by what the official scorekeepers would analyze. Novel proposals that didn't fit their modeling frameworks often couldn't get scored at all, making them politically impossible regardless of their merits.

**Expertise hoarding.** The skills to build and maintain these models concentrated in a few institutions. Academic economists could study tax policy, but they couldn't replicate the government's analytical infrastructure.

**Democratic deficit.** Citizens and advocacy groups who wanted to understand how policies affected people like them had to take official estimates on faith. The asymmetry between governors and governed extended to the very tools used to evaluate policy.

Some academics pushed back. At the National Bureau of Economic Research, Daniel Feenberg began building TAXSIM in the early 1980s {cite}`feenberg1993taxsim`. By the 1990s, it had become internet-accessible—one of the first tax calculators available online. Feenberg would maintain TAXSIM for his entire career, a quiet but essential contribution that enabled generations of tax research. When researchers needed to calculate tax liabilities for survey respondents, TAXSIM was there—reliable, documented, freely available to academics.

But TAXSIM was a research tool, not a policy analysis platform. It calculated taxes for individual records; it didn't produce the aggregate estimates and distributional tables that drove policy debates. Feenberg had demonstrated that useful tools could be built outside government, even if they couldn't fully replicate official infrastructure. The question was whether anyone could go further.

---

## The Challengers

The first serious challenge to the government monopoly on policy analysis came from within the establishment—but outside the government.

In 2002, C. Eugene Steuerle and Leonard Burman founded the Tax Policy Center, a joint venture of the Urban Institute and Brookings Institution {cite}`tpc2024model`. Both were tax policy veterans—Steuerle had served at Treasury, Burman had worked at CBO and the Treasury Department. They understood the government's models because they had helped build them. Now they wanted to create something similar that would be independent, publicly accessible, and willing to analyze proposals the official scorekeepers wouldn't touch.

TPC built a microsimulation model using IRS public-use tax return data—the same foundation as government models, though with less granular data than what JCT accessed through confidential returns. The model could estimate revenue effects and distributional impacts of tax proposals, producing the kind of analysis that had previously required government resources.

The impact was immediate. When Mitt Romney ran for president in 2012, TPC published an analysis showing that his tax plan—which cut rates while claiming revenue neutrality through unspecified base broadening—was mathematically impossible without raising taxes on the middle class or losing revenue {cite}`tpc2012romney`. The finding dominated media coverage and reshaped the campaign debate. Romney's team disputed the analysis but couldn't rebut it with their own numbers—they didn't have a comparable model.

During the 2017 Tax Cuts and Jobs Act debate, TPC's distributional analysis showed that the benefits tilted heavily toward high-income households—a finding that complicated Republican messaging about the bill helping the middle class. JCT's official score put the ten-year cost at $1.46 trillion; TPC's estimates were broadly consistent but added distributional detail that JCT didn't publish.

Kent Smetters at the University of Pennsylvania launched the Penn Wharton Budget Model (PWBM) in 2016, adding another independent voice {cite}`pwbm2017tcja`. PWBM distinguished itself by producing dynamic estimates—incorporating macroeconomic feedback effects that static models ignore. For the TCJA, PWBM projected a cost of $1.8 to $2.2 trillion on a dynamic basis, significantly higher than JCT's static estimate. The difference reflected PWBM's assessment that the economic growth effects of the tax cuts would be modest—enough to offset some but not most of the revenue loss.

The Budget Lab at Yale, launched later, brought another analytical lens. By the mid-2020s, the ecosystem of independent tax analysis organizations had grown from zero to half a dozen, each with its own model, data, and methodology. The government's analytical monopoly was broken.

---

## The Dynamic Scoring Wars

Beneath the institutional competition lay a deeper methodological dispute: should budget scores account for macroeconomic feedback?

The question sounds technical. It's actually political dynamite.

Here's the issue. When JCT scores a tax cut, it traditionally uses "static" scoring—calculating the direct effect on revenue without assuming the tax cut changes the size of the economy. A $100 billion tax cut costs $100 billion.

But supply-side economists have long argued this understates the benefits of tax cuts. Lower tax rates increase incentives to work and invest, they claim. The economy grows. Some of that growth generates additional tax revenue, partially offsetting the cost. Under "dynamic" scoring, the $100 billion tax cut might cost only $70 billion.

The debate raged for decades. In 2003, the American Enterprise Institute hosted a forum on dynamic scoring featuring Alan Auerbach, William Gale, and other leading economists. In 2005, Auerbach published a formal treatment arguing that dynamic scoring was conceptually correct but practically difficult—the macroeconomic models needed to estimate feedback effects were themselves uncertain {cite}`auerbach2005dynamic`.

In January 2015, the new Republican House majority passed a rule requiring JCT to provide dynamic scores for major legislation—bills with budgetary effects exceeding 0.25% of GDP {cite}`crs2015dynamic`. This was a victory for supply-side advocates who believed static scoring systematically overstated the cost of tax cuts.

The first major test came with the TCJA in 2017. JCT's static score: $1.46 trillion in revenue loss over ten years. JCT's dynamic score: $1.07 trillion, reflecting projected economic growth that would generate $389 billion in additional revenue. The dynamic score reduced the estimated cost by 27%—significant, but far from the supply-side dream that the cuts would "pay for themselves."

Seven years later, the data confirmed that the supply-side prediction was wrong. Real revenue from 2018 through 2024—excluding the anomalous 2022 pandemic spike—came in within 0.5% of CBO's 2018 projections {cite}`crfb2024tcja`. The tax cuts did not pay for themselves. The microsimulation models had been approximately right.

Doug Elmendorf, Glenn Hubbard, and Heidi Williams published a comprehensive assessment of dynamic scoring in the Brookings Papers on Economic Activity in 2024, concluding that the practice had improved budget analysis at the margins but hadn't resolved the fundamental uncertainty about macroeconomic feedback {cite}`elmendorf2024dynamic`. The models were better than guessing, but they weren't the precision instruments that advocates on either side wanted them to be.

---

## The UK Alternative

Across the Atlantic, a different model was emerging.

The IFS had shown that independent analysis was possible. But TAXBEN remained proprietary—academics and journalists could read IFS reports, but they couldn't run the model themselves.

The real breakthrough came from an unlikely source: the European Union.

In 1996, researchers led by Holly Sutherland began building EUROMOD—a tax-benefit microsimulation model that would eventually cover all EU member states {cite}`sutherland2013euromod`. The ambition was staggering: harmonize the wildly different tax and benefit systems of dozens of countries into a single analytical framework, enabling cross-national comparisons that had never before been possible.

EUROMOD was developed at the University of Essex, funded by European Commission research grants. And crucially, it was designed for broad access. Researchers could apply for access to the model, learn its methodology, and conduct their own analyses. The code wasn't fully open source, but the ethos was one of sharing rather than hoarding.

By 2021, EUROMOD had grown so successful that the European Commission took over its maintenance, transferring responsibility to the Joint Research Centre. The university-based project had become official EU infrastructure.

But Essex wasn't done. In 2018, with funding from the Nuffield Foundation, a team led by Mike Brewer spun off the UK component of EUROMOD into a new model: UKMOD {cite}`ukmod2020`. This time, they went further. UKMOD would be fully open source, freely available to anyone who wanted to use it.

"We wanted to democratize access to tax-benefit analysis," Brewer explained. The Scottish Parliament's research service started using UKMOD. So did NHS Health Scotland and the Welsh Government. For the first time, subnational governments in the UK had access to the same analytical tools as Westminster.

This openness enabled a new generation of independent analysts. Howard Reed had run TAXBEN at the IFS from 2000 to 2004, learning the craft of institutional model maintenance {cite}`northumbria2024reed`. After stints at IPPR as Chief Economist, he founded Landman Economics in 2008 and built his own Tax-Transfer Model. Reed used it to analyze Universal Basic Income, welfare reform, and the cumulative impact of austerity—producing the kind of detailed distributional analysis that had once been the exclusive domain of government and established think tanks. His goal, he said, was "a new settlement of the same scale and sustainability as the Beveridge-inspired reforms of 1945."

Malcolm Torry, directing the Citizen's Basic Income Trust, showed what civil society organizations could do with these tools {cite}`torry2019ubi`. Using EUROMOD, he conducted nearly a decade of research on basic income schemes, producing detailed analyses of costs, distributional effects, and implementation options. Torry's work demonstrated that advocacy groups could be rigorous analysts—if they had access to the right tools.

---

## The Open Source Emergence

The 2010s brought a new possibility: fully open-source tax microsimulation.

In France, the government itself released OpenFisca—source code for a tax-benefit calculator that anyone could use, modify, and extend {cite}`openfisca2024about`. OpenFisca's architecture was distinctive: it represented tax and benefit rules as code in a modular framework, where each provision was a separate function that could be tested, inspected, and updated independently. The framework would later be adopted by governments in New Zealand, Tunisia, and elsewhere—not just for analysis but as part of a broader "rules as code" movement that treated legislation as software.

In the United States, the open source push came from an unexpected source: a conservative think tank.

In 2013, Matt Jensen founded the Open Source Policy Center (OSPC) at the American Enterprise Institute {cite}`aei2015taxbrain`. The premise was counterintuitive—AEI was known for market-oriented policy advocacy, not software development. But Jensen argued that better public policy analysis required transparency, and transparency required open source. "A fundamental reason for adopting open source methods," OSPC stated, "is to let people from all backgrounds contribute to the models that our society uses to assess economic policy."

OSPC built Tax-Calculator and a web interface called TaxBrain, along with supporting tools: Tax-Data for processing IRS microdata, Behavioral-Response for modeling labor supply effects, OG-USA for overlapping-generations macroeconomic analysis. The next chapter tells that story in detail—how these tools proved that rigorous microsimulation could happen in the open.

The ideological irony was productive. A conservative think tank building open-source tools meant the project couldn't be dismissed as a left-wing effort to undermine official estimates. It was a genuine commitment to transparency that attracted contributors across the political spectrum.

These projects proved the concept—rigorous microsimulation could be done in the open. But they also revealed the challenges. Building the tools was one thing; making them usable by non-experts was another. The code was public, but who could read it? The models were open, but who could trust them? Open source had demonstrated what was possible; it hadn't yet delivered on the promise of democratized policy analysis.

---

## The Landscape Today

By the 2020s, tax microsimulation had stratified into distinct tiers—but the tiers were multiplying and the boundaries were blurring.

**Government models** remained the most authoritative for official purposes. JCT scores still determined what Congress believed policies would cost. Treasury estimates still informed Administration proposals. CBO projections still anchored long-term fiscal debates. These models had the best data—actual tax returns, confidential and comprehensive—and the institutional authority that came from decades of use.

**Established think tanks** operated the next tier—and the tier was growing. The Tax Policy Center {cite}`tpc2024model` had been joined by the Penn Wharton Budget Model, the Tax Foundation (which built its own microsimulation model emphasizing dynamic effects), the Institute on Taxation and Economic Policy (ITEP, whose model focused on state and local taxes and distributional analysis), and the Budget Lab at Yale. Each had a different methodological emphasis, different data sources, and—inevitably—different political valence. TPC and ITEP leaned left on distributional analysis. The Tax Foundation leaned right on growth effects. PWBM positioned itself as neutral. The plurality meant that any major tax proposal would face a barrage of competing estimates, each legitimate, each different.

**Open-source projects** represented the newest tier. Tax-Calculator, UKMOD, and PolicyEngine made it possible for anyone with technical skills to run tax simulations—and in PolicyEngine's case, anyone with a web browser. They couldn't match government models' data quality, but they offered something government models couldn't: transparency, accessibility, and the ability to be adapted for new purposes.

**Civil society users** like Malcolm Torry demonstrated that the tools could be used effectively by advocates and independent researchers—blurring the line between analyst and advocate, but expanding who could participate in policy debates.

The asymmetry that had characterized the field for decades was finally breaking down. Not completely—government still had the best data, the legal authority, and the institutional credibility. But the monopoly on analytical capability was ending. By 2025, a reasonably informed person could access half a dozen independent estimates of any major tax proposal within days of its introduction. That would have been unimaginable in 1990.

---

## What the Wars Revealed

The tax model wars weren't really about models. They were about power—specifically, the power to define what policies would cost and who they would affect.

When only government could run the numbers, policy debates were constrained by what government chose to analyze. When think tanks gained analytical capability, they could propose alternatives and critique official estimates. When open-source tools emerged, the barrier to entry dropped further.

Each expansion of capability shifted the terms of debate. IFS's independence from government gave it credibility to challenge official estimates. Tax-Calculator's open-source nature meant anyone could verify its methodology. UKMOD's free availability meant Scottish policymakers didn't have to rely on London for analysis.

But capability isn't enough. The best models in the world are useless if no one trusts them, understands them, or uses them appropriately. The next challenge wasn't building better models—it was making them genuinely useful for democratic deliberation.

That challenge would require going beyond tax microsimulation, beyond any single policy domain, to ask what it would mean to model society itself.

---

## References

```{bibliography}
:filter: docname in docnames
```

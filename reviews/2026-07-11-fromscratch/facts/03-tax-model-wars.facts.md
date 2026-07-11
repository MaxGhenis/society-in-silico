# Facts catalog — Chapter 2: The tax model wars

Source: `manuscript/part-1-closed-stack/02-tax-model-wars.md`

## Facts

- In 1983, a small London think tank (the Institute for Fiscal Studies) built a working model of the British tax and benefit system and turned it on the government's own budget.
- The Institute for Fiscal Studies was founded in 1969 by four financial professionals frustrated with the opacity of UK tax policy [@ifs2024history].
- TAXBEN is the IFS's microsimulation model of British taxes and benefits.
- Using TAXBEN, IFS could feed new budget rules in and simulate their effects on families up and down the income distribution within hours, publishing results before the official gloss set.
- IFS's annual Green Budget analyses became required reading for journalists, civil servants, and politicians.
- In 1974, Congress created the Congressional Budget Office to give itself analytical capacity independent of the executive branch.
- Alice Rivlin, an economist from Brookings, became CBO's first director; she wanted a nonpartisan, analytical office willing to publish numbers that discomfited both parties, and hired economists rather than political operatives [@rivlin1984economics].
- CBO built microsimulation models for health insurance, Social Security, and tax analysis; for long-run fiscal projections it built CBOLT, a long-term model of the whole federal budget [@cbo2018overview].
- The Joint Committee on Taxation was created in 1926 [@jct2024history].
- By the 1970s the JCT had developed a suite of microsimulation models: an individual income model, a corporate model, an estate and gift model, and an international cross-border model [@jct2024revenue].
- The budget process, built on the Congressional Budget Act of 1974 and later amendments, made JCT's numbers the official revenue estimates for tax bills.
- JCT scoring mechanics (data content): staff feed a proposal into the models, which apply the new rules to a representative sample of actual tax returns and, within days — sometimes hours — produce a score: the projected change in federal revenue over ten years. That number decides whether an amendment fits the budget resolution, survives reconciliation, or is fiscally viable at all; a score too high kills a proposal before a vote.
- Treasury's Office of Tax Analysis had experimented with computerized tax models since George Sadowsky's work in the early 1960s [@sadowsky1991computing]; by the 1980s it maintained the Individual Income Tax Model, refreshed regularly from IRS returns, producing the revenue estimates behind the Administration's proposals (as JCT's served Congress).
- The Urban Institute ran TRIM3, updated every year from the Current Population Survey to model benefit programs — SNAP, Medicaid, TANF, SSI, housing assistance — that the tax-focused models left out; it captured the interaction between taxes and transfers but served government clients rather than the public.
- The chapter states this was "the kind of work Karen Smith had been doing at Urban since the 1980s (chapter 1)." (Cross-reference: the provided Chapter 1 text does not mention Karen Smith.)
- Section 6103 of the Internal Revenue Code forbids disclosure of individual tax-return information, with a narrow set of exceptions; under Section 6103(l), JCT and Treasury have statutory access to the returns themselves. External researchers do not.
- The government's models run on the full universe of actual returns (every filer, every dollar, the true joint distribution of income, deductions, and credits); everyone outside works from public-use files that are sampled, anonymized, and top-coded — the highest incomes collapsed into a single category or swapped for an average, blurred exactly where the biggest tax fights are decided.
- At the National Bureau of Economic Research, Daniel Feenberg began building TAXSIM in the early 1980s [@feenberg1993taxsim]; by the 1990s it was reachable over the internet, one of the first tax calculators anyone could run remotely; Feenberg maintained it for the rest of his career.
- TAXSIM calculated taxes for individual records; it did not produce the aggregate revenue estimates and distributional tables that drove policy fights.
- In 2002, Gene Steuerle and Len Burman founded the Tax Policy Center as a joint venture of the Urban Institute and the Brookings Institution [@tpc2024model]. Steuerle had helped build the official models at Treasury; Burman at CBO and Treasury.
- TPC built its microsimulation on the same IRS public-use files available to everyone outside government (less granular than the confidential returns), enough to estimate revenue and distributional effects within days.
- In 2012, when Mitt Romney campaigned on a tax plan promising to cut rates while staying revenue-neutral through unspecified base-broadening, TPC showed the promise was mathematically impossible: the numbers could not balance without raising taxes on the middle class or losing revenue [@tpc2012romney]. Romney's team could dispute but not rebut it with numbers.
- During the 2017 Tax Cuts and Jobs Act debate, TPC showed how heavily the bill's benefits tilted toward high-income households.
- Kent Smetters launched the Penn Wharton Budget Model at the University of Pennsylvania in 2016; it distinguished itself by producing dynamic estimates — scores that let a tax change move the size of the economy rather than holding it fixed [@pwbm2017tcja].
- The Budget Lab at Yale followed later with another lens.
- In little more than a decade, the number of independent shops able to score a major tax proposal went from essentially zero to half a dozen.
- Political leanings (data content): the Tax Policy Center and the Institute on Taxation and Economic Policy leaned left on distributional questions; the Tax Foundation leaned right on growth effects; Penn Wharton positioned itself in the middle.
- Traditionally, JCT scored a tax cut statically — a $100 billion cut costs $100 billion, with the size of the economy held fixed. Supply-siders argued this overstated the true cost; under dynamic scoring, the same cut might book at $70 billion.
- Alan Auerbach and William Gale worked through dynamic scoring in forums and papers across the 2000s; in 2005 Auerbach laid out the issues formally: dynamic scoring was conceptually correct but practically treacherous because the macroeconomic models needed to estimate the feedback were themselves deeply uncertain [@auerbach2005dynamic].
- In January 2015, the new Republican House majority required JCT to produce dynamic scores for legislation with budgetary effects above a quarter of a percent of GDP [@crs2015dynamic].
- TCJA scores (data content): JCT's static score put the ten-year cost at $1.46 trillion; its dynamic score came in at $1.07 trillion, reflecting roughly $385 billion of revenue recovered through faster growth — a ~27 percent reduction in cost [NEEDS CITATION: JCT TCJA static and dynamic scores].
- Penn Wharton, running the feedback through its own model, put the TCJA dynamic cost higher, in the range of $1.8 to $2.2 trillion, judging the growth effects modest [@pwbm2017tcja].
- The 2017 law's individual provisions did not expire on the schedule it set; the One Big Beautiful Bill Act extended them in 2025 [@obbba2025].
- Douglas Elmendorf, Glenn Hubbard, and Heidi Williams later assessed the dynamic-scoring experiment: it had improved budget analysis at the margins without resolving the fundamental uncertainty about macroeconomic feedback [@elmendorf2024dynamic].
- From 1993, Ann Harding built a microsimulation program at the National Centre for Social and Economic Modelling (NATSEM) in Canberra; her edited volume *Microsimulation and Public Policy* (1996) served for years as the field's standard reference [@harding1996microsimulation].
- NATSEM's models were used across Australian government agencies, parliamentary committees, and media, on issues from tax reform to childcare policy.
- From 1996, a team led by Holly Sutherland set out to build EUROMOD, a single tax-benefit model that would eventually span every EU member state, harmonizing national systems so reforms in different countries could be compared on the same terms [@sutherland2013euromod].
- EUROMOD was developed at the University of Essex on European Commission research grants; researchers could apply to use it; the code was not fully open but the ethos was sharing; the European Commission eventually took over its maintenance through its Joint Research Centre.
- With funding from the Nuffield Foundation, a project led by economist Mike Brewer turned EUROMOD's UK component into a standalone model, UKMOD, housed at Essex's Centre for Microsimulation and Policy Analysis under Matteo Richiardi, introduced in a 2021 paper by Richiardi, Diego Collado, and Daria Popova [@ukmod2020].
- UKMOD's first free public release, in October 2019, made it the UK's first freely available tax-benefit model, fully open and usable by anyone.
- UKMOD users included the Scottish Parliament's research service, NHS Health Scotland, and the Welsh Government.
- Howard Reed ran TAXBEN inside the IFS from 2000 to 2004 [@northumbria2024reed]; after a spell as chief economist at IPPR, he founded Landman Economics in 2008 and built his own tax-transfer model, using it to analyze basic income, welfare reform, and the cumulative toll of austerity.
- Malcolm Torry, directing the Citizen's Basic Income Trust, used EUROMOD across nearly a decade of research to cost basic-income schemes in granular detail [@torry2019ubi].
- In January 2011, Camille Landais, Thomas Piketty, and Emmanuel Saez published *Pour une révolution fiscale* ("For a Tax Revolution"), arguing for restructuring French income tax into a single progressive levy [@landais2011revolution].
- The companion website revolution-fiscale.fr let any French citizen design a tax reform and watch its budgetary and distributional consequences resolve on screen; it drew hundreds of thousands of visitors [@landais2011revolution].
- France gave its parliament no analytical shop of its own (unlike the US, with its independent CBO); evaluating a proposed amendment meant going through the Finance Ministry.
- Four months after the book, a small team inside the French government released OpenFisca — not a simulator but the source code beneath one. It came out of the Centre d'analyse stratégique (later renamed France Stratégie) and was written by Mahdi Ben Jelloul and Clément Schaff, on the premise that tax and benefit rules should exist as executable code, not only legal prose [@openfisca2024about].
- The rules-as-code idea went by several names: rules as code, legislation as code, machine-consumable rules.
- In 2018, New Zealand's Service Innovation Lab spent three weeks translating a piece of legislation into Python and human-readable rules at once, showing a law could be drafted in both forms simultaneously [@nz2018betterrules].
- The OECD published *Cracking the Code* in 2020, a primer for governments on the rules-as-code approach [@oecd2020cracking].
- OpenFisca spread across four continents — powering France's Mes Aides benefits calculator, a New Zealand rates rebate, and adaptations in Tunisia, Senegal, and beyond — and collected an OECD Innovation of the Year nod and recognition from the European Commission as its most innovative open-source software [@openfisca2024about].
- In 2013, Matt Jensen founded the Open Source Policy Center at the American Enterprise Institute, a market-oriented think tank [@aei2015taxbrain]. He recruited Martin Holmer, an MIT-trained economist, to write Tax-Calculator, an open-source model of US federal income and payroll taxes [@holmer2024profile].
- At the 2016 Open Government Partnership summit in Paris, a team of French and Tunisian volunteers modeled Senegal's income tax in under thirty-six hours and won the hackathon [@openfisca2024about].
- By 2019, France's National Assembly had built LexImpact on top of OpenFisca, letting legislators simulate the effects of proposed amendments; within two years the tool had informed well over a hundred simulations in parliamentary debate.
- Tax-Calculator grew into the Policy Simulation Library, a loose confederation of independent open-source models sharing transparency and interoperability standards while each specialized — overlapping-generations macro models for dynamic scoring, a capital-cost-recovery model from the Tax Foundation, computational-economics tools from QuantEcon — with contributors from CBO to the City of New York.
- The Federal Reserve released a Python implementation of FRB/US, its several-hundred-equation macroeconomic model, in 2022 [@frbus2024].
- PolicyEngine is named as the tool that would eventually put the open approach in front of anyone with a web browser.

## Story beats

- **IFS founding → TAXBEN → 1983.** Four financial professionals found the IFS in 1969 over UK tax-policy opacity; they build TAXBEN; in 1983 they turn it on the government's budget, publishing family-level effects within hours (Green Budget) before officials can set the narrative.
- **The Rivlin lineage (continued from Ch 1).** 1974: Congress creates the CBO to escape dependence on executive-branch numbers; Rivlin, from Brookings, becomes first director, hires economists over operatives, and builds a culture of methodological transparency that outlasts her by five decades.
- **The JCT scoring scene (mechanics up close).** A senator drafts a tax amendment → JCT staff feed it into the models → within days/hours a ten-year revenue score emerges → that single number decides the amendment's fate, with no hearing or floor debate; on a reconciliation bill the score often *is* the decision.
- **The dynamic-scoring fight.** Static vs. dynamic scoring ("$100B cut costs $100B" vs. "might book at $70B"); supply-side argument that static scoring overstates cost; Auerbach's 2005 formal treatment (correct but treacherous); the January 2015 House rule mandating dynamic scores above 0.25% of GDP; the TCJA as first real test; models disagree on magnitude, none find a free lunch.
- **Romney 2012.** TPC runs the arithmetic on the revenue-neutral rate-cut promise and shows it mathematically impossible; the finding reshapes the campaign debate; Romney's team, lacking a comparable model, can dispute but not rebut.
- **The French break.** Landais/Piketty/Saez publish the book (Jan 2011); the revolution-fiscale.fr site lets ordinary citizens design reforms and see consequences, breaking the Finance Ministry's monopoly with code rather than institutional authority.
- **OpenFisca release.** Ben Jelloul and Schaff, inside the French government's strategy unit, open the *machinery* (source code), not just the *results*.
- **Senegal hackathon.** 2016 Paris OGP summit: French and Tunisian volunteers model Senegal's income tax in under 36 hours and win.
- **AEI / Jensen / Holmer.** A conservative think tank (2013) builds open tools; the irony (a market-oriented institution building open-source estimation) makes the project harder to dismiss as partisan and draws cross-spectrum contributors.

## Quotes

- Mike Brewer (on UKMOD): "We wanted to democratize access to tax-benefit analysis" [NEEDS CITATION: Brewer quote].
- Howard Reed (stated ambition): "a new settlement of the same scale and sustainability as the Beveridge-inspired reforms of 1945" [NEEDS CITATION: Reed quote].

(These are the only two verbatim external quotations in the chapter.)

## Arguments

1. Microsimulation gave outside bodies (IFS first, then TPC and others) the power to contest official numbers with calculations of their own — beginning to crack the information asymmetry that favored those in power.
2. But the tax model wars were never really about models; they were about the power to define what a policy costs and whom it helps, and that power rested on the data.
3. Section 6103 gives JCT and Treasury statutory access to the full universe of real returns, while everyone outside works from public-use files that are sampled, anonymized, and top-coded — blurred precisely at the top of the distribution where the biggest tax fights are decided.
4. The confidentiality is justified, but its byproduct is an analytical moat no open-source software can drain: you can publish your code, methods, and assumptions and still not have the data.
5. The secrecy had concrete costs: disliked estimates could be dismissed as biased with no external check; wrong estimates couldn't be reconstructed from outside; debate narrowed to what the scorekeepers were willing to model (proposals that didn't fit became politically impossible); expertise pooled inside a few institutions; citizens had to take official numbers on faith.
6. The open-source counter-movement (TAXSIM → TPC → Penn Wharton → OpenFisca → Tax-Calculator → PolicyEngine) broke the monopoly on analytical *capability* — but every gain was a gain in *method*, not in data; the moat stayed dry and impassable.
7. Rules-as-code has a second limit hiding inside the first: encoding the rules yields an engine that can compute any individual scenario, but producing an aggregate revenue estimate or distributional table requires something the engine doesn't contain — a representative population — which runs straight back into Section 6103.
8. The only answer the constraint permits: build a synthetic population from the public files you are allowed to use, calibrate it against the administrative totals the government does publish (using the government's own published numbers as the answer key), then run the open rules over it — reconstructing statistically what stands behind the moat without exposing any real return. Whether the reconstruction can be made faithful enough is the problem the rest of the book must solve.

## Author-texture (verbatim, may be reused)

Chapter 2 is expository/institutional; texture is thesis-bearing epigram rather than personal scene. Selectively preserved:

- "You can publish your code, your methods, and your assumptions, and you still will not have the data."
- "The engine was open. The last mile—to something an ordinary person could use, and rely on—was not yet built."
- "You do not breach the moat. You reconstruct, statistically, what stands behind it."
- "because you cannot open-source a dataset you are legally forbidden to hold."
- "Independence of analysis, it turned out, could follow from a freely downloadable model as surely as from a new institution."

## Structural notes

- **Chapter's job in the book.** Second in Part I. Builds out the "closed stack": the federal modeling apparatus (CBO, JCT, Treasury, plus Urban's TRIM3) and, crucially, the Section 6103 data moat — the book's central, durable constraint. Then traces the decades-long open-source counter-movement and shows it advanced method but never touched the data advantage. Ends by naming the synthesize-and-calibrate strategy the rest of the book pursues.
- **Cross-references.** Back to Chapter 1 (Rivlin → CBO lineage; Sadowsky's Treasury work; the disputed "Karen Smith … (chapter 1)" reference not actually present in Ch 1). Forward: the TCJA static/dynamic numbers recur in Chapter 3; PolicyEngine and the synthetic-population construction are set up as "the next layer of this story"; the moat/calibration framing recurs throughout.
- **Protected lines.** None explicitly listed in the task for this chapter, but the moat thesis is load-bearing: "you cannot open-source a dataset you are legally forbidden to hold" and "You do not breach the moat. You reconstruct, statistically, what stands behind it."
- **Handoff.** Ends on the synthesize-and-calibrate answer ("fit an artificial population … then run the open rules over the population you built") — hands off to Chapter 3's accuracy question (are the numbers any good?) and, downstream, to the synthetic-population build.

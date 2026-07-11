# Adversarial review of the fact base

**Review date:** 11 July 2026  
**Materials attacked:** `rewrite-facts.md`, the 19 chapter fact catalogs, and `from-scratch-outline.md`  
**Standard:** what a hostile subject-matter expert, benchmark author, budget scorer, or historian could sustain from primary evidence—not what the manuscript would like to be true.

## Executive finding

The current fact base is not safe to draft from. Its central case may survive, but several of its best-sounding proofs do not. It repeatedly:

- upgrades a sample into a census, a comparator into ground truth, target fit into external validation, and a conditional projection into an observable causal forecast;
- compares budget estimates that measure different objects, then calls the spread model error;
- describes benchmark tasks as much harder than their papers say they were, while freezing live leaderboard results at already-stale values;
- claims firsts over UKMOD, EUROMOD, SOUTHMOD, and Statistics Canada's SPSD/M that those projects' own histories refute;
- treats facts reported by the author's own projects as if they had independent replication; and
- contradicts the rewrite's explicit prohibitions on the CTC rescore, retired names, launch status, and corrected HiveSight/GSS numbers.

`rewrite-facts.md` should be treated as an editorial constraint sheet, not an evidentiary authority. It is itself wrong on at least the PolicyBench snapshot/metric, the CTC effective year, and the implication that the listed Enhanced CPS source set and performance figure are settled. Where it conflicts with enacted law or a dated primary source, the primary source must win and the constraint sheet must be amended.

Verdicts below use four labels:

- **WRONG:** contradicted by the primary source or by elementary identification logic.
- **OVERSTATED:** a narrower claim is supported, but the proposed wording outruns it.
- **MIXED:** some numbers are real, but the comparison, date, denominator, or interpretation is not.
- **SUPPORTED WITH QUALIFICATION:** retain only with the stated scope and date.

---

## 1. FACTUAL ATTACK: the first 15 claims a hostile expert will check

### 1. “It took eighteen years after Orcutt's 1957 paper to produce a working microsimulation”

**Verdict: OVERSTATED; it conflates the first working realization with the later DYNASIM project.**

The catalog tells two incompatible histories. It acknowledges a 1961 empirical model, then turns the 1975 completion of DYNASIM into the first “working” realization (`02-birth-of-microsimulation.facts.md:31-44,98`). A historian will object immediately. The 1957 paper was the manifesto; Orcutt and collaborators published a concrete microsimulation in 1961; DYNASIM was the later, much more ambitious longitudinal system developed at Urban.

**What the primary record says.** The National Academies' history dates the Urban effort to the late 1960s, with the first DYNASIM version completed in 1975, written in MASH/FORTRAN for a DEC System-10 and simulating roughly 10,000 people. Other histories date the project start to 1969 and the major publication to 1976. That supports “about six years for DYNASIM” and “eighteen years from manifesto to DYNASIM,” not “eighteen years to any working microsimulation.” See the [National Academies history](https://www.nationalacademies.org/read/1835/chapter/12) and the [International Journal of Microsimulation history](https://www.microsimulation.pub/articles/00280).

**Required rewrite.** Use three dated milestones: conceptual proposal (1957), first empirical realization (1961), and first large-scale DYNASIM version (1975). Do not state the exact 1968 hire date or a six-year build unless a personnel/project record is cited.

### 2. “No one had opened the UK tax-benefit system before openfisca-uk”

**Verdict: WRONG unless reduced to a tightly dated and technically specific claim.**

`05-a-wall-of-frustration.facts.md:45-47` says there was no open UK tax-benefit model, while `03-tax-model-wars.facts.md:46` and `06-proof-of-concept.facts.md:13` call UKMOD the first freely available UK model in 2019. The book also alternates among “open,” “open source,” “free to researchers,” and “publicly inspectable” as if they were synonyms. They are not.

**What the primary record says.** UKMOD originated from the UK component of EUROMOD and was first released in 2019; its authors call it freely accessible, open source, and documented. The launch account also says the UK component of EUROMOD had already been downloadable and modifiable by researchers. EUROMOD's software became open source in December 2020, while access to underlying microdata remained restricted. See the [UKMOD paper](https://microsimulation.pub/articles/00231), [2019 UKMOD announcement](https://www.iser.essex.ac.uk/blog/2019/08/05/ukmod-a-new-free-to-use-tax-and-benefit-microsimulation-model-for-the-uk), and [EUROMOD history](https://euromod-web.jrc.ec.europa.eu/overview/what-is-euromod).

**Required rewrite.** Date the openfisca-uk work and name its actual delta: a particular engine, licensing regime, API, contribution model, or policy-year surface. Drop the priority claim unless it survives a documented comparison with EUROMOD's UK component and UKMOD.

### 3. “JCT and Treasury run their models on the full universe of every actual tax return”

**Verdict: WRONG.**

This is repeated as a key explanation of the public/private modeling divide (`03-tax-model-wars.facts.md:23,88`; `12-microsimulation-anywhere.facts.md:38`), even though the same catalog correctly calls the production input a representative sample (`03-tax-model-wars.facts.md:18`). Confidential access is a real advantage. “Every filer, every dollar, the true joint distribution” is not.

**What the primary record says.** JCT describes large, carefully edited micro-level **samples** of tax returns supplied by IRS Statistics of Income, supplemented by surveys, administrative aggregates, and other sources. The model weights and calibrates those records; it does not simply calculate over the complete return universe. The relevant disclosure authorities are also more specific than “Section 6103”: JCT access is principally under §6103(f), while Treasury access is under §6103(h), not §6103(l). See JCT's [Revenue Estimating Process](https://www.jct.gov/getattachment/29cf59ce-31ca-450b-adea-3848d0d33350/Revenue-Estimating-Process-January-2025.pdf), IRS SOI's [individual-return report](https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-returns-complete-report-publication-1304), and [26 U.S.C. §6103](https://www.law.cornell.edu/uscode/text/26/6103).

**Required rewrite.** Say “confidential, statistically selected and edited return microdata with detail unavailable in public-use files.” Delete “full universe,” “every return,” and “true joint distribution.”

### 4. “Static scoring means no behavioral response”

**Verdict: WRONG as a description of JCT/CBO conventional scoring.**

The catalogs repeatedly equate static or conventional estimates with mechanically applying new law while nobody changes behavior (`03-tax-model-wars.facts.md:34,37`; `04-the-accuracy-question.facts.md:46-47`; `07-the-household-and-the-society.facts.md:83`). This collapses three different distinctions: fixed population versus dynamically aged population, fixed aggregate economy versus macro feedback, and behavioral versus no-behavior calculation.

**What the primary record says.** JCT conventional estimates generally hold aggregate GNP fixed, but incorporate many behavioral responses: timing, organizational form, portfolio composition, avoidance, consumption, labor supply, and indirect tax effects. A separate macroeconomic analysis allows the proposal to change aggregate output. See JCT's [Revenue Estimating Process](https://www.jct.gov/getattachment/29cf59ce-31ca-450b-adea-3848d0d33350/Revenue-Estimating-Process-January-2025.pdf).

**Required rewrite.** Reserve “mechanical/no-behavior” for a calculation that truly freezes behavior. Define JCT's conventional score as fixed-macro but behavior-aware, and “dynamic scoring” as adding macroeconomic feedback. Do not use the microsimulation term “dynamic” without saying which sense is intended.

### 5. “TCJA scorekeepers differed by a factor of five, and realized receipts show who was right”

**Verdict: WRONG COMPARISON and OVERSTATED RETROSPECTIVE.**

The catalog juxtaposes JCT's $1.456 trillion conventional revenue loss, Penn Wharton's $1.8–$2.2 trillion, and Tax Foundation's $448 billion dynamic loss (`04-the-accuracy-question.facts.md:7-9,45-47`). It then treats subsequent receipts—sometimes excluding 2022—as a natural experiment capable of adjudicating supply-side assumptions.

**What the primary record says.** JCT estimated a roughly $1.456 trillion conventional ten-year budget loss and about $384 billion of macro feedback, for a net loss near $1.071 trillion. Penn Wharton's $1.9–$2.2 trillion figure is an increase in **debt**, while its revenue reduction after growth was about $1.5–$1.7 trillion. Tax Foundation reported roughly $1.47 trillion static and $448 billion dynamic revenue losses. The “factor of five” therefore mixes static revenue, dynamic revenue, and debt. See [JCT's conventional estimate](https://www.jct.gov/publications/2017/jcx-67-17/), [JCT's macro analysis](https://www.jct.gov/publications/2017/jcx-69-17/), [Penn Wharton's analysis](https://budgetmodel.wharton.upenn.edu/legacy-briefs/2017-12-18-the-tax-cuts-and-jobs-act-reported-by-conference-committee-121517-preliminary-static-and-dynamic-effects-on-the-budget-and-the-economy/), and [Tax Foundation's analysis](https://taxfoundation.org/research/all/federal/final-tax-cuts-and-jobs-act-details-analysis/).

CBO's retrospective says 2018–2024 receipts exceeded its April 2018 nominal projection by about $1.5 trillion, but identifies inflation, real activity, tariffs, subsequent law, and the pandemic as major contributors and explicitly warns that isolating TCJA is difficult. Gross receipts are not the unobserved no-TCJA counterfactual. See [CBO's retrospective](https://www.cbo.gov/publication/60987).

**Required rewrite.** Put all estimates on the same fiscal concept, window, baseline, and feedback convention before comparing them. Present the receipts exercise as a forecast-error decomposition with enormous confounding—not as a clean causal verdict—and do not discard a single anomalous year merely because it spoils the result.

### 6. “CBO got the ACA uninsured rate within one point because exchange and Medicaid errors canceled”

**Verdict: MIXED and post hoc.**

The catalog reconstructs an adjusted 9.4 percent prediction against a 10.4 percent outcome, then calls the result luck because marketplace and Medicaid errors canceled (`04-the-accuracy-question.facts.md:16-24,61`). The hostile check is whether that 9.4 percent was an actual ex ante CBO forecast, with the same population, year, enrollment concept, and legal baseline. It was not.

**What the primary record says.** CBO's own 2017 retrospective reports that its March 2010 projection for 2016 was 21 million uninsured, or 8 percent; the observed figure was 28 million, or 10 percent. After the Supreme Court made Medicaid expansion optional, CBO's May 2013 projection was 31 million, or 11 percent. Marketplace enrollment, Medicaid expansion, population definitions, average versus end-of-year enrollment, and later legal changes all moved. See [CBO's retrospective](https://www.cbo.gov/publication/53094), its [underlying report](https://www.cbo.gov/system/files/115th-congress-2017-2018/reports/53094-acaprojections.pdf), and the [March 2010 estimate](https://www.cbo.gov/publication/21279).

**Required rewrite.** Reproduce the dated primary tables and compare like with like. If the manuscript wants to discuss offsetting component errors, call it a retrospective decomposition, not the original headline forecast and not proof that aggregate accuracy was “luck.”

### 7. “The tax benchmarks gave models the full law, complete returns, and unlimited thought”

**Verdict: HEADLINE SCORES SUPPORTED; TASK DESCRIPTIONS WRONG.**

This is the opening evidentiary spine (`01-introduction.facts.md:18-24,57,87`; `09-the-ai-cant-do-your-taxes.facts.md:14-15`). Two separate studies are inflated:

1. The GPT-4 study's 186/276 result is about 67 percent, but the supplied legal corpus was SARA's roughly 16-page simplified statute—not the full Internal Revenue Code.
2. TaxCalcBench's best original score was 32.35 percent under strict scoring, but the benchmark contained 51 hand-built, entirely synthetic, fairly simple federal tax-year-2024 cases. It evaluated selected Form 1040 line outputs, supplied necessary taxpayer facts and some line guidance, used five bounded reasoning settings, and ran each configuration four times. It did not hand models the full tax law or unlimited time.

See the [GPT-4/SARA paper](https://arxiv.org/abs/2309.09992), the [paper text](https://par.nsf.gov/servlets/purl/10529300), and [TaxCalcBench](https://arxiv.org/abs/2507.16126).

The introduction also reverses its own result: “fewer than one in three correct” means more than two thirds wrong, not “wrong a third of the time” (`01-introduction.facts.md:57`).

**Required rewrite.** Preserve the original dated scores, but describe the benchmark surfaces exactly. The honest conclusion is stronger: models failed even on a small, synthetic, bounded federal task. Do not pretend the task was a complete real-world filing.

### 8. “PolicyBench's best model misses roughly one in six households; most miss a quarter or more”

**Verdict: OUTDATED and METRICALLY MISLABELED as of the review date.**

This claim appears throughout the outline, constraint sheet, and catalogs (`rewrite-facts.md:227-234`; `01-introduction.facts.md:25-27`; `09-the-ai-cant-do-your-taxes.facts.md:17-20`; `18-society-in-silico.facts.md:26`). The live page on 10 July 2026 listed 24 models and a top exact score of 88.7 percent—about one miss in nine weighted scored outputs, not one in six. Only 9 of 24 models were below 75 percent, so “most” was also false on that snapshot.

**What the primary record says.** The [live PolicyBench board](https://policybench.org/) ranks models over 100 public household scenarios and 18 weighted output groups. “Exact” is a household-output-row metric, not clearly “the share of complete households for which every tax and benefit output is within one dollar.” The board's secondary near-match measure also has a special tolerance around zero. The public, fixed 100-case set creates an obvious future contamination/overfitting problem; the site itself warns that protected claims need rotating held-out cases. The older [frozen PolicyBench paper](https://www.policybench.org/paper/policybench.pdf) reports a different model set and must not be silently blended with the live board.

**Required rewrite.** Archive a dated board snapshot and name the metric/denominator exactly, or use only a durable qualitative statement. Never convert weighted output accuracy into “fraction of households fully correct.” Treat any current leaderboard value as volatile, not ground truth.

### 9. “Enhanced CPS fused CPS, SCF, CEX, RECS, and ATUS, matched 9,168 targets, and cut deviation 97 percent”

**Verdict: DATASET LIST WRONG; TARGET COUNT HISTORICAL; PERFORMANCE CLAIM UNSOURCED/IN-SAMPLE.**

`08-three-ingredients.facts.md:66` names five inputs, four of which do not match the launch source. `06-proof-of-concept.facts.md:80` and `07-the-household-and-the-society.facts.md:76` repeat 9,168 targets and a 97 percent reduction, while the current methodology reports a different target count. The bibliography key points to a 2022 item for an August 2025 release.

**What the primary record says.** PolicyEngine's [August 2025 launch post](https://www.policyengine.org/us/research/enhanced-cps-launch) names CPS ASEC, IRS Public Use File, SIPP, SCF, and ACS. It supports 9,168 calibration targets and the use of quantile-regression forests plus gradient reweighting. It does not support the catalog's CPS/SCF/CEX/RECS/ATUS list or, on that page, the asserted 8.3-to-0.2 percent result. Current [policyengine-us-data documentation](https://policyengine.github.io/policyengine-us-data/) describes 2,813 targets and openly notes the nine-year PUF/CPS mismatch and the limitations of imputation and marginal calibration.

Even if 8.3-to-0.2 can be recovered from a run artifact, fit to the targets used by the optimizer is not independent validation. It says nothing by itself about held-out aggregates, joint distributions, tails, or fiscal scores.

**Required rewrite.** Correct the source list; label 9,168 as the August 2025 release configuration; cite the run that produces 8.3 and 0.2, including its loss function and weighting; and add held-out validation. Reconcile the claim with the catalogs' simultaneous admission that revenue remains roughly one-third low.

### 10. “HM Treasury's March 2025 evaluation found PolicyEngine good enough for use”

**Verdict: DATE WRONG and STATUS OVERSTATED.**

The attractive fact—almost 60 percent of National Insurance data points within 0.5 percent—is real but narrow (`06-proof-of-concept.facts.md:69-70,92-96`). The chapter strips away the official caveats and turns a beta investigation into adoption.

**What the primary record says.** HM Treasury's [Algorithmic Transparency Record](https://www.gov.uk/algorithmic-transparency-records/hmt-modelling-policy-engine) was published on 17 December 2024, not in March 2025. It says HMT **does not currently use PolicyEngine**. It describes a beta/pilot, says the NI comparison was promising, says the income-tax comparison was less promising because of mapping difficulties, and says further evaluation was pending. It did not directly validate PolicyEngine's random-forest component.

**Required rewrite.** Call it an external exploratory comparison, state non-use, retain the negative income-tax result, and distinguish an algorithmic transparency filing from formal production acceptance.

### 11. “Five African countries acquired public, inspectable models in one week; none had one before”

**Verdict: WRONG.**

The same catalog disproves its claim: it says the new encodings were checked against GHAMOD, UGAMOD, MicroZAMOD, ETMOD, and RWAMOD (`12-microsimulation-anywhere.facts.md:9,13-19`). Those comparators were existing national models. Calling the reimplementation the countries' first public models erases the teams whose work made the comparison possible.

**What the primary record says.** UNU-WIDER initiated SOUTHMOD around 2014–2015 with EUROMOD, SASPRI/LSE, and national partners. It maintains a mature family of models, with most model code and input data available free for non-commercial research. Ghana's GHAMOD and the other named systems existed before the RuleSpec exercise. The June 2026 bundle and tenth-anniversary materials describe ongoing maintenance, broader country coverage, and policy years through 2025. See [SOUTHMOD phase 3](https://www.wider.unu.edu/project/southmod-simulating-tax-and-benefit-policies-development-phase-3), [access terms](https://www.wider.unu.edu/about/accessing-southmod-models), and [SOUTHMOD at 10](https://www.wider.unu.edu/publication/southmod-10).

**Required rewrite.** Claim the genuine contribution: a rapid **independent RuleSpec reimplementation**, source grounding, per-record comparison, and upstream issue discovery. Document what “one week” includes—agent time, human preparation, pre-existing adapters, policy scope, tests, and review. Do not claim the entire national tax-benefit system or the first model without a coverage matrix.

### 12. “Oracle parity establishes the one right answer, hides nothing, and makes silent staleness impossible”

**Verdict: OVERSTATED and presently SELF-ATTESTED.**

The reported comparisons are useful engineering evidence: 78,479 Belgian workers within €0.03, small UK suites, and dispositioned SOUTHMOD mismatches. They do not establish legal truth over the full policy surface. The evidence is largely generated by the organization being profiled, with no independent replication package cited.

**What the evidence can support.** Agreement between independent implementations over named cases, outputs, years, input conventions, and tolerances is conformance evidence. It can reveal bugs in either implementation. It cannot exclude shared source errors, correlated interpretation errors, missing eligibility pathways, untested boundary cases, wrong input mapping, stochastic take-up differences, or an omitted change in law. The catalogs themselves admit oracle bugs (`11-the-verification-problem.facts.md:43-47`) and uncovered new rules (`:52-53`).

The phrase “per-unit hides nothing” is also false. A representative population does not contain every rare legal state or threshold boundary. “100 percent explained” is a disposition rate among observed mismatches, not 100 percent correctness or 100 percent coverage. Eight raw matches out of nineteen Universal Credit cases remains eight raw matches; explaining the rest is valuable but is a different metric.

**Required rewrite.** Publish case manifests, hashes, source versions, inputs, raw outputs, tolerances, dispositions, coverage denominators, and an independent rerun. Use “no unexplained mismatches on the tested surface.” A ratchet prevents regressions on tests already present; it does not discover new law and cannot make staleness impossible.

### 13. “Every microsimulation counterfactual can become a forecast that reality will later grade”

**Verdict: WRONG as a matter of causal identification.**

This is not a missing caveat; it breaks the architecture of the proposed Thesis ledger (`13-the-decomposition.facts.md:23-33`; `14-the-uncertainty-gap.facts.md:77-79`; `16-simulating-democracy.facts.md:49`). If a reform is enacted, the no-reform world is unobserved. If it is not enacted, the reform world is unobserved. An official future outturn can resolve an observable—unemployment, caseload, revenue—not the causal difference between mutually exclusive worlds.

The catalogs already state the correct point elsewhere: a never-enacted counterfactual cannot be checked against reality (`04-the-accuracy-question.facts.md:85`). A conditional forecast resolves only when its condition occurs, and even then only its realized arm. Policy impact requires a causal design—randomization, a credible comparison group, discontinuity, synthetic control, or a structural model whose assumptions remain contestable.

**What primary methodology says.** The JRC's [microeconomic policy-evaluation program](https://knowledge4policy.ec.europa.eu/microeconomic-evaluation/jrc-technical-reports_en) treats ex post causal evaluation as a separate identification problem, not a lookup of the first official print.

**Required rewrite.** The ledger must label four different objects: directly resolvable forecasts; conditionally resolvable forecasts; descriptive nowcasts; and causal/counterfactual estimates that require an identification design and may never receive a definitive score. Do not promise that every policy score resolves.

### 14. “The OBBBA facts and the $23 billion CTC score are publication-ready”

**Verdict: MIXED. The law summary needs corrections; the CTC score is expressly prohibited and unverified.**

Four separate points have been collapsed:

- **CTC effective year:** Public Law 119-21 applies the $2,200 maximum to tax years beginning after 31 December 2024—tax year 2025, not “from 2026.” The amount is indexed after 2025; the refundable cap is $1,700 for 2026. See the [enrolled law](https://www.govinfo.gov/content/pkg/PLAW-119publ21/pdf/PLAW-119publ21.pdf) and [IRS family guidance](https://www.irs.gov/newsroom/tax-benefits-for-parents-and-families).
- **SNAP benefit cost sharing:** The 0/5/10/15 percent tiers for state error rates below 6, 6–8, 8–10, and at least 10 percent are real, and USDA reports a FY2025 national rate of 10.62 percent. But each state's rate—not the national average—determines its share; states can choose specified measurement years, and some high-error states receive delayed implementation. “All begin in FY2028” is too simple. See USDA's [payment-error-rate page](https://www.fna.usda.gov/snap/qc/per) and the enacted law.
- **SNAP administrative costs:** the federal share falls from 50 to 25 percent, equivalently raising the ordinary state share from 50 to 75 percent, for FY2027. State implementation details still matter. See USDA's [24 June 2026 rule notice](https://www.fna.usda.gov/snap/fr-062426).
- **Medicaid community engagement:** CMS's June 2026 interim final rule says states generally must implement by 1 January 2027 and specifies an 80-hours-per-month framework. “Systems due December 31” is an imprecise paraphrase. See the [CMS fact sheet](https://www.cms.gov/newsroom/fact-sheets/medicaid-community-engagement-requirement-certain-individuals-interim-final-rule-comment-period-cms).

Most importantly, `rewrite-facts.md:318-325` requires the literal placeholder `[[CTC-RESCORE]]` because earlier estimates conflicted. Yet `07-the-household-and-the-society.facts.md:86-88` and `14-the-uncertainty-gap.facts.md:85-88` silently assert about $23 billion, a 2.6-point child-poverty reduction, and 1.9 million children. That is an author-run model output, not an independently verified fact, and it violates the controlling prohibition.

**Required rewrite.** Restore `[[CTC-RESCORE]]`. Publish the reform file, model/data versions, population and poverty definitions, weights, year, baseline law, and sensitivity checks before promoting any replacement number.

### 15. “HiveSight and GSS supply settled benchmark evidence for simulated opinion and values”

**Verdict: INTERNALLY CONTRADICTORY and NOT YET INDEPENDENTLY SUBSTANTIATED.**

The outline says HiveSight persona MAE was 36.6 points and cells achieved 6.2-point subgroup MAE (`from-scratch-outline.md:30-34`). The constraint sheet and chapter catalog instead say persona was roughly 25 points; cells scored 9.2 topline and 9.8 subgroup MAE; direct estimation scored 8.6 and 9.8; and the methods tied under the registered equivalence margin (`rewrite-facts.md:251-265`; `15-simulating-opinion.facts.md:31,37-43`). Both cannot be used.

The cited bibliography item is titled **HiveSight Benchmark Pre-analysis Plan**, yet the catalogs use it as the results citation. A pre-analysis plan can establish what was promised; it cannot establish what happened. The public evidence must include the preregistration timestamp, immutable target definitions, raw predictions, estimator code, exact model/version and cutoff, uncertainty, exclusions, and a reproducible scoring script. Until then these are self-reported results from the author's own product.

The GSS series is also internally wrong. `17-simulating-values.facts.md:13` says nearly 63 percent in 2022 and just under 56 in 2024, while its own next note and the mandatory correction give about 61 and 55—a roughly six-point reversal, not seven (`rewrite-facts.md:274-278`). The [GSS](https://gss.norc.org/) is the primary data source, but a defensible result must state the variable coding, sample restrictions, survey weights, mode treatment, and standard errors. A change in a noisy survey estimate is not the ground truth of a latent social value.

**Required rewrite.** Choose the registered HiveSight numbers from a results artifact, not the outline; label the topline tie prominently; reproduce the GSS estimate from public code; and call survey targets noisy, wording-specific measurements rather than certifiable latent opinion.

---

## 2. GAPS: the 10 missing stories and source bases the book most needs

### 1. Statistics Canada's SPSD/M: the closest predecessor to the proposed stack

The book cannot present rules + synthetic population + distributional scoring as a new architecture without confronting the Social Policy Simulation Database and Model. Statistics Canada first released SPSD/M in 1988. The current v34.0, released 12 February 2026, combines a non-confidential synthetic person/family database derived from surveys and tax/benefit administrative records with a static federal/provincial tax-transfer model, thousands of parameters, base/reform analysis, and commodity taxes. It supports policy years from 1997 through 2030 and has been used across government and academia for decades.

Sources: Statistics Canada's [history](https://www150.statcan.gc.ca/n1/pub/11-633-x/11-633-x2017008-eng.htm), [overview](https://www.statcan.gc.ca/en/microsimulation/spsdm/overview), and [v34.0 release](https://www150.statcan.gc.ca/n1/daily-quotidien/260212/dq260212c-eng.pdf).

**Why it matters.** SPSD/M anticipates the book's integration of rules, synthetic/calibrated population data, a GUI/modeling layer, marginal-rate analysis, and public distribution. The rewrite must say what the new stack changes: open and machine-addressable code, provenance gates, per-record conformance, web/API access, licensing, geographic/program breadth, and agent-assisted maintenance. Otherwise its novelty claim is historically false.

**Owner:** Chs. 1–2 for lineage; Ch. 7 for architecture and data access.

### 2. EUROMOD's baseline-validation literature and operating institution

EUROMOD is treated mainly as an oracle or a project that “publishes and moves on.” That erases three decades of institutional design. It began in 1996, expanded from EU-15 to all 27 member states, transferred progressively to the JRC from 2018 to 2021, and became open source in December 2020. National teams and the JRC continuously update policy systems; country reports compare baseline simulations with EU-SILC and external administrative statistics; a 2025 macrovalidation tool formalized part of that work; and EUROMOD supports current Eurostat flash poverty estimates and European Semester analysis.

Sources: JRC's [EUROMOD overview](https://euromod-web.jrc.ec.europa.eu/overview/what-is-euromod), [country reports](https://euromod-web.jrc.ec.europa.eu/resources/country-reports), the foundational [validation paper](https://microsimulation.pub/articles/00075), the [baseline report](https://publications.jrc.ec.europa.eu/repository/handle/JRC128718), and the [2025 macrovalidation guide](https://euromod-web.jrc.ec.europa.eu/sites/default/files/2025-02/Quick_guide_EUROMOD_macrovalidation_Feb2025.pdf).

**Why it matters.** The defensible contrast is not “no validation loop.” It is that EUROMOD's mature baseline/macro validation generally is not a preregistered, per-policy, interval-scored forecast docket. That narrower delta is interesting and true.

**Owner:** Chs. 2, 10, and 13.

### 3. SOUTHMOD as a mature network—and a live competitor in synthetic data

The rewrite needs SOUTHMOD's actual origin, governance, access model, and current trajectory, not merely five names used as Axiom comparators. SOUTHMOD began around 2014–2015, developed national teams and a shared EUROMOD-compatible framework, now maintains roughly fourteen models, and has released bundles with broad non-commercial access. Its 2026 work includes new policy years, Egypt, and a Ghana feasibility study on synthetic data and AI tools.

Sources: [phase 3](https://www.wider.unu.edu/project/southmod-simulating-tax-and-benefit-policies-development-phase-3), [access terms](https://www.wider.unu.edu/about/accessing-southmod-models), [SOUTHMOD at 10](https://www.wider.unu.edu/publication/southmod-10), and the 2026 [synthetic-data study](https://doi.org/10.35188/UNU-WIDER/ATZV1858).

**Why it matters.** This changes the plot from “agents gave five countries models” to “agents rapidly produced a second implementation against mature national public goods.” It also destroys any suggestion that populace is alone in exploring synthetic microdata for data-constrained countries.

**Owner:** Chs. 2 and 11.

### 4. The Census SIPP Synthetic Beta: “move the referee, not the data” prior art

The Census SIPP Synthetic Beta links SIPP with IRS and SSA earnings/benefit records, releases fully synthetic implicates after disclosure review, and invites researchers to submit code that Census staff rerun on the confidential “Gold Standard,” returning disclosure-cleared validation results. This is a direct ancestor of the proposed custodian pack.

Sources: Census's [product and validation protocol](https://www.census.gov/programs-surveys/sipp/guidance/sipp-synthetic-beta-data-product.html), [construction paper](https://www.census.gov/library/working-papers/2018/adrm/SIPP-Synthetic-Beta.html), and [2024 accuracy assessment](https://www.census.gov/library/working-papers/2024/adrm/ced-wp-2024-004.html).

**Why it matters.** The novelty cannot be “send code to the confidential data custodian and get cleared outputs.” It may be a standardized, cross-country, preregistered, low-dimensional scorecard plus reproducible manifests. Credit the ancestor and sharpen the delta.

**Owner:** Chs. 7 and 11.

### 5. The existing uncertainty literature in tax-benefit microsimulation

The claim that policy microsimulation “produces scenarios, not distributions” ignores at least thirty years of methods. Pudney and Sutherland derived confidence intervals for a UK tax-benefit model in 1994. Goedemé and coauthors explained how to test microsimulation differences while respecting baseline/reform covariance. Tax Policy Center researchers bootstrapped a large US tax model and found narrow aggregate but sometimes wide or asymmetric subgroup intervals.

Sources: [Pudney and Sutherland (1994)](https://doi.org/10.1016/0047-2727(94)90030-2), [Goedemé et al. (2013)](https://euromod-web.jrc.ec.europa.eu/research/publications/testing-statistical-significance-microsimulation-results-often-easier-you), and the [TPC bootstrap study](https://www.microsimulation.pub/articles/00216).

**Why it matters.** The true indictment is institutional, not methodological: routine public scores rarely propagate and report all material uncertainties. The author's 10×1,000 exercise can illustrate neglected practice, but cannot be presented as inventing interval estimation.

**Owner:** Ch. 13.

### 6. Policy2Code and the 2024–2025 AI rules-as-code community

The Georgetown/Digital Benefits Network Policy2Code effort ran four experiments translating SNAP and Medicaid policy across seven states into summaries, machine-readable rules, and code. It published prompts, outputs, rubrics, and scores; twelve US and Canadian teams participated in the challenge. Its conclusion is the nuanced one the book needs: LLMs can accelerate pieces of translation, but complex policy logic still needs external knowledge, explicit evaluation, and human/legal oversight.

Sources: the March 2025 [AI-Powered Rules as Code report](https://digitalgovernmenthub.org/publications/ai-powered-rules-as-code-experiments-with-public-benefits-policy/) and [cross-sector community report](https://digitalgovernmenthub.org/publications/cross-sector-insights-from-the-rules-as-code-community-of-practice/).

**Why it matters.** This is direct recent prior art, and Ariel Kennan is a report coauthor. Omitting it makes the Axiom origin story look curated. RuleSpec, money-atom grounding, signed manifests, and oracle ratchets should be argued as advances over a documented community, not spontaneous invention.

**Owner:** Chs. 8–9.

### 7. Post Office Horizon: the canonical warning against treating software as an oracle

Erroneous Horizon accounting evidence supported prosecutions and civil actions over two decades. The 2019 Bates judgment examined bugs, errors, and defects; Parliament's 2024 legislation quashed hundreds of convictions; the statutory inquiry's July 2025 volume documented severe human harm and redress failures. As of 8 July 2026, later technical/governance inquiry volumes were still pending, so the book must not pre-attribute their conclusions.

Sources: the [Bates judgment](https://www.judiciary.uk/wp-content/uploads/2019/12/bates-v-post-office-judgment.pdf), the government's [2024 quashing announcement](https://www.gov.uk/government/news/post-office-horizon-convictions-quashed), and the inquiry's [reports/status](https://www.postofficehorizoninquiry.org.uk/reports-and-statements).

**Why it matters.** Horizon is the exact adversarial counterexample to “oracle parity establishes correctness.” Institutions treated computer output as presumptively true and shifted the burden to individuals. A technical conformance board without appeal rights, evidence disclosure, and institutional accountability can reproduce the same failure.

**Owner:** Ch. 10, with a return in Ch. 17.

### 8. The Dutch childcare-benefits scandal: exact execution can still automate injustice

The Dutch parliamentary inquiry found that core rule-of-law principles were violated; small errors were treated as fraud, parents were wrongly branded intentional fraudsters, nationality was used unlawfully/discriminatorily, and inaccurate or obsolete fraud-list data had grave consequences. Harms to children remained an active government issue in 2025.

Sources: the Dutch Parliament's [inquiry report announcement](https://www.tweedekamer.nl/nieuws/kamernieuws/eindverslag-onderzoek-kinderopvangtoeslag-overhandigd), the data-protection authorities' [fraud-blacklist summary](https://www.edpb.europa.eu/news/national-news/2022/tax-administration-fined-fraud-black-list_ga), and the government's [June 2025 response on affected children](https://www.government.nl/latest/news/2025/06/30/government-acknowledges-additional-suffering-of-children-placed-in-care).

**Why it matters.** Perfect provenance and deterministic execution do not make legislation just, classifications nondiscriminatory, institutional incentives healthy, or appeals effective. This story forces the book to distinguish faithful calculation from legitimate administration.

**Owner:** Chs. 9–10 and 15–17.

### 9. HealthCare.gov's failure and recovery: rules are only one layer of delivery

GAO found that the 2013 launch suffered inadequate capacity planning, coding errors, missing functionality, inconsistent testing, unmanaged requirements, and weak oversight. HHS OIG documented unclear leadership and poor coordination between policy and technical work, then the managerial reorganization that enabled recovery.

Sources: [GAO-15-238](https://www.gao.gov/products/gao-15-238), [GAO-14-694](https://www.gao.gov/products/gao-14-694), and HHS OIG's [recovery case study](https://oig.hhs.gov/reports/all/2016/healthcaregov-case-study-of-cms-management-of-the-federal-marketplace/).

**Why it matters.** Accurate rules, tests, and source anchors do not solve procurement, ownership, integration, load, security, or operations. The recovery also avoids the lazy conclusion that government cannot build technology: governance and execution changed the outcome.

**Owner:** Chs. 5 and 10.

### 10. The 2025–2026 legal and benchmark environment is moving under the thesis

The book needs a dated “state of the field” box rather than sprinkling current claims through permanent prose:

- The EU AI Act classifies systems used to evaluate, grant, reduce, revoke, or reclaim essential public-assistance benefits as high-risk; the precise 2026 compliance timetable and guidance were themselves changing. See [Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3) and the Commission's [high-risk guidance page](https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-high-risk-systems).
- US OMB M-25-21 (April 2025) presumptively treats AI used for benefit adjudication, continuing eligibility, fraud detection, and penalties as high-impact and requires minimum risk practices. See [M-25-21](https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf).
- OBBBA implementation in 2026 is creating real state system changes in SNAP and Medicaid, not merely new formula parameters.
- PolicyBench's live board already moved enough to falsify the manuscript's July 2026 headline, and its fixed public set raises contamination risk.
- SOUTHMOD, EUROMOD, Policy2Code, and Census synthetic-data programs are moving in adjacent directions.

**Why it matters.** “Decision support, not replacement” should be connected to actual legal obligations. Benchmark and launch claims must be frozen to dated artifacts. A book arguing for permanent verification infrastructure cannot itself ship an unverifiable moving-target fact base.

**Owner:** A dated note in the Introduction, then Chs. 8–10.

---

## 3. INTERNAL CONTRADICTIONS AND UNRESOLVED COLLISIONS

These are contradictions inside the supplied materials; no external disagreement is required to reject them.

1. **Retired data-layer name remains in the design.** `from-scratch-outline.md:145-147` calls the synthetic-microdata layer “microplex”; `rewrite-facts.md:12-16` explicitly prohibits that name and says the entire layer is populace. Delete every current use.

2. **Axiom is both launched and not launched.** `from-scratch-outline.md:78-82` says “Axiom launched,” while `rewrite-facts.md:54-57` and multiple catalogs set the public launch for 28 July 2026. On the review date, 11 July, the past tense is false. Separate drafting-date status from intended post-launch publication text.

3. **Atlanta Fed is both nameable and confidential.** `from-scratch-outline.md:285-286` says the regional Fed must remain unnamed. `rewrite-facts.md:24-26` expressly authorizes “Federal Reserve Bank of Atlanta,” and `06-proof-of-concept.facts.md:86-89` names it. Choose the ground-truth authorization and remove the stale prohibition.

4. **TaxCalcBench is fewer than one-third correct but only one-third wrong.** `01-introduction.facts.md:18-23` states the first; `:57` states the second. The complement of under one-third correct is over two-thirds wrong.

5. **JCT uses a representative sample and every return.** `03-tax-model-wars.facts.md:18` says sample; `:23,88` and `12-microsimulation-anywhere.facts.md:38` say full universe. The sample formulation is the one consistent with JCT's documentation.

6. **The UK had no open model, UKMOD was first, and EUROMOD was already open.** `05-a-wall-of-frustration.facts.md:45-47`, `03-tax-model-wars.facts.md:44-46`, `06-proof-of-concept.facts.md:13,19`, and `01-introduction.facts.md:37` cannot all be true without careful dates and access definitions. The catalogs call EUROMOD open source a decade ago and separately date open-sourcing to December 2020.

7. **TAXSIM starts in the 1970s and the early 1980s.** `03-tax-model-wars.facts.md:24` gives the early 1980s; `06-proof-of-concept.facts.md:83` says it powered research since the 1970s. NBER documents federal law back to 1960 and state law from 1977, but law coverage is not project birth. Resolve from the model's own history rather than infer a launch date from supported tax years.

8. **Enhanced CPS has incompatible input data.** `08-three-ingredients.facts.md:66` says CPS/SCF/CEX/RECS/ATUS. The August 2025 primary launch source says CPS/PUF/SIPP/SCF/ACS. The fact catalog is not merely imprecise; it names the wrong product.

9. **A 97 percent calibration improvement coexists with a one-third revenue miss without vintage or metric.** `06-proof-of-concept.facts.md:73-80,147,175-176` and `07-the-household-and-the-society.facts.md:76,165,195-196` assert both. They can coexist only if one is in-sample target loss and the other is a held-out total, or if they concern different versions. The manuscript currently invites the reader to infer that 97 percent means general accuracy.

10. **CBO is “about as accurate” as peers and also beats all of them.** `04-the-accuracy-question.facts.md:27,80` gives parity with Blue Chip/Administration; `14-the-uncertainty-gap.facts.md:31` says CBO beats the Administration, Blue Chip, and SPF. CBO's own study varies by variable and horizon and says only roughly half of two-year forecasts beat SPF. State the conditional result.

11. **CBO both self-grades and “publishes and moves on.”** `04-the-accuracy-question.facts.md:25-30,80` praises public retrospectives and a feedback loop. `13-the-decomposition.facts.md:33`, `14-the-uncertainty-gap.facts.md:76`, and `18-society-in-silico.facts.md:29` deny one exists. The defensible distinction is aggregate budget/economic retrospectives versus a preregistered per-policy forecast ledger.

12. **Counterfactuals are both unresolvable and inevitably graded.** `04-the-accuracy-question.facts.md:85` says an unenacted counterfactual can never be checked against reality. `13-the-decomposition.facts.md:24,32`, `14-the-uncertainty-gap.facts.md:77-78`, and `16-simulating-democracy.facts.md:49` imply every reform estimate will be graded. The first statement is correct; the latter requires a causal design, not an outturn.

13. **The CTC placeholder is silently replaced by a result.** `rewrite-facts.md:318-325` mandates `[[CTC-RESCORE]]`. `07-the-household-and-the-society.facts.md:86-88` and `14-the-uncertainty-gap.facts.md:85-88` assert $23 billion, 2.6 percentage points, and 1.9 million children. Restore the placeholder or formally amend the ground-truth sheet with a reproducible run.

14. **HiveSight has two incompatible benchmark histories.** `from-scratch-outline.md:30-34` gives 36.6-point persona and 6.2-point cell errors. `rewrite-facts.md:251-265` and `15-simulating-opinion.facts.md:31,37-43` give roughly 25 for personas, 9.2/9.8 for cells, and 8.6/9.8 for direct estimation. The outline values are stale or refer to a different experiment and must not migrate into prose.

15. **The GSS reversal has two values in adjacent notes.** `17-simulating-values.facts.md:13` says nearly 63 to just under 56; `:15`, `rewrite-facts.md:274-278`, and `from-scratch-outline.md:223-225` say roughly 61 to 55. The change is about six points, not seven or seventeen.

16. **Simulation scale alternates between 100,000 records and millions of households.** `07-the-household-and-the-society.facts.md:69,82` and `14-the-uncertainty-gap.facts.md:17` describe about 100,000 records; `14-the-uncertainty-gap.facts.md:35` and `18-society-in-silico.facts.md:11` say millions of synthetic households. Distinguish physical records, replicated/synthetic records, and the weighted population represented.

17. **The official and modeled poverty baselines are mixed.** `07-the-household-and-the-society.facts.md:91` gives 9.6 percent beside Census's roughly 12.4 percent and flags the mismatch. Without year, unit, resource definition, threshold, geography, and dataset, the proposed reform effect has no interpretable denominator.

18. **Nigeria is both begun and built.** `rewrite-facts.md:186-188` says the work has begun and lacks an oracle; `12-microsimulation-anywhere.facts.md:21` says the encoding “has been built.” Use “begun” until a coverage manifest says otherwise.

19. **Uganda has zero findings despite a stated divergence.** `12-microsimulation-anywhere.facts.md:14,24-30` reports a maximum 0.4-shilling difference, defines a finding as a dispositioned divergence, and reports zero findings. Define the tolerance and call sub-tolerance differences non-findings, or change the count.

20. **“None had a model” coexists with five named national models.** `12-microsimulation-anywhere.facts.md:9,13-19` names GHAMOD, UGAMOD, MicroZAMOD, ETMOD, and RWAMOD immediately after denying public inspectable predecessors. The intended claim must be narrowed to a specific license, format, or implementation.

21. **An oracle is an independent second opinion and proof of correctness.** `11-the-verification-problem.facts.md:18-20,43-47,91-92` admits oracle fallibility; `:87` says racing establishes correctness. It establishes scoped concordance and generates discrepancies; it does not prove truth.

22. **Deterministic policy has one exact answer and also depends on ambiguity/discretion.** `08-three-ingredients.facts.md:48,82` and `11-the-verification-problem.facts.md:24,89` claim singular exactness. `06-proof-of-concept.facts.md:66-71` and `07-the-household-and-the-society.facts.md:56-57` document mapping disputes, documentation, assets, locality, and discretion. Exactness exists only conditional on an interpretation, inputs, period, and output definition.

23. **Silent staleness is admitted and declared impossible in the same passage.** `11-the-verification-problem.facts.md:52-53` admits that a new rule or program can escape coverage, then says silent staleness cannot occur; `:93`, `12-microsimulation-anywhere.facts.md:34`, and `18-society-in-silico.facts.md:60` repeat the absolute. Regression protection is not change detection.

24. **Aggregate agreement is disqualified and then called sufficient.** `11-the-verification-problem.facts.md:9-12,82-84` says offsetting errors can make aggregates look right; `08-three-ingredients.facts.md:68` says marginals do not validate the joint distribution. `12-microsimulation-anywhere.facts.md:56-58` then treats a handful of low-dimensional custodian outputs as sufficient to trust a transferred population. Such a scorecard is privacy-preserving evidence, not per-record validation.

25. **“Per-unit validation” is used for aggregate calibration.** `02-birth-of-microsimulation.facts.md:64` and `13-the-decomposition.facts.md:52` say a household is checked against administrative totals. An administrative total validates a weighted aggregate or marginal, not the attributes of a particular synthetic household.

26. **The complete corpus is public and includes protected microdata.** `13-the-decomposition.facts.md:51-53` says every project begins from a complete public corpus including populace; `12-microsimulation-anywhere.facts.md:44-45,55-58` says the microdata may be legally unable to leave its custodian. The architecture must allow private inputs with public schemas, methods, tests, and cleared scorecards.

27. **Opinion has no ground truth and is nevertheless graded as if it does.** `14-the-uncertainty-gap.facts.md:89` denies a certifiable target; `15-simulating-opinion.facts.md:37-45,70-71` grades against GSS, SHED, and BRFSS while conceding that ground truth is partial. Survey estimates are noisy, sample- and wording-specific observed targets—not direct observations of latent opinion.

28. **Money-atom scope expands from obligations to everything.** `rewrite-facts.md:116-119` and `10-encoding-the-law.facts.md:65` limit the hard gate to monetary obligations. `10-encoding-the-law.facts.md:68` says every number traces to law, and `09-the-ai-cant-do-your-taxes.facts.md:33` says every parameter has legislative/regulatory provenance. Empirical, administrative, and behavioral parameters do not come from statute.

29. **Chapter numbering is offset.** Beginning with `09-the-ai-cant-do-your-taxes.facts.md:3`, the catalog metadata adds one to the canonical chapter positions in `from-scratch-outline.md:157-232`. Fix metadata before assigning citations, definitions, or cross-references.

30. **Three taxonomies each masquerade as the master decomposition.** `01-introduction.facts.md:65-72` has four questions; `08-three-ingredients.facts.md:13-17` has rules/data/dynamics; `13-the-decomposition.facts.md:56-59` has rules/predictions/values. They can coexist only if named as different levels: questions asked, ingredients of a policy model, and epistemic primitives.

---

## 4. CONCEPT INVENTORY: define once, in dependency order

The rewrite should adopt the following canonical definitions. The owning chapter gives the first full definition; later chapters should cross-reference it rather than redefine or mutate the term.

| # | Concept | Canonical definition and boundary | Owning chapter |
|---:|---|---|---|
| 1 | **Model, simulation, counterfactual** | A **model** is a formal representation of a target system. A **simulation** executes that representation under specified inputs. A **counterfactual** compares mutually exclusive states while explicitly listing what is held fixed; it is not automatically observable later. | Introduction |
| 2 | **Microsimulation and unit of analysis** | Microsimulation applies rules or transition processes to micro-units and then aggregates. Name the operative entity—person, tax unit, benefit unit, family, household, or firm—because they are not interchangeable. | Ch. 1, *The birth of microsimulation* |
| 3 | **Nonlinear aggregation** | In general, applying a nonlinear rule to an average does not equal averaging the rule applied to each unit: \(E[f(X)] \ne f(E[X])\). Micro-calculation solves that aggregation problem but does not make sample estimates exact. | Ch. 1 |
| 4 | **Static and dynamic microsimulation** | A static model holds the population and usually behavior fixed for the comparison; a dynamic model ages units or models transitions through time. Neither definition is the same as budget-score “dynamic scoring,” which concerns macro feedback. | Ch. 1 |
| 5 | **Baseline, reform, score, incidence** | A baseline is the dated policy/economic scenario used for comparison; a reform changes specified rules; a score is the modeled reform-minus-baseline delta; incidence asks who ultimately bears or receives that delta under stated behavioral and market assumptions. | Ch. 2, *The tax model wars* |
| 6 | **Microdata and disclosure treatment** | Microdata are record-level observations. Define survey versus administrative records, public-use restrictions, sampling, top-coding, swapping, and synthetic records. A synthetic person is not an actual person and is not automatically representative. | Ch. 2 |
| 7 | **Conventional, mechanical, and macro/dynamic scoring** | Mechanical scoring freezes behavior; conventional JCT-style scoring holds aggregate output fixed but can include behavioral responses; macro/dynamic scoring also models aggregate economic feedback. These labels must never be collapsed into “static versus dynamic” without qualification. | Ch. 2 |
| 8 | **Ground truth and validation hierarchy** | Ground truth is external, scope-bound evidence, not a synonym for a favored implementation. Distinguish unit/component validation, aggregate validation, predictive/out-of-sample validation, and legal/source validation. Passing one does not imply the others. | Ch. 3, *The accuracy question* |
| 9 | **Estimate, projection, forecast, backtest, resolution** | An estimate measures a current or latent quantity; a projection is conditional on assumptions; a forecast predicts a future observable; a backtest simulates an earlier information set; resolution is the later observation of the named target. A policy causal effect usually does not directly resolve. | Ch. 3 |
| 10 | **Effective marginal tax rate and benefit cliff** | The effective marginal rate is the local share of an incremental unit of earnings lost to taxes and benefit withdrawals. A cliff is a discrete loss at a threshold and should not be disguised as an ordinary marginal rate. | Ch. 4, *A wall of frustration* |
| 11 | **Representative sample, survey weight, population statistic** | A survey weight maps a sampled record to represented population units. Weighted totals, rates, deciles, and poverty measures are estimates with sampling and specification error, not enumerations. Define percent versus percentage-point change here. | Ch. 6, *The household and the society* |
| 12 | **Disposable income, poverty, and distributional analysis** | Disposable income is resources after specified taxes and transfers; poverty depends on a named resource measure, unit, threshold, equivalence scale, geography, and year; distributional analysis groups modeled changes by a declared ranking variable and baseline/reform convention. | Ch. 6 |
| 13 | **Statistical matching, imputation, synthesis** | Matching borrows attributes from donor records; imputation estimates missing attributes; synthesis generates artificial records. None by itself recovers the true joint distribution or eliminates model error. | Ch. 7, *Three ingredients* |
| 14 | **Calibration, joint structure, uprating, and aging** | Calibration changes weights or records to match selected marginal targets; the joint distribution describes dependence among variables and is not validated by marginal fit. Uprating moves monetary variables to a target period using declared indices; aging changes weights or attributes to represent a later population. None creates new observed data, and all require held-out, joint, tail, and downstream checks. | Ch. 7 |
| 15 | **Elasticity and structural behavior** | An elasticity is a reduced-form proportional response parameter; taxable-income elasticity includes avoidance and timing as well as real activity. A structural model derives choices from assumed preferences, constraints, and expectations. Both are uncertain inputs, not law. | Ch. 7 |
| 16 | **Entitlement, take-up, administrative discretion** | Entitlement is the result under a specified legal interpretation and complete inputs. Take-up is whether an eligible unit participates. Administration includes documentation, caseworker judgment, timing, errors, appeals, and local practice. Only the first may be deterministic in the narrow sense. | Ch. 7 |
| 17 | **LLM tool calling and MCP** | Tool calling means a language model selects and invokes an external function; MCP standardizes discovery and invocation. Neither mechanism warrants the tool's data, law, calculation, or result. | Ch. 8, *The AI can't do your taxes* |
| 18 | **Rules as code and RuleSpec** | Rules as code is an executable interpretation of authoritative text, including logic, parameters, dates, scope, and tests. RuleSpec is this book's particular representation. Machine readability does not remove interpretation or confer legal authority. | Ch. 9, *Encoding the law* |
| 19 | **Provenance, source anchor, money atom, signed manifest** | Provenance records origin and transformation; a source anchor binds an artifact to a passage/version; a money atom requires a monetary obligation to trace to authority; a signed manifest records exact inputs and checks. Grounding establishes traceability, not correct logic or just policy. | Ch. 9 |
| 20 | **Oracle, parity, finding, disposition, conformance ratchet** | An oracle is an independent comparator, not infallible truth. Parity is agreement over an enumerated surface and tolerance; a finding is a defined class of mismatch; a disposition is its evidenced explanation; a ratchet preserves already-tested invariants. None proves completeness or detects unencoded law. | Ch. 10, *The verification problem* |
| 21 | **Transfer evaluation, custodian pack, scorecard** | Transfer evaluation tests whether a population/model works in another domain. A custodian pack sends fixed code/tests to protected data; a returned scorecard is disclosure-cleared aggregate evidence. It is not equivalent to per-record validation. | Ch. 11, *Microsimulation anywhere* |
| 22 | **Uncertainty, intervals, and propagation methods** | Separate sampling/input, parameter, structural/model, implementation, and future/process uncertainty. Confidence, credible, and prediction intervals answer different questions. Monte Carlo propagates declared probability distributions; bootstrap resamples units; sensitivity varies assumptions without probabilities; scenarios compare coherent conditional worlds. | Ch. 13, *The uncertainty gap* |
| 23 | **Conditional forecast, scoring rule, probabilistic calibration** | A conditional forecast resolves only if its condition occurs. A proper scoring rule rewards honest probability distributions; calibration is a repeated-frequency property, not one interval containing one outcome. The unchosen causal branch remains unobserved. | Ch. 13 |
| 24 | **Silicon sampling, post-stratification, and evaluation hygiene** | Silicon sampling uses model-generated estimates, not respondents. Persona role-play, direct aggregate estimates, and within-cell distributions are distinct estimators. Define MAE, rank correlation, variance, and equivalence margins here; preregister scoring, hold out targets from tuning, reconstruct backtests honestly, and audit leakage rather than infer cleanliness from a model cutoff. | Ch. 14, *Simulating opinion* |
| 25 | **Values, beliefs, preferences, futarchy** | Values specify ends; beliefs concern facts and causal consequences; preferences are choices or rankings under a measurement procedure. Futarchy proposes voting on objectives and using conditional markets for means; it does not itself confer democratic legitimacy or reveal latent values. | Ch. 15, *Simulating democracy* |

## Rewrite gate

No chapter draft should be generated from these catalogs until four repairs are complete:

1. replace the volatile benchmark and policy snapshots with dated, archived primary artifacts;
2. resolve every contradiction above in `rewrite-facts.md` itself so the next writer receives one canonical instruction set;
3. add a source ledger distinguishing independent primary evidence, project-authored evidence, pre-analysis plans, live dashboards, and unverifiable author calculations; and
4. reserve “true,” “exact,” “first,” “complete,” “all,” “every,” and “impossible” for claims with an explicit denominator and a source capable of proving the universal.

Until then, a ground-up rewrite will merely make the same factual weaknesses harder to find.

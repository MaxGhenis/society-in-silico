# Microsimulation Model Validation Cases

This document catalogs concrete examples where microsimulation models made predictions that can be compared to actual outcomes. These cases illuminate the accuracy, limitations, and evolution of policy modeling.

## Executive Summary

Microsimulation models have a mixed track record. Some predictions (CBO on ACA coverage expansion, UK pension auto-enrollment) came remarkably close to reality. Others (1986 Tax Reform corporate revenues, Medicare Part D costs, TCJA revenues) missed by wide margins—sometimes off by 25-50%. The best predictions tend to be short-term (1-3 years), involve well-established programs, and focus on participation rather than revenues. The worst failures typically involve behavioral responses, macroeconomic interactions, or novel policies where historical patterns don't apply.

---

## 1. Tax Cuts and Jobs Act (TCJA) 2017

### Predictions (December 2017)

**Joint Committee on Taxation (JCT):**
- Conventional estimate: Reduce revenues by $1,438 billion over 2018-2027
- Dynamic estimate (with macroeconomic feedback): Reduce revenues by ~$1 trillion over 10 years

**Source:** [CBO Publication 53312](https://www.cbo.gov/publication/53312)

### Actual Outcomes

**Revenue Shortfall (FY2018):**
- Total revenue shortfall: $275 billion below CBO's January 2017 projection (7.6% below expectations)
- Corporate income tax: $135 billion below projection (almost exactly 40% decline)
- Individual income tax: $97 billion below projection (5.4% decline)

**Long-term Assessment (2018-2027):**
- CBO pre-TCJA projection (June 2017): $43.016 trillion in revenues
- CBO post-TCJA projection (August 2019): $41.409 trillion in revenues
- **Actual decline: ~$1.6 trillion** vs. JCT's dynamic estimate of $1 trillion

**Budget Impact:**
- Pre-TCJA deficit projection for FY2018: $563 billion
- Actual FY2018 deficit: $780 billion (+39% higher, +$217 billion)
- Revenues as % of GDP: Averaged 17.0% (2018-2023) vs. pre-TCJA projection of 18.1%

### Lessons Learned

- The TCJA cost significantly more than originally projected—estimates were 50% larger by 2018
- Revenue feedback effects from economic growth were substantially smaller than hoped
- Prediction was complicated by intervening factors (pandemic, inflation, immigration)
- "Did it pay for itself?" No—contrary to some proponents' claims

**Sources:**
- [Tax Policy Center: TCJA Cost More Than Expected](https://taxpolicycenter.org/taxvox/revisions-revenue-projections-suggest-tcja-cost-more-expected)
- [Brookings: Did the TCJA Pay for Itself?](https://www.brookings.edu/articles/did-the-2017-tax-cut-the-tax-cuts-and-jobs-act-pay-for-itself/)
- [CRFB: Has TCJA Paid For Itself?](https://www.crfb.org/blogs/has-tcja-paid-itself)
- [CRS: Economic Effects of TCJA](https://www.congress.gov/crs-product/R48485)

---

## 2. Tax Reform Act of 1986

### Predictions

**Joint Committee on Taxation:**
- Revenue neutral overall (by design—Reagan promised to veto if not revenue-neutral)
- Shift of $120.3 billion from individual to corporate taxes (1987-1991)
- Individual tax revenues: Decrease $121.9 billion
- Corporate tax revenues: Increase $120.3 billion

**Key mechanism:** Lower rates offset by base-broadening measures (eliminating investment tax credit, restricting depreciation, limiting tax shelters)

**Source:** [NBER Working Paper 3940](https://www.nber.org/papers/w3940)

### Actual Outcomes

**Corporate Tax Revenue Shortfall:**
- Corporate taxes fell "far short" of projections in every year 1987-1991
- Corporate revenues were below even pre-TRA projections (not just below the higher post-TRA targets)
- The shortfall was **not just a failure to increase revenues as predicted—actual collections fell below what would have happened without reform**

**Individual Tax Revenue:**
- Individual income tax revenues grew faster than expected, nearly 6% above projections
- Lower rates generated stronger taxpayer response (classic supply-side effect)

**Source:** [NBER: Why Didn't the Tax Reform Act of 1986 Raise Corporate Taxes?](https://www.nber.org/system/files/chapters/c10839/c10839.pdf)

### Reasons for the Discrepancy

1. **Corporate profits lower than expected** - Forecasts assumed historically high profit rates that didn't materialize
2. **Higher corporate debt** - Interest payments substantially larger as share of corporate income (reduced taxable income)
3. **Rise of S-corporations** - Income shifted from corporate to individual tax system (S-corp income taxed as individual income). This was a behavioral response not fully anticipated.
4. **Unexpected behavioral responses** - Stock repurchases increased more rapidly than expected; dividend payouts changed differently than predicted

### Lessons Learned

- Revenue-neutral tax reform is extremely difficult to predict because it involves offsetting large behavioral changes
- Behavioral responses to changed incentives can overwhelm static revenue estimates
- Corporate profit forecasting is inherently uncertain
- Tax structure changes can cause income shifting between tax systems (corporate vs. individual)
- This case illustrates why dynamic scoring is needed but also why it's difficult

**Sources:**
- [Treasury Working Paper 59: Noncorporate Business Taxation](https://home.treasury.gov/system/files/131/WP-59.pdf)
- [Tax Foundation: Modeling Economic Effects of Past Tax Bills](https://taxfoundation.org/research/all/federal/modeling-economic-effects-past-tax-bills/)
- [Heritage Foundation: Tax Reform Revenue Impact](https://www.heritage.org/taxes/report/how-measure-the-revenue-impact-changes-tax-rates)

---

## 3. Affordable Care Act (ACA) 2010

### Predictions (March 2010)

**CBO/JCT Estimates:**
- **Exchange enrollment in 2020:** 24.6 million
- **Medicaid expansion:** Assumed all states would expand (pre-Supreme Court decision)
- **Uninsured rate for non-elderly (2016):** 7.6% (assuming full Medicaid expansion)
- **Subsidy costs (2014-2016):** Specific dollar amounts projected
- **Premium levels:** Within 1% of actual 2017 average marketplace premiums (remarkably accurate)

**Sources:**
- [Commonwealth Fund: CBO's Crystal Ball](https://www.commonwealthfund.org/publications/issue-briefs/2015/dec/cbos-crystal-ball-how-well-did-it-forecast-effects-affordable)
- [CBO: Record of Projecting ACA Subsidies](https://www.cbo.gov/publication/53094)

### Actual Outcomes

**Exchange Enrollment:**
- **2014 actual:** 6.3 million (predicted: 8.6 million)
- **2020 actual:** 10.7 million (predicted: 24.6 million)
- **Shortfall:** 11+ million below estimates every year since 2016

**Medicaid Enrollment:**
- **Average increase through 2014:** ~8 million
- **Current projection:** 13 million in 2023 (vs. earlier projection of 12 million)
- Reasonably accurate given the Medicaid expansion uncertainty

**Uninsured Rate (2016):**
- **Predicted (adjusted for partial Medicaid expansion):** 9.4%
- **Actual:** 10.4%
- **Difference:** 1 percentage point (quite close)

**Subsidy Costs:**
- **2014-2015:** Very close to predictions
- **2016:** Much too high
- Overall: CBO's estimates much closer to actual than other forecasters

**Why Exchange Enrollment Lower Than Expected:**
- CBO projected 1-6 million people would shift from employer coverage to exchanges
- **This didn't happen** - employer coverage remained stable
- Some eligible individuals chose not to enroll despite subsidies

### Lessons Learned

- **Premium predictions were excellent** (within 1%)
- **Enrollment predictions were off** but better than most other forecasters
- **Uninsured rate prediction was quite good** (within 1 percentage point)
- CBO correctly predicted "historic coverage gains" even if exact numbers were off
- Other forecasters (especially CMS) were much worse - CMS estimates were 2-3x higher than actual outcomes
- Behavioral responses to subsidies were lower than expected
- Employer response to reform was overpredicted

**Assessment:** Mixed but generally favorable. The big picture (millions gaining coverage, reduced uninsured rate) was correct. Specific enrollment numbers were off but directionally right.

**Sources:**
- [AAF: Comparing ACA Projections to Actual Performance](https://www.americanactionforum.org/insight/comparing-aca-projections-to-actual-performance/)
- [CBPP: CBO Correctly Predicted Historic Coverage Gains](https://www.cbpp.org/blog/cbo-correctly-predicted-historic-coverage-gains-under-aca)
- [KFF: Assessing ACA Marketplace Enrollment](https://www.kff.org/affordable-care-act/assessing-aca-marketplace-enrollment/)

---

## 4. Medicare Part D (2003-2013)

### Predictions (2003)

**When enacted:** Medicare Prescription Drug, Improvement, and Modernization Act of 2003

**CBO projections:** Specific cost estimates for the voluntary prescription drug benefit beginning 2006

**CMS actuaries (2003):** Projected national drug spending growth continuing at high rates

### Actual Outcomes

**Spending Lower Than Expected:**
- **2013 spending: ~50% below CBO's 2003 projections**
- One of the largest favorable forecast errors in major entitlement programs

**Why Costs Were Lower:**

1. **Slower national drug spending growth:**
   - 1999-2003 average: 13% annual growth
   - 2007-2010 average: 2% annual growth
   - National drug spending in 2012: ~40% less than CMS predicted in 2003

2. **Lower enrollment than expected**
3. **Greater competition among Part D plans**
4. **Shift to generic drugs happened faster than expected**

### Recent Reversal (2024-2026)

**Unexpected Cost Spike:**
- Insurers' 2026 bids anticipate **35% increase** in annual per-enrollee costs
- CBO had expected ~5% increase
- **Projected additional cost:** ~$500 billion more over next decade than previously projected

**Current enrollment (2025):** 54.8 million of 68.8 million Medicare beneficiaries

**Sources:**
- [CBO: Competition and Medicare Part D Cost](https://www.cbo.gov/publication/45552)
- [CBO: Call for New Research on Part D Spending](https://www.cbo.gov/publication/61824)
- [CBO Economic Brief: Medicare Part D 2012](https://www.cbo.gov/sites/default/files/cbofiles/attachments/12-01-MedicarePartD.pdf)

### Lessons Learned

- Sometimes models are too pessimistic—Part D was much cheaper than expected for a decade
- Broader market trends (generic drug adoption, slower pharma spending growth) can dominate program-specific factors
- Long-term pharmaceutical cost prediction is extremely difficult
- Recent experience (2024-2026 spike) shows that favorable surprises can reverse suddenly
- Competition and plan design matter more than initially appreciated

---

## 5. CBO Budget Projection Accuracy (1984-2023)

### Overall Track Record

**CBO evaluation of its own projections** covering four decades of deficit and debt forecasts.

**Source:** [CBO: Evaluation of Projections 1984-2023](https://www.cbo.gov/publication/61067)

### Key Accuracy Metrics

**Deficit Projections (2024):**
- **May 2023 projection for FY2024 deficit:** Underestimated by 1.1% of GDP
- **Revenue projection:** Underestimated by 1%
- **Outlay projection:** Underestimated by 6%
- **Social Security outlays:** Overestimated by $2 billion (<1%)
- **Other mandatory programs:** Overestimated by $36 billion (9%)
- **Veterans' benefits:** Overestimated by $6 billion (3%)

**Average Errors:**
- **Budget-year revenue projections:** Average error of 1.2% (slight tendency to overestimate)
- **Interest outlays:** Historically the least accurate component (greatest uncertainty)

**Improvement Over Time:**
- Accuracy improved substantially from 1989-2001 to 2002-2019 (approximately 3x improvement)
- Recent years (post-2020) more difficult due to unprecedented shocks

**Source:** [CBO: Accuracy of FY2024 Projections](https://www.cbo.gov/publication/61158)

### Lessons Learned

- Short-term (1 year) projections are reasonably accurate for established programs
- Interest rate projections add significant uncertainty
- Mandatory program spending easier to project than discretionary
- Major legislation and economic shocks create large forecast errors
- Accuracy has generally improved with better models and data

**Sources:**
- [CBO: Accuracy of FY2023 Projections](https://www.cbo.gov/publication/59682)
- [CBO: Transparency Plans 2024](https://www.cbo.gov/publication/60228)
- [House Budget Committee: Dr. Swagel Testimony on CBO Accuracy](https://budget.house.gov/download/10/31/2024/dr-phillip-swagel-witness-testimony)

---

## 6. 2021 Child Tax Credit Expansion

### Predictions

**Employment effects predicted by simulation models:**
- Range: 300,000 to 1,460,000 parents leaving workforce
- Most estimates: 300,000-400,000
- Rationale: Cash payments reduce need to work

**Source:** [Columbia: Expanded CTC Impact](https://povertycenter.columbia.edu/publication/2021/expanded-child-tax-credit-impact-on-employment)

### Actual Outcomes

**Employment Effects:**
- **Actual labor force participation change:** Statistically insignificant
- Employment among parents and non-parents both rose 1.7 percentage points in 2021
- University of Michigan study: "No significant employment effects for any outcome"
- **Prediction vs. reality: Models substantially overpredicted work disincentives**

**Participation/Take-up:**
- **62 million children** received monthly payments (July-December 2021)
- **~90% of U.S. children** in families received payments
- **However:** 13% claiming mismatch between CPS model predictions and actual IRS returns
- Lower-income households more likely to have nonclaiming or benefit misassignment
- Administrative burdens led some lowest-income families to miss benefits
- Racial/ethnic minorities more likely to lack access

**Poverty Impact:**
- **Child poverty fell to 5.2%** (lowest level ever)
- **2022 (after expiration):** Returned to 12.4%
- Columbia estimate: Expansion reduced child poverty by 26%; could have been 40% with full take-up

**Sources:**
- [CBPP: Gains From Expanded CTC](https://www.cbpp.org/research/federal-tax/gains-from-expanded-child-tax-credit-outweigh-overstated-employment-worries)
- [ANNALS: What We Learned from 2021 CTC Expansion](https://journals.sagepub.com/doi/10.1177/00027162241272320)
- [ANNALS: Consequences of 2021 CTC Expansion](https://journals.sagepub.com/doi/full/10.1177/00027162241272327)
- [Penn Wharton: CTC Effects](https://budgetmodel.wharton.upenn.edu/issues/2021/10/25/expanding-the-child-tax-credit-effects)

### Lessons Learned

- Microsimulation models substantially **overpredicted labor supply responses**
- Static models struggled with this time-limited, pandemic-era intervention
- Administrative take-up challenges (13% claiming errors) hard to predict
- Actual poverty reduction effects were dramatic and measurable
- The "jobs vs. poverty" tradeoff predicted by models didn't materialize in reality
- Family structure complexity creates benefit assignment challenges

---

## 7. UK Pension Auto-Enrollment (2012+)

### Predictions (Pre-2012)

**Problem:** Private sector pension participation declining from 47% (2000) to 32% (2012)

**Policy:** Automatic enrollment into workplace pensions with opt-out (behavioral economics/"nudge")

**Predicted outcomes:** Higher participation, but uncertain magnitude

### Actual Outcomes

**Participation Rates:**
- **Medium/large employers:** ~90% participation
- **Small employers:** ~70% participation
- **Overall eligible private sector workers:** >90% participation

**Age Groups:**
- **22-25 year-olds:** 20% before → 88% after
- **51-55 year-olds:** 55% before → 93% after

**Financial Security Groups:**
- **Least financially secure:** 22% before → >90% after
- **Most financially secure:** 72% before → 95% after
- Auto-enrollment **dramatically reduced inequality** in pension participation

**Ethnic Differences (remaining challenges):**
- White employees: 10% not participating
- Pakistani employees: 16% not participating
- Bangladeshi employees: 24% not participating

**Self-employed:** Only 16% saving in private pension (2018), down from 48% (1998)—auto-enrollment doesn't reach them

**Sources:**
- [IFS: First Decade of Auto-Enrollment](https://ifs.org.uk/articles/roll-first-decade-automatic-enrolment-workplace-pensions)
- [IFS: Auto-Enrollment Too Successful a Nudge?](https://ifs.org.uk/articles/automatic-enrolment-too-successful-nudge-boost-pension-saving)
- [IFS: Ethnic Differences in Pension Participation](https://ifs.org.uk/publications/ethnic-differences-private-pension-participation-after-automatic-enrolment)

### Lessons Learned

- **Behavioral economics interventions can exceed expectations** when well-designed
- Automatic enrollment with opt-out far more effective than opt-in (classic nudge success)
- Small employers show lower participation (70% vs. 90%), suggesting implementation challenges scale with employer size
- Policy reversed a decade-long decline in participation
- **Remaining challenge:** Many save too little (30-40% won't meet retirement income benchmarks)
- Demonstrates that **participation prediction** is easier than **contribution adequacy prediction**

---

## 8. EITC Participation Rates

### Historical Estimates

**1990 Participation Rate:**
- Estimated **80-86% of eligible taxpayers** received EITC
- Implies <2.1 million eligible taxpayers didn't claim it
- Nonparticipation appeared consistent with rational/voluntary explanations

**Current (2022):**
- **19.2% of eligible taxpayers didn't claim** EITC
- ~80% claim rate (4 in 5 eligible workers)
- **23 million workers and families** received ~$57 billion in EITC
- Average EITC: $2,541

**Sources:**
- [IRS: EITC Participation Rate by States](https://www.eitc.irs.gov/eitc-central/participation-rate-by-state/eitc-participation-rate-by-states)
- [IRS: EITC Statistics](https://www.irs.gov/credits-deductions/individuals/earned-income-tax-credit/earned-income-tax-credit-statistics)
- [National Tax Journal: EITC Participation](https://www.journals.uchicago.edu/doi/abs/10.1086/NTJ41789053)

### Challenges in Measuring Take-Up

**Methodological issues:**
1. Determining filing unit composition
2. Measuring AGI and total earned income accurately
3. Identifying number of EITC qualifying children
4. Lower-income families less likely to file if below filing threshold
5. Language barriers (non-English speakers have lower take-up)

**California state EITC study:** Matched SNAP enrollment data to tax returns to measure CalEITC participation

### Lessons Learned

- Take-up rate has remained remarkably stable (~80%) for 30+ years
- Prediction of participation easier for well-established programs
- Administrative barriers and information gaps still prevent ~20% take-up
- Multilingual outreach matters for equity
- Linking administrative datasets (SNAP + tax returns) improves validation

**Sources:**
- [Science Direct: Measuring California EITC Take-Up](https://www.sciencedirect.com/science/article/abs/pii/S0047272723001846)
- [CRS: EITC Economic Analysis](https://www.congress.gov/crs-product/R44057)

---

## 9. Finland Basic Income Pilot (2017-2018)

### Design

- **2,000 participants** aged 25-58, randomly selected from unemployment benefit recipients
- **€560 per month** unconditional income (even if they found work)
- **Duration:** 2 years (January 2017 - December 2018)
- **Methods:** Randomized controlled trial + microsimulation modeling

**Pre-pilot microsimulation analysis** examined effects on governmental budget, income distribution, and work incentives

**Sources:**
- [World Economic Forum: Finland UBI Results](https://www.weforum.org/stories/2019/02/the-results-finlands-universal-basic-income-experiment-are-in-is-it-working/)
- [Intereconomics: Basic Income in Finnish Context](https://www.intereconomics.eu/contents/year/2017/number/2/article/basic-income-in-the-finnish-context.html)
- [EU Social: Finnish UBI Experiment](https://ec.europa.eu/social/BlobServlet?docId=20846&langId=en)

### Actual Outcomes

**Employment effects:** Minimal (similar to 2021 CTC finding)

**Wellbeing effects:**
- Reduced stress
- Improved mental health
- Greater life satisfaction
- These wellbeing benefits were **not well-captured by pre-pilot microsimulations**

### Lessons Learned

- Microsimulation can model **financial flows** but struggles with **wellbeing outcomes**
- Finland was the only country to complete nationwide RCT of basic income
- "Virtual pilot projects" via microsimulation can test fiscal and employment effects
- Still need physical pilots to test wellbeing effects that models can't capture
- Results context-dependent (Finland ≠ Kenya ≠ United States)

**Sources:**
- [BIEN: UK Basic Income Pilot Analysis](https://basicincome.org/news/2017/12/uk-basic-income-pilot-possible/)
- [IPA: Effects of UBI in Kenya](https://poverty-action.org/effects-universal-basic-income-kenya)
- [McKinsey: UBI Experiment](https://www.mckinsey.com/industries/social-sector/our-insights/an-experiment-to-inform-universal-basic-income)

---

## 10. Australian APPSIM Model Validation

### Model

**APPSIM** = Australian Population and Policy Simulation Model (dynamic microsimulation)

**Data source:** HILDA (Household, Income and Labour Dynamics in Australia) Survey

**Source:** [International Journal of Microsimulation: Validating Dynamic Models](https://microsimulation.pub/articles/00038)

### Validation Framework (Five Stages)

1. Data/coefficient/parameter validation
2. Algorithmic validation (programmer review)
3. Module-specific validation
4. Multi-module validation
5. Impact validation (policy simulation reliability)

### Specific Prediction vs. Outcome Comparisons

**Labour force participation (2006):**
- **Retirement rates by age/sex:** APPSIM "reasonably well aligned" with HILDA
- APPSIM rates slightly lower at younger ages (retirement before 55 not simulated)

**Year-to-year transitions (2004-2005):**
- Full-time employed workers aged 25-54
- **APPSIM predicted:** 88% remain full-time employed
- **HILDA actual:** 91% remain full-time employed
- **Difference:** 3 percentage points (quite close)

**Fertility prediction challenges:**
- Only 43% of actual births came from highest probability quintile
- 20% of births came from lowest probability quintile
- Demonstrates significant randomness requiring alignment adjustments

**Tools used:**
- 672 different summary statistics per simulation
- Individual Output Tool (IOT) for tracking specific individuals
- Cohort tracking
- Alignment mechanisms to match external benchmarks

### Lessons Learned

- **Multi-stage validation catches different types of errors**
- Transition probabilities (88% vs 91%) can be quite accurate over short periods
- High-probability events don't always happen; low-probability events do (fertility example)
- Alignment to external benchmarks is necessary for long-run accuracy
- Validation is ongoing—"clients very often run a policy simulation that the NATSEM modellers have not managed to anticipate"
- Even with 10+ years experience (STINMOD), new validation challenges emerge

**Sources:**
- [NATSEM: STINMOD Use in Policy Process](https://researchprofiles.canberra.edu.au/en/publications/stinmod-use-of-a-statistic-microsimulation-model-in-the-policy-pr)
- [University of Canberra: Reviewing STINMOD](https://ideas.repec.org/p/cba/wpaper/wp114.html)

---

## 11. JCT Revenue Estimating: General Track Record

### Transparency and Retrospective Analysis

**1995 Initiative:** JCT Chief of Staff Kenneth Kies declared "the public knows too little about how the Joint Committee on Taxation prepares revenue estimates" and outlined transparency initiatives.

**Retrospective analysis challenges:**
- Limited to "relatively infrequent situations" where tax change is isolated (not part of larger package)
- Need to identify taxes actually collected/lost from specific provision
- Most tax changes are bundled, making retrospective validation difficult

**10 years later (2005):** Unclear how much transparency initiatives accomplished. JCT has not systematically "selected several estimates" for retrospective analysis as originally envisioned.

**Sources:**
- [JCT: Revenue Estimating FAQ](https://www.jct.gov/operations/revenue-estimating/)
- [Heritage: Transparency in Revenue Estimating](https://www.heritage.org/node/17542/print-display)
- [Capitol History: JCT from Outside Looking In](https://capitolhistory.org/wp-content/uploads/2016/02/USCHS-History-Role-Joint-Committee-Taxation-Samuels.pdf)

### Key Practices

- Estimates take into account behavioral responses (not purely "static" despite terminology)
- Conventional estimates have included behavioral responses for >25 years
- Objective: "accurate, consistent, fair, and impartial estimates"
- Technical foundations for specific estimates remain largely confidential

### Lessons Learned

- **Systematic retrospective validation remains rare** in tax policy
- Bundling of provisions makes it difficult to isolate effects
- Tension between transparency and maintaining confidentiality of methods
- Behavioral response modeling has been incorporated longer than many realize
- Lack of formal validation studies limits ability to improve estimating techniques

**Sources:**
- [CRS: Dynamic Scoring for Tax Legislation](https://www.congress.gov/crs-product/R43381)
- [Tax Foundation: TPC Methodology](https://taxpolicycenter.org/resources/tpcs-methodology-model-revenue-estimates)

---

## 12. International Microsimulation Models (Overview)

### France: IPP TAXIPP Model

**Model:** Tax and benefit microsimulation for French households

**Data sources:**
- Fideli (INSEE): Housing tax, income tax, property tax files
- Felin (DGFiP): 500,000 tax units with exhaustive high-income representation
- DADS: Worker information from employers for payroll taxes
- BNS (Insee): Similar to DADS for self-employed

**Validation approach:**
- Compare forecasts with other models using similar methods/data
- Administrative data provides more precision than household surveys

**No specific prediction vs. outcome validation studies found in search**

**Sources:**
- [IPP: TAXIPP Microsimulation Model](https://www.ipp.eu/en/methods/taxipp-micro-simulation/)
- [INSEE: INES Model](https://www.insee.fr/en/information/6049866?sommaire=6049874)
- [IPP: TAXIPP Version 1.1](https://www.ipp.eu/en/publication/the-taxipp-microsimulation-model-version-1-1/)

### Canada: SPSD/M and CTaCS

**SPSD/M** (Social Policy Simulation Database and Model):
- Oldest Statistics Canada microsimulation model (released 1988)
- Static model for distributional impact of tax/transfer changes
- Non-confidential, statistically representative database
- Used by hundreds of sites across Canada

**CTaCS** (Canadian Tax and Credit Simulator):
- Simulates personal income tax and transfer system
- Stata-based
- Database of parameters from 1962-2005
- Computes marginal tax rates for labor supply modeling

**No specific prediction vs. outcome validation studies found in search**

**Sources:**
- [Statistics Canada: SPSD/M Overview](https://www.statcan.gc.ca/en/microsimulation/spsdm/spsdm)
- [ResearchGate: Inventory of Canadian Models](https://www.researchgate.net/publication/238597596_An_Inventory_of_Canadian_Microsimulation_Models)
- [Statistics Canada: DYSEM Platform](https://www150.statcan.gc.ca/n1/pub/11-633-x/11-633-x2017008-eng.htm)

### UK: IFS TAXBEN and OBR

**TAXBEN Model:**
- Operating since 1983
- Family Expenditure Survey (7,000 UK households)
- Substantially revised in 1990
- Used for real-time budget analysis

**Office for Budget Responsibility (OBR):**
- Publishes Forecast Evaluation Reports (FERs)
- Three purposes: (1) Accountability, (2) Identify persistent bias, (3) Illustrate impact of shocks
- Recent years: Large unanticipated shocks (Covid, Ukraine energy crisis, inflation)

**IFS accuracy critique (2024):**
- 90% chance that 2027/28 borrowing will be 40 billion pounds higher than OBR forecast
- 2027/28 borrowing likely 3.1% of GDP vs. OBR forecast of 1.7%
- Chancellors "don't respond symmetrically to economic shocks" (creates forecast bias)

**Historical comparison (2016):**
- IFS forecast for 2019-20 deficit: £14.9 billion
- Very close to OBR's pre-measures forecast of £13.6 billion

**Sources:**
- [OBR: Forecast Evaluation Reports](https://obr.uk/forecast-evaluation-reports/)
- [IFS: TAXBEN Model](https://ifs.org.uk/publications/taxben-ifs-tax-and-benefit-microsimulation-model)
- [Investing.com: IFS Sees 90% Chance of Deficit Overshoot](https://www.investing.com/news/economy/uks-ifs-sees-90-chance-of-budget-deficit-overshoot-by-202728-3184721)

---

## Summary: What Makes Predictions Accurate?

### Factors Associated with More Accurate Predictions

1. **Short time horizons** (1-3 years better than 5-10 years)
2. **Established programs** with historical data (EITC, Social Security)
3. **Participation/enrollment** easier to predict than revenue
4. **Well-understood behavioral responses** (auto-enrollment nudges)
5. **Administrative data** availability for validation
6. **Isolated policy changes** (easier to measure than bundles)

### Factors Associated with Large Forecast Errors

1. **Long time horizons** (5-10 years)
2. **Novel policies** without historical precedent
3. **Revenue predictions** (especially corporate taxes)
4. **Macroeconomic interactions** and feedback effects
5. **Behavioral responses to incentives** (particularly labor supply)
6. **Bundled legislation** (hard to isolate effects)
7. **External shocks** (pandemic, wars, inflation)
8. **Income/profit shifting** across tax systems

### Model Limitations Revealed by Validation

- **Employment disincentive effects routinely overpredicted** (2021 CTC, Finland UBI)
- **Wellbeing effects not captured** by financial microsimulation
- **Administrative take-up challenges** hard to model (13% CTC claiming error)
- **Behavioral adaptation** often differs from historical patterns
- **Political economy effects** (Chancellors' asymmetric responses to shocks)
- **Dynamic feedback** smaller than hoped (TCJA revenue feedback)

### Recommendations for Future Modeling

1. **Conduct more retrospective validation studies** (currently rare, especially for tax policy)
2. **Report uncertainty ranges**, not just point estimates
3. **Separate prediction types**: participation vs. revenue vs. behavioral effects
4. **Update models** as data accumulates (CBO does this; JCT less transparent)
5. **Link administrative datasets** for validation (IRS + Census + program enrollment)
6. **Test novel policies** with small-scale RCTs before full implementation
7. **Publish validation results** even when models fail (Finland did this well)

---

## Conclusion

The validation cases reveal a humbling reality: microsimulation models are powerful tools but imperfect crystal balls. Their best use is not predicting the future with precision, but **illuminating tradeoffs, comparing alternatives, and estimating orders of magnitude**. The most valuable models are those whose creators regularly compare predictions to outcomes, acknowledge errors, and refine their methods—a practice more common at CBO than JCT, more common for spending programs than tax policy, and still too rare overall.

The field would benefit from a norm of systematic retrospective analysis. As Kenneth Kies wrote in 1995, "the public knows too little about how...revenue estimates" are prepared. Thirty years later, we also know too little about whether those estimates were right.
# PolicyEngine Validation Against Official Scorers

Research findings on how PolicyEngine estimates compare to official scorers (CBO, JCT, Tax Policy Center, IFS).

**Research Date:** 2025-12-23
**Issue:** society-in-silico-ozz

## Executive Summary

PolicyEngine has made significant strides in validation, but **lacks published head-to-head comparisons with CBO, JCT, or Tax Policy Center estimates** for specific policy proposals. The primary validation work focuses on:

1. **Technical validation** against NBER's TAXSIM model
2. **Calibration** to administrative aggregates from IRS, CBO, JCT, and Treasury
3. **Self-reported accuracy improvements** through enhanced microdata
4. **Third-party use** by organizations like the Niskanen Center

**Critical gap:** No independent third-party evaluation of PolicyEngine's accuracy exists in the published literature.

## Known Accuracy Limitations

### Revenue Estimate Discrepancy

PolicyEngine openly acknowledges a systematic underestimation issue:

> "Because PolicyEngine uses a household survey, its revenue impacts are around a third lower than official estimates which use administrative tax datasets (which are less likely to miss out high-income filers)."

**Source:** [Introducing Utah State Income Tax Analysis on PolicyEngine](https://blog.policyengine.org/introducing-utah-state-income-tax-analysis-on-policyengine-4a1ccc262628)

**Why this matters:**
- Household surveys systematically under-sample high-income filers
- Administrative tax data (used by CBO/JCT) captures the full distribution
- Revenue estimates being "around a third lower" is a substantial discrepancy
- This affects cost estimates for any policy touching high earners

**PolicyEngine's planned fix:** Enhanced microdata integration (see below)

## Validation Approaches

### 1. TAXSIM Validation (NBER)

PolicyEngine validates against NBER's TAXSIM-35 model, the established academic standard.

**Methodology:**
- Tests run on every new version update
- Validates tax units in Current Population Survey
- Uses $15 tolerance for "matching" (allows for rounding differences)
- Tests both federal and state tax calculations

**Key resource:** [PolicyEngine TAXSIM emulator](https://github.com/PolicyEngine/policyengine-taxsim) provides "high-fidelity emulator for TAXSIM-35"

**Validation documentation:** [Validation against TAXSIM](https://policyengine.github.io/policyengine-us/validation/taxsim.html)

**What this proves:** Technical implementation of tax rules matches NBER's model within tolerance
**What this doesn't prove:** Aggregate estimates match CBO/JCT for specific policy proposals

### 2. Calibration to Administrative Aggregates

PolicyEngine's enhanced microdata calibrates to **2,813 targets** from authoritative sources:

**Data sources for calibration:**
- IRS Statistics of Income
- Census population projections
- Congressional Budget Office benefit program estimates
- Treasury expenditure data
- Joint Committee on Taxation tax expenditure estimates
- Healthcare spending patterns
- Other benefit program costs

**Methodology:**
- Combines Current Population Survey (CPS) with IRS Public Use File (PUF)
- Uses quantile regression forests to impute 67 tax variables from PUF onto CPS records
- Applies reweighting algorithm using gradient descent
- Develops loss metric based on differences between survey aggregates and true aggregates

**Key papers:**
- [Enhancing the Current Population Survey for policy analysis](https://blog.policyengine.org/enhancing-the-current-population-survey-for-policy-analysis-9a7d8bf8267)
- [Beta-launch: PolicyEngine's enhanced microdata](https://policyengine.org/us/research/enhanced-cps-beta)
- [Technical documentation](https://policyengine.github.io/policyengine-us-data/)

**Claimed improvement:** "PolicyEngine expects to cut errors by 90% for assessing more targeted policies compared to the raw CPS"

**What this proves:** Aggregate totals match administrative data better than raw CPS
**What this doesn't prove:** Individual policy estimates match CBO/JCT for specific reforms

### 3. UK Validation Against Survey of Personal Incomes

PolicyEngine UK validates against administrative tax data:

- [Validation against the Survey of Personal Incomes](https://policyengine.org/us/research/uk-spi-validation)
- UK Government's evaluation: [HMT: Policy Engine UK](https://www.gov.uk/algorithmic-transparency-records/hmt-modelling-policy-engine)

**UK-specific claim:** "PolicyEngine has launched new survey weights that cut deviations from administrative statistics by 97%"

**Source:** [How machine learning tools make PolicyEngine more accurate](https://policyengine.org/uk/research/how-machine-learning-tools-make-policyengine-more-accurate)

### 4. Behavioral Response Parameters

PolicyEngine implements CBO's methodology for behavioral responses:

**From CBO:**
- Default income elasticity: -0.05 (CBO's central estimate)
- Heterogeneous substitution elasticities that vary by income level
- Captures both income effects and substitution effects

**Source:** [Behavioral Responses in PolicyEngine US](https://blog.policyengine.org/behavioral-responses-in-policyengine-us-18ecb8bf8267) (December 2024)

**What this proves:** Uses same behavioral assumptions as CBO
**What this doesn't prove:** Overall estimates match when all parameters combined

## Third-Party Use Cases

### Niskanen Center Child Tax Credit Analysis (March 2024)

**First external organization to use PolicyEngine's enhanced microdata**

**Report:** [Building a stronger foundation for American families: Options for Child Tax Credit reform](https://www.niskanencenter.org/building-a-stronger-foundation-for-american-families-options-for-child-tax-credit-reform/)

**Key findings using PolicyEngine:**
- Baseline CTC expansion: $109.7 billion cost in 2024, 31.2% child poverty reduction
- 44% of population sees net income gain
- Eliminating head of household filing status: $83.8 billion total cost (saves $26B)
- Eliminating CDCTC: $105.9 billion cost (saves $4B)

**PolicyEngine's summary:** [PolicyEngine Powers Niskanen Center's Analysis](https://www.policyengine.org/us/research/niskanen-center-analysis)

**Note:** This is a use case, not an independent validation. Niskanen Center relied on PolicyEngine's numbers; they did not verify against CBO/JCT estimates.

## Specific Policy Comparisons

### EITC and ACTC Calibration

**GitHub issue:** [Calibrate EITC and ACTC #4276](https://github.com/PolicyEngine/policyengine-us/issues/4276)

**Comparison found:**
- CBO projects EITC payment (where earned income credit exceeds liability for tax): $62.7 billion in 2024
- PolicyEngine ECPS (Enhanced CPS) yields: $68.4 billion total EITC in 2024
  - Includes $39.6B from base CPS
- **Discrepancy:** PolicyEngine ~9% higher than CBO

**What this shows:** PolicyEngine tracks major program totals but with notable differences

### JD Vance's $5,000 Child Tax Credit Proposal

**PolicyEngine analysis:** [Analysis of JD Vance's $5,000 Child Tax Credit Proposal](https://blog.policyengine.org/analysis-of-jd-vances-5-000-child-tax-credit-proposal-6bfde7f7a322)

**Could not find:** CBO or JCT estimate for this specific proposal to compare against

### Romney Child Tax Credit Proposals

Multiple organizations analyzed Romney's proposals, but no direct PolicyEngine vs CBO comparison found:

**Other scorers:**
- Tax Foundation: Romney's proposal analysis
- ITEP (Institute on Taxation and Economic Policy): Multiple analyses
- CBPP (Center on Budget and Policy Priorities): Analysis
- Penn Wharton Budget Model: $283 billion over ten years estimate

**Sources:**
- [Romney Child Allowance & Child Tax Credit Proposal](https://taxfoundation.org/blog/child-allowance-romney-tax-proposal/)
- [ITEP Romney analysis](https://itep.org/romney-child-tax-credit-leaves-many-families-worse-off/)
- [CBPP Romney analysis](https://www.cbpp.org/research/federal-tax/romney-child-tax-credit-proposal-is-step-forward-but-falls-short-targets-low)
- [Penn Wharton analysis](https://budgetmodel.wharton.upenn.edu/issues/2021/3/3/incentive-effects-of-romney-and-biden-neal-child-tax-credit-proposals)

**PolicyEngine did analyze:** [The Child Tax Credit in 2023](https://policyengine.org/us/blog/2023-02-09-the-child-tax-credit-in-2023)

**Gap:** No published comparison showing PolicyEngine estimate vs Penn Wharton/CBO/JCT for the same Romney proposal

## What We Did NOT Find

### Missing Comparisons

1. **No CBO head-to-head comparisons:** No published document comparing PolicyEngine and CBO estimates for the same policy proposal
2. **No JCT comparisons:** No results found for Joint Committee on Taxation vs PolicyEngine
3. **No Tax Policy Center comparisons:** No direct comparison of estimates despite both organizations modeling similar policies
4. **No IFS comparisons:** No comparison between PolicyEngine UK and Institute for Fiscal Studies estimates
5. **No independent academic evaluation:** No third-party papers evaluating PolicyEngine's accuracy against official scorers

### Search Queries That Returned No Results

- `site:policyengine.org CBO estimate comparison`
- `site:policyengine.org validation official estimates accuracy`
- `"PolicyEngine" "one third" revenue estimate household survey` (found the quote but no deeper analysis)
- `"PolicyEngine" third-party independent evaluation review 2023 2024`
- `PolicyEngine UK IFS Institute Fiscal Studies comparison`

## Official Scorer Methodologies (For Context)

### Congressional Budget Office (CBO)

**Revenue baseline:** CBO produces 10-year projection of Federal receipts
**Data sources:** Primarily administrative tax data from IRS
**Advantages:** Captures high-income filers that surveys miss
**Process:** [How CBO and JCT Analyze Major Proposals](https://www.cbo.gov/publication/53571)

**CBO accuracy self-evaluation:**
- "CBO's accuracy improved 3x from 1989-2001 to 2002-2019" {cite}`cbo2024deficit` [NEEDS PROPER CITATION - this came from user's references.bib]
- [An Evaluation of CBO's Projections](https://www.cbo.gov/publication/61067)

### Joint Committee on Taxation (JCT)

**Congressional mandate:** "Revenue estimates provided by the Joint Committee staff will be the official estimates for all tax legislation considered by the Congress" (Congressional Budget Act of 1974)

**Models used:**
- Individual Model (microsimulation)
- Corporate Model (microsimulation)
- Estate and Gift Model (microsimulation)

**Data sources:**
- Primary: IRS Statistics of Income (SOI) division
- Multiple government and non-government sources

**Source:** [Revenue Estimating](https://www.jct.gov/operations/revenue-estimating/)

### Tax Policy Center (TPC)

**Structure:** Joint venture of Urban Institute and Brookings Institution
**Methodology:** [TPC's Methodology for "Off-Model" Revenue Estimates](https://taxpolicycenter.org/resources/tpcs-methodology-model-revenue-estimates)

**No PolicyEngine comparison found**

## Recommendations for the Book

### What You Can Confidently Claim

1. **Technical validation exists:** PolicyEngine validates against NBER TAXSIM within $15 tolerance
2. **Calibration is comprehensive:** 2,813 targets from IRS, CBO, JCT, Treasury data
3. **Improvement trajectory:** Enhanced microdata claims 90% error reduction vs raw CPS
4. **Real-world use:** Niskanen Center and other organizations use PolicyEngine
5. **Behavioral parameters:** Uses CBO's methodology for elasticities
6. **Open and transparent:** All code is open source, methodology is documented

### What Requires Hedging

1. **Revenue estimates:** "Around a third lower than official estimates" due to survey data limitations
2. **No independent validation:** No third-party academic papers evaluating accuracy
3. **No head-to-head comparisons:** No published CBO vs PolicyEngine for same policy
4. **Untested at scale:** Most official scorers use administrative data; PolicyEngine uses enhanced survey data

### Suggested Framing for the Book

**Honest assessment:**
> PolicyEngine represents a new generation of tax-benefit modeling: open source, user-friendly, and rapidly improving. The organization has invested heavily in validation, calibrating to thousands of administrative targets and testing against NBER's TAXSIM model. However, it openly acknowledges that its survey-based estimates run "around a third lower" than official estimates using administrative tax data.
>
> What's missing is the kind of validation that only comes with time: independent academic evaluation and head-to-head comparisons with CBO and JCT estimates for specific policy proposals. When the Niskanen Center used PolicyEngine to model Child Tax Credit reforms, they relied on PolicyEngine's numbers without cross-checking against official scorers.
>
> This doesn't mean PolicyEngine is inaccurate—it means we don't yet know how accurate it is at the task that matters most: predicting the cost and distributional effects of proposed legislation. The tool's transparency is both its greatest strength and a source of scrutiny that proprietary models avoid.

### Questions to Pursue

1. **Why no CBO comparisons?** Is this because:
   - CBO rarely publishes enough detail to replicate?
   - PolicyEngine focuses on different policies than CBO scores?
   - The comparison would be unfavorable?
   - It's simply not a priority yet?

2. **What about prediction vs calibration?** PolicyEngine calibrates to known totals. Can it predict outcomes for novel policies?

3. **How do other open-source models validate?** What does OSPC (Open Source Policy Center) do? What about ITEP?

4. **When will administrative data integration be complete?** The "around a third lower" problem has a stated solution (enhanced microdata). What's the timeline?

### Potential Interviews/Follow-up

- **Max Ghenis:** Ask directly about validation strategy and why no CBO comparisons
- **Niskanen Center researchers:** Why choose PolicyEngine? Did they validate any numbers independently?
- **NBER TAXSIM maintainers:** How do they view PolicyEngine's emulator?
- **Former CBO/JCT staff:** What would convince them PolicyEngine is accurate?

## Key Sources

### PolicyEngine Documentation
- [PolicyEngine US Documentation](https://policyengine.github.io/policyengine-us/)
- [PolicyEngine UK Documentation](https://policyengine.github.io/policyengine-uk/)
- [TAXSIM Validation](https://policyengine.github.io/policyengine-us/validation/taxsim.html)
- [Enhanced Microdata Technical Docs](https://policyengine.github.io/policyengine-us-data/)

### PolicyEngine Research & Blog Posts
- [Enhancing the Current Population Survey](https://blog.policyengine.org/enhancing-the-current-population-survey-for-policy-analysis-9a7d8bf8267)
- [Enhanced CPS Beta Launch](https://policyengine.org/us/research/enhanced-cps-beta)
- [Behavioral Responses in PolicyEngine US](https://blog.policyengine.org/behavioral-responses-in-policyengine-us-18ecb8bf8267)
- [Utah State Income Tax Analysis](https://blog.policyengine.org/introducing-utah-state-income-tax-analysis-on-policyengine-4a1ccc262628)
- [UK Machine Learning for Accuracy](https://policyengine.org/uk/research/how-machine-learning-tools-make-policyengine-more-accurate)
- [UK Validation Against SPI](https://policyengine.org/us/research/uk-spi-validation)

### Third-Party Uses
- [Niskanen Center CTC Report](https://www.niskanencenter.org/building-a-stronger-foundation-for-american-families-options-for-child-tax-credit-reform/)
- [PolicyEngine Powers Niskanen Analysis](https://www.policyengine.org/us/research/niskanen-center-analysis)

### GitHub Resources
- [PolicyEngine US Repository](https://github.com/PolicyEngine/policyengine-us)
- [PolicyEngine TAXSIM Emulator](https://github.com/PolicyEngine/policyengine-taxsim)
- [EITC/ACTC Calibration Issue](https://github.com/PolicyEngine/policyengine-us/issues/4276)

### Official Scorers
- [CBO Cost Estimates](https://www.cbo.gov/cost-estimates)
- [CBO Evaluation of Projections](https://www.cbo.gov/publication/60664)
- [JCT Revenue Estimating](https://www.jct.gov/operations/revenue-estimating/)
- [Tax Policy Center](https://taxpolicycenter.org/)
- [TPC Methodology](https://taxpolicycenter.org/resources/tpcs-methodology-model-revenue-estimates)
- [Institute for Fiscal Studies](https://ifs.org.uk/)

### UK Government Evaluation
- [HMT: Policy Engine UK - Algorithmic Transparency](https://www.gov.uk/algorithmic-transparency-records/hmt-modelling-policy-engine)

### Related Tools & Models
- [NBER TAXSIM](https://www.nber.org/research/data/taxsim)
- [ITEP Tax Model](https://itep.org/itep-tax-model/)
- [Open Source Policy Center TaxModels](https://www.ospc.org/taxmodels/)

### Romney CTC Analysis (Multiple Sources)
- [Tax Foundation Romney Analysis](https://taxfoundation.org/blog/child-allowance-romney-tax-proposal/)
- [CBPP Romney Analysis](https://www.cbpp.org/research/federal-tax/romney-child-tax-credit-proposal-is-step-forward-but-falls-short-targets-low)
- [ITEP Romney Analysis](https://itep.org/romney-child-tax-credit-leaves-many-families-worse-off/)
- [Penn Wharton Romney Analysis](https://budgetmodel.wharton.upenn.edu/issues/2021/3/3/incentive-effects-of-romney-and-biden-neal-child-tax-credit-proposals)
- [Niskanen Romney vs Rubio Comparison](https://www.niskanencenter.org/comparing-rubio-and-romneys-plans/)

## Conclusion

PolicyEngine has built impressive validation infrastructure, but **lacks the gold standard: independent third-party evaluation and head-to-head comparisons with CBO/JCT for specific legislative proposals.**

For the book, this creates an honest story: a promising new tool with transparent methodology and real-world adoption, but not yet proven against the established scorers that Congress relies on. The "around a third lower" revenue estimate issue is particularly important to address directly.

The validation gap is not necessarily a criticism—it may simply reflect PolicyEngine's youth and different use case (public education vs congressional scoring). But for "Society in Silico" to maintain credibility, it must acknowledge what we know and what we don't know about PolicyEngine's accuracy.

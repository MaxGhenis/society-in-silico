# Policy Modeling Landscape 2019-2021

## Overview

This document chronicles the state of microsimulation and policy modeling tools during 2019-2021, the period immediately preceding and during PolicyEngine's founding. This context reveals the ecosystem that PolicyEngine entered: which tools researchers were using, what gaps existed, and what the state of the art looked like.

## Key Developments Timeline

### 2019

**OpenFisca International Expansion**
- Recognized as most innovative open source software by European Commission through Joinup program {cite}`openfisca_about`
- 11 countries and cities using OpenFisca by October 2019: Mali, New Zealand, Senegal, Tunisia, Uruguay, Barcelona, Ivory Coast, France, Italy, Israel, and Australia
- Aotearoa New Zealand's OpenFisca implementation active following Better Rules initiative (2018), with Rates Rebate app as first production service outside Europe

**UK Microsimulation: UKMOD Launch**
- UKMOD first released in September 2019, funded by Nuffield Foundation (2018-2021 project) {cite}`ukmod_iser_blog`
- Addressed major gap: UK had multiple proprietary models (IFS TAXBEN, HM Treasury IGOTM, DWP PSM) but none freely available
- UKMOD based on EUROMOD's UK component, enhanced and extended for wider accessibility {cite}`ukmod_ijm`
- Training courses held (October 2019 documented)

**TAXSIM Evolution**
- Federal law coverage: 1960-2023; State laws: 1977-2018 available
- Used in academic research extensively; ~20,000 lines of FORTRAN 77

**Policy Simulation Library Activity**
- Tax-Calculator active development, updating parameters for 2019-2021 policy years
- TaxBrain web interface operational at apps.ospc.org, providing accessible interface to Tax-Calculator
- AEI's Open Source Policy Center hosting PSL Demo Days and meetings

**France: TAXIPP**
- IPP's TAXIPP microsimulation model actively maintained by permanent team at Paris School of Economics
- October 2019: IPP published analysis on capital income tax reforms using TAXIPP

**Australia**
- NATSEM at University of Canberra continuing microsimulation research tradition
- ANU's PolicyMod active for analyzing Australian tax and transfer system

### 2020

**COVID-19 Transforms Policy Analysis Landscape**
- Microsimulation models urgently needed to analyze pandemic relief policies
- International Microsimulation Association held online conference on "Microsimulation modelling of policy responses to COVID-19" (December 2, 2020) {cite}`ima_covid_conference`
- Special issue of International Journal of Microsimulation dedicated to COVID policy analysis

**TAXSIM35 Launch**
- Implements Tax Cuts and Jobs Act (TCJA) pass-through provisions
- Implements temporary CARES Act provisions for 2020 and 2021 {cite}`taxsim_nber`
- New variables added for business tax deduction, recovery rebate credit, FICA adjustments
- Compatible with TAXSIM27 and TAXSIM32 input files
- Accessible from Stata, SAS, R, and Python

**Tax-Calculator COVID Updates**
- Current law baseline updated to include CARES Act
- Later updated for Consolidated Appropriations Act of 2021 and American Rescue Plan Act
- Updates to EITC, CTC parameters for 2021

**EUROMOD Transition to Full JRC Control**
- December 2020: EUROMOD becomes fully open source (previously "open access")
- Transition from University of Essex to sole JRC European Commission management finalized end of 2020
- January 2021: JRC assumes sole responsibility for development, management, maintenance {cite}`euromod_jrc`

**OpenFisca-UK Development Begins**
- Nikhil Woodruff creates OpenFisca-UK repository
- November 2020: Initial releases (versions 0.1.0, 0.2.1) {cite}`openfisca_uk_changelog`
- Used Family Resources Survey 2019-2020 as data source
- Research application: UBI Center analysis of personal allowance elimination

**Policy Simulation Library Infrastructure**
- PSL Demo Day webinars begin (end of 2020)
- Behavioral-Responses package (version 0.11.0, September 2020) for estimating behavioral responses to tax changes
- COMPUTE Studio platform hosting PSL model web applications
- Models sharing transparency standards and interoperability criteria

**Field-Wide Challenges Identified**
- Dynamic microsimulation survey paper identifies reliance on "oral tradition" limiting knowledge transfer {cite}`ijm_dynamic_survey`
- Behavioral modeling remains challenging: structural labor supply models demanding, no consensus on design
- Validation concerns: "little published work on the validity of microsimulation models"
- Complexity vs. interpretability trade-offs recognized

### 2021

**PolicyEngine Founded**
- Founded by Max Ghenis and Nikhil Woodruff, spun out of UBI Center {cite}`psl_2021_review`
- September 2021: PolicyEngine UK announced
- Built on OpenFisca fork
- "Members of civil society started modelling British and then USA legislation" {cite}`openfisca_about`
- Joined Policy Simulation Library catalog

**OpenFisca-UK Continued Development**
- Multiple releases through 2021
- OpenFisca-UK-Data package released with microdata preparation tools
- Tests updated to use FY20-21 parameters

**EUROMOD I4.0+ Release**
- Policy years simulated: 2018-2021 for all countries {cite}`euromod_i40`
- Updated COVID-19 related policies
- Experimental labour market transitions for 2020-2021
- New EUROMOD input data for 2019 (income reference year: 2018)
- EUROMOD used to estimate distributional effects of policy changes implemented in 2019-2020 in EU countries and UK

**Policy Simulation Library Expansion**
- Capital Cost Recovery model (R) joins PSL
- DSGE model (Julia) joins PSL
- Federal-State Tax Project added (data imputation tools for state tax data)
- OG-USA overlapping-generations model joins catalog
- July 2021: IPP France published housing benefits analysis using TAXIPP

**Tax-Calculator v3.2.1**
- Released August 6, 2021
- Bug fixes for CTC_new_c_under6_bonus and EITC_c values
- Full release history maintained at taxcalc.pslmodels.org

**COVID Policy Analysis Papers**
- Child Tax Credit expansion research (2021 expansion analysis)
- Unemployment insurance simulations
- Multiple microsimulation papers analyzing CARES Act, American Rescue Plan impacts

## Gaps and Limitations in 2019-2021

### Accessibility Barriers

**TAXSIM**
- Free to use but requires technical expertise
- Batch processing model, not interactive
- FORTRAN codebase limits modern integration
- No web-based interactive interface for public use

**IFS TAXBEN**
- Proprietary, unavailable outside IFS
- First version 1983, long-established UK standard
- Used for authoritative UK budget analysis but not reproducible by external researchers

**Other UK Models**
- HM Treasury IGOTM: Internal government use only
- DWP PSM: Department-specific, not public
- IPPr-commissioned model: Limited availability
- Gap: No open-source UK model until UKMOD (2019)

**Tax-Calculator/PSL**
- Strong technical capabilities but steep learning curve
- Python programming required for custom analyses
- Web interfaces (TaxBrain, COMPUTE Studio) simplified access but limited customization
- US-focused; no UK or other country implementations

**EUROMOD**
- Open access but not open source until December 2020
- Academic/institutional focus, not public-facing
- Coverage: EU countries plus UK, not other major economies
- Requires substantial technical expertise

### Technical Limitations

**Validation and Reproducibility**
- "Little published work on the validity of microsimulation models" {cite}`microsim_policy_eval`
- Proprietary models prevent external validation
- "Oral tradition" in dynamic microsimulation limits knowledge transfer
- No consensus on behavioral response modeling approaches

**Behavioral Modeling**
- Most tax-benefit calculations "non-behavioral" due to complexity
- Establishing structural models "demanding with respect to finding suitable data"
- No clear consensus on labor supply model design
- Trade-off between complexity and interpretability

**User Interface**
- Most models require command-line or programming interface
- Limited web-based interactive tools
- Gap between researcher capabilities and policymaker/public needs
- COMPUTE Studio and TaxBrain provided web access but limited to specific PSL models

**Geographic Coverage**
- US: TAXSIM, Tax-Calculator mature
- France: TAXIPP operational
- UK: Multiple proprietary models, UKMOD newly launched (2019)
- Australia: PolicyMod, NATSEM models
- New Zealand: OpenFisca-Aotearoa
- Major gap: Many countries lacked open-source microsimulation tools

## State of the Art in 2021

### Technical Capabilities

**Microsimulation Engines**
- MODGEN: Established dynamic microsimulation platform
- LIAM2: Open-source dynamic microsimulation (De Menten et al., 2014)
- JASMINE: Modular simulation framework
- neworder: Emerging framework (Smith, 2021)
- OpenFisca: Rules-as-code approach, modular design

**Programming Languages**
- Python dominant in new tools (Tax-Calculator, OpenFisca, PolicyEngine)
- R for statistical analysis and some models (Capital Cost Recovery)
- Julia for macroeconomic models (DSGE)
- Legacy FORTRAN still in use (TAXSIM)

**Performance Improvements**
- Run-time "much faster" than earlier amateur frameworks
- Vectorized computation becoming standard
- Better programming in generalized frameworks

**Data Infrastructure**
- US: CPS, IRS-SOI Public Use File
- UK: Family Resources Survey, Understanding Society
- EU: EUROMOD SILC database (EMSD) from Eurostat
- Improved uprating factors and nowcasting techniques

### Research Applications (2019-2021)

**COVID-19 Policy Analysis**
- CARES Act distributional analysis
- Unemployment insurance expansion impacts
- Recovery rebate credit (stimulus checks) analysis
- Child Tax Credit expansion projections

**Tax Reform Studies**
- TCJA implementation and effects
- State tax policy interactions
- Behavioral responses to marginal rate changes
- Capital income taxation (IPP France, 2019)

**Validation Studies**
- Model projections validated against 2011-2019 observed data
- Cross-validation approaches for predictive models
- Sequence analysis and trajectory methods for validation

### Institutional Landscape

**Academic Institutions**
- NBER (TAXSIM)
- IFS (TAXBEN)
- JRC European Commission (EUROMOD)
- ANU Centre for Social Research & Methods (PolicyMod)
- Paris School of Economics/IPP (TAXIPP)
- University of Canberra NATSEM

**Policy Organizations**
- Policy Simulation Library (PSLmodels)
- Open Source Policy Center at AEI
- UBI Center (incubating PolicyEngine)
- International Microsimulation Association

**Government Integration**
- New Zealand: Rules-as-code pilot programs
- HM Treasury, DWP: Internal UK models
- US: CBO, JCT use of academic models
- France: IPP advising on tax policy

## Implications for PolicyEngine

### Market Gaps PolicyEngine Could Address

1. **UK Open-Source Model**: UKMOD launched 2019 but PolicyEngine offered more accessible interface
2. **Web-Based Accessibility**: Gap between technical models and public/policymaker usability
3. **International Expansion**: OpenFisca architecture proven for multi-country implementation
4. **Real-Time Policy Analysis**: Interactive tools lacking for immediate reform feedback
5. **Transparency**: Proprietary models dominant despite reproducibility concerns

### Ecosystem PolicyEngine Built Upon

1. **OpenFisca Framework**: Proven rules-as-code approach, modular design
2. **PSL Standards**: Transparency and interoperability criteria
3. **Open Data**: Family Resources Survey (UK), CPS (US) publicly available
4. **Python Ecosystem**: Modern tooling, scientific computing libraries
5. **COVID Policy Urgency**: Demonstrated need for accessible policy analysis tools

### Competitive Landscape

**UK Models (2021)**
- TAXBEN: Authoritative but proprietary
- UKMOD: Free, open-access, academic-focused
- PolicyEngine: Open-source, web interface, public-facing

**US Models (2021)**
- TAXSIM: Established, free, technical interface
- Tax-Calculator: Open-source, PSL standards, requires programming
- PolicyEngine US: (Launched 2022) Web-based, interactive

**Differentiation**
- User interface: Web-based, no programming required
- Speed: Instant results for individual households
- Accessibility: Public-facing, not just researchers
- Integration: API for external applications
- Transparency: Fully open-source, reproducible

## Research Questions This Period Raised

1. How to validate microsimulation models without administrative data access?
2. Can web interfaces make sophisticated models accessible without sacrificing rigor?
3. What's the optimal trade-off between model complexity and interpretability?
4. How to model behavioral responses when structural approaches are demanding?
5. Can open-source models compete with established proprietary tools for policy influence?
6. How to maintain models as policy changes rapidly (COVID demonstrated challenge)?

## Key Takeaways

The 2019-2021 period represented a critical transition:

1. **COVID-19 Catalyst**: Pandemic created urgent need for rapid policy analysis tools
2. **Open Source Momentum**: EUROMOD went fully open source (2020); UKMOD launched (2019)
3. **Accessibility Gap**: Technical capabilities advanced but user interfaces lagged
4. **International Expansion**: OpenFisca proven in multiple countries, creating template
5. **Validation Concerns**: Field recognized reproducibility and validation challenges
6. **PSL Maturation**: Policy Simulation Library standards enabled interoperability

PolicyEngine emerged in this context as:
- **Modern architecture**: Python, web-based, OpenFisca framework
- **Accessibility-focused**: Bridging gap between technical models and public usability
- **International from start**: UK and US models, expandable architecture
- **Open and transparent**: Addressing reproducibility concerns
- **Policy-responsive**: Rapid updates for COVID and other policy changes

The landscape revealed both opportunity (gaps in accessibility, open-source UK tools) and infrastructure (OpenFisca, PSL standards, open data) that enabled PolicyEngine's development.

## References

See `references.bib` for full citations. Key sources include:

- NBER TAXSIM documentation and updates
- OpenFisca About page and country implementations
- UKMOD launch announcements and documentation
- EUROMOD JRC transition documentation
- Policy Simulation Library blog and catalog
- International Journal of Microsimulation papers
- IPP TAXIPP documentation

## Related Research Notes

- [[policyengine]]
- [[openfisca]]
- [[taxsim]]
- [[ifs-taxben]]
- [[nikhil-woodruff]]
- [[max-ghenis]]
- [[policy-simulation-library]]
- [[microsimulation-validation]]

## Tags

#research #timeline #policy-modeling #microsimulation #landscape-analysis #2019-2021

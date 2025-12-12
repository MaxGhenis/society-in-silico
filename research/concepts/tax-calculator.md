# Tax-Calculator

**Institution**: AEI Open Source Policy Center → Policy Simulation Library (PSL)
**Type**: Open-source microsimulation model
**Language**: Python
**Focus**: US federal individual income and payroll tax

## What It Is

Tax-Calculator is a microsimulation model for estimating aggregate revenue and distributional effects of US tax reforms. It takes individual tax return data and calculates how policy changes would affect tax liabilities.

## Significance to This Story

Tax-Calculator was [[max-ghenis]]'s gateway into open-source policy simulation:

> "Wanted to test UBI and CTC ideas quantitatively. Didn't want to leave Google immediately for a think tank. Found AEI's Tax-Calculator project. Started using it, then contributing to it."

The discovery that **policy simulation could be open source** was transformative—it showed an alternative to closed institutional models like [[ifs-taxben]].

## History

### Open Source Policy Center (OSPC)
- Housed at American Enterprise Institute (AEI)
- Created Tax-Calculator as open-source alternative to proprietary models
- Built ecosystem: Tax-Data, Tax-Calculator, Behavior-Response, Tax-Brain, Tax-Cruncher

### Policy Simulation Library (PSL)
- Tax-Calculator joined the PSL Catalog
- PSL hosts monthly meetings for open-source policy modelers
- Broader ecosystem of open policy tools

## Technical Approach

- Uses IRS Public Use File and Current Population Survey data
- Applies tax rules to individual records
- Aggregates to estimate revenue and distributional impacts
- Python-based, allowing integration with other tools

## Key Users

> "Tax-Calculator has supported many prominent users, including administrations from both parties, lawmakers, newspapers, and academic researchers."

Examples:
- Alex Brill (AEI): Analyzed Biden's American Rescue Plan
- Erin Melly (AEI): TCJA distributional visualizations
- Academic researchers: Behavioral response modeling

## Max's Contributions (2018)

During the "three months off" from Google:
- Contributed to imputation of CPS variables to IRS data
- Produced synthetic releasable version of IRS Public Use File
- Conducted distributional analysis of EITC, CTC, UBI
- Built `microdf` Python library for weighted survey analysis

## Relationship to PolicyEngine

Tax-Calculator demonstrated the viability of open-source tax modeling. [[policyengine]] extended this approach:
- Added benefit programs (not just taxes)
- Built web interface for non-programmers
- Expanded to UK and other countries
- Enhanced microdata using ML

The progression: Tax-Calculator (taxes only, US, Python API) → PolicyEngine (taxes + benefits, US + UK, web app + API).

## The Open Source Difference

Why this mattered:

| Traditional | Open Source (Tax-Calculator) |
|-------------|------------------------------|
| Proprietary code | Public GitHub repo |
| Black box | Auditable calculations |
| Institutional access | Anyone can use |
| Wait for updates | Contribute improvements |

This model proved that serious policy analysis didn't require institutional gatekeeping.

## Sources

- [OSPC](https://www.ospc.org/)
- [AEI Tax-Calculator events](https://www.aei.org/tag/tax-calculator/)
- [PSL](https://www.pslmodels.org/)

## Links

- [[max-ghenis]]
- [[policyengine]]
- [[taxsim]]
- [[microsimulation-definition]]

## Tags

#concept #tool #opensource #pivotal

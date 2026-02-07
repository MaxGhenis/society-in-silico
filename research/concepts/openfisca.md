---
chapters: [1, 2, 3, 5, 10, 15]
primary_chapter: 3
narrative_role: "Government-backed open-source framework for encoding tax-benefit rules as executable code"
---

# OpenFisca

**Founded**: May 2011
**Origin**: France Centre d'analyse stratégique (now France Stratégie)
**Type**: Open source digital common
**License**: GNU Affero General Public License v3

## What It Is

> "Turn legislation into code."

OpenFisca is a framework for encoding tax and benefit rules as machine-readable code. Provide a situation (income, family structure), ask for a calculation (tax liability, benefit eligibility), get results.

## Creators

**Mahdi Ben Jelloul** (PhD, public economist) and **Clément Schaff** at France's Centre d'analyse stratégique (CAS). Ben Jelloul later affiliated with Institut des politiques publiques (IPP) and Paris School of Economics.

## History

### Prehistory: The Piketty-Saez-Landais Simulator
- January 2011: Landais, Piketty, and Saez publish *Pour une révolution fiscale* with revolution-fiscale.fr
- Interactive tax simulator letting citizens design their own reforms
- 500,000+ visitors; demonstrated public appetite for open policy tools
- The underlying model (TAXIPP v0.0) later evolved into IPP's TAXIPP model
- Direct lineage: revolution-fiscale.fr → TAXIPP → integration with OpenFisca

### 2011: Origins
- Development began May 2011 at Centre d'analyse stratégique
- Support from Institut d'économie publique (IDEP, Aix-Marseille)
- Source code released November 2011 under GNU AGPL v3

### 2014: Etalab Restructuring
- Etalab (French PM's open data task force) restructured codebase
- Discontinued Qt desktop version, separated engine from interface
- Introduced Web API
- **Mes Aides** simulator launched (citizen-facing benefits calculator)

### 2016: International Breakthrough
- OGP Paris Summit demonstration
- Team of French and Tunisian volunteers modeled Senegal's income tax in under 36 hours
- Won first prize at OGP hackathon
- Proved international applicability

### 2017: Internationalization
- New contributors from Italy and Barcelona
- Documentation rewrite, launch of openfisca.org

### 2018: New Zealand
- Matti Schneider (OpenFisca internationalization lead) moved to New Zealand
- Service Innovation Lab built **Rapu Ture** (Rates Rebate Act as code)
- First production service outside Europe
- 170,000+ people using NZ platform

### 2019: Recognition and LexImpact
- Named most innovative open source software by European Commission (Joinup program)
- French National Assembly created **LexImpact** on top of OpenFisca
- MPs can simulate effects of amendments on income tax, local authority allocations, social security
- 122 legislative simulations in parliamentary debates by 2021

### 2022: Scale
- Nearly 700,000 simulations on "1 jeune 1 solution" platform
- 2,300 young people using daily in France

### 2023: World Government Summit
- Won **Edge of Government Innovation Award** at World Government Summit in Dubai
- Distinguished among 1,000+ candidates screened by OECD

## Global Adoption

Countries/regions using OpenFisca (per official packages page):
- France (FR) — original
- United Kingdom (GB) — via PolicyEngine
- United States (US) — via PolicyEngine
- New Zealand (NZ) — Rapu Ture, Rates Rebate app
- Tunisia (TN)
- Senegal (SN)
- Barcelona (ES-B) — "Les meves ajudes" benefits eligibility tool
- Italy (IT)
- Japan (JP) — "Support Estimator" by Institute for Poverty Prevention
- New South Wales/Australia (AU-NSW) — first machine-readable regulation
- Côte d'Ivoire (CI)
- Mali (ML)
- Uruguay (UY)
- Canada

## Technical Approach

- Rules encoded as Python
- Parametric: values (thresholds, rates) separate from logic
- Temporal: rules vary by date
- Vectorized: can process millions of households efficiently

## Governance

> "OpenFisca is a digital common: it is free and open source software designed, developed and used by many people around the world through democratic, horizontal governance processes such as Requests For Comments (RFCs) and open discussions."

## Relationship to PolicyEngine

[[policyengine]] forked OpenFisca-Core to create policyengine-core, adding:
- Performance optimizations
- Better microsimulation support
- Enhanced API
- Web application layer

## Appears in Manuscript

**Chapter 2 (Tax Model Wars)**
- Section: "Open Source Emergence" (line 73)
- Coverage: Brief mention alongside Tax-Calculator as examples of open-source revolution
- Details: Named as government-released source code for tax-benefit calculator

**Chapter 3 (Open Source Revolution)** - PRIMARY
- Section: Opening (lines 3-9)
- Coverage: Founding story (May 2011, France Stratégie), premise, and significance
- Section: "Two Architectures, One Vision" (lines 59-71)
- Coverage: Detailed comparison with Tax-Calculator
  - Architecture: Unified framework approach
  - Global deployment: France (Mes Aides), New Zealand, Tunisia, Senegal, Australia, Canada
  - Recognition: OECD Innovation of Year, EU Joinup program
  - Vs Tax-Calculator: government backing vs independence, unified vs federation

## Book Narrative Notes

OpenFisca represents the "rules as code" movement—the idea that legislation should exist in both human-readable and machine-readable form. Its French government origins give it legitimacy; its open-source nature enables global adoption.

The 36-hour Senegal demonstration is a great story: showing that tax code is more similar across countries than different.

## Sources

- [OpenFisca.org](https://openfisca.org/en/)
- [GitHub](https://github.com/openfisca)
- [EU recognition](https://interoperable-europe.ec.europa.eu/collection/egovernment/document/france-opens-source-code-tax-and-benefits-calculators-increase-transparency)

## Links

- [[policyengine]]
- [[rules-as-code]]
- [[microsimulation-definition]]

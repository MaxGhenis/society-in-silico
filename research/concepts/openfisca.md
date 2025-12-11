# OpenFisca

**Founded**: May 2011
**Origin**: France Centre d'analyse stratégique (now France Stratégie)
**Type**: Open source digital common
**License**: GNU Affero General Public License v3

## What It Is

> "Turn legislation into code."

OpenFisca is a framework for encoding tax and benefit rules as machine-readable code. Provide a situation (income, family structure), ask for a calculation (tax liability, benefit eligibility), get results.

## History

### 2011: Origins
- Development began at Centre d'analyse stratégique
- Support from Institut d'économie publique (IDEP, Aix-Marseille)

### Early Development
- Core improved by Etalab (French government open data agency)
- French model developed by CGSP with IDEP and Institut des politiques publiques (IPP)

### First Applications
- **Mes Aides**: Citizen-facing benefits assessment tool
- Payroll simulator
- French State Startups incubator adoption

### 2016: International Breakthrough
- OGP Paris Summit demonstration
- Team modeled Senegal's income tax in under 36 hours
- Proved international applicability

### 2019: Recognition
- Named most innovative open source software by European Commission (Joinup program)

## Global Adoption

Countries/regions using OpenFisca:
- France (original)
- Tunisia
- New Zealand (Rates Rebate app—first production service outside Europe)
- Australia
- Polynesia
- Canada
- UK (via PolicyEngine fork)
- US (via PolicyEngine fork)
- Senegal
- Barcelona

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

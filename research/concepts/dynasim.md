# DYNASIM

**Institution**: Urban Institute
**Director**: Guy Orcutt
**Development**: 1969-1975 (first version)
**Language**: FORTRAN (MASH system on DEC-10)

## What It Was

DYNASIM (Dynamic Simulation of Income Model) was the first large-scale implementation of [[guy-orcutt]]'s microsimulation vision. A longitudinal model that simulated life events for individuals over time.

## Technical Specifications

- **Sample**: 10,000 person dataset
- **Type**: Longitudinal closed model
- **Software**: Microanalytic Simulation of Households (MASH) system
- **Platform**: DEC system-10

## Modules

### Demographic Module
- Leaving home
- Births
- Deaths
- Partnership formation and dissolution
- Disability
- Education
- Location

### Labor Market Module
- Labor force participation
- Hours worked
- Unemployment
- Labor income

### Tax-Transfer and Wealth Module
- Capital income
- Main tax and transfer instruments
- Simple macroeconomic model
- Feedback loops

## Timeline

- **1957**: Orcutt publishes conceptual paper
- **1961**: Prototype microsimulation model developed
- **1969**: Work begins on DYNASIM at Urban Institute
- **1975**: First version completed

## Legacy

DYNASIM spawned:
- **CORSIM**: Direct descendant
- **CANSIM**: Canadian adaptation
- **SVERIGE**: Swedish adaptation

> "While the field of microsimulation has progressed greatly in many aspects since the original paper of Orcutt, the rate of progress in dynamic microsimulation is arguably slow given that we still share the same model design and face similar problems as early DYNASIM modellers did nearly 40 years ago."

## The Ambition

DYNASIM attempted to simulate "all major demographic and economic life events":
- Birth, death
- Marriage, remarriage
- Unemployment, migration

This comprehensive ambition—modeling whole lives—required enormous computing resources for the era.

## State of the Art (1975)

The MASH software was considered cutting-edge:
- Interactive operation
- Extensive command language
- Researcher collaboration features

## Book Narrative Notes

DYNASIM is the "big bang" of microsimulation implementation. The gap between Orcutt's 1957 paper and the 1975 working model shows how far ahead of technology the vision was.

The continuity from DYNASIM to modern models (similar design, similar problems) is both remarkable and sobering—we're still working on the same fundamental challenges.

## Sources

- [SOA DYNASIM Chapter](https://www.soa.org/493824/globalassets/assets/files/research/projects/chapter_3.pdf)
- [Survey of dynamic microsimulation](https://microsimulation.pub/articles/00082)
- [National Academies report](https://nap.nationalacademies.org/read/1835/chapter/9)

## Links

- [[guy-orcutt]]
- [[microsimulation-definition]]

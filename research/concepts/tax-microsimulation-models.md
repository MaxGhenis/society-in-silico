# Tax Microsimulation Models: Key Players and History

Research note for Chapter 2: "The Tax Model Wars"

## US Federal Models

### Treasury Office of Tax Analysis (OTA)

- **Model**: Individual Income Tax Model (ITM)
- **Origins**: George Sadowsky introduced computerized revenue estimation 1962-1965
- **Current state**: ITM based on 2019 tax year data; documented in Technical Paper 12 (2023)
- **Data**: SOI tax returns
- **Purpose**: Revenue estimates, distributional analysis for Administration proposals
- **Notable**: Robert Gillette leads current documentation efforts

**Sources**:
- [OTA Overview](https://home.treasury.gov/about/tax-policy/office-of-tax-analysis)
- [OTA Technical Papers](https://home.treasury.gov/ota-technical-papers)
- {cite}`sadowsky1991computing`

### Congressional Budget Office (CBO)

- **Model**: CBO Microsimulation Tax Model
- **Long-term model**: CBOLT (Congressional Budget Office Long-Term)
- **Data**: Statistics of Income (SOI) Public Use Tax File
- **Notable features**:
  - CBOLT projects individual earnings over lifetimes
  - Models marriage transitions, labor force participation, Social Security claiming
- **Early documentation**: Technical papers from 2002-2004

**Sources**:
- [CBO Tax Model Overview (2018)](https://www.cbo.gov/publication/54096)
- [CBOLT Working Paper](https://www.cbo.gov/publication/44306)

### Joint Committee on Taxation (JCT)

- **Models**: Individual Model, Corporate Model, International Cross Border Model, Estate and Gift Model
- **History**: JCT created 1926; first Chief of Staff L.H. Parker
- **Authority**: Budget Act of 1974 made JCT official estimates for Congress
- **Behavioral responses**: Incorporated for 25+ years
- **Dynamic scoring**: Required since House Rule 13 (2003)
- **Data**: SOI from IRS

**Sources**:
- [JCT Revenue Estimating](https://www.jct.gov/operations/revenue-estimating/)
- [JCT History](https://www.jct.gov/about-us/history/)

## US Non-Government Models

### NBER TAXSIM

- **Creator**: Daniel Feenberg (Princeton PhD 1980)
- **Institution**: National Bureau of Economic Research
- **History**: Feenberg has maintained TAXSIM his entire career at NBER
- **Coverage**: Federal 1960-2023, State 1977-2018
- **Notable**: Open access, internet-based since early days
- **Documentation**: Feenberg & Coutts (1993), "An introduction to the TAXSIM model"

**Sources**:
- [NBER TAXSIM](https://www.nber.org/research/data/taxsim)
- [Daniel Feenberg profile](https://www.nber.org/people/daniel_feenberg)

### Urban-Brookings Tax Policy Center (TPC)

- **Institutions**: Urban Institute + Brookings Institution (joint project)
- **Key researchers**: Karen Smith (senior fellow, 30+ years microsimulation), Gordon Mermin
- **Scope**: Federal and state personal income tax
- **Similarity**: "Similar to those used by CBO, JCT, and Treasury OTA"

**Sources**:
- [TPC Microsimulation Model](https://www.urban.org/research/publication/urban-brookings-tax-policy-center-microsimulation-model)
- [TPC Model FAQ](https://taxpolicycenter.org/resources/tpcs-microsimulation-model-faq)

### Penn Wharton Budget Model (PWBM)

- **Founder**: Kent Smetters (former CBO economist 1995-1999, former Treasury deputy assistant secretary 2001)
- **Founded**: ~2014 ("a decade ago" as of 2024)
- **Model components**: Microsimulation + Tax Module + Social Security Module + Dynamic OLG
- **Variables**: Projects 60+ demographic and economic variables
- **Notable**: Combines microsimulation with macroeconomic modeling
- **Validation**: Known for accurate forecasting

**Sources**:
- [PWBM Microsimulation](https://budgetmodel.wharton.upenn.edu/microsim)
- [Kent Smetters bio](https://en.wikipedia.org/wiki/Kent_Smetters)
- [Arnold Ventures profile](https://www.arnoldventures.org/stories/how-a-small-think-tanks-mathematical-models-are-shaping-modern-politics)

### Institute on Taxation and Economic Policy (ITEP)

- **Founded**: 1996
- **Data**: 750,000 actual federal tax returns
- **Unique features**:
  - Only model doing race/ethnicity disaggregation at state level
  - Comprehensive: income, consumption, property taxes
  - All 50 states + local jurisdictions
- **Notable work**: "Who Pays?" reports on state tax systems

**Sources**:
- [ITEP Tax Model Overview](https://itep.org/itep-tax-model/)
- [ITEP Model Technical Documentation](https://itep.sfo2.digitaloceanspaces.com/OverviewITEPModel.pdf)

## State-Level Models

Most states lack capacity for own microsimulation models:

- **California, New York**: Maintain own models
- **Minnesota Department of Revenue**: Has own model
- **Most states**: Rely on ITEP or less detailed methods

**Source**: [ITEP overview](https://itep.org/itep-tax-model/)

## International Models

### UK Models

The UK has a particularly rich ecosystem of tax-benefit models, which is relevant since PolicyEngine operates there.

#### Institute for Fiscal Studies (IFS) TAXBEN

- **Institution**: Institute for Fiscal Studies (founded 1969)
- **Model start**: 1983
- **Data**: Family Expenditure Survey (now Living Costs and Food Survey)
- **Sample**: ~7,000 UK households
- **Key documentation**: Giles & McCrae (1995), Waters (2017)
- **Purpose**: Budget analysis, distributional impact
- **Notable**: Howard Reed had primary responsibility for TAXBEN 2000-2004

**Sources**:
- [TAXBEN documentation](https://ifs.org.uk/publications/taxben-ifs-tax-and-benefit-microsimulation-model)
- [IFS History](https://ifs.org.uk/about/history-ifs)

#### UKMOD (University of Essex)

- **Institution**: Centre for Microsimulation and Policy Analysis (CeMPA), University of Essex
- **Project lead**: Professor Mike Brewer
- **Key developers**: Mike Brewer, Kakia Chatsiou, Paola De Agostini, Chrysa Leventi, Sara Reis, Holly Sutherland, Iva Tasseva
- **Genesis**: 2018, funded by Nuffield Foundation
- **History**: 20+ years of development; spin-off from UK component of EUROMOD
- **Key feature**: Separate policy systems for England, Scotland, Wales, Northern Ireland
- **Access**: Free, open-source
- **Updates**: Twice yearly (Spring/Autumn)
- **Notable users**: Scottish Parliament (SPICe), NHS Health Scotland, Welsh Government

**Sources**:
- [UKMOD Home](https://www.microsimulation.ac.uk/ukmod/)
- [UKMOD History](https://www.microsimulation.ac.uk/ukmod/history/)
- [UKMOD paper in IJM](https://microsimulation.pub/articles/00231)

#### Landman Economics Tax-Transfer Model (TTM)

- **Creator**: Howard Reed (founder of Landman Economics, 2008)
- **Background**: Reed was Chief Economist at IPPR 2004-2008, responsible for IFS TAXBEN 2000-2004
- **Original version**: Written 2008-09 for IPPR and Resolution Foundation
- **Data**: Family Resources Survey (FRS), UKHLS, Living Costs and Food Survey (LCF)
- **Notable applications**: Universal Basic Income modelling, cumulative impact assessments of welfare reforms
- **Clients**: Scottish Government, Welsh Government, Equality and Human Rights Commission
- **Funding**: £2 million+ from public/third sector bodies

**Sources**:
- [Landman Economics Research](http://www.landman-economics.co.uk/research/)
- [Howard Reed profile](https://www.northumbria.ac.uk/about-us/our-staff/r/howard-reed/)

#### IPPR/PERU Tax-Benefit Model

- **Institution**: IPPR (Institute for Public Policy Research, founded 1988)
- **Maintainer**: PERU (Policy Evaluation and Research Unit) at Manchester Metropolitan University
- **Key figure**: Ashwin Kumar (Director of Research & Policy at IPPR, Professor at MMU)
- **Users**: IPPR, Resolution Foundation, Joseph Rowntree Foundation, New Economics Foundation, Legatum Institute
- **Data**: Family Resources Survey
- **Access**: Licensed for hefty fee; structural changes require commissioning PERU
- **Limitations**: No public documentation of assumptions or macro-validation

**Sources**:
- [IPPR Model at MMU PERU](https://mmuperu.co.uk/modelling-the-effects-of-the-tax-and-benefit-system/)

#### Scotland-Specific Models

- **UKMOD Scotland component**: Used by SPICe and NHS Health Scotland
- **Fraser of Allander Institute**: Uses IPPR model v2.7.8 for some work
- **ScotMS**: Spatial microsimulation model for Scotland (SRUC)
- **Scotben**: Julia-based model by Graham Stark (formerly IFS, 20 years; now Open University/Virtual Worlds Research)

**Sources**:
- [ScotMS paper](https://pure.sruc.ac.uk/en/publications/scotms-microsimulation-model-for-scotland-construction-and-valida/)
- [Scotben at JuliaCon 2022](https://pretalx.com/juliacon-2022/talk/KPRZAM/)

### Canada: SPSD/M

- **Institution**: Statistics Canada
- **Full name**: Social Policy Simulation Database and Model
- **Start**: 1985
- **Type**: Static accounting model
- **Components**:
  - **SPSD (Database)**: Non-confidential, statistically representative database of Canadian individuals/families
  - **SPSM (Model)**: Calculates federal and provincial taxes and transfers
- **Current version**: Version 30 (database year 2018)
- **Access**: Free with signed Licence Agreement; available through Data Liberation Initiative for academics
- **Users**: Federal departments, provincial governments, universities, interest groups, consultants
- **Status**: "In wide use by policy analysts in Canada studying virtually every change to the tax and transfer system since 1985"

**Sources**:
- [SPSD/M Overview](https://www.statcan.gc.ca/en/microsimulation/spsdm/spsdm)
- [SPSD/M Product Description](https://www.statcan.gc.ca/en/microsimulation/spsdm/overview1)

### European Union: EUROMOD

- **Origins**: 1996, EU-funded (FP3, FP4, FP5 projects)
- **Initial coverage**: EU-15 countries
- **Development**: 2004-2018 at University of Essex (ISER Microsimulation Unit)
- **Current management**: JRC (Joint Research Centre) since 2021
- **Data**: EU-SILC (European Statistics on Income and Living Conditions)
- **Expansion**: SOUTHMOD for Global South (Ghana, Ethiopia, Zambia, Tanzania, Mozambique, Ecuador, Vietnam)

**Sources**:
- [EUROMOD History](https://www.microsimulation.ac.uk/euromod/history/)
- [What is EUROMOD](https://euromod-web.jrc.ec.europa.eu/overview/what-is-euromod)

## Timeline Summary

| Year | Event |
|------|-------|
| 1957 | Orcutt proposes microsimulation |
| 1960 | TAXSIM federal coverage begins |
| 1962-65 | Sadowsky brings microsimulation to Treasury |
| 1969 | IFS founded |
| 1974 | Budget Act makes JCT official for Congress |
| 1975 | DYNASIM completed |
| 1977 | TAXSIM state coverage begins |
| 1983 | IFS TAXBEN launched |
| 1985 | Statistics Canada SPSD/M begins |
| 1988 | IPPR founded |
| 1993 | Feenberg & Coutts publish TAXSIM documentation |
| 1996 | EUROMOD project begins; ITEP founded |
| ~2000 | Urban-Brookings TPC established |
| 2000-04 | Howard Reed leads TAXBEN at IFS |
| 2008 | Howard Reed founds Landman Economics, creates TTM |
| ~2014 | PWBM founded by Kent Smetters |
| 2018 | UKMOD project begins (spin-off from EUROMOD) |
| 2021 | EUROMOD transferred to JRC |

## Key Themes for Chapter 2

1. **Asymmetry**: Government has models; public doesn't
2. **Opacity**: Most models are black boxes to outsiders
3. **Institutional knowledge**: Models often depend on key individuals (Feenberg at NBER, Sadowsky at Treasury)
4. **Data access**: SOI is gold standard but access is restricted
5. **State capacity gap**: Most states can't do their own modeling
6. **International variation**: Different models, different data, hard to compare

## Open Questions

- Who specifically created the first JCT model?
- What was the first Treasury tax model before Sadowsky?
- What triggered CBO's development of its own model vs using JCT?

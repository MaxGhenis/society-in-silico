# Primary-source integration, September 7, 2026

The separate `research-society` lane saved a source cache and proposed patch,
then stopped with an authentication error before completing `sources.md` or its
final report. This implementation checked the selected cached primary documents
and integrated the supported findings after completing the PolicyEngine milestone.
The proposed patch was not applied wholesale. No chapter was edited by that lane.

The cache is at
`/Users/maxghenis/capacity-sprint-20260907/research-society/sources-cache/`.
`source-cache-sha256.json` identifies the inspected files; the links below and
bibliography identify their public sources. Full papers and microdata are not
included in this repository.

| Passage | Verified evidence and locator | Integrated wording and limits |
| --- | --- | --- |
| Chapter 13, AHCA chronology | [House roll 256](https://clerk.house.gov/evs/2017/roll256.xml): May 4, 2017 passage, 217–213. [Senate vote 179](https://www.senate.gov/legislative/LIS/roll_call_votes/vote1151/vote_115_1_00179.xml): July 28, 2017, 01:24 AM, amendment 667 rejected 49–51. GovInfo bill-status XML ends with return to the calendar. | Distinguishes House bill passage from Senate rejection of the skinny-repeal amendment. Does not call the latter a vote on final passage of the House text. |
| Chapter 13, Finnish basic income trial | [Pre-analysis plan](https://www.socialscienceregistry.org/versions/140144/docs/version/document), section 4.1 and table 2: 175,222 in the sampling frame, 2,000 treated, 173,222 controls. [Verho, Hämäläinen and Kanninen](https://doi.org/10.1257/pol.20200143), 2022, AEJ: Economic Policy 14(1), 501–522; title/authors/date checked against Crossref. The cached VATT working-paper version, table 1, describes the 23-point full-time participation-tax-rate reduction and the first-year employment result. | Corrects the control count and the previously incorrect author/year/volume entry. First-year employment is statistically unchanged, not proved to be exactly zero. |
| Chapter 13, later Finnish employment result | [Final evaluation 2020:15](https://julkaisut.valtioneuvosto.fi/handle/10024/162219), English summary: approximately six extra employment days over November 2017–October 2018; the 2018 activation reform also changed controls' benefit conditions. | States the joint-policy interpretation; removes the unsupported description of a permanent payment and the categorical explanation of why models were wrong. Does not attribute the whole later effect to basic income. |
| Chapter 7, state EITCs | [NCSL tracker](https://www.ncsl.org/human-services/earned-income-tax-credit-overview), updated June 9, 2026, table as of May 2026: 31 states plus DC. Washington's amount depends on household size. | Dates the count. Omits the proposed claim that Washington is wholly untethered from federal rules: its eligibility still refers to the federal EITC. |
| Chapters 3 and 6, benefit underreporting | [Meyer and Mittag 2019](https://doi.org/10.1257/app.20170478), table 1: false negatives 42.8% SNAP, 63.3% public assistance, 35.6% housing assistance; text rounds to 43/63/36. New York State, CPS ASEC survey years 2008–2013. | Names geography, years and denominator. Uses absence of recorded receipt, which includes survey imputation errors, rather than asserting every missing receipt is a respondent's denial. These are not current national rates. |
| Chapter 3, Social Security underreporting | [Bee and Mitchell 2017](https://www.census.gov/content/dam/Census/library/working-papers/2017/demo/SEHSD-WP2017-39.pdf), table 6 panel A: 0.078 false-negative rate among recipients aged 65+, 2013 CPS ASEC linked to SSA/IRS, income year 2012. | Approximately eight percent, with age and survey vintage stated. Reuses the existing bibliography entry rather than creating a duplicate. |
| Chapter 3, elderly SSI take-up | [McGarry and Schoeni 2015](https://mrdrc.isr.umich.edu/publications/papers/pdf/wp319.pdf), abstract and introduction; historical studies estimate roughly 50–60%, with HRS analysis through 2010. | Describes study estimates rather than asserting a newly measured 2026 rate. Cached document was retrieved by the source lane through the Internet Archive because the live host blocked access. |

The patch's long source quotations and internal audit notes were not copied into
the public bibliography. Citation metadata remains concise; this memo carries the
verification context. Unrelated citation, verification, and partner-approval markers
remain in place. The book is a review draft, not a publication-ready artifact.

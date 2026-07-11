# Part I primary-source verification

Scope: the four chapters of `manuscript/part-1-closed-stack/` (01 birth of microsimulation,
02 tax model wars, 03 the accuracy question, 04 a wall of frustration). Every load-bearing
claim was checked against the most primary source reachable. Verdicts: **CONFIRMED**,
**CORRECTED** (value/attribution must change), **UNVERIFIED** (could not confirm from a
primary source in this pass). Researcher: primary-source pass, 2026-07-11.

Chapter 4 is Max's personal narrative; its biographical claims (Alex's injury, Berkeley
IEOR 131, Finelite, Google/YouTube dates, UBI Center 2019, Nate Golden, Nikhil Woodruff)
are first-person and not externally verifiable here. Only its externally-checkable facts
(GiveDirectly 2012 Google.org award; Tax-Calculator/OpenFisca provenance; American Family
Act sponsors) touch the public record and are noted at the end.

---

## CORRECTIONS (values or attributions that must change)

### 1. Chapter 1 — historian's name: "Hsiang-Ke Cheng" → **Chung-Tang Cheng**
The chapter (line 93) reads "As the historian Hsiang-Ke Cheng put it…" The author of the
cited article is **Chung-Tang Cheng**, historian of economics at National Taipei University.
"Hsiang-Ke" belongs to a *different* historian of econometrics, **Hsiang-Ke Chao** — an easy
and classic confusion. The surname (Cheng), citekey (`@cheng2020orcutt`), and the quote
itself are correct; only the first name is wrong.
- Article: Chung-Tang Cheng, "Guy H. Orcutt's Engineering Microsimulation to Reengineer
  Society," *History of Political Economy* 52 (S1): 191–217, 2020.
- Source: https://read.dukeupress.edu/hope/article-abstract/52/S1/191/166649/ ;
  https://www.semanticscholar.org/paper/54d15af0c58bee82463f4b85e05af5ad44241703
- Quote CONFIRMED verbatim: microsimulation was "an engine designed for not only scrutinizing
  the system but reengineering the society." ("Tinbergen dream" also confirmed from abstract.)

### 2. Chapter 3 — ACA source has wrong author AND the quote is from the wrong piece
Two distinct problems in the sentence citing `@collins2015aca`:
- **(a) Wrong authors in the bib.** The `references.bib` entry `collins2015aca` lists
  "Collins, Sara R. and Gunja, Munira and Doty, Michelle M. and Beutel, Sophie." The actual
  authors of "The CBO's Crystal Ball: How Well Did It Forecast the Effects of the Affordable
  Care Act?" (Commonwealth Fund, Dec 2015) are **Sherry A. Glied, Anupama Arora, and Claudia
  Solís-Román**. Fix the author field (and ideally rename the key `glied2015aca`).
  PDF byline confirms: `…1851_glied_cbo_crystal_ball_forecast_aca…`; NYU Scholars lists it
  under Glied. This is a Chen-vs-Blair-Stanek–class misattribution.
- **(b) Quote is misattributed.** The line "was in estimating *where* the uninsured would get
  covered, not *how many* of them would gain coverage" is the framing of the **FactCheck.org**
  analysis (Kiely, 2017), already in the bib as `@kiely2017aca`, not the Commonwealth Fund
  brief. Attribute the quote to `@kiely2017aca`.
- Sources: https://www.factcheck.org/2017/03/cbos-obamacare-predictions-how-accurate/ ;
  https://www.commonwealthfund.org/publications/issue-briefs/2015/dec/cbos-crystal-ball-how-well-did-it-forecast-effects-affordable
- The *numbers* around the quote are all CONFIRMED (see Chapter 3 below).

### 3. Chapter 3 — the "random walk beat the CBO" finding is NOT the Berkeley thesis's own result
The chapter (line 51) says "A Berkeley thesis examining CBO forecasts from 1976 to 2007 found
that a 'random walk'… would have beaten the CBO on average, over both short and medium
horizons [@inayatali2023cbo]." The thesis is real, but this specific finding is **quoted in
its literature review from Kliesen and Thornton (2012)**, not produced by the thesis.
- The thesis (Ammar Inayatali, "Always in Motion is the Future: The Accuracy of Historical
  CBO Debt Projections," UC Berkeley, supervised by David Romer) analyzes CBO **long-term
  projections from 1996–2008** and finds CBO "overestimated the size the cumulative budget
  balance by 3.9% of cumulative GDP." It does **not** run a 1976–2007 random-walk comparison.
- The thesis text: "Kliesen and Thornton (2012)… find that in forecasts published from **1976
  to 2007**, the CBO tended to underestimate the size of budget deficits… The authors also
  find that **random walk projections would have, on average, fared better** in both the short
  and medium run than those published by the CBO."
- **Fix:** attribute the random-walk claim (and the "1976 to 2007" range, which is deficit-,
  not debt-, focused) to **Kliesen & Thornton (2012)**, "How Good Are the Government's Deficit
  and Debt Projections and Should We Care?", *Federal Reserve Bank of St. Louis Review* 94(1):
  21–39. The thesis can stay as a secondary pointer, or be re-cited for its own 3.9%-of-GDP
  result. New source added to the bib.
- Sources: https://econ.berkeley.edu/sites/default/files/Inayatali_Ammar_Thesis.pdf ;
  https://research.stlouisfed.org/publications/review/2012/01/01/how-good-are-the-governments-deficit-and-debt-projections-and-should-we-care

### 4. Chapter 2 — statutory citation: "Section 6103(l)" → **Section 6103(f)** for JCT
The chapter (line 27) says "Under Section 6103(l), JCT and Treasury have statutory access to
the returns themselves." The correct provision for the **Joint Committee on Taxation's** access
to returns is **§6103(f)** ("Disclosure to Committees of Congress" — Ways and Means, Senate
Finance, and JCT; and to the JCT Chief of Staff). **§6103(l)** governs disclosure "for purposes
*other than* tax administration" (to SSA, HHS, state agencies, etc.) — not JCT/Treasury access.
Treasury/OTA access for tax administration is inherent / under §6103(h). The chapter's larger
point (6103 makes returns confidential; JCT and Treasury have privileged access outsiders lack)
is correct; only the subsection letter is wrong.
- Source: 26 U.S.C. §6103, https://www.law.cornell.edu/uscode/text/26/6103 ; CRS R48323,
  "Disclosure of Federal Tax Return Information to Congressional Committees."

### 5. Minor value/attribution nuances (fix if convenient; not headline errors)
- **Ch 2, OpenFisca timing.** "Four months later [≈ May 2011]… released… the source code" —
  OpenFisca *development began* at the Centre d'analyse stratégique in May 2011, but the code
  was first published open-source (AGPL) in **November 2011**. Consider "began building"
  rather than "released," or move the date. (openfisca.org/en/about)
- **Ch 2, TPC founders.** The chapter names Steuerle and Burman; TPC's own history names a
  **third co-founder, William (Bill) Gale**. Not wrong, but incomplete.
  (https://taxpolicycenter.org/taxvox/happy-birthday-tpc)
- **Ch 2, JCT dynamic offset.** "$385 billion of revenue recovered through faster growth" — the
  $385B is the *net deficit* reduction (≈$451B more revenue **minus ≈$66B more interest
  spending**). Precise wording: "reduced the deficit by ~$385 billion." (JCT JCX-69-17)
- **Ch 3, Inayatali bib year.** `inayatali2023cbo` is dated 2023, but the thesis cites CBO's
  January 2019 outlook as the latest data — it is almost certainly a **2019** thesis. Verify.
- **Ch 2, `ukmod2020` key.** Points to a **2021** paper (IJM 14(1):92–101). Key year is
  cosmetic but mismatched.

---

## CHAPTER 1 — The birth of microsimulation

| Claim | Verdict | Primary source | Note |
|---|---|---|---|
| Orcutt 1957, "A New Type of Socio-Economic System," *Review of Economics and Statistics* | CONFIRMED | RES 39(2):116–123, 1957; reprint microsimulation.pub/articles/00002 | Vol/issue/pages exact. |
| Quote: "interacting units which receive inputs and generate outputs" | CONFIRMED | 1957 paper (reprint) | Verbatim: "…consists of various sorts of interacting *units* which receive *inputs* and generate *outputs*." |
| Quote: "rather limited predictive usefulness" | CONFIRMED | 1957 paper | Verbatim in opening paragraph. |
| Quote: "The most distinctive feature of this new type of model is the key role played by actual decision-making units… the individual, the household, and the firm" | CONFIRMED | 1957 paper | Verbatim. |
| Quote: "Predictions about aggregates will still be needed but will be obtained by aggregating behavior of elemental units…" | CONFIRMED | 1957 paper | Verbatim (chapter trims the tail; faithful). |
| Quote: "appears rather appalling" (dynamic paths) | CONFIRMED | 1957 paper | Verbatim: "the problem of keeping track of all possible paths and their respective probabilities appears rather appalling." |
| Quote: "inherent difficulty, if not practical impossibility, in aggregating…" | CONFIRMED | 1957 paper | Verbatim. |
| B.S. physics, Michigan, 1939; grad work then Ph.D. 1944 | CONFIRMED | Watts 1991, JEP 5(1):171–179 | Watts: undergrad "in three years with a B.S. in physics"; "began graduate work in economics in 1939"; dissertation 1944. Nuance: the switch to economics dates to 1939 (start of grad school), not the 1940 M.A. |
| "regression analyzer" analogue machine (Tinbergen-inspired) | CONFIRMED | Watts 1991; Cheng 2020 | Designed in the 1944 dissertation; **prototype built at MIT** after his 1944 MIT appointment. (Task's "at MIT" is right; chapter omits MIT — optional to add.) |
| Cochrane–Orcutt procedure, 1949 | CONFIRMED | Watts 1991 ("Cochrane and Orcutt, 1949") | Still standard. |
| Directed Harvard's Littauer Statistical Laboratory; consulted Fed & IMF | CONFIRMED | Watts 1991 | Watts lists Harvard, MIT, Cambridge, IMF, World Bank, Urban Institute. |
| "Tinbergen dream"; "microanalytic simulation" | CONFIRMED | Cheng 2020 (abstract) | "Tinbergen dream" is Cheng's phrase for Orcutt's ambition. |
| Founded Social Systems Research Institute (SSRI), Wisconsin, 1959 | CONFIRMED | Watts 1991 | "In the fall of 1959 the Social Systems Research Institute (SSRI) was launched." (Offer came 1958.) |
| Wisconsin effort a "failed trial" | CONFIRMED (author corrected — see #1) | Cheng 2020 | Cheng frames the Wisconsin decade as a failed attempt; Watts: Orcutt "left after seven extremely active years." |
| 1961 book *Microanalysis of Socioeconomic Systems: A Simulation Study*, three co-authors incl. Rivlin | CONFIRMED | Harper, 1961 | Co-authors: **Greenberger, Korbel, Rivlin** — all three confirmed. |
| Rivlin was Orcutt's **doctoral student** | CONFIRMED | AEA/Fed bios | Orcutt was Rivlin's thesis adviser; she took her Ph.D. at Radcliffe, 1958. |
| Rivlin → first CBO director (1975, "fourteen years" after 1961), later Fed vice chair | CONFIRMED | federalreservehistory.org/people/alice-m-rivlin | See also Ch 2. |
| Asimov, *Foundation and Empire* (1952): "The reaction of one man could be forecast by no known mathematics; the reaction of a billion is something else again" | CONFIRMED | Foundation and Empire, 1952 | Verbatim. Fuller context worth using: "Psycho-history dealt not with man, but with man-masses. It was the science of mobs; mobs in their billions." |
| IBM 704 ≈ 12,000 FLOPS | CONFIRMED | IBM 704 spec | "up to 12,000 floating-point additions per second." Resolves the [NEEDS CITATION]. |
| von Neumann cast weather forecasting as computing before 1957 death; Simon & Newell first AI programs at Carnegie Tech | CONFIRMED (well-established) | — | Uncontested history. |
| Sadowsky brought computers to Treasury OTA, 1962–65; modeled preliminary Revenue Act of 1964; static, no aging | CONFIRMED | Sadowsky ACM/Ubiquity interview; georgesadowsky.org | He was a Treasury consultant (from early 1963) while a Yale grad student; "probably the most useful program I ever wrote," 3 months, 1963. |
| Sadowsky → Brookings → Urban Institute; operated DYNASIM | CONFIRMED | Watts 1991 | Watts: MASH "was developed by George Sadowsky to operate DYNASIM." |
| Urban Institute hired Orcutt 1968 to lead DYNASIM; resourced by 1969 | CONFIRMED (with context) | Watts 1991; Urban DYNASIM overview | Orcutt joined Urban ~1968, then took the Yale Griswold chair in **1970**; DYNASIM work continued at Urban (Harold Guthrie, project coordinator) and Yale. |
| DYNASIM: DEC System-10 mainframe, MASH framework, 10,000 people | CONFIRMED | SOA 1997 ch.3 DYNASIM | MASH = "Microanalytic Simulation of Households," FORTRAN on a DEC System-10; closed 10,000-person dataset. |
| First DYNASIM version complete 1975 (18 yrs after 1957) | CONFIRMED | SOA 1997; Orcutt, Caldwell & Wertheimer 1976 | Model completed 1975; documented in the 1976 Urban Institute book *Policy Exploration through Microanalytic Simulation*. |
| DYNASIM generations: retirement-income version early 1980s; ~2000 overhaul projecting 75 yrs on trustees' assumptions; 4th gen (DYNASIM3) still active | CONFIRMED | Urban DYNASIM3 overview | — |
| CORSIM (Caldwell, Cornell) → POLISIM, DYNACAN; SPSD/M (Statistics Canada); SVERIGE (Sweden) | CONFIRMED (family well-documented) | Li & O'Donoghue 2013 survey (`@li2013survey`) | Descendant lineage standard in the survey literature. |
| Pechman & Okner, *Who Bears the Tax Burden?* (Brookings, 1974), 72,000 households (MERGE file) | CONFIRMED | Brookings, 1974 | "representative sample of 72,000 American families," 1966 data. |
| Orcutt died **March 5, 2006** (b. July 5, 1917) | CONFIRMED | Wikipedia/Wikidata/legacy.com concur; `@prabook2024orcutt` | Date corroborated widely; sourcing could be upgraded to a scholarly obituary if one is desired. |
| Daughter Alice Orcutt Nakamura (economist); granddaughter **Emi Nakamura, Clark Medal 2019** | CONFIRMED | Eberly & Woodford, JEP 34(1):222–239, 2020; AEA | Bonus theme: Emi's citation praises work "using less aggregated data" — a three-generations echo. |
| Cheng: microsimulation "an engine designed for not only scrutinizing the system but reengineering the society" | CONFIRMED (author corrected — see #1) | Cheng 2020, HOPE 52(S1):191–217 | Verbatim. |
| Orcutt autobiographical quote: "my early fascination with science, my transition from engineering to economics" | UNVERIFIED (source exists) | Orcutt 1990, JEBO 14(1):5–27, "From engineering to microsimulation" | Essay confirmed to exist; exact wording of this fragment not machine-verified. Thematically consistent (Watts paraphrases "from engineering through physics to economics"). |

---

## CHAPTER 2 — The tax model wars

| Claim | Verdict | Primary source | Note |
|---|---|---|---|
| IFS founded 1969 by four financial professionals frustrated with UK tax-policy opacity | CONFIRMED | ifs.org.uk/about/history-ifs | Incorporated 21 May 1969. Founders: banker **Will Hopper**, investment-trust manager **Bob Buist**, stockbroker **Nils Taube**, tax consultant **John Chown**; sparked by the 1965 Finance Act (capital gains tax); decided at a dinner 30 July 1968, Stella Alpina restaurant, London. Rich detail available. |
| TAXBEN operating since 1983 | CONFIRMED | ifs.org.uk; IFS WP 95/19 | "IFS has operated a tax and benefit model of the UK, known as TAXBEN, since 1983." |
| CBO created 1974; Rivlin first director; nonpartisan, hired economists | CONFIRMED | Congressional Budget & Impoundment Control Act 1974; `@rivlin1984economics` | Well-established. |
| CBO built health/SocSec/tax microsim + CBOLT long-term model | CONFIRMED | `@cbo2018overview` | — |
| JCT created **1926** | CONFIRMED (well-established) | Revenue Act of 1926; jct.gov history | — |
| JCT suite: individual, corporate, estate/gift, international models; official revenue estimator under the 1974 Budget Act | CONFIRMED | `@jct2024revenue` | — |
| Treasury OTA Individual Income Tax Model since Sadowsky (1960s), refreshed from IRS returns | CONFIRMED | `@sadowsky1991computing` | — |
| Urban Institute's TRIM3, annual from CPS, models SNAP/Medicaid/TANF/SSI/housing | CONFIRMED (well-documented) | trim3.urban.org | Note: chapter's "Karen Smith… (chapter 1)" cross-ref is dangling — Karen Smith is not introduced in Ch 1 (flagged in facts file). |
| §6103 confidentiality; privileged government access; outsiders use sampled/anonymized/top-coded public-use files | CONFIRMED (subsection CORRECTED — see #4) | 26 U.S.C. §6103 | JCT access is §6103(f), not (l). |
| Feenberg built TAXSIM at NBER (early 1980s); internet-reachable by 1990s; maintained decades | CONFIRMED (minor date nuance) | Feenberg & Coutts 1993, JPAM 12(1):189–194 | NBER also dates TAXSIM's roots to the late 1970s ("since the 1970s"); "early 1980s" is close. |
| "over 1,200 papers" cite/apply TAXSIM | CONFIRMED | nber.org/research/data/taxsim | "Over 1,200 papers have applied TAXSIM." Chapter says "thousand-plus." |
| TPC founded 2002 (Urban+Brookings); Steuerle & Burman built official models | CONFIRMED (add Gale — see #5) | tpc; `@tpc2024model` | Third co-founder Bill Gale omitted. Steuerle founding director 2002–08. |
| 2012: TPC showed Romney's revenue-neutral rate-cut promise mathematically impossible | CONFIRMED | `@tpc2012romney` | — |
| PWBM launched 2016 by Kent Smetters (Penn); dynamic estimates | CONFIRMED | news.wharton.upenn.edu, June 2016 | SocSec/immigration modules June 2016; tax module Sept 2016. |
| Auerbach 2005 formalized dynamic-scoring issues (correct but treacherous) | CONFIRMED | Auerbach, "Dynamic Scoring: An Introduction to the Issues," *AER* 95(2):421–425, 2005 | Exact title/venue. |
| Jan 2015 House rule: JCT dynamic scores for legislation > 0.25% of GDP | CONFIRMED | CRS; CRFB 2015-01-08 | Threshold 0.25% of GDP; adopted Jan 2015. |
| TCJA: JCT static **$1.46T**; dynamic **$1.07T** (~$385B offset) | CONFIRMED (resolves [NEEDS CITATION]) | JCT JCX-67-17 (static ~$1,456B); JCX-69-17 (dynamic, ~$385B) | Dynamic ≈ $1.07–1.1T. See #5 on "$385B" wording. |
| PWBM TCJA dynamic **$1.8–2.2T** | CONFIRMED | `@pwbm2017tcja` | — |
| OBBBA (2025) extended TCJA individual provisions | CONFIRMED | `@obbba2025` | Consistent w/ project facts. |
| Elmendorf, Hubbard & Williams assessed dynamic scoring | CONFIRMED | "Dynamic Scoring: A Progress Report on Why, When, and How," *BPEA* Fall 2024, pp. 93–134 (NBER WP 33425) | Exact venue/pages. |
| Ann Harding built microsim at NATSEM (Canberra) from 1993; ed. vol. *Microsimulation and Public Policy* (1996) standard reference | CONFIRMED | canberra.edu.au (NATSEM founding, Jan 1993); Harding (ed.) 1996, North-Holland | Harding founded NATSEM 1993; the 1996 volume exists (JASSS review). |
| EUROMOD from 1996, team led by Holly Sutherland; spans EU member states | CONFIRMED | Sutherland & Figari 2013, IJM 6(1):4–26 | — |
| EUROMOD developed at Essex on EC grants; access-by-application; ethos of sharing | CONFIRMED | microsimulation.ac.uk/euromod | — |
| EUROMOD later maintained by the EC's **Joint Research Centre**; open-source **Dec 2020** | CONFIRMED | euromod-web.jrc.ec.europa.eu | Open-source since Dec 2020 (CC BY 4.0 + EUPL-1.2); JRC manages it since 2021. |
| UKMOD from EUROMOD's UK component; Nuffield-funded; led by **Mike Brewer**; at Essex CeMPA under **Matteo Richiardi**; 2021 intro paper by **Richiardi, Collado, Popova** | CONFIRMED | Richiardi, Collado & Popova 2021, IJM 14(1):92–101; iser.essex.ac.uk | Nuffield 3-yr project 2018–21; Brewer PI. |
| UKMOD first free public release **October 2019**; UK's first freely available tax-benefit model | CONFIRMED (with nuance) | iser.essex.ac.uk (Aug 2019 announcement; Oct 2019 training launch) | ISER announced Aug 2019; public launch/training 23–25 Oct 2019. "October 2019" defensible. |
| UKMOD users: Scottish Parliament research service, NHS Health Scotland, Welsh Government | UNVERIFIED | — | Plausible; not machine-verified this pass. |
| Brewer quote: "We wanted to democratize access to tax-benefit analysis" | UNVERIFIED (framing confirmed) | Nuffield: "New tool to democratise debates on tax and welfare policy across the UK" | The "democratise" language is the project's own; exact sentence not sourced. Consider softening or citing the Nuffield page. |
| Howard Reed ran TAXBEN at IFS 2000–04; founded Landman Economics 2008 | UNVERIFIED | `@northumbria2024reed` | Not checked this pass. |
| Reed quote: "a new settlement of the same scale and sustainability as the Beveridge-inspired reforms of 1945" | UNVERIFIED | — | [NEEDS CITATION] still open. |
| Malcolm Torry (Citizen's Basic Income Trust) used EUROMOD ~a decade to cost UBI | CONFIRMED (source cited) | `@torry2019ubi` | — |
| Jan 2011: Landais, Piketty & Saez, *Pour une révolution fiscale*; single progressive levy | CONFIRMED | piketty.pse.ens.fr | Book Jan 2011; free PDF from 20 Apr 2011. |
| revolution-fiscale.fr let citizens design reforms; "hundreds of thousands of visitors" | CONFIRMED | French coverage | "more than **500,000 visitors**." Chapter's "hundreds of thousands" is safe. |
| France has no independent parliamentary scoring shop (unlike US CBO) | CONFIRMED (well-established) | — | Evaluations ran through the Finance Ministry. |
| OpenFisca released ~4 months later by Ben Jelloul & Schaff at the Centre d'analyse stratégique | CONFIRMED (timing nuance — see #5) | openfisca.org/en/about | Dev began May 2011 at CAS (later France Stratégie); AGPL open-source release Nov 2011. |
| NZ Service Innovation Lab, 2018: 3-week Better Rules exercise, legislation as Python + human-readable rules | CONFIRMED | serviceinnovationlab.github.io | Early 2018; 3-week exploration (Inland Revenue, MBIE, PCO + software firm); Python/Jupyter. |
| OECD *Cracking the Code* (2020), rules-as-code primer | CONFIRMED (cited) | `@oecd2020cracking` | — |
| OpenFisca powered Mes Aides, NZ rates rebate; adaptations Tunisia, Senegal…; OECD/EC recognition | CONFIRMED | `@openfisca2024about` | — |
| 2013: Matt Jensen founded Open Source Policy Center at AEI; recruited Martin Holmer to write Tax-Calculator | CONFIRMED | aei.org; ospc.org | Jensen founding director 2013–2022. |
| 2016 OGP Paris summit: French + Tunisian volunteers modeled Senegal income tax in **under 36 hours**, won hackathon | CONFIRMED | github.com/openfisca/openfisca-senegal; openfisca.org/en/about | Web-UI simulator shipped; first prize. |
| By 2019 France's National Assembly built LexImpact on OpenFisca; within two years "well over a hundred" simulations | CONFIRMED | leximpact.an.fr; beta.gouv.fr | **122 simulations** by MPs in 2021; LexImpact launched 2019 (EIG cohort 3), used in 2020 Finance Bill debate. |
| Tax-Calculator → Policy Simulation Library federation (OG models, Tax Foundation cost-recovery, QuantEcon); CBO–NYC users | CONFIRMED (well-documented) | PSL catalog | — |
| Federal Reserve released a Python implementation of FRB/US (several-hundred-equation model) in 2022 | CONFIRMED | federalreserve.gov/econres/us-models-python.htm | PyFRB/US, April 2022; ~284–375 equations. (Model package first made public 2014 in EViews — optional context.) |

---

## CHAPTER 3 — The accuracy question

| Claim | Verdict | Primary source | Note |
|---|---|---|---|
| JCT TCJA static $1.46T; PWBM dynamic $1.8–2.2T | CONFIRMED | see Ch 2 | — |
| Three validation levels (component / aggregate / predictive) | CONFIRMED (framework, uncontested) | — | Author's frame. |
| ACA: March 2010 CBO projected non-elderly uninsured **18%→7.6%** by 2016 (full Medicaid expansion) | CONFIRMED | Glied, Arora & Solís-Román 2015 (Commonwealth Fund) — see #2 | "from over 18 percent… to 7.6 percent in 2016." |
| Court made expansion optional; 19 states declined; adjusted projection **9.4%** | CONFIRMED | Kiely 2017 (FactCheck) | — |
| Actual 2016 non-elderly uninsured **10.4%** (CDC) | CONFIRMED | `@kiely2017aca` | Within a point of adjusted projection. |
| Table: exchange 21–23M → **10.4M**; Medicaid 10M → **14.4M**; total uninsured 30M → **27.9M** | CONFIRMED | Kiely 2017; Glied et al. 2015 | Glied et al.: CBO over-estimated marketplace enrollment ~30%, costs ~28%, under-estimated Medicaid ~14%. |
| Quote: error "was in estimating *where*… not *how many*…" | CONFIRMED — but reattribute to `@kiely2017aca` (see #2) | FactCheck 2017 | — |
| CBO sixth-year deficit MAE fell **3.2%→1.0%** of GDP (1989–2001 → 2002–2019) | CONFIRMED | CBO pub. 61067, "An Evaluation of CBO's Projections of Deficits and Debt From 1984 to 2023" (Dec 2024) | Exact. Resolves `@cbo2024deficit`. |
| CBO ≈ Blue Chip (~50 forecasters) ≈ Administration | CONFIRMED (cited) | `@cbo2025forecasting` (pub. 61334) | — |
| 2021 largest overestimate on record; 2023 largest underestimate, off **3.9%** of GDP | CONFIRMED | CBO pub. 61067 | — |
| "Random walk beat CBO 1976–2007, short & medium horizons" | CORRECTED — Kliesen & Thornton (2012), not the thesis (see #3) | St. Louis Fed *Review* 94(1):21–39 | Thesis's own result: CBO overestimated cumulative budget balance by 3.9% of GDP, 1996–2008. |
| TCJA: real revenue 2018–2024 (ex-2022) within **0.5%** of CBO's 2018 projections | CONFIRMED | CRFB, "Has TCJA Paid For Itself?" | Verbatim: "$100 billion lower, but within 0.5 percent." 2022 spike = capital gains + inflation. |
| OBBBA July 2025 extended TCJA; pass-through deduction permanent; CTC $2,200 for 2026 | CONFIRMED | `@obbba2025` | Consistent w/ project facts. |
| NBER: prediction markets "weakly more accurate than survey forecasts" (GDP, inflation, employment) | CONFIRMED (substance); quote wording approximate | Snowberg, Wolfers & Zitzewitz 2012, NBER WP 18222 | Documented language: market forecasts "at least as accurate… somewhat superior to… survey forecasts." Verify the exact "weakly more accurate" phrasing against the paper. |
| Polymarket had Trump at **58%** the Monday before the 2024 vote | CONFIRMED (cited) | `@polymarket2024election` | — |
| Prediction markets ≈/> FiveThirtyEight | CONFIRMED (cited) | `@crane2020prediction` | — |
| Good Judgment superforecasters beat Fed futures by **~30%**, 2024–25 | CONFIRMED | goodjudgment.com/good-judgment-2024-in-review; FT coverage | GJ's own claim ("30% more accurate… than the futures in 2024–2025"); chapter's "reportedly" is apt. |
| Tetlock: most experts ≈ chance; ~2% consistently outperform | CONFIRMED (cited) | `@tetlock2005expert`; `@tetlock2015superforecasting` | — |
| Meyer: CPS underreporting — SNAP **40–50%**, TANF/GA **>60%**, housing ~1/3, Social Security ~1/10 | CONFIRMED (SS ~10% consistent) | Meyer & Mittag 2015 (NBER WP 21676; AEJ:Applied 2019) | SNAP 40–50%, TANF/GA 60%, housing >1/3 confirmed; SS ~10% consistent with Meyer (least-underreported major transfer). |
| Falling survey response since 1990s; non-responders skew low-income/young/mobile; imputation reliance | CONFIRMED (well-documented) | Census AIS/SEHSD papers | — |
| Bee & Mitchell: senior income **30% higher** in admin data ($44,400 vs $33,800); senior poverty **9.1% (CPS) vs 6.9% (validated)**, a 2.2-pt gap | CONFIRMED | Bee & Mitchell 2017 (Census/CES) | Exact. `@census2017retirement` — verify its author field names **Bee & Mitchell**. |
| Very high earnings top-coded in public-use data → compressed top | CONFIRMED (resolves [NEEDS CITATION]) | Census CPS ASEC top-coding ("swap values"); Larrimore, Burkhauser, Feng & Zayatz 2008 | Suggested cite added to bib. |
| Confidential-IRS models still miss non-filers, non-taxable transfers, and use tax units not households | CONFIRMED (well-established) | — | — |
| TAXSIM as validation benchmark; deterministic tax rules; 1,200+ citing papers; taxes-only, record-by-record | CONFIRMED | see Ch 2 | — |
| Four TCJA scores a factor of 5 apart: JCT $1.46T; PWBM $1.8–2.2T; **Tax Foundation $448B**; TPC ≈ JCT on revenue | CONFIRMED | Tax Foundation TCJA analysis | Tax Foundation's ~$448B (larger growth response) confirmed as the low-cost outlier. |
| Take-up: EITC **78–80%**; SNAP **~82%** (wide state variation); SSI elderly ~50–60% | CONFIRMED (EITC, SNAP) | IRS/Census EITC (TY2022 = 78%); USDA SNAP (2018 = 82%) | `@irs2024eitc`, `@usda2024snap`. SSI-elderly 50–60% plausible, not machine-verified. |
| TCJA pass-through surge (20% deduction) unforeseen by static models | CONFIRMED (well-documented) | — | — |
| AHCA (2017): CBO estimated **23 million** more uninsured by 2026 | CONFIRMED | CBO pub. 52752, H.R. 1628 cost estimate (May 2017) | `@cbo2017ahca`. |
| 2021 CTC expansion: ~$105B/yr, ~40% child-poverty cut, largest gains to lowest-income | CONFIRMED (well-documented) | Census/JEC | Directionally exact. |
| Census SPM child poverty **9.7%→5.2%** in 2021; reverted after lapse | CONFIRMED | Census, "Child Poverty Fell to Record Low 5.2% in 2021" (Sept 2022) | `@census2022spm`. (9.7% = 2020 rate.) |
| Columbia poverty center tracked monthly declines | CONFIRMED (cited) | `@parolin2021monthly` | — |
| Box: "all models are wrong, but some are useful" | CONFIRMED | Box, "Science and Statistics," *JASA* 71(356):791–799, 1976 | "all models are wrong" is in Box 1976; the exact "…but some are useful" clause was crystallized in Box & Draper 1987. Attribution to 1976 is standard and fine. |
| Admissibility rule (component/aggregate/forecast → ground truth) | CONFIRMED (author's frame) | — | Load-bearing thesis; internally consistent. |

---

## CHAPTER 4 — A wall of frustration (externally-checkable items only)

| Claim | Verdict | Primary source | Note |
|---|---|---|---|
| Google.org gave GiveDirectly a **$2.4M Global Impact Award** in 2012 | CONFIRMED (cited) | `@givedirectly2012google` | — |
| Tax-Calculator = open-source US federal income/payroll model out of AEI's OSPC | CONFIRMED | see Ch 2 | — |
| American Family Act introduced by Sens. **Michael Bennet and Sherrod Brown** | UNVERIFIED (widely reported) | — | Consistent with public record; not machine-verified this pass. |
| UBI Center founded 2019, open-source | CONFIRMED (cited) | `@ubicenter2019` | — |
| microdf + openfisca-uk accepted into Policy Simulation Library | UNVERIFIED | PSL catalog | Plausible; not checked this pass. |
| Yang Freedom Dividend: 74% poverty cut; ~$2.8T cost vs ~$1.2T from five taxes → ~$1.6T gap | UNVERIFIED (author's own UBI Center analysis) | [NEEDS CITATION: UBI Center report] | Internal analysis; cite the original UBI Center report. |
| £100/tonne UK carbon tax → 14% poverty cut, 33% deep-child-poverty cut | UNVERIFIED (author's own analysis) | [NEEDS CITATION: UBI Center report] | Same. |

Personal-narrative claims (Alex's 2004 injury, Berkeley IEOR 131 in 2008, Finelite, Project
Lorenz at Google 2012, YouTube 2015, leaving Google July 2018, MIT MicroMasters) are
first-person and outside the scope of external verification.

---

## Counts
- **CONFIRMED:** ~92 load-bearing claims (incl. all 6 Orcutt 1957 quotes verbatim, all core
  dates and dollar figures, and the four [NEEDS CITATION] resolutions: IBM 704 FLOPS, JCT TCJA
  static/dynamic, CPS top-coding, and — via reattribution — the random-walk finding).
- **CORRECTED:** 4 headline (Cheng first name; ACA author + quote source; random-walk
  attribution; §6103(l)→(f)) + 5 minor nuances.
- **UNVERIFIED:** ~10 (mostly Chapter 2/4 quotes and biographical asides — Brewer quote, Reed
  bio+quote, UKMOD user list, SSI-elderly take-up, UBI Center report figures, American Family
  Act sponsors).

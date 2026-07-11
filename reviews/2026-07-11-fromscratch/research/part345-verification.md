# Part III–V fact verification (AI benchmarks, OBBBA, gov-tech, opinion/values)

Primary-source pass, 2026-07-11. Covers manuscript chapters 8–9 (Part III), 13–14 (Part IV), 15–17 (Part V).
Verdicts: **CONFIRMED** / **CORRECTED→[value]** / **UNVERIFIED**. Primary URLs given per claim.
New/primary BibTeX entries are in `part345-new-sources.bib`.
Internal Axiom/Thesis/populace program numbers (parity results, SOUTHMOD findings, money-atom/rule-file counts, HiveSight benchmark, value-forecasting figures) were treated as the author's own systems and **not** re-verified here, per the brief.

---

## CORRECTIONS FIRST (read these)

1. **Westworld epigraph is a paraphrase, not a verbatim quote.** Ch 17 (and the ch 13 frame) put in quotation marks: *"I don't predict the future," he says. "I create it."* Serac never says this line. Every transcript/recap renders his philosophy as narration ("his job isn't to predict the future like an oracle, but to create it"). The closest **verbatim** Serac line (S3E2 "The Winter Line," to Maeve) is: *"…humanity has been a miserable little den of thugs stumbling from one catastrophe to the next. Our history is like the ravings of lunatics. Chaos. But we've changed that. For the first time, history has an author."* → Either drop the quotation marks and present as characterization, or replace with the verified line. Primary: transcripts/recaps of S3E2; https://www.denofgeek.com/tv/westworld-season-3-who-is-serac/

2. **California Poppy figures (ch 8) are off on four specifics.** CORRECTED→ pilot ran across **67 departments** (not "fifty"); **2,800+** employees (book's "more than two thousand" is a floor, not the figure); drew on **~10 models / "multiple"** — CDT lists Claude, Gemini, GPT, Nova — **not "eleven"**; the **pilot began Sept 29, 2025** (before the IRS Nov 2025 deployment), with statewide rollout **July 2026** — so "a month later [Dec 2025]… launched" is wrong (a Newsom AI announcement did land Dec 16, 2025). Primary: https://www.cdt.ca.gov/poppy/

3. **The "13 million fewer insured by 2027" claim (ch 13) is miscited.** It is attributed to `[@cbo2017ahca]` (the AHCA cost estimate, pub 52752), but the 13M/2027 figure comes from a **different** CBO report: *Repealing the Individual Health Insurance Mandate: An Updated Estimate*, Nov 2017, **pub 53300** (4M more uninsured in 2019, 13M in 2027). → Add `@cbo2017mandate` and re-point that sentence. Primary: https://www.cbo.gov/publication/53300

4. **"The global tax-tech market was climbing toward $60 billion" (ch 9) reads as a current size; ~$60B is a ~2034 projection.** CORRECTED→ tax-tech market ≈ **$20.8B (2025) / $23.4B (2026)**, projected **~$60.7B by 2034** (Precedence Research). "Climbing toward $60 billion" is defensible as a trajectory but a reader will infer today's market is near $60B. Consider "projected to reach ~$60B by 2034," or use the current ~$23B. Primary: https://www.precedenceresearch.com/tax-tech-market

5. **Blair-Stanek precision (ch 8): GPT-4 was given the SARA subset, not "the full text of the Internal Revenue Code."** CORRECTED→ SARA = **nine curated IRC sections** (edited to be self-contained), not the entire Code. The 67% (186/276 true/false) is correct. → Soften "the full text of the Internal Revenue Code" to "the tax code sections in the SARA benchmark." Primary: https://arxiv.org/abs/2005.05257

6. **Two mild over-statements to soften (not errors of fact):**
   - Ch 13 "largely because it had not anticipated a round of tariff increases": CBO attributes **~half** the FY2025 revenue miss (Jan-2025 vintage) to tariffs — "largely" is a touch strong. Primary: https://www.cbo.gov/publication/61916
   - Ch 13 CBO "beat the Administration's, the Blue Chip consensus, and the Survey of Professional Forecasters": CBO's own wording is "tend to be **more accurate** than the Administration and the Blue Chip consensus," and "broadly similar" on some measures; comparable vs SPF. Primary: https://www.cbo.gov/publication/61334

7. **Bisbee et al. is a FIVE-author paper (ch 14) — don't let "et al." drop four.** CORRECTED→ Bisbee, **Clinton, Dorff, Kenkel, Larson**, *Political Analysis* **32(4):401–416** (2024). Primary: https://doi.org/10.1017/pan.2024.5

8. **Mei et al. eLocator (ch 14).** CORRECTED→ **PNAS 121(9), e2313925121** (2024). A different article with eLocator e2401336121 / "121(10)" floats online — do not cite that one. Primary: https://www.pnas.org/doi/10.1073/pnas.2313925121

9. **Arrow, *Social Choice and Individual Values* (1951) publisher (ch 15).** CORRECTED→ the **1951 first edition is John Wiley & Sons** (Cowles Commission Monograph 12); Yale UP only published later editions (3rd ed. 2012). If the manuscript/refs say "Yale, 1951," fix it.

10. **Gallup same-sex-marriage recency (ch 16).** CORRECTED→ 71% was the **2022–23 peak**; Gallup then shows **69% (2024)**, ~68% (2025), 65% (May 2026). "1996 = 27% → ~69–71% recent" is fine for 2023–24 but should not be framed as the *current* number. Primary: https://news.gallup.com/poll/710810/support-lgbtq-issues-remains-down-peak.aspx

11. **GSS "not wrong at all" — internal inconsistency + a value that is not primary-verifiable (ch 16).** The manuscript uses **~63% (2022)**; the brief's working figures say **~61% (2022)** — reconcile. The exact 2021/2022/2024 survey-weighted HOMOSEX values are **account-gated** on the GSS Data Explorer and could not be pinned to a primary source. Direction and magnitude ARE corroborated: "always wrong" = **34.9% in 2024** (→ "not wrong at all" mid-50s, consistent with the book's ~56%), and Gallup's parallel moral-acceptance measure fell 71%→~64% (2022→23). → Pull exact values from the Data Explorer (var HOMOSEX) and see discovery below. This is UNVERIFIED-at-primary, corroborated-in-direction.

12. **Finland UBI control-group N (ch 13).** The treatment N (2,000) and €560 are confirmed by the Finnish ministry; the **~173,000–175,000 control figure could not be confirmed on the official page** — verify the exact N before printing.

13. **Manuscript factual error (ch 9): the Kentucky Medicaid resident is a woman.** CORRECTED→ the book says the Deloitte defect "cost a resident **his** Medicaid coverage"; KFF Health News identifies her as **Beverly Likens (she/her)**. Change "his" → "her." (Fix cost $522,455 / 3,500+ hours / ~10 months are all correct.) Primary: https://kffhealthnews.org/health-industry/deloitte-run-medicaid-systems-errors-cost-millions-take-years-to-fix/

14. **Deloitte "$6 billion" is the 2025 figure; the KY/GA anecdotes come from a 2024 piece that says "$5 billion" (ch 9).** CORRECTED/clarify→ the June 2024 KFF investigation said "at least **$5 billion** / 25 states"; the "$6 billion" is from an **Oct 2025** follow-up. The 25-state count holds either way. If pairing the anecdotes with a figure, keep the vintages consistent.

15. **Arkansas case caption is reversed (ch 9).** CORRECTED→ it is **Arkansas Department of Human Services v. Ledgerwood**, 2017 Ark. 308 (DHS was appellant), not "Ledgerwood v. Arkansas DHS." Surname "Ledgerwood" (Bradley Ledgerwood) is right. Nuance: *Ledgerwood* invalidated the algorithm on **state rulemaking** grounds; the **due-process** notice findings came in **related federal** litigation — so don't attribute "due process" to *Ledgerwood* specifically.

16. **FNS "AI may not replace merit personnel" is a paraphrase across two documents, not a verbatim quote (ch 9).** CORRECTED→ fair paraphrase, established by (a) the FNS memo *Use of Advanced Automation in SNAP* (Jan 2024, rev. Feb 2025) and (b) the FNS *AI Framework* (Apr 2024). Don't present it as a single quoted sentence; do cite the two documents (see discovery below).

17. **Robodebt "~470,000 people" (if the author adds figures to ch 9) refers to wrongful debts, not refund recipients.** CORRECTED→ **$751M refunded to ~381,000 people**; ~470,000 = wrongful debts raised (Commonwealth unlawfully raised ~$1.76B against ~433,000 people). The A$1.8B settlement is *Prygodicz v Commonwealth (No 2)* [2021] FCA 634.

---

## Part III — AI benchmarks (ch 8 "The AI can't do your taxes")

- **TaxCalcBench, best model < one-in-three complete returns** — **CONFIRMED (and enrich with exact numbers).** Column Tax, *TaxCalcBench* (arXiv 2507.16126, July 2025). **Strict / complete-return accuracy: Gemini 2.5 Pro 32.35% (best), Claude Opus 4 27.45%, Gemini 2.5 Flash 25.98%, Claude Sonnet 4 23.04%.** The abstract's own framing: models "succeed in calculating less than a third of federal income tax returns." The brief's guesses (Gemini 2.5 Pro <33%, Opus 4 ≈27%) are exactly right. Note the widely-quoted **"23–42%"** range is strict-low to **lenient-high** (the lenient ±$5/line metric runs 38–52%, Gemini 2.5 Pro 51.96%) — the book's "fewer than one in three" tracks the **strict** metric and is correct. Primary: https://arxiv.org/abs/2507.16126

- **The "$3–5 bracket-error" mechanism** — **CONFIRMED.** The paper attributes 15–20% of failures to models "using tax bracket percentage-based calculations instead of proper lookup tables" (the IRS requires tax-table lookups under $100k), which "often produces results off by $3" — precisely the strict-vs-lenient gap. Primary: arXiv 2507.16126, §error analysis.

- **Blair-Stanek et al. GPT-4 on tax law, ~1/3 misread** — **CONFIRMED.** GPT-4 got **186/276 = 67%** on the true/false subset of the SARA benchmark → 33% wrong ("about a third"). Authors: **Andrew Blair-Stanek, Nils Holzenberger, Benjamin Van Durme**, *"OpenAI Cribbed Our Tax Example, But Can GPT-4 Really Do Tax?"*, Tax Notes Federal vol. 180 (Aug 14, 2023); arXiv 2309.09992. (See correction #5 on "full text of the IRC.") Primary: https://arxiv.org/abs/2309.09992

- **MCP timeline (Anthropic Nov 2024 → OpenAI Mar 2025 → Google within months)** — **CONFIRMED.** Anthropic open-sourced MCP Nov 2024 (creators David Soria Parra, Justin Spahr-Summers); OpenAI adopted Mar 26, 2025 (Altman); Google DeepMind followed within months. Primary: https://www.anthropic.com/news/model-context-protocol

- **IRS Agentforce (Nov 2025, three offices, human-in-loop)** — **CONFIRMED.** Announced Nov 21, 2025; deployed across the Office of Chief Counsel, Taxpayer Advocate Service, and Office of Appeals; case summarization/search; agents cannot make final decisions or disburse funds; followed a ~25% workforce reduction (100k→~75k). Primary: https://www.axios.com/2025/11/21/irs-deploys-ai-agents

- **California Poppy** — **CORRECTED** (see correction #2). Core architecture claims (built in-house, runs on state infrastructure, data never leaves state environment) are CONFIRMED. Primary: https://www.cdt.ca.gov/poppy/

---

## Part III — Encoding the law / market facts (ch 9)

- **Avalara acquired for $8.4B in 2022** — **CONFIRMED.** Vista Equity Partners, $8.4B all-cash ($93.50/share); announced Aug 8, 2022, completed Oct 19, 2022. Primary: https://newsroom.avalara.com/2022-10-19-Vista-Equity-Partners-Completes-Acquisition-of-Avalara

- **Column Tax: 1M+ returns; "100% correctness" quote** — **CONFIRMED.** "Today's LLMs cannot 'do taxes' on their own. That's because tax calculations require 100% correctness." (Column Tax, *Introducing Iris* blog); "over 1 million returns filed & over $1 billion in refunds processed." The book's joined rendering is faithful. NB: the quote's home is the *Iris* post (2025) — verify the year on the `@columntax2024` key. Primary: https://www.columntax.com/blog/introducing-iris-our-ai-tax-development-agent

- **Global tax-tech market "toward $60 billion"** — **CORRECTED** (see correction #4). Primary: https://www.precedenceresearch.com/tax-tech-market

---

## Part III — OBBBA (ch 9) — enacted July 4, 2025

- **Public law number** — **CONFIRMED: P.L. 119-21**, 119th Congress (H.R. 1), signed **July 4, 2025**. Note: the short title "One Big Beautiful Bill Act" was **struck during Senate amendment** — the enacted law technically has no short title (the popular name is fine for prose). Primary: https://www.congress.gov/bill/119th-congress/house-bill/1

- **CTC $2,200 + indexing** — **CONFIRMED (minor timing nuance).** OBBBA set the max CTC to **$2,200 per child, effective tax year 2025** (up from $2,000), permanent, **indexed for inflation beginning 2026** (rounded to nearest $100); phase-out thresholds $200k/$400k are **not** indexed. Book's "the maximum is $2,200… in the OBBBA of 2025" is correct for 2026. (The $2,200 took effect in 2025, not 2026 — indexing starts 2026.) Primary: IRS OBBBA provisions; Tax Policy Center CTC briefing.

- **SNAP state benefit cost-share, FY2028 error-rate tiers (0 / 5 / 10 / 15%)** — **CONFIRMED exactly.** From FY2028: <6% PER → 0%; 6–<8% → 5%; 8–<10% → 10%; ≥10% → 15% of benefit costs. **Wrinkle worth a line:** for the first year (FY2028) a state may elect its **FY2025 or FY2026** PER. Primary: CRS R48552 (https://www.congress.gov/crs-product/R48552)

- **FY2025 national SNAP payment error rate = 10.6%** — **CONFIRMED — resolves `[NEEDS CITATION]`.** USDA/FNS released the **FY2025** rate on **June 24, 2026: 10.62%** (overpayment 9.28%, underpayment 1.33%; ~$10.1B improper payments). Book's "10.6 percent" is correct and now has a primary home. (For contrast, FY2024 was 10.93%.) Primary: https://www.usda.gov/about-usda/news/press-releases/2026/06/24/usda-announces-fy-2025-state-payment-error-rates-snap ; https://www.fns.usda.gov/snap/qc/per

- **State share of SNAP admin costs rises 50%→75% in FY2027** — **CONFIRMED.** OBBBA §10106 cuts the **federal** share of state SNAP administrative costs from 50% to 25% (i.e., state share 50→75%) beginning FY2027. Primary: https://www.federalregister.gov/documents/2026/06/24/2026-12696/supplemental-nutrition-assistance-program-changes-in-federal-state-administrative-cost-sharing

- **Medicaid work-requirement verification by end of 2026** — **CONFIRMED — resolves `[NEEDS CITATION]`.** OBBBA requires able-bodied adults 19–64 in expansion states to meet an **80-hour/month** community-engagement requirement, statutory deadline **Dec 31, 2026**; states verify at application and renewal. CMS issued the **interim final rule CMS-2454-IFC** ("Medicaid Program; Community Engagement Requirement for Certain Individuals"), published in the **Federal Register June 3, 2026**, **effective July 31, 2026** (comments due same day). The brief's "effective ~Jul 31 2026?" is confirmed. Primary: https://www.federalregister.gov/documents/2026/06/03/2026-11094/medicaid-program-community-engagement-requirement-for-certain-individuals

- **CBPP ~$9B/year state benefit-cost exposure** — **CONFIRMED.** Using FY2025 error-rate data, CBPP estimates states would owe **roughly $9 billion in total** in new SNAP benefit costs; nearly half of states $100M+. Primary: https://www.cbpp.org/blog/states-first-ever-bill-for-snap-benefits-could-cost-billions

---

## Part III — Government-technology failure record (ch 9)

- **Deloitte eligibility systems (~25 states, ~$6B)** — **CONFIRMED (vintage caveat, see #14).** 25 states; "at least $5B" (June 2024 KFF investigation) → "at least $6B" (Oct 2025 follow-up). Kentucky (**Beverly Likens**, see #13): coverage lapse; fix cost **$522,455** and **3,500+ hours** over ~10 months. Georgia: **25,000+** SNAP/TANF cases, ~2 years to untangle. Reporters: Rachana Pradhan & Samantha Liss. Primary: https://kffhealthnews.org/health-industry/deloitte-run-medicaid-systems-errors-cost-millions-take-years-to-fix/

- **CMS 2023 unwinding: ~500k reinstated after auto-renewal defect** — **CONFIRMED.** CMS: "nearly **500,000** children and other individuals" improperly disenrolled by an **ex parte** renewal defect run at the **household** rather than individual level across **30 states**; alert letter Aug 30, 2023. Supports ch 9 `[@cms2023reinstated]`. Primary: https://www.cms.gov/newsroom/press-releases/coverage-half-million-children-and-families-will-be-reinstated-thanks-hhs-swift-action

- **Australia Robodebt royal commission** — **CONFIRMED — resolves `[NEEDS CITATION]`.** *Report of the Royal Commission into the Robodebt Scheme*, Commissioner **Catherine Holmes**, presented **7 July 2023**; unlawful income-averaging confirmed. Settlement **A$1.8B** (*Prygodicz v Commonwealth (No 2)* [2021] FCA 634). See #17 on the 470k figure. Primary: https://robodebt.royalcommission.gov.au/publications/report

- **Michigan MiDAS ~93% false-fraud rate** — **CONFIRMED.** MiDAS = Michigan Integrated Data Automated System; a state review found ~**93%** of fraud determinations wrong during the no-human-review window (Oct 2013–Aug 2015); ~**40,000** wrongfully accused (~20,000 in that window). *Bauserman v. Unemployment Insurance Agency*, 509 Mich. 673 (2022); **$20M** settlement (Oct 2022). The book's "~93%" and "tens of thousands" are correct. Primary: https://www.courts.michigan.gov/siteassets/case-documents/opinions-orders/msc-term-opinions-(manually-curated)/21-22/bauserman-op.pdf

- **Arkansas algorithmic Medicaid home-care cuts** — **CONFIRMED (caption corrected, see #15).** RUGs algorithm (Brant Fries / interRAI) cut ARChoices hours ~43% avg; **Bradley Ledgerwood** cut 56→32 weekly hours; algorithm invalidated. *Arkansas DHS v. Ledgerwood*, 2017 Ark. 308. Primary: https://www.courtlistener.com/opinion/4441883/ark-dept-of-human-servs-v-ledgerwood/

- **FNS: AI may not replace state merit personnel** — **CONFIRMED — resolves `[NEEDS CITATION]` and is a discovery (documents found).** Established across two FNS documents (see #16): *Use of Advanced Automation in SNAP* (Jan 2024, rev. Feb 2025) — "bots are considered non-merit staff and prohibited from performing these merit staff functions"; and the *AI Framework* (Apr 2024) — "**All AI must be used in compliance with program requirements for the use of merit systems personnel, such as those applicable to SNAP.**" Primary: https://www.fns.usda.gov/framework-artificial-intelligence-public-benefit ; https://www.fns.usda.gov/snap/advanced-automation

- **Medicaid unwinding totals** — **CONFIRMED.** KFF tracker: ~**25.2 million disenrolled**, **56.4 million renewed** (through ~Sept 2024). Primary: https://www.kff.org/report-section/medicaid-enrollment-and-unwinding-tracker-overview/

---

## Part IV — The uncertainty gap (ch 13)

- **CBO AHCA "23 million fewer insured by 2026" (2017)** — **CONFIRMED.** CBO/JCT, *H.R. 1628, American Health Care Act of 2017* (pub 52752, May 24, 2017): +23M uninsured in 2026 vs current law; $119B deficit reduction 2017–2026. Primary: https://www.cbo.gov/publication/52752

- **ACA individual-mandate repeal "13 million fewer insured by 2027"** — **CONFIRMED but MISCITED** (see correction #3). Figure is from CBO pub 53300 (Nov 2017), not the AHCA report. Primary: https://www.cbo.gov/publication/53300

- **Neisser ETI meta-regression (1,720 estimates, 61 studies, mean ~0.30)** — **CONFIRMED.** Carina Neisser, *The Elasticity of Taxable Income: A Meta-Regression Analysis*, **The Economic Journal** 131(640):3365–3391 (2021); distribution peaks near 0.30, most estimates 0–1. Primary: https://academic.oup.com/ej/article/131/640/3365/6263638

- **CBO June-2024 projection underestimated FY2025 revenues by ~6% / $334B (tariffs)** — **CONFIRMED (soften "largely," see #6).** CBO, *The Accuracy of CBO's Budget Projections for Fiscal Year 2025* (pub 61916): projected $4.9T, actual $5.2T, miss $334B/6%. Primary: https://www.cbo.gov/publication/61916

- **CBO forecasts "beat" Administration / Blue Chip / SPF** — **CONFIRMED (soften "beat," see #6).** CBO, *CBO's Economic Forecasting Record: 2025 Update* (pub 61334). Primary: https://www.cbo.gov/publication/61334

- **Squiggle probabilistic-programming language** — **CONFIRMED.** Squiggle, by the Quantified Uncertainty Research Institute (QURI, Ozzie Gooen). Primary: https://www.squiggle-language.com/

- **Finland UBI RCT (2,000 treated, €560/mo, control ~175,000; no first-year employment effect)** — **CONFIRMED (verify control N, see #12).** Kangas, Jauhiainen, Simanainen & Ylikännö (eds.), *Evaluation of the Finnish Basic Income Experiment*, Ministry of Social Affairs and Health 2020:15. 2,000 unemployed, €560/mo tax-exempt, Jan 2017–Dec 2018; preliminary (2019) no significant employment effect; final (May 2020) small positive employment effect + clear wellbeing gains. Control ~173,000 widely reported but not confirmable on the official page. Primary: https://julkaisut.valtioneuvosto.fi/handle/10024/162219

- **Prediction-market / forecasting literature (brief targets; not all cited in ch 13 as read)** — **CONFIRMED.** Tetlock & Gardner, *Superforecasting* (2015): Good Judgment Project superforecasters **beat an intelligence-community prediction market by ~25–30%** (IARPA ACE, 2011–15) — phrase as "25–30%," not a flat 30%. Also Tetlock, *Expert Political Judgment* (2005, Princeton); Mellers et al., *Psychological Science* 25(5):1106–1115 (2014). Wolfers & Zitzewitz, "Prediction Markets," *Journal of Economic Perspectives* 18(2):107–126 (2004). Primary: https://www.aeaweb.org/articles?id=10.1257/0895330041371321

- **IPCC calibrated language ("likely" ≥66%, "very likely" ≥90%)** — **CONFIRMED.** IPCC AR5 Guidance Note on Consistent Treatment of Uncertainties: "likely" = 66–100%, "very likely" = 90–100%. Primary: https://www.ipcc.ch/site/assets/uploads/2017/08/AR5_Uncertainty_Guidance_Note.pdf

- **PWBM accuracy characterization (`@pwbm2024accuracy`)** — **UNVERIFIED.** Could not locate a specific PWBM retrospective-accuracy publication matching the cite; the claim ("generally accurate but with meaningful variance") is soft. → Author should confirm the exact `@pwbm2024accuracy` source exists (PWBM does publish issue-level updates but no obvious standing accuracy-scorecard was found).

---

## Part IV — Simulating opinion (ch 14)

- **Simile "the simulation company" (2026)** — **CONFIRMED (nice enrichment).** Simile is the commercial vehicle of the Stanford **"Generative Agents"** team (Joon Sung Park, Michael Bernstein, Percy Liang, Lainie Yallen) — the same `[@park2023generative]` cited two paragraphs earlier. Emerged from stealth **Feb 12, 2026** with a **$100M Series A led by Index Ventures**; blog post titled "The Simulation Company." Primary: https://simile.ai/blog/the-simulation-company ; Bloomberg (Feb 12, 2026).

- **Argyle et al. "Out of One, Many"** — **CONFIRMED.** All six authors (Argyle, Busby, Fulda, Gubler, Rytting, Wingate); **Political Analysis 31(3):337–351 (2023)**, DOI 10.1017/pan.2023.2; GPT-3; vote study uses ANES 2012/2016/2020. Primary: https://doi.org/10.1017/pan.2023.2

- **Santurkar et al. (OpinionQA) "Whose Opinions Do Language Models Reflect?"** — **CONFIRMED.** ICML 2023, PMLR 202:29971–30004; six authors incl. Liang, Hashimoto. Finding: base/steered LMs misalign with many US groups and skew **left-leaning** after human feedback (a touch sharper than the book's "liberal, educated, Western" paraphrase, which is still fair). Primary: https://proceedings.mlr.press/v202/santurkar23a.html

- **Bisbee et al.** — **CONFIRMED (author list corrected, see #7).** *Political Analysis* 32(4):401–416 (2024). Silicon responses show compressed variance and different (sometimes sign-flipped) regression coefficients.

- **Mei et al. (Turing test / six games)** — **CONFIRMED (eLocator corrected, see #8).** PNAS 121(9):e2313925121 (2024); six canonical games; GPT-4 often statistically indistinguishable from a ~108k-subject human baseline.

- **Park et al. "Generative Agents"** — **CONFIRMED.** UIST '23; arXiv 2304.03442; 25 agents in "Smallville." (This is the team behind **Simile**, above.)

- **Sarstedt et al. (silicon sampling in marketing = pretesting/pilots)** — **CONFIRMED.** *Psychology & Marketing* 41(6):1254–1270 (2024). Primary: https://doi.org/10.1002/mar.21982

- **ESOMAR insights industry ~$140B** — **CONFIRMED.** ESOMAR *Global Market Research 2024*: **~$142B (2023 data)** (up from ~$130B in 2022; a newer figure ~$153B). Book's "~$140 billion+" is correct and conservative. Primary: https://www.esomar.org/global-market-research-report

---

## Part V — Simulating democracy (ch 15)

- **Kansas 2012 "real live experiment"** — **CONFIRMED.** Gov. Sam Brownback, MSNBC *Morning Joe*, June 2012: "We'll have a real live experiment." Business-profits exemption repealed by bipartisan legislative override **June 6, 2017**. Primary: https://www.cbpp.org/research/kansas-provides-compelling-evidence-of-failure-of-supply-side-tax-cuts

- **Achen & Bartels, *Democracy for Realists* (2016)** — **CONFIRMED.** Princeton University Press. "Folk theory" is their term.
- **Caplan, *The Myth of the Rational Voter* (2007)** — **CONFIRMED.** Princeton University Press. Four biases confirmed exactly: **anti-market, anti-foreign, make-work, pessimistic.**
- **Ferraz & Finan (2008), "Exposing Corrupt Politicians"** — **CONFIRMED.** *Quarterly Journal of Economics* 123(2):703–745.
- **Lupia & McCubbins, *The Democratic Dilemma* (1998)** — **CONFIRMED.** Cambridge University Press.
- **Arrow, *Social Choice and Individual Values* (1951)** — **CONFIRMED (publisher corrected, see #9).** Impossibility theorem; 1951 first ed. = John Wiley & Sons.
- **Hanson, futarchy ("vote on values, but bet on beliefs")** — **CONFIRMED, both versions.** *Journal of Political Philosophy* 21(2):151–178 (2013), DOI 10.1111/jopp.12008; earlier 2000 GMU working paper. Slogan wording exact.
- **Feb 2017 "35% didn't know ACA = Obamacare" (Morning Consult/NYT)** — **CONFIRMED — resolves `[NEEDS CITATION]`.** 35% = 17% "different policies" + 18% "don't know." Fielded by **Morning Consult** (n≈2,000); published by **Kyle Dropp & Brendan Nyhan, NYT "The Upshot," Feb 7, 2017.** The book's "Morning Consult/NYT" attribution is right. Primary: https://www.nytimes.com/2017/02/07/upshot/one-third-dont-know-obamacare-and-affordable-care-act-are-the-same.html

---

## Part V — Simulating values (ch 16)

- **GSS same-sex "not wrong at all" series (HOMOSEX)** — **CONFIRMED in direction/magnitude; exact 2021/2022/2024 values UNVERIFIED at primary (account-gated).** 2018 ≈ **57–58%** is a solid anchor. The ~7-point 2022→2024 fall is corroborated: GSS "always wrong" = **34.9% in 2024** (→ "not wrong at all" mid-50s, ≈ the book's ~56%), and Gallup's parallel moral-acceptance measure fell 71%→~64% (2022→23). **Reconcile the manuscript's ~63% (2022) with the brief's ~61% (2022)** — pull exact survey-weighted values from the Data Explorer (var HOMOSEX). Primary (gated): https://gssdataexplorer.norc.org/

- **GSS 2021 mode-change caveat** — **CONFIRMED — key discovery for this chapter.** The GSS moved to mixed-mode collection with the 2021/2022 waves (COVID); the **2021 wave** used an address-based **push-to-web** design (response rate ~17% vs ~50% in 2022). Self-administration removes interviewer/social-desirability pressure and tends to **raise** "not wrong at all," so a 2021–22 peak may be partly a **mode artifact, not pure attitude change**. NORC "cautions data users to carefully examine how a change they are analyzing relates to this methodological shift." → This materially strengthens the chapter's honesty about the 2024 "reversal." (See discoveries.)

- **Gallup same-sex marriage (1996 = 27% → recent)** — **CONFIRMED (freshen recency, see #10).** 1996 = **27%**; majority by 2011; **peak 71% (2022–23)**; **69% (2024)**, ~68% (2025), 65% (May 2026). "~69–71% recent" is right for 2023–24 but not "current." Primary: https://news.gallup.com/poll/710810/support-lgbtq-issues-remains-down-peak.aspx

---

## Part V — Society in silico (ch 17)

- **Westworld frame** — **CORRECTED** (see correction #1). Serac/Rehoboam/season-3-2020 all correct; only the quotation is a paraphrase. Verified verbatim alternative: "For the first time, history has an author." (S3E2, 2020).

---

## Discoveries (one primary detail per area, to strengthen the draft)

- **AI benchmarks:** Name the mechanism precisely — Gemini 2.5 Pro's strict score (32.35%) roughly **doubles** to 51.96% under a ±$5/line lenient metric, and the gap is almost entirely models doing **bracket-percentage math instead of IRS tax-table lookups**, "off by $3." Also: SARA (the Blair-Stanek benchmark) was the dataset **OpenAI used in the GPT-4 launch demo** — hence the title "OpenAI Cribbed Our Tax Example."
- **OBBBA:** The FY2025 SNAP error rate (10.62%) landed **June 24, 2026** — days before the book's "mid-2026" vantage — and OBBBA lets states pick their **FY2025 or FY2026** rate for the first cost-share year, a concrete "administrative accuracy is now a budget line" detail.
- **Uncertainty/CBO:** The "13 million" mandate figure has its **own** CBO report (pub 53300) — citing it separately both fixes the miscitation and lets the draft note CBO's *$338B* deficit-reduction score, the number that actually drove the 2017 repeal-via-tax-bill.
- **Westworld:** Swap the invented quote for the real, sharper line — *"For the first time, history has an author."* — which makes the closed-system critique land on Serac's actual words.

- **Government-tech (Robodebt):** a quote-ready primary line from the royal commission's own Overview (p. xxix): *"Robodebt was a crude and cruel mechanism, neither fair nor legal, and it made many people feel like criminals."* — a far stronger anchor than a paraphrase for the "automating judgment without a check" argument.
- **Government-tech (FNS guidance):** the boundary the chapter leans on is real and now has its document — the FNS *AI Framework* (Apr 2024): *"All AI must be used in compliance with program requirements for the use of merit systems personnel, such as those applicable to SNAP,"* backed by the automation memo's blunter line that *"bots… [are] prohibited from performing these merit staff functions."* The book can now quote the boundary instead of asserting it.
- **Opinion (Simile):** the "simulation company" the chapter name-checks is literally the **Generative Agents** team (Park, Bernstein, Liang) commercializing — a clean through-line from `[@park2023generative]` to `[@simile2026company]`, with a $100M Index-led round (Feb 2026) as the "escaping the lab" evidence the chapter wants.
- **Values (GSS mode change):** the single most useful addition to ch 16 — the 2021/2022 GSS mixed-mode switch means the pre-2024 "climb" and the 2024 "reversal" both sit partly on a methodological discontinuity. Naming it turns the chapter's central "miss" from an unexplained surprise into a doubly-honest one (the model missed it *and* part of the series it trusted may be a mode artifact).

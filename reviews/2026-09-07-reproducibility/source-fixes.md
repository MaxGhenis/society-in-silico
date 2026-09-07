# Focused source review fixes

The independent source delta review of exact `d43b859` identified two P2
completeness findings, accepted by the coordinator. The report is preserved
unchanged in `independent/source-delta-review.md`. These owner fixes continue the
delivered draft PR #5 at `755f75d`; they do not claim targeted rereview approval.

| Finding | Focused repair | Primary evidence |
| --- | --- | --- |
| Chapter 3:61 and chapter 6:67 omitted the household denominator of the New York linked-record rates. | Chapter 3 now names households receiving each of SNAP, TANF/General Assistance and housing assistance. Chapter 6 explicitly says actual SNAP recipient households. The dates, 43/63/36 percentages, no-receipt-recorded language and person-level Social Security sentence are unchanged. | Meyer–Mittag section I.A, printed p.180, states that individual links are aggregated to households; Table 1, printed p.183, supplies the recipient-household rates. The source review's extract is `society-source-review/artifacts/evidence/meyer-mittag.txt` in the sprint directory. |
| Chapter 6:49's continuous official-calculator claim exceeded the replacement citation's coverage. | The sentence now says the team publishes UK comparisons of national tax and benefit aggregates with official statistics and UKMOD estimates. It no longer asserts continuous execution, named household-calculator checks or a discrepancy-handling procedure from this citation. | The same first-party notebook pinned at `5e57717fcb7fa12c969e0aa33eeb1d9786fccaeb` contains national aggregate comparisons for 2023–2025. The source review's complete unexecuted extract is `society-source-review/artifacts/evidence/pe-uk-validation-source.txt`. |

No new source campaign, citation, computation, parameter, weight or raw receipt
was introduced. The original six editorial commits and original checkouts remain
preserved. All other recovered source limits, including Pennsylvania's credit,
the Finnish activation-rule confound and unresolved prediction marker, remain.

Fresh validation is recorded in `logs/source-fixes/`: `make check` passes with
19 citation / 25 verification / 2 decision markers; source checks confirm the
entire marker sequence, exact Social Security sentence and protected files are
unchanged; the full HTML and PDF builds pass; the artifact validator confirms
notebook/JSON/chapter values and downloads still agree. WebKit inspected chapters
3 and 6 at 1440px and 390px without horizontal overflow or page/HTTP errors. The
three changed passages were visually inspected in PDF physical pages 36, 56 and
57 and in the HTML screenshots. No costly unchanged national pipeline was rerun.

Screenshots and local validation helpers are at
`/Users/maxghenis/capacity-sprint-20260907/society/source-fixes-validation/`
and `output/playwright/source-fixes-review/` in the isolated working tree.
`SOURCE-FIXES-REVIEW-READY.md` in the lane directory supplies the exact fix head,
diff and hashes for the coordinator. Targeted rereview remains pending; all
editorial, partner and publication gates remain in force.

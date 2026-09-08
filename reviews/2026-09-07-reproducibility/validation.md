# Validation record

The completed continuation retains the executed calculations from `61c5ce5` and
integrates the FINAL recovered sources plus explicit link/display repairs through
`d43b859`. Independent computation evidence is committed at `cfed6e3`. Later
validation/report commits do not alter the computation, notebook or receipts.

Both receipts name SHA256
`9776b561a04d62feea227b55bb732b25ead823dde1b3c3063bf4696c8dc9051b`
for `scripts/pe_computed_numbers.py`, matching the unchanged executed source.
The notebook ran all four code cells with managed PolicyEngine 5.3.0 / US 1.764.6
on the hash-verified certified local Build P dataset. The owner's separate final
national execution reproduced the preceding completed run to within $0.000069;
poverty outputs matched exactly. Weighted JSON aggregate checkpoints reconcile
to the saved deltas within $0.046. Details are in `national-validation.json`.

| Check | Result |
| --- | --- |
| Focused reproduction tests | 9 passed; also independently passed in the frozen review checkout |
| Ruff 0.16.6 | Passed after parenthesizing a validator string; no calculation change |
| `UV_OFFLINE=1 make check` | Passed; 7 advisory concept warnings; 19 citation / 25 verification / 2 decision markers remain |
| `make build` | Passed; all 20 HTML inputs rendered |
| `scripts/check_pe_artifacts.py` | Passed; source hashes, notebook outputs/counts, receipt-derived chapter numbers, anchors, byte-identical notebook and supporting downloads |
| `quarto render --to pdf --output-dir output/pdf` | Passed; 158-page PDF using local LuaLaTeX |
| WebKit over host loopback | 10 page/viewport checks: chapters 1/3/6/7/13 at 1440px and 390px; no page/HTTP errors or horizontal overflow; actual notebook download SHA matches |
| Full generated-book links/assets | 1,346 internal targets and anchors, zero failures |
| External HTTP reachability | All 167 unique URLs checked: 110 status 200, 2 status 202, 50 status 403, 5 network/TLS/DNS errors; four confirmed 404s repaired from primary evidence |

External access denials and network failures remain visible in the exception
inventory. Unchanged URLs reuse their same-session check; repaired URLs were
newly checked. External fragment targets were not validated. This is not a claim
that every external source is reachable by an automated client or that all
external-source claims in the manuscript were audited.

The bibliography/footnote wrapping fix was verified using the actual generated
stylesheet, not only an injected-style probe. Desktop and mobile screenshots show
readable text and complete URLs, including Pennsylvania's credit, the Finnish
activation-rule confound and explicit model-prediction VERIFY marker, and the
scoped SNAP/SSI source statements. PDF inspection covers the affected calculation
and source passages plus repaired bibliography entries. Both unchanged notebook
figures were inspected in the original completed run.

The original restricted environment blocked browser/Jupyter sockets. The
continuation's real WebKit browser now works on host loopback; Chrome/CDP was
never used. The notebook's committed in-process executor remains valid execution
evidence and explicitly records that backend; no Jupyter execution is claimed.

## Independent computational review

The coordinator's host reviewer reported **no actionable computational findings**
at `61c5ce5`. All supplied hashes match the unchanged computation/receipt files.
The review reran 15 scalar household calls and targeted national ACA/BHP terms,
checked the installed formulas, managed MicroSeries weights and entity mapping,
recomputed receipt/summary arithmetic, and ran the nine tests. It did not rerun
the entire national poverty/fiscal pipeline.

The targeted run found zero reform changes in assigned PTC, annualized premium
tax credit and BHP, despite a $156.80m raw ACA entitlement increase. No PTC/BHP
expenditure addition is needed for this score. This finding is specific to the
frozen reform/data; other reforms need explicit coverage of nonzero terms. See
`independent/review.md` and the preserved scripts, receipts, logs and manifests.

This verdict does not cover later source integration, unrelated manuscript
claims, empirical validation of every household, behavior or uncertainty bands.
Coordinator source review remains pending. Publication, author and partner gates
remain separate.

## Artifact locations

- Refreshed committed logs and inventories: `logs/continuation/`.
- Structured check record and PDF/notebook hashes: `continuation-validation.json`.
- Full PDF: `output/pdf/Society-in-Silico.pdf` in the isolated working tree.
- Browser screenshots: `output/playwright/recovered-source-review/`.
- PDF screenshots and link-source caches:
  `/Users/maxghenis/capacity-sprint-20260907/society/review-head-validation/`.
- Exact review handoff:
  `/Users/maxghenis/capacity-sprint-20260907/society/REVIEW-READY.md`.

The PDF and HTML remain local review artifacts; neither was published or merged.

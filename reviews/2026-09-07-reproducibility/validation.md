# Validation record

The notebook executed all four code cells with managed PolicyEngine 5.3.0 / US
1.764.6 on the certified local Build P dataset. Both calculation receipts name
SHA256 `9776b561a04d62feea227b55bb732b25ead823dde1b3c3063bf4696c8dc9051b`
for `scripts/pe_computed_numbers.py`, matching the final source.

The final national run reproduced the earlier completed run to within $0.000069;
all poverty outputs were identical. The JSON aggregate checkpoints preserve
weighted child counts and rates exactly, and their differences in weighted dollar
totals reconcile to weighted sums of changes within $0.046. See
`national-validation.json` for each difference and the validation tolerances.

| Check | Result |
| --- | --- |
| `.venv-pe/bin/python -m pytest tests/test_pe_computed_numbers.py -q` | 9 passed |
| Ruff on computation, reporting, executor, artifact validator and tests | Passed |
| `UV_OFFLINE=1 make check` | Passed; 7 advisory concept warnings; 19 citation / 24 verification / 2 decision markers remain |
| `make build` | Passed; all 20 HTML book inputs rendered |
| `.venv-pe/bin/python scripts/check_pe_artifacts.py` | Passed; final source hashes, execution counts, rounded numbers, anchors, and copied notebook/resources |
| `quarto render --to pdf --output-dir output/pdf` | Passed; local LuaLaTeX |
| Visual inspection | Both notebook figures and PDF physical pages 36, 54, 55, 59, 63, 109, 113, 115 inspected |

PDF inspection covered the new MTR, historical/current household CTC, national
score and uncertainty language, Finland and AHCA corrections, and the chapter
3/7 source updates. Text, citations and footnotes are legible without clipping or
overlap. Automatic numbering previously produced “8 Chapter 6”; disabling it
preserves the authored chapter numbers consistently. Some unrelated verification
markers remain visible because this is a review draft.

The HTML checks verify actual generated pages and resources, but are not browser
screenshots. Local WebKit launch aborted under the environment's restrictions;
Chrome/CDP was not used. Jupyter kernel startup was also blocked by socket
permissions, so the notebook's plain Python cells ran through the committed
in-process executor, which records outputs and errors and identifies its backend.

Logs are saved in this review directory and in the sprint lane at
`/Users/maxghenis/capacity-sprint-20260907/society/`. The full PDF is at
`output/pdf/Society-in-Silico.pdf`; the inspected PNGs are in the lane's
`rendered-page-inspection/`. Neither artifact was published.

The Subfleet semantic-review attempt was blocked by DNS and is not a pass.
The household fixtures, source checks and accounting checks do not substitute for
an independent model audit. Static model results also do not provide a behavioral
forecast or confidence interval.

# Reproducing the book's PolicyEngine calculations

The notebook `pe-computed-numbers.ipynb` and `../pe_computed_numbers.py` reproduce
the household marginal-rate examples and the 2026 Child Tax Credit (CTC)
full-refundability score used in chapters 6 and 13.

## Environment

From the repository root:

```sh
uv venv --python 3.14 .venv-pe
uv pip install --python .venv-pe/bin/python -r scripts/notebooks/requirements.txt
.venv-pe/bin/python scripts/pe_computed_numbers.py households
.venv-pe/bin/python scripts/pe_computed_numbers.py national
```

To execute and save every notebook cell, including both calculations:

```sh
.venv-pe/bin/python scripts/execute_pe_notebook.py
.venv-pe/bin/python -m pytest tests/test_pe_computed_numbers.py -q
```

The executor runs the notebook's plain Python cells in order and checkpoints
outputs after each cell. It opens no Jupyter ports (kernel startup is blocked in
the sprint environment). It records that execution backend in notebook metadata;
the same cells also run in an interactive Jupyter kernel. The notebook imports
the computation module, so clone the repository rather than downloading only
the notebook. Figures and numeric receipts are in `../results/pe-computed-numbers/`.

The September 7, 2026 run installed entirely from the local uv cache by adding
`--offline` to the first two commands. The complete environment is pinned in
`requirements.txt` (Python 3.14.4, macOS arm64). PolicyEngine 5.3.0 was verified
against the [PyPI release listing](https://pypi.org/project/policyengine/), which
lists its August 30, 2026 release. Its bundled US model is 1.764.6, core 3.30.1,
and certified national dataset is Microcosm's `populace_us_2024`, Build P:
`populace-us-2024-buildp-sparse-rmloss100-cae8640-20260728T011454Z`.

The national command uses only a locally cached copy of that exact dataset, or
an explicit `--dataset-file /path/to/populace_us_2024.h5`. It verifies SHA256
`48b9d479fb4fd1c3537f9383ce4697d130b6f618658409d74f6233c43b994c7e` before
calling `pe.us.managed_microsimulation()`. A missing or mismatched file fails
without downloading or replacing it. No private microdata is committed.

National runs use one baseline/reform pipeline at a time with numerical threads
limited to one. They require substantially more memory and time than household
calculations. All results are static estimates with the model's take-up
assumptions held fixed, not forecasts or benefit determinations.

## Calculation conventions

- **Marginal rates:** $100 forward earnings differences over $0–$60,000, plus
  the chapter's $38,000→$39,000 comparison. Net income includes modeled non-cash
  benefits and excludes health valuations. It is not a bank-balance measure.
- **Households:** 35-year-old single parents, $18,000 annual rent, no voucher.
  NC has children aged 8 (SSI disability) and 5; NY has one child aged 8 (SSI
  disability). Explicit parent counts enable parental SSI deeming; explicit
  absence of an SSI spouse prevents the convenience API's single marital-unit
  grouping from introducing spousal deeming. Other inputs and program take-up
  use the pinned model defaults.
- **Capital gains:** an NYC single filer, age 45, with $30m in qualifying
  long-term gains and a further $10,000. This does not describe all carried
  interest or compensation.
- **CTC receipt:** refundable CTC plus applied nonrefundable credits in a case
  where CTC is the only such credit (checked). The model's `ctc` variable alone
  is an entitlement before tax-liability limits. The reform retains the $2,200
  maximum and high-income phase-out; it removes refundability restrictions.
- **National score:** managed MicroSeries with explicit `map_to`. The fiscal
  calculation follows the components of PolicyEngine 5.3.0's
  `tax_benefit_models/us/analysis.py:calculate_budgetary_impact`, including the
  model's federal and state health-cost variables once. Net household gains and
  federal income-tax revenue loss are distinct reported measures. The federal,
  state and unattributed accounting partition is preserved.
- **Filing and health interactions:** fixed take-up assumptions do not mean
  fixed filing status. In the pinned model, `eligible_for_refundable_credits`
  depends on refundable CTC; `tax_unit_is_filer` combines that eligibility with
  the dataset's filing propensities. Filing status feeds both ACA PTC and
  Medicaid's filer/non-filer household rules. The saved run therefore reports
  health-program changes as well as income-tax changes. This code path explains
  why such an interaction is possible; it is not an independent validation of
  each affected household or a behavioral forecast. Earnings remain fixed.
- **Uncertainty:** no behavioral scenarios or confidence interval have been
  estimated. The old dense Enhanced CPS results are not reproduced by this
  different certified population. A new score must state its own data vintage.

## Book and artifact validation

After executing the notebook, build the book and check the complete artifact chain:

```sh
make check
make build
.venv-pe/bin/python scripts/check_pe_artifacts.py
```

The last command verifies that both receipts match the final computation source,
the notebook cells executed without errors, chapters 6 and 13 contain the rounded
results derived from those receipts, internal anchors resolve, and the downloadable
notebook and bundled resources exactly match the repository files.

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

# Independent computation review — Society in Silico

**Verdict: no actionable computational findings at frozen head `61c5ce5ee55032419d1021bbde6bd9e62dc27884`.** The specified household outputs and the national point-estimate accounting are supported within the stated model/data scope. This is a scoped computational review, not approval of the entire manuscript or later editorial integration.

Reviewed 2026-09-07 on the host. The immutable snapshot is `/Users/maxghenis/capacity-sprint-20260907/society/computation-review-61c5ce5`. No owner-checkout edits, commits, pushes, publication, external messages, paid compute, or resets were performed. The disconnected earlier external reviewer is not counted as approval.

## Verified evidence

- **Real pinned software and data:** independently inspected runtime package metadata: Python 3.14.4, PolicyEngine 5.3.0, US 1.764.6, core 3.30.1, MicroSeries/microdf-python 1.3.0 and NumPy 2.5.3. The installed bundle manifest hash matches both saved receipts (`57c6fe9c5c370ea2b9460120656004b1a583db06cabb6c774551effc3c125695`). Both receipt source hashes match frozen `scripts/pe_computed_numbers.py` (`9776b561a04d62feea227b55bb732b25ead823dde1b3c3063bf4696c8dc9051b`).
- **Certified population:** independently ran the local dataset integrity check, confirming Build P `populace-us-2024-buildp-sparse-rmloss100-cae8640-20260728T011454Z`, SHA256 `48b9d479fb4fd1c3537f9383ce4697d130b6f618658409d74f6233c43b994c7e`. Read-only H5 table shapes confirm 57,240 households, 166,321 person records, 79,729 tax units and 59,900 SPM units. Record counts are not weighted population totals. No private microdata was copied into review artifacts.
- **Baseline and reform:** inspected actual installed parameters. 2026 full refundability defaults to false; the CTC maximum is $2,200 for children below 17; health-benefit valuation defaults to false. The script explicitly holds the latter convention constant and changes only full refundability for 2026 (`scripts/pe_computed_numbers.py:370`). Historical full refundability is false/true/false in 2020/2021/2022. National earnings are held fixed; filing propensities are fixed inputs, while eligibility-dependent filing can change.
- **Weighting and units:** `run_national` maps annual dollar quantities to households and poverty/child flags to persons (`scripts/pe_computed_numbers.py:396`). Actual installed core `Microsimulation` derives entity weights from calibrated household weights internally; group-to-household mapping apportions group values through members and sums them, avoiding duplication. The book code retains MicroSeries through arithmetic and weighted aggregation. `person_in_poverty` projects the SPM-unit `in_poverty` flag; `is_child` means age below 18. Filtering children before `.mean()` and `.sum()` is correct (`scripts/pe_computed_numbers.py:500`). No manual person/tax-unit/SPM weights or unweighted population arrays were used by the implementation or review.
- **Fresh scalar household reproduction:** 15 separate `pe.us.calculate_household` calls, without the original earnings axes, match the frozen saved curve points and chapter examples. NC $38,000→$39,000 gives $73 higher modeled net income, $500 lower SSI, and a 92.7% finite-increment marginal rate; NY $30,000→$30,100 gives -$4.8046875 and 104.8046875%. NC SSI is positive at $55,100 and zero at $55,200. The official [SSA 2026 child-deeming table](https://www.ssa.gov/ssi/text-child-ussi.htm) independently supports the $4,598/month boundary for one parent and one ineligible child, under its stated assumptions; North Carolina is listed as not supplementing the federal child benefit.
- **CTC:** fresh calls reproduce $1,875/$7,200/$1,875 for the same ages and earnings under 2020/2021/2022 rules, $1,875 in the 2026 baseline, and $4,400 under the reform at earnings of $0, $15,000 and $60,000. The implementation checks that CTC is the only nonrefundable credit before using applied, capped nonrefundable credits, rather than mistaking the uncapped entitlement for receipt (`scripts/pe_computed_numbers.py:240`).
- **Capital gains:** fresh scalar calls at $30m and $30.01m produce a $2,380 federal-tax increase, $1,478 state/city-tax increase and 38.58% combined finite-increment rate. This is the specified NYC long-term-gains case, not a claim about all carried interest or ordinary compensation.
- **National arithmetic and artifacts:** independently recomputed summary values from the frozen household/national JSON. They exactly match `summary.json`; the four notebook cells have sequential execution counts and no error outputs, and the printed values match the receipts. The chapter 6 examples (lines 23, 25, 43 and 79) and chapter 13 national paragraph (line 79) round those same outputs correctly. Child population 77,947,677.2421 × poverty rates exactly gives the saved 13,264,611.3520 and 11,787,302.0601 poor-child totals; the reduction is 1,477,309.2919, or 1.8952576192 percentage points. These are model-weighted estimates, not observed 2026 population counts.
- **Existing focused tests:** all nine tests in `tests/test_pe_computed_numbers.py` pass in the isolated frozen snapshot. They cover unequal-weight child arithmetic, exclusion of adults, alignment, preservation of a mismatched data file, CTC entitlement/receipt distinction, SSI boundary and all household increment identities.

## Fiscal issue investigated and resolved for this reform

The frozen fiscal calculation (`scripts/pe_computed_numbers.py:477`) correctly reproduces the signs and components of the installed PolicyEngine 5.3.0 budget helper. However, that helper's shared-funding health-cost variables cover Medicaid/CHIP/MSP, while the model's normal refundable-credit list excludes ACA PTC and health valuations are switched off. The saved raw `aca_ptc` increase of $156.80m therefore warranted a separate check; copying the API formula alone did not establish completeness.

I independently ran a targeted managed national baseline/reform calculation on the same hash-verified bundle, retaining MicroSeries and `map_to="household"` throughout. The resulting annual weighted changes were:

| Variable | Reform minus baseline |
|---|---:|
| `aca_ptc` (before take-up) | $156,795,505.1766565 |
| `assigned_aca_ptc` (after take-up) | $0 |
| `premium_tax_credit` (annualized) | $0 |
| `basic_health_program` | $0 |

Thus the raw entitlement change is **not an omitted fiscal expenditure in this run**. The reported $20,868,288,652.26 net fiscal cost needs no PTC/BHP addition. The -$20.02m combined federal/state shared-health-cost change is included once. The $20,885,352,314.07 `income_tax` revenue loss and $20,888,305,889.45 household net-income gain are distinct measures and are correctly distinguished in the receipts. Their small resource-identity discrepancy is about $2,450 nationally, consistent with the disclosed float32 aggregation tolerance, and immaterial to printed rounding.

This zero-result verification is specific to the frozen reform and data. If the accounting helper is reused for a reform with nonzero assigned PTC/BHP effects, those expenditure terms need explicit coverage. It would be useful to retain these annual zero deltas in future receipts and label raw `aca_ptc` as entitlement before take-up; neither observation is a blocking defect in the present numbers. Do not add raw `aca_ptc` to fiscal cost or count both assigned and annualized PTC.

## Limits and follow-through

This review independently reran representative households and the targeted national health terms, not the full national poverty/fiscal pipeline. The frozen owner's `reviews/2026-09-07-reproducibility/national-validation.json` records a separate full repeat with identical poverty and monetary differences below $0.0001; that is prior execution evidence, not a second full execution performed by this reviewer. I inspected the weighting, formulas, provenance and independent arithmetic supporting those saved totals.

I did not re-run the full HTML/PDF build or re-audit unrelated chapter claims. Model take-up, filing responses, imputations, calibration and future-year uprating remain conditional assumptions. No confidence interval, behavioral forecast, prevalence estimate for the illustrative marginal rates, or independent empirical validation of every affected household has been established. The notebook/README and reviewed chapter paragraphs appropriately state these limits. The external-source editorial integration occurring after this frozen head is outside this verdict; revised computational code or receipts should receive a focused recheck before reusing this conclusion.

## Review artifacts

All under `/Users/maxghenis/capacity-sprint-20260907/society/computation-review-61c5ce5/`:

- `independent_household_checks.py`, `independent-household-results.json`, `independent-household-checks.log`: 15 fresh scalar calls and comparisons.
- `independent_health_accounting.py`, `independent-health-accounting-results.json`, `independent-health-accounting.log`: targeted managed national run; baseline/reform aggregate checkpoints under `output/pe-reproduction/`.
- `independent-artifact-arithmetic.json`: receipt/summary/notebook arithmetic and H5 table counts.
- `model-evidence/`: 12 copied installed primary code/parameter files and their SHA256 hashes, preserving the weighting and fiscal trace.
- `independent-review-manifest.json`: frozen head, source/artifact hashes, commands and skills read.

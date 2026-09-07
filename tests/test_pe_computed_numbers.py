"""Statistical and policy-boundary checks for the book's reproduction."""

import hashlib
import importlib.util
import json
from pathlib import Path

import pytest
from microdf import MicroSeries

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "pe_numbers", ROOT / "scripts/pe_computed_numbers.py"
)
pe_numbers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pe_numbers)


def test_child_rates_use_child_population_and_survey_weights():
    # A large adult record must not enter either child numerator/denominator.
    weights = [10, 90, 1000, 20]
    baseline = MicroSeries([True, False, True, True], weights=weights)
    reform = MicroSeries([False, False, True, False], weights=weights)
    child = MicroSeries([True, True, False, True], weights=weights)
    result = pe_numbers.child_poverty_statistics(baseline, reform, child)
    assert result["child_population"] == 120
    assert result["baseline"]["child_poverty_rate"] == 0.25
    assert result["reform"]["child_poverty_rate"] == 0
    assert result["percentage_point_reduction"] == 25
    assert result["children_lifted_out"] == 30


def test_child_rates_reject_unweighted_or_misaligned_inputs():
    child = MicroSeries([True, False], weights=[1, 9])
    with pytest.raises(TypeError):
        pe_numbers.child_poverty_statistics([True, False], child, child)
    with pytest.raises(ValueError, match="align"):
        pe_numbers.child_poverty_statistics(child, child.set_axis([4, 5]), child)


def test_offline_dataset_check_preserves_mismatched_existing_file(tmp_path):
    source = tmp_path / "certified.h5"
    source.write_bytes(b"certified fixture")
    receipt = {
        "us_release": {
            "datasets": {
                "populace_us_2024": {
                    "path": "populace_us_2024.h5",
                    "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                }
            }
        }
    }
    destination = tmp_path / "run/data/populace_us_2024.h5"
    destination.parent.mkdir(parents=True)
    destination.write_bytes(b"preexisting file")
    with pytest.raises(FileExistsError):
        pe_numbers.stage_cached_dataset(receipt, tmp_path / "run", source)
    assert destination.read_bytes() == b"preexisting file"


def test_fiscal_cost_includes_health_savings_and_preserves_attribution():
    cost = pe_numbers.fiscal_statistics(
        {
            "household_tax": -100,
            "household_benefits": 10,
            "federal_benefit_cost": -6,
            "state_benefit_cost": -4,
            "income_tax": -98,
            "employee_payroll_tax": 0,
            "state_income_tax": -2,
        }
    )
    assert cost["tax_and_nonhealth_benefit_cost"] == 110
    assert cost["total_cost"] == 100
    assert cost["federal_attributed_cost"] == 92
    assert cost["state_attributed_cost"] == -2
    assert cost["unattributed_cost"] == 10


@pytest.fixture(scope="module")
def households():
    return json.loads(
        (ROOT / "scripts/results/pe-computed-numbers/households.json").read_text()
    )


def test_ctc_applies_refundability_not_uncapped_entitlement(households):
    ctc = households["ctc"]
    at_15k = ctc["earnings"].index(15_000)
    # 15% of earnings over $2,500 at this zero-liability income; two $2,200 credits.
    assert ctc["baseline"]["ctc_received"][at_15k] == pytest.approx(1875, abs=0.02)
    assert ctc["reform"]["ctc_received"][at_15k] == pytest.approx(4400, abs=0.02)
    assert ctc["baseline"]["ctc_received"][0] == 0
    assert ctc["reform"]["ctc_received"][0] == 4400


def test_historical_ctc_holds_family_inputs_fixed(households):
    history = households["historical_ctc"]
    assert [
        history[str(year)]["ctc_received"] for year in (2020, 2021, 2022)
    ] == pytest.approx([1875, 7200, 1875], abs=0.02)
    assert (
        history["2020"]["inputs"]["people"]
        == history["2021"]["inputs"]["people"]
        == history["2022"]["inputs"]["people"]
    )


def test_ssi_parental_deeming_matches_2026_ssa_eligibility_boundary(households):
    # SSA's 2026 table: one parent, one ineligible child, earned income only:
    # eligibility below $4,598/month = $55,176/year (no NC child supplement).
    # https://www.ssa.gov/ssi/text-child-ussi.htm
    curve = households["curves"]["nc_two_children"]
    output = curve["outputs"]
    assert output["ssi"][curve["earnings"].index(55_100)] > 0
    assert output["ssi"][curve["earnings"].index(55_200)] == 0
    assert not any(output["spousal_deemed_income"])
    lo, hi = (curve["earnings"].index(e) for e in (38_000, 39_000))
    assert output["ssi"][hi] - output["ssi"][lo] == pytest.approx(-500, abs=0.02)


def test_all_curve_increments_reconcile_to_taxes_and_benefits(households):
    for curve in households["curves"].values():
        output = curve["outputs"]
        for i, mtr in enumerate(curve["mtr_100_dollar_forward"]):
            tax_change = output["household_tax"][i + 1] - output["household_tax"][i]
            benefit_change = (
                output["household_benefits"][i + 1] - output["household_benefits"][i]
            )
            health_cost_change = (
                output["household_health_costs"][i + 1]
                - output["household_health_costs"][i]
            )
            assert mtr * 100 == pytest.approx(
                tax_change - benefit_change + health_cost_change, abs=0.02
            )

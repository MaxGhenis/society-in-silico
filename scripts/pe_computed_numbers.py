"""Reproduce the PolicyEngine calculations in chapters 6 and 13, offline.

The notebook imports this module so there is one implementation of each run.
Population calculations retain MicroSeries throughout; no manual survey weights.
"""

from __future__ import annotations

import argparse
import gc
import hashlib
import importlib.metadata as md
import json
import os
import platform
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

# Bound local numerical concurrency before importing PolicyEngine/numpy.
for _name in (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
):
    os.environ[_name] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "scripts" / "results" / "pe-computed-numbers"
YEAR = 2026
PINS = {
    "policyengine": "5.3.0",
    "policyengine-us": "1.764.6",
    "policyengine-core": "3.30.1",
}
REFUNDABILITY = "gov.irs.credits.ctc.refundable.fully_refundable"
HEALTH = "gov.simulation.include_health_benefits_in_net_income"


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def provenance() -> dict:
    versions = {name: md.version(name) for name in PINS}
    if versions != PINS:
        raise RuntimeError(
            f"Use the pinned environment: expected {PINS}, found {versions}"
        )
    manifest_path = Path(
        md.distribution("policyengine").locate_file(
            "policyengine/data/bundle/manifest.json"
        )
    )
    manifest = json.loads(manifest_path.read_text())
    return {
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "packages": {
            **versions,
            "microdf-python": md.version("microdf-python"),
            "numpy": md.version("numpy"),
        },
        "bundle_manifest_sha256": sha256(manifest_path),
        "us_release": manifest["data_releases"]["us"],
        "script_sha256": sha256(Path(__file__)),
        "year": YEAR,
    }


def single_parent(state: str, children: list[dict]) -> dict:
    people = [
        {
            "age": 35,
            "is_male": False,
            "employment_income": 0,
            "pre_subsidy_rent": 18_000,
        },
        *children,
    ]
    for i, person in enumerate(people):
        person.update(
            {
                "is_tax_unit_head": i == 0,
                "is_tax_unit_spouse": False,
                "is_tax_unit_dependent": i > 0,
                "own_children_in_household": len(children) if i == 0 else 0,
                # The convenience API puts everyone in one marital unit. None of
                # these unmarried people is an ineligible spouse of an SSI claimant.
                "is_ssi_ineligible_spouse": False,
            }
        )
    return {
        "people": people,
        "tax_unit": {"filing_status": "HEAD_OF_HOUSEHOLD"},
        "spm_unit": {"takes_up_housing_assistance_if_eligible": False},
        "household": {"state_code": state},
        "year": YEAR,
    }


def household_columns(result) -> dict:
    """Select ordinary household-axis lists, never population MicroSeries."""
    columns = {
        name: getattr(result.household, name)
        for name in (
            "household_net_income",
            "household_tax",
            "household_benefits",
            "household_health_costs",
            "household_health_benefits",
        )
    }
    columns.update(
        {
            name: getattr(result.tax_unit, name)
            for name in (
                "income_tax",
                "employee_payroll_tax",
                "state_income_tax",
                "eitc",
                "refundable_ctc",
                "income_tax_capped_non_refundable_credits",
            )
        }
    )
    columns["snap"] = result.spm_unit.snap
    columns["ssi"] = [sum(amounts) for amounts in zip(*(p.ssi for p in result.person))]
    columns["spousal_deemed_income"] = [
        sum(amounts)
        for amounts in zip(
            *(p.ssi_income_deemed_from_ineligible_spouse for p in result.person)
        )
    ]
    return columns


EXTRAS = [
    "income_tax",
    "employee_payroll_tax",
    "state_income_tax",
    "refundable_ctc",
    "income_tax_capped_non_refundable_credits",
    "household_health_costs",
    "household_health_benefits",
    "ssi",
    "ssi_income_deemed_from_ineligible_spouse",
    "housing_assistance",
]


def run_households() -> dict:
    import policyengine as pe

    receipt = provenance()
    cases = {
        "nc_two_children": single_parent(
            "NC", [{"age": 8, "is_ssi_disabled": True}, {"age": 5}]
        ),
        "ny_one_child": single_parent("NY", [{"age": 8, "is_ssi_disabled": True}]),
    }
    curves = {}
    for name, inputs in cases.items():
        print(f"Computing {name} earnings curve", flush=True)
        result = pe.us.calculate_household(
            **inputs,
            reform={HEALTH: False},
            extra_variables=EXTRAS,
            axes=[
                [{"name": "employment_income", "min": 0, "max": 60_000, "count": 601}]
            ],
        )
        earnings = result.person[0].employment_income
        columns = household_columns(result)
        net = columns["household_net_income"]
        rates = [
            1 - (b - a) / (y - x)
            for a, b, x, y in zip(net, net[1:], earnings, earnings[1:])
        ]
        assert not any(columns["spousal_deemed_income"]), (
            "Unmarried case must have no spousal SSI deeming"
        )
        assert not any(columns["household_health_benefits"])
        assert not any(result.spm_unit.housing_assistance)
        curves[name] = {
            "inputs": inputs,
            "earnings": earnings,
            "outputs": columns,
            "mtr_100_dollar_forward": rates,
        }
        del result
        gc.collect()

    print("Computing NYC long-term capital-gains increment", flush=True)
    rich_inputs = {
        "people": [{"age": 45, "long_term_capital_gains": 30_000_000}],
        "tax_unit": {"filing_status": "SINGLE"},
        "household": {"state_code": "NY", "in_nyc": True},
        "year": YEAR,
    }
    rich = pe.us.calculate_household(
        **rich_inputs,
        reform={HEALTH: False},
        extra_variables=EXTRAS + ["net_investment_income_tax"],
        axes=[
            [
                {
                    "name": "long_term_capital_gains",
                    "min": 30_000_000,
                    "max": 30_010_000,
                    "count": 2,
                }
            ]
        ],
    )
    rich_columns = household_columns(rich)
    rich_rates = {
        name: (values[1] - values[0]) / 10_000 for name, values in rich_columns.items()
    }
    rich_rates["combined_mtr"] = 1 - rich_rates["household_net_income"]

    print("Computing household CTC full refundability", flush=True)
    ctc_inputs = single_parent("NC", [{"age": 4}, {"age": 2}])
    ctc = {}
    for label, fully_refundable in (("baseline", False), ("reform", True)):
        result = pe.us.calculate_household(
            **ctc_inputs,
            reform={HEALTH: False, REFUNDABILITY: fully_refundable},
            extra_variables=EXTRAS
            + ["income_tax_non_refundable_credits", "non_refundable_ctc"],
            axes=[
                [{"name": "employment_income", "min": 0, "max": 60_000, "count": 13}]
            ],
        )
        columns = household_columns(result)
        # In this simple case CTC is the only nonrefundable credit: check, then
        # use the applied cap. `ctc` and `non_refundable_ctc` are entitlements.
        assert (
            result.tax_unit.income_tax_non_refundable_credits
            == result.tax_unit.non_refundable_ctc
        )
        columns["ctc_received"] = [
            a + b
            for a, b in zip(
                columns["refundable_ctc"],
                columns["income_tax_capped_non_refundable_credits"],
            )
        ]
        ctc[label] = columns
        ctc["earnings"] = result.person[0].employment_income
        del result
        gc.collect()
    ctc["inputs"] = ctc_inputs
    for index, earnings in enumerate(ctc["earnings"]):
        if earnings == 15_000:
            assert abs(ctc["baseline"]["ctc_received"][index] - 1_875) < 0.02
            assert abs(ctc["reform"]["ctc_received"][index] - 4_400) < 0.02
        assert (
            ctc["reform"]["ctc_received"][index]
            >= ctc["baseline"]["ctc_received"][index] - 0.02
        )
    print("Computing the 2020–2022 household CTC comparison", flush=True)
    historical_ctc = {}
    for year in (2020, 2021, 2022):
        inputs = single_parent("NC", [{"age": 4}, {"age": 2}])
        inputs["year"] = year
        inputs["people"][0]["employment_income"] = 15_000
        result = pe.us.calculate_household(
            **inputs,
            extra_variables=[
                "refundable_ctc",
                "income_tax_capped_non_refundable_credits",
                "income_tax_non_refundable_credits",
                "non_refundable_ctc",
            ],
        )
        assert (
            result.tax_unit.income_tax_non_refundable_credits
            == result.tax_unit.non_refundable_ctc
        )
        historical_ctc[str(year)] = {
            "inputs": inputs,
            "ctc_received": result.tax_unit.refundable_ctc
            + result.tax_unit.income_tax_capped_non_refundable_credits,
        }
        del result
        gc.collect()
    answer = {
        "provenance": receipt,
        "curves": curves,
        "capital_gains": {
            "inputs": rich_inputs,
            "increment": 10_000,
            "outputs": rich_columns,
            "rates": rich_rates,
        },
        "ctc": ctc,
        "historical_ctc": historical_ctc,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "households.json").write_text(json.dumps(answer, indent=2) + "\n")
    return answer


@contextmanager
def working_directory(path: Path):
    original = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original)


def stage_cached_dataset(
    receipt: dict, run_dir: Path, source: Path | None = None
) -> Path:
    """Hash-check local data before the managed loader can attempt a download."""
    dataset = receipt["us_release"]["datasets"]["populace_us_2024"]
    if source is None:
        # Only inspect the named bundle's ref in the normal Hugging Face cache.
        from huggingface_hub import try_to_load_from_cache

        source = try_to_load_from_cache(
            dataset["repo_id"],
            dataset["path"],
            revision=dataset["revision"],
            repo_type="dataset",
        )
        if not isinstance(source, str):
            raise FileNotFoundError(
                f"Certified data is not cached: {dataset['revision']}/{dataset['path']}. Supply --dataset-file with a local matching file. No download attempted."
            )
        source = Path(source)
    source = source.resolve()
    if not source.is_file() or sha256(source) != dataset["sha256"]:
        raise ValueError(
            f"Dataset must match certified SHA256 {dataset['sha256']}: {source}"
        )
    destination = run_dir / "data" / dataset["path"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() or destination.is_symlink():
        if not destination.is_file() or sha256(destination) != dataset["sha256"]:
            raise FileExistsError(
                f"Refusing to replace preexisting mismatched data: {destination}"
            )
    else:
        destination.symlink_to(source)
    return destination


def run_national(dataset_file: Path | None = None) -> dict:
    import policyengine as pe
    from microdf import MicroSeries

    receipt = provenance()
    run_dir = ROOT / "output" / "pe-reproduction"
    stage_cached_dataset(receipt, run_dir, dataset_file)
    snapshots = {}
    runtime_provenance = {}
    with working_directory(run_dir):
        for label, full in (("baseline", False), ("reform", True)):
            print(
                f"Computing national {label} using the certified local bundle",
                flush=True,
            )
            sim = pe.us.managed_microsimulation(
                reform={
                    REFUNDABILITY: {"2026-01-01.2026-12-31": full},
                    HEALTH: {"2026-01-01.2026-12-31": False},
                }
            )
            runtime_provenance[label] = sim.policyengine_bundle
            snapshot = {}
            for variable in (
                "household_net_income",
                "household_tax",
                "household_benefits",
                "household_health_costs",
                "income_tax",
                "state_income_tax",
                "employee_payroll_tax",
                "medicaid",
                "chip",
                "aca_ptc",
                "federal_benefit_cost",
                "state_benefit_cost",
                "ssi",
                "snap",
                "tanf",
                "employment_income",
            ):
                snapshot[variable] = sim.calc(variable, period=YEAR, map_to="household")
            for variable in ("person_in_poverty", "is_child"):
                snapshot[variable] = sim.calc(variable, period=YEAR, map_to="person")
            if not all(isinstance(series, MicroSeries) for series in snapshot.values()):
                raise TypeError("Population outputs must retain MicroSeries weights")
            snapshots[label] = snapshot
            # Save weighted aggregates while MicroSeries metadata is intact.
            # Plain pandas pickling drops MicroSeries weights; never use it as
            # a resumable population checkpoint.
            (run_dir / f"{label}-aggregates.json").write_text(
                json.dumps(
                    {
                        "provenance": receipt,
                        "runtime_provenance": sim.policyengine_bundle,
                        "aggregates": aggregate_snapshot(snapshot),
                    },
                    indent=2,
                    default=str,
                ) + "\n"
            )
            del sim
            gc.collect()
    baseline, reform = snapshots["baseline"], snapshots["reform"]
    assert baseline["is_child"].equals(reform["is_child"])
    changes = {}
    for variable in sorted(baseline.keys() - {"person_in_poverty", "is_child"}):
        assert baseline[variable].index.equals(reform[variable].index)
        changes[variable] = float((reform[variable] - baseline[variable]).sum())
    poverty = child_poverty_statistics(
        baseline["person_in_poverty"], reform["person_in_poverty"], baseline["is_child"]
    )
    fiscal = fiscal_statistics(changes)
    # Resource accounting is separate from the government health-cost change.
    assert abs(fiscal["tax_and_nonhealth_benefit_cost"] - changes["household_health_costs"] - changes["household_net_income"]) < 100_000, (
        "Fiscal/net-income identity exceeds float32 tolerance"
    )
    assert abs(changes["employment_income"]) < 1, "Static score must hold earnings fixed"
    answer = {
        "provenance": receipt,
        "runtime_provenance": runtime_provenance,
        "reform": {REFUNDABILITY: {"2026-01-01.2026-12-31": True}},
        "conventions": {
            HEALTH: False,
            "behavior": "static; dataset take-up assumptions held fixed",
            "poverty_measure": "Supplemental Poverty Measure; children under 18",
        },
        "changes_reform_minus_baseline": changes,
        "net_fiscal_cost": fiscal["total_cost"],
        "fiscal": fiscal,
        "federal_income_tax_revenue_loss": -changes["income_tax"],
        "poverty": poverty,
    }
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "national.json").write_text(
        json.dumps(answer, indent=2, default=str) + "\n"
    )
    return answer


def aggregate_snapshot(snapshot: dict) -> dict:
    """Durable totals/rates, computed before serializing away survey metadata."""
    from microdf import MicroSeries

    if not all(isinstance(s, MicroSeries) for s in snapshot.values()):
        raise TypeError("Aggregate checkpoints require weighted MicroSeries")
    poverty = child_poverty_statistics(
        snapshot["person_in_poverty"],
        snapshot["person_in_poverty"],
        snapshot["is_child"],
    )
    return {
        "weighted_totals": {
            name: float(series.sum())
            for name, series in snapshot.items()
            if name not in {"person_in_poverty", "is_child"}
        },
        "child_population": poverty["child_population"],
        **poverty["baseline"],
    }


def fiscal_statistics(changes: dict) -> dict:
    """PolicyEngine 5.3.0 budget accounting on MicroSeries weighted changes.

    Same components/signs as pe.us.calculate_budgetary_impact; its Simulation
    output-table helper is replaced here by the managed MicroSeries interface.
    Health valuations are explicitly excluded from household_benefits in both
    runs, so the model's government health-cost variables must be added once.
    """
    tax_and_benefits = changes["household_benefits"] - changes["household_tax"]
    health = changes["federal_benefit_cost"] + changes["state_benefit_cost"]
    federal = -changes["income_tax"] - changes["employee_payroll_tax"] + changes["federal_benefit_cost"]
    state = -changes["state_income_tax"] + changes["state_benefit_cost"]
    total = tax_and_benefits + health
    return {
        "tax_and_nonhealth_benefit_cost": tax_and_benefits,
        "shared_funding_health_cost_change": health,
        "federal_attributed_cost": federal,
        "state_attributed_cost": state,
        "unattributed_cost": total - federal - state,
        "total_cost": total,
    }


def child_poverty_statistics(baseline, reform, child) -> dict:
    """Weighted child SPM rates/counts on person-mapped MicroSeries."""
    from microdf import MicroSeries

    if not all(
        isinstance(s, MicroSeries) and s.dtype.kind == "b"
        for s in (baseline, reform, child)
    ):
        raise TypeError("Expected boolean person-mapped MicroSeries")
    if not baseline.index.equals(child.index) or not reform.index.equals(child.index):
        raise ValueError("Person indices must align before filtering")
    population = float(child.sum())
    if population <= 0:
        raise ValueError("No positively weighted children")
    result = {"child_population": population}
    for label, status in (("baseline", baseline), ("reform", reform)):
        poor_children = status[child]
        result[label] = {
            "child_poverty_rate": float(poor_children.mean()),
            "children_in_poverty": float(poor_children.sum()),
        }
    # Subtract scalar rates, not boolean MicroSeries (numpy rejects the latter).
    result["percentage_point_reduction"] = 100 * (
        result["baseline"]["child_poverty_rate"]
        - result["reform"]["child_poverty_rate"]
    )
    result["children_lifted_out"] = (
        result["baseline"]["children_in_poverty"]
        - result["reform"]["children_in_poverty"]
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("part", choices=["households", "national", "all"])
    parser.add_argument(
        "--dataset-file",
        type=Path,
        help="Existing local certified H5; hash checked, never downloaded",
    )
    args = parser.parse_args()
    if args.part in ("households", "all"):
        run_households()
    if args.part in ("national", "all"):
        run_national(args.dataset_file)


if __name__ == "__main__":
    main()

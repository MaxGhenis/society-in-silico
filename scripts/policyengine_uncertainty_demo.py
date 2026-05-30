#!/usr/bin/env python3
"""Run a small paired-subsample uncertainty demo against PolicyEngine US."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import statistics
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


DEFAULT_DATASET = "hf://policyengine/policyengine-us-data/enhanced_cps_2024.h5"
DEFAULT_REFORM = "policyengine_us.reforms.eitc.streamlined_eitc:streamlined_eitc"


@dataclass
class AggregateDelta:
    seed: int
    delta_eitc: float
    delta_net: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Estimate a simple sampling-uncertainty range for a PolicyEngine US reform."
    )
    parser.add_argument(
        "--policyengine-us-path",
        type=Path,
        help="Path to a local policyengine-us checkout if the package is not already installed.",
    )
    parser.add_argument(
        "--dataset",
        default=DEFAULT_DATASET,
        help=f"Dataset URI to load (default: {DEFAULT_DATASET}).",
    )
    parser.add_argument(
        "--period",
        default="2025",
        help="Period to simulate (default: 2025).",
    )
    parser.add_argument(
        "--reform",
        default=DEFAULT_REFORM,
        help=(
            "Import path for the reform class/function in module:attr format "
            f"(default: {DEFAULT_REFORM})."
        ),
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=1000,
        help="Households per paired subsample replicate (default: 1000).",
    )
    parser.add_argument(
        "--replicates",
        type=int,
        default=10,
        help="Number of paired subsample replicates to run (default: 10).",
    )
    parser.add_argument(
        "--seed-start",
        type=int,
        default=1,
        help="Starting seed for paired subsamples (default: 1).",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        help="Optional path to write the full results as JSON.",
    )
    return parser.parse_args()


def maybe_add_policyengine_path(explicit_path: Path | None) -> Path | None:
    candidates: list[Path] = []
    if explicit_path is not None:
        candidates.append(explicit_path.expanduser())

    env_path = os.getenv("POLICYENGINE_US_PATH")
    if env_path:
        candidates.append(Path(env_path).expanduser())

    candidates.append(Path.home() / "PolicyEngine" / "policyengine-us")

    for candidate in candidates:
        if (candidate / "policyengine_us").exists():
            candidate_str = str(candidate.resolve())
            if candidate_str not in sys.path:
                sys.path.insert(0, candidate_str)
            return candidate.resolve()

    return None


def load_reform(import_path: str) -> Any:
    module_name, attr_name = import_path.split(":", 1)
    module = importlib.import_module(module_name)
    return getattr(module, attr_name)


def calc_totals(simulation: Any, period: str) -> dict[str, float]:
    return {
        "eitc": float(simulation.calc("eitc", period=period).sum()),
        "household_net_income": float(
            simulation.calc("household_net_income", period=period).sum()
        ),
    }


def format_billions(value: float) -> str:
    sign = "-" if value < 0 else ""
    return f"{sign}${abs(value) / 1_000_000_000:.1f}B"


def summarize(values: list[float]) -> dict[str, float]:
    return {
        "mean": statistics.mean(values),
        "stdev": statistics.stdev(values) if len(values) > 1 else 0.0,
        "min": min(values),
        "max": max(values),
    }


def format_range(values: list[float]) -> str:
    return f"{format_billions(max(values))} to {format_billions(min(values))}"


def print_markdown_table(full_sample: dict[str, float], replicates: list[AggregateDelta]) -> None:
    eitc_values = [item.delta_eitc for item in replicates]
    net_values = [item.delta_net for item in replicates]
    eitc_summary = summarize(eitc_values)
    net_summary = summarize(net_values)

    print()
    print("| Statistic | Aggregate EITC change | Aggregate household net income change |")
    print("| --- | ---: | ---: |")
    print(
        "| Full-sample point estimate | "
        f"{format_billions(full_sample['delta_eitc'])} | "
        f"{format_billions(full_sample['delta_net'])} |"
    )
    print(
        "| Mean across paired subsamples | "
        f"{format_billions(eitc_summary['mean'])} | "
        f"{format_billions(net_summary['mean'])} |"
    )
    print(
        "| Range across paired subsamples | "
        f"{format_range(eitc_values)} | "
        f"{format_range(net_values)} |"
    )


def main() -> None:
    args = parse_args()
    maybe_add_policyengine_path(args.policyengine_us_path)

    try:
        from policyengine_us import Microsimulation  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Could not import policyengine_us. Install it or pass "
            "--policyengine-us-path /path/to/policyengine-us."
        ) from exc

    reform = load_reform(args.reform)

    started_at = time.time()
    baseline_full = Microsimulation(dataset=args.dataset)
    reform_full = Microsimulation(dataset=args.dataset, reform=reform)
    baseline_totals = calc_totals(baseline_full, args.period)
    reform_totals = calc_totals(reform_full, args.period)
    full_sample = {
        "delta_eitc": reform_totals["eitc"] - baseline_totals["eitc"],
        "delta_net": (
            reform_totals["household_net_income"] - baseline_totals["household_net_income"]
        ),
    }

    replicate_rows: list[AggregateDelta] = []
    for seed in range(args.seed_start, args.seed_start + args.replicates):
        baseline = Microsimulation(dataset=args.dataset)
        baseline.subsample(args.sample_size, seed=seed)
        reform_sim = Microsimulation(dataset=args.dataset, reform=reform)
        reform_sim.subsample(args.sample_size, seed=seed)

        baseline_subsample = calc_totals(baseline, args.period)
        reform_subsample = calc_totals(reform_sim, args.period)
        replicate_rows.append(
            AggregateDelta(
                seed=seed,
                delta_eitc=reform_subsample["eitc"] - baseline_subsample["eitc"],
                delta_net=(
                    reform_subsample["household_net_income"]
                    - baseline_subsample["household_net_income"]
                ),
            )
        )

    elapsed_seconds = time.time() - started_at
    eitc_values = [item.delta_eitc for item in replicate_rows]
    net_values = [item.delta_net for item in replicate_rows]

    output = {
        "dataset": args.dataset,
        "period": args.period,
        "reform": args.reform,
        "sample_size": args.sample_size,
        "replicates": args.replicates,
        "seed_start": args.seed_start,
        "elapsed_seconds": elapsed_seconds,
        "full_sample": full_sample,
        "summary": {
            "delta_eitc": summarize(eitc_values),
            "delta_net": summarize(net_values),
        },
        "replicate_deltas": [asdict(item) for item in replicate_rows],
    }

    if args.output_json is not None:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(json.dumps(output, indent=2))

    print(json.dumps(output["summary"], indent=2))
    print_markdown_table(full_sample, replicate_rows)


if __name__ == "__main__":
    main()

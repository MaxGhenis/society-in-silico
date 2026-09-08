"""Tables and figures from the book's saved PolicyEngine outputs."""

from __future__ import annotations

import json
from pathlib import Path

from pe_computed_numbers import OUTPUT


def increment(curve: dict, lower: int, upper: int) -> dict:
    lo, hi = (curve["earnings"].index(e) for e in (lower, upper))
    changes = {key: values[hi] - values[lo] for key, values in curve["outputs"].items()}
    return {
        "earnings_from": lower,
        "earnings_to": upper,
        "mtr": 1 - changes["household_net_income"] / (upper - lower),
        "changes": changes,
    }


def household_summary(results: dict) -> dict:
    ctc = results["ctc"]
    index = ctc["earnings"].index(15_000)
    return {
        "nc_38000_to_39000": increment(
            results["curves"]["nc_two_children"], 38_000, 39_000
        ),
        "ny_30000_to_30100": increment(
            results["curves"]["ny_one_child"], 30_000, 30_100
        ),
        "nyc_capital_gains_mtr": results["capital_gains"]["rates"]["combined_mtr"],
        "ctc_at_15000": {
            label: ctc[label]["ctc_received"][index] for label in ("baseline", "reform")
        },
        "historical_ctc": {
            year: row["ctc_received"] for year, row in results["historical_ctc"].items()
        },
    }


def figures(results: dict, destination: Path = OUTPUT) -> list[Path]:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter, PercentFormatter

    destination.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update(
        {"font.size": 10, "axes.spines.top": False, "axes.spines.right": False}
    )
    curve = results["curves"]["nc_two_children"]
    earnings = curve["earnings"]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.4), layout="constrained")
    axes[0].plot(
        earnings, curve["outputs"]["household_net_income"], color="#23415a", linewidth=2
    )
    axes[0].set(
        xlabel="Annual earnings",
        ylabel="Modeled annual net income",
        title="North Carolina: one parent, two children",
    )
    axes[0].xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x / 1000:.0f}k"))
    axes[0].yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x / 1000:.0f}k"))
    axes[0].axvspan(38_000, 39_000, color="#c57e3d", alpha=0.2)
    # Show the full relevant interval; the left panel preserves wider cliffs.
    selected = [
        (e, r)
        for e, r in zip(earnings, curve["mtr_100_dollar_forward"])
        if 35_000 <= e < 40_000
    ]
    axes[1].plot([e for e, _ in selected], [r for _, r in selected], color="#23415a")
    axes[1].axhline(
        results["capital_gains"]["rates"]["combined_mtr"],
        color="#8d4b32",
        linestyle="--",
        label="NYC: $30m long-term gains",
    )
    axes[1].set(
        xlabel="Annual earnings before $100 increase",
        ylabel="Share of the increase withdrawn",
        title="The upper-$30,000 earnings range",
        ylim=(0, 1.05),
    )
    axes[1].xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x / 1000:.0f}k"))
    axes[1].yaxis.set_major_formatter(PercentFormatter(1))
    axes[1].legend(loc="lower left", frameon=False)
    fig.suptitle("2026 tax and benefit interactions", fontsize=14)
    mtr = destination / "household-marginal-rates.png"
    fig.savefig(mtr, dpi=180)
    plt.close(fig)

    ctc = results["ctc"]
    fig, ax = plt.subplots(figsize=(7.5, 4.4), layout="constrained")
    ax.plot(
        ctc["earnings"],
        ctc["baseline"]["ctc_received"],
        color="#23415a",
        label="2026 baseline",
        marker="o",
        markersize=3,
    )
    ax.plot(
        ctc["earnings"],
        ctc["reform"]["ctc_received"],
        color="#8d4b32",
        label="Full refundability",
        linestyle="--",
    )
    ax.set(
        xlabel="Annual earnings",
        ylabel="Annual CTC received",
        title="One parent with children aged 2 and 4",
        ylim=(0, 4800),
    )
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x / 1000:.0f}k"))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.legend(frameon=False)
    credit = destination / "ctc-full-refundability.png"
    fig.savefig(credit, dpi=180)
    plt.close(fig)
    return [mtr, credit]


def write_summary(households: dict, national: dict | None = None) -> dict:
    summary = {"households": household_summary(households)}
    if national is not None:
        summary["national"] = {
            key: national[key]
            for key in ("net_fiscal_cost", "federal_income_tax_revenue_loss", "poverty")
        }
    (OUTPUT / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    return summary

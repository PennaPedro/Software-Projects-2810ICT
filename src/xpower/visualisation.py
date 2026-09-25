"""Electricity usage and bill visualisation functions for XPower."""

import matplotlib.pyplot as plt


def usage_line_chart(data):
    """Create a line chart showing electricity usage over time."""

    if data is None or not hasattr(data, "columns"):
        return "Error : invalid electricity usage data"

    if "timestamp" not in data.columns or "usage_kwh" not in data.columns:
        return "Error : data must contain timestamp and usage_kwh columns"

    if data.empty:
        return "Error : no electricity usage data available"

    fig, ax = plt.subplots()

    ax.plot(
        data["timestamp"],
        data["usage_kwh"],
    )

    ax.set_title("Electricity Usage Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Usage (kWh)")
    ax.grid(True, alpha=0.3)

    fig.autofmt_xdate()
    fig.tight_layout()

    return fig


def bill_comparison_chart(comparison):
    """Create a bar chart comparing tariff bill totals."""

    if not isinstance(comparison, dict) or "bills" not in comparison:
        return "Error : invalid comparison result"

    bills = comparison["bills"]

    if not isinstance(bills, dict) or not bills:
        return "Error : no bill results available"

    for cost in bills.values():
        if not isinstance(cost, (int, float)) or cost < 0:
            return "Error : invalid bill value"

    tariff_names = list(bills.keys())
    tariff_costs = list(bills.values())

    fig, ax = plt.subplots()

    bars = ax.bar(tariff_names, tariff_costs)

    ax.set_title("Tariff Bill Comparison")
    ax.set_xlabel("Tariff")
    ax.set_ylabel("Bill Cost ($)")

    # Show the bill amount above each bar.
    for bar, cost in zip(bars, tariff_costs):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"${cost:.2f}",
            ha="center",
            va="bottom",
        )

    fig.tight_layout()

    return fig
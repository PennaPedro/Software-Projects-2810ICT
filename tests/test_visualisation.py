"""Tests for XPower electricity usage and bill visualisations."""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from src.xpower.visualisation import (
    usage_line_chart,
    bill_comparison_chart,
)


def test_usage_line_chart_creates_figure():
    data = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-01-01 00:00",
            "2026-01-01 01:00",
            "2026-01-01 02:00",
        ]),
        "usage_kwh": [1.2, 0.9, 1.5],
    })

    result = usage_line_chart(data)

    assert isinstance(result, Figure)
    assert result.axes[0].get_title() == "Electricity Usage Over Time"

    plt.close(result)


def test_usage_line_chart_has_correct_labels():
    data = pd.DataFrame({
        "timestamp": pd.to_datetime([
            "2026-01-01 00:00",
            "2026-01-01 01:00",
        ]),
        "usage_kwh": [1.0, 2.0],
    })

    result = usage_line_chart(data)

    ax = result.axes[0]

    assert ax.get_xlabel() == "Time"
    assert ax.get_ylabel() == "Usage (kWh)"

    plt.close(result)


def test_usage_line_chart_invalid_data():
    result = usage_line_chart("invalid")

    assert "Error" in result


def test_usage_line_chart_missing_columns():
    data = pd.DataFrame({
        "usage": [1.0, 2.0]
    })

    result = usage_line_chart(data)

    assert "Error" in result


def test_usage_line_chart_empty_data():
    data = pd.DataFrame(columns=["timestamp", "usage_kwh"])

    result = usage_line_chart(data)

    assert "Error" in result


def test_bill_comparison_chart_creates_figure():
    comparison = {
        "bills": {
            "Flat Rate": 85,
            "Time-of-Use": 92,
            "Tiered": 110,
        }
    }

    result = bill_comparison_chart(comparison)

    assert isinstance(result, Figure)
    assert result.axes[0].get_title() == "Tariff Bill Comparison"

    plt.close(result)


def test_bill_comparison_chart_invalid_comparison():
    result = bill_comparison_chart("invalid")

    assert "Error" in result


def test_bill_comparison_chart_empty_bills():
    comparison = {
        "bills": {}
    }

    result = bill_comparison_chart(comparison)

    assert "Error" in result


def test_bill_comparison_chart_negative_bill():
    comparison = {
        "bills": {
            "Flat Rate": 85,
            "Time-of-Use": -20,
            "Tiered": 110,
        }
    }

    result = bill_comparison_chart(comparison)

    assert "Error" in result
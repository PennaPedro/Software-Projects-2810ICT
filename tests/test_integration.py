"""Integration tests for the complete XPower analysis flow."""

from pathlib import Path

import matplotlib.pyplot as plt
import pytest
from matplotlib.figure import Figure

from src.xpower.data_import import (
    DataImportError,
    load_electricity_data,
)
from src.xpower.tariffs import (
    flat_bill,
    tiered_bill,
    tou_bill,
)
from src.xpower.billing import (
    compare_tariffs,
    calculate_savings,
    cost_saving_suggestion,
)
from src.xpower.visualisation import (
    usage_line_chart,
    bill_comparison_chart,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_CSV = (
    REPO_ROOT
    / "data"
    / "sample"
    / "sample_usage_data_month.csv"
)


def test_complete_xpower_analysis_flow():
    """Check that the main XPower modules work together."""

    # 1. Import electricity usage data.
    data = load_electricity_data(SAMPLE_CSV)

    assert len(data) == 720

    total_usage = float(data["usage_kwh"].sum())

    # 2. Calculate the three tariffs.
    flat_result = flat_bill(
        total_usage,
        rate=0.25,
        fee=10,
    )

    tou_result = tou_bill(
        data,
        peak_rate=0.40,
        shoulder_rate=0.25,
        off_peak_rate=0.15,
        fee=10,
        peak_start=18,
        peak_end=22,
        off_peak_start=22,
        off_peak_end=7,
    )

    tiered_result = tiered_bill(
        total_usage,
        t1_limit=100,
        t1_rate=0.20,
        t2_limit=300,
        t2_rate=0.30,
        t3_rate=0.40,
        fee=10,
    )

    assert isinstance(flat_result, (int, float))
    assert isinstance(tou_result, dict)
    assert isinstance(tiered_result, (int, float))

    # 3. Compare the calculated bills.
    comparison = compare_tariffs(
        flat_result,
        tou_result,
        tiered_result,
    )

    assert isinstance(comparison, dict)

    assert set(comparison["bills"].keys()) == {
        "Flat Rate",
        "Time-of-Use",
        "Tiered",
    }

    # 4. Calculate savings and suggestion.
    savings = calculate_savings(comparison)
    suggestion = cost_saving_suggestion(comparison)

    assert savings >= 0

    assert (
        comparison["cheapest_tariff"]
        in suggestion
    )

    # 5. Create the visualisations.
    usage_chart = usage_line_chart(data)
    bill_chart = bill_comparison_chart(comparison)

    assert isinstance(usage_chart, Figure)
    assert isinstance(bill_chart, Figure)

    plt.close(usage_chart)
    plt.close(bill_chart)


def test_complete_flow_rejects_invalid_file(tmp_path):
    """Check that invalid input stops the analysis correctly."""

    invalid_file = tmp_path / "invalid.csv"

    invalid_file.write_text(
        "timestamp,kWh\n"
        "not-a-date,10\n"
    )

    with pytest.raises(
        DataImportError,
        match="invalid timestamp",
    ):
        load_electricity_data(invalid_file)
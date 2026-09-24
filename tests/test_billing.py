"""Tests for bill comparison, savings and cost-saving suggestions."""

from src.xpower.billing import (
    compare_tariffs,
    calculate_savings,
    cost_saving_suggestion,
)


def test_compare_tariffs_finds_cheapest_option():
    result = compare_tariffs(85, 92, 110)

    assert result["bills"]["Flat Rate"] == 85
    assert result["bills"]["Time-of-Use"] == 92
    assert result["bills"]["Tiered"] == 110
    assert result["cheapest_tariff"] == "Flat Rate"
    assert result["cheapest_cost"] == 85
    assert result["most_expensive_tariff"] == "Tiered"
    assert result["most_expensive_cost"] == 110


def test_compare_tariffs_accepts_tou_dictionary():
    tou_result = {
        "usage_kwh": {
            "Peak": 100,
            "Shoulder": 120,
            "Off-Peak": 80,
        },
        "costs": {
            "Peak": 40,
            "Shoulder": 30,
            "Off-Peak": 12,
        },
        "fixed_fee": 10,
        "total": 92,
    }

    result = compare_tariffs(85, tou_result, 110)

    assert result["cheapest_tariff"] == "Flat Rate"
    assert result["bills"]["Time-of-Use"] == 92


def test_compare_tariffs_invalid_result():
    result = compare_tariffs(85, "invalid", 110)

    assert "Error" in result


def test_compare_tariffs_negative_total():
    result = compare_tariffs(-10, 92, 110)

    assert "Error" in result


def test_calculate_savings():
    comparison = compare_tariffs(85, 92, 110)

    savings = calculate_savings(comparison)

    assert savings == 25


def test_calculate_savings_invalid_comparison():
    result = calculate_savings("invalid")

    assert "Error" in result


def test_cost_saving_suggestion():
    comparison = compare_tariffs(85, 92, 110)

    suggestion = cost_saving_suggestion(comparison)

    assert "Flat Rate" in suggestion
    assert "$85.00" in suggestion


def test_cost_saving_suggestion_invalid_comparison():
    result = cost_saving_suggestion("invalid")

    assert "Error" in result
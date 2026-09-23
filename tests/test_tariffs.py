"""Tests for Flat Rate, Time-of-Use and Tiered tariff functions."""

import pandas as pd

from src.xpower.tariffs import flat_bill, tiered_bill, time_slot, tou_bill


def test_flat_bill_example():
    assert flat_bill(300,0.25,10)==85


def test_flat_bill_negative_units():
    assert "Error" in flat_bill(-1,0.25,10)


def test_tiered_bill_example():
    assert tiered_bill(350,fee=10)==110


def test_tiered_bill_negative_units():
    assert "Error" in tiered_bill(-1,fee=10)


def test_time_slot_default_periods():
    assert time_slot(19)=="Peak"
    assert time_slot(23)=="Off-Peak"
    assert time_slot(12)=="Shoulder"


def test_time_slot_custom_peak_period():
    assert time_slot(17,peak_start=17,peak_end=21)=="Peak"


def test_time_slot_invalid_hour():
    assert "Error" in time_slot(25)


def test_tou_bill_assignment_example():
    data=pd.DataFrame({
        "timestamp":pd.to_datetime([
            "2025-01-01 19:00:00",
            "2025-01-01 12:00:00",
            "2025-01-01 23:00:00"
        ]),
        "usage_kwh":[100,120,80]
    })

    result=tou_bill(data,0.40,0.25,0.15,10)

    assert result["usage_kwh"]["Peak"]==100
    assert result["usage_kwh"]["Shoulder"]==120
    assert result["usage_kwh"]["Off-Peak"]==80
    assert result["costs"]["Peak"]==40
    assert result["costs"]["Shoulder"]==30
    assert result["costs"]["Off-Peak"]==12
    assert result["total"]==92


def test_tou_bill_negative_rate():
    data=pd.DataFrame({
        "timestamp":pd.to_datetime(["2025-01-01 19:00:00"]),
        "usage_kwh":[1]
    })

    assert "Error" in tou_bill(data,-0.40,0.25,0.15,10)

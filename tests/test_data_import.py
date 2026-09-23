"""Tests for CSV/Excel data import and validation."""

from pathlib import Path

import pandas as pd
import pytest

from src.xpower.data_import import DataImportError, load_electricity_data


@pytest.fixture
def valid_csv(tmp_path: Path) -> Path:
    path = tmp_path / "usage.csv"
    pd.DataFrame(
        {
            "timestamp": ["2025-01-01 02:00:00", "2025-01-01 01:00:00"],
            "kWh": [0.5, 0.25],
        }
    ).to_csv(path, index=False)
    return path


def test_load_valid_csv_and_normalise_columns(valid_csv: Path):
    result = load_electricity_data(valid_csv)

    assert list(result.columns) == ["timestamp", "usage_kwh"]
    assert len(result) == 2
    assert result.iloc[0]["usage_kwh"] == 0.25
    assert result["timestamp"].is_monotonic_increasing


def test_load_valid_excel(tmp_path: Path):
    path = tmp_path / "usage.xlsx"
    pd.DataFrame(
        {
            "date": ["2025-01-01", "2025-01-02"],
            "consumption_kwh": [10, 12.5],
        }
    ).to_excel(path, index=False)

    result = load_electricity_data(path)

    assert list(result.columns) == ["timestamp", "usage_kwh"]
    assert result["usage_kwh"].sum() == pytest.approx(22.5)


def test_missing_timestamp_column_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"kWh": [1.0]}).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="Missing timestamp"):
        load_electricity_data(path)


def test_missing_usage_column_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"timestamp": ["2025-01-01 00:00"]}).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="Missing electricity usage"):
        load_electricity_data(path)


def test_non_numeric_usage_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame(
        {"timestamp": ["2025-01-01 00:00"], "kWh": ["not-a-number"]}
    ).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="non-numeric"):
        load_electricity_data(path)


def test_negative_usage_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame(
        {"timestamp": ["2025-01-01 00:00"], "kWh": [-1.0]}
    ).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="negative"):
        load_electricity_data(path)


def test_duplicate_timestamp_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame(
        {
            "timestamp": ["2025-01-01 00:00", "2025-01-01 00:00"],
            "kWh": [1.0, 2.0],
        }
    ).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="Duplicate timestamps"):
        load_electricity_data(path)


def test_unsupported_file_type_raises(tmp_path: Path):
    path = tmp_path / "usage.txt"
    path.write_text("timestamp,kWh\n2025-01-01,1")

    with pytest.raises(DataImportError, match="Unsupported file type"):
        load_electricity_data(path)


def test_invalid_timestamp_raises(tmp_path: Path):
    path = tmp_path / "bad.csv"
    pd.DataFrame(
        {"timestamp": ["not-a-date"], "kWh": [1.0]}
    ).to_csv(path, index=False)

    with pytest.raises(DataImportError, match="invalid timestamp"):
        load_electricity_data(path)

"""CSV/Excel import and validation for XPower electricity data."""

from __future__ import annotations

from pathlib import Path
import warnings

import pandas as pd


TIMESTAMP_ALIASES = {"timestamp", "datetime", "date", "time"}
USAGE_ALIASES = {
    "kwh",
    "usage",
    "usage_kwh",
    "consumption",
    "consumption_kwh",
}


class DataImportError(ValueError):
    """Raised when an electricity data file cannot be imported or validated."""


def _normalise_column_name(name: object) -> str:
    """Return a simple lower-case column name for matching."""
    return str(name).strip().lower().replace(" ", "_")


def _find_column(columns: list[object], aliases: set[str]) -> object | None:
    """Find the first column whose normalised name is in aliases."""
    for column in columns:
        if _normalise_column_name(column) in aliases:
            return column
    return None


def _read_file(file_path: Path) -> pd.DataFrame:
    """Read a supported CSV or Excel file."""
    suffix = file_path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(file_path)
    if suffix == ".xlsx":
        return pd.read_excel(file_path, sheet_name=0)
    raise DataImportError("Unsupported file type. Please select a .csv or .xlsx file.")


def _warn_about_missing_periods(result: pd.DataFrame) -> None:
    """Warn about gaps for supported hourly or daily datasets.

    The expected interval is inferred from the median timestamp difference so
    valid daily data is not incorrectly reported as having missing hours.
    Missing values are never invented automatically.
    """
    if len(result) < 2:
        return

    differences = result["timestamp"].diff().dropna()
    if differences.empty:
        return

    median_difference = differences.median()

    if median_difference <= pd.Timedelta(hours=2):
        expected_interval = pd.Timedelta(hours=1)
        frequency_name = "hourly"
    elif median_difference >= pd.Timedelta(hours=20):
        expected_interval = pd.Timedelta(days=1)
        frequency_name = "daily"
    else:
        # The prototype requirements cover hourly and daily data. Do not make
        # assumptions about an unsupported sampling interval.
        return

    gaps = differences > expected_interval
    if gaps.any():
        count = int(gaps.sum())
        warnings.warn(
            f"The {frequency_name} data contains {count} missing time period(s). "
            "Missing periods were not filled.",
            UserWarning,
            stacklevel=3,
        )


def _validate_and_normalise(data: pd.DataFrame) -> pd.DataFrame:
    """Validate the imported data and return a standardised DataFrame."""
    if data.empty:
        raise DataImportError("The selected file contains no data.")

    original_columns = list(data.columns)
    timestamp_column = _find_column(original_columns, TIMESTAMP_ALIASES)
    usage_column = _find_column(original_columns, USAGE_ALIASES)

    if timestamp_column is None:
        raise DataImportError(
            "Missing timestamp column. Expected one of: timestamp, datetime, date, time."
        )
    if usage_column is None:
        raise DataImportError(
            "Missing electricity usage column. Expected one of: kWh, usage, "
            "usage_kwh, consumption, consumption_kwh."
        )

    result = data[[timestamp_column, usage_column]].copy()
    result.columns = ["timestamp", "usage_kwh"]

    result["timestamp"] = pd.to_datetime(result["timestamp"], errors="coerce")
    invalid_timestamps = result["timestamp"].isna()
    if invalid_timestamps.any():
        count = int(invalid_timestamps.sum())
        raise DataImportError(f"Found {count} invalid timestamp value(s).")

    result["usage_kwh"] = pd.to_numeric(result["usage_kwh"], errors="coerce")
    invalid_usage = result["usage_kwh"].isna()
    if invalid_usage.any():
        count = int(invalid_usage.sum())
        raise DataImportError(f"Found {count} non-numeric or blank usage value(s).")

    if (result["usage_kwh"] < 0).any():
        raise DataImportError("Electricity usage cannot contain negative values.")

    if result["timestamp"].duplicated().any():
        duplicates = int(result["timestamp"].duplicated(keep=False).sum())
        raise DataImportError(
            f"Duplicate timestamps detected ({duplicates} affected row(s)). "
            "Duplicate records must be fixed before billing."
        )

    result = result.sort_values("timestamp").reset_index(drop=True)
    _warn_about_missing_periods(result)

    return result


def load_electricity_data(file_path: str | Path) -> pd.DataFrame:
    """Load, validate, clean and sort a CSV or Excel electricity data file.

    Returns a DataFrame with exactly two standard columns:
    ``timestamp`` and ``usage_kwh``.

    Daily data is accepted. Hourly data is also accepted and can be used by
    the Time-of-Use tariff. Missing periods generate a warning; values are
    never invented automatically.
    """
    path = Path(file_path)
    if not path.exists():
        raise DataImportError(f"File not found: {path}")
    if not path.is_file():
        raise DataImportError(f"Not a file: {path}")

    try:
        data = _read_file(path)
    except DataImportError:
        raise
    except Exception as exc:
        raise DataImportError(f"Could not read file: {exc}") from exc

    return _validate_and_normalise(data)


# Short alias for callers that prefer the project terminology.
import_data = load_electricity_data

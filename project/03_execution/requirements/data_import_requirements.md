# CSV / Excel Electricity Data Requirements Analysis

**Status:** Done for requirements analysis; implementation remains To Do.

## Purpose
XPower requires customers to upload household electricity consumption data from CSV or Excel files. The data may contain daily or hourly electricity usage and must be usable by the tariff-calculation features.

## Tutor-provided sample structure
The supplied sample file uses exactly these columns:

| Field | Meaning |
|---|---|
| `timestamp` | Date and time of the electricity usage record |
| `kWh` | Electricity consumed during that record |

The supplied sample contains hourly data from `2025-01-01 00:00:00` through `2025-01-30 23:00:00`.

Known sample checks:
- 720 hourly records
- no missing hours in the supplied sample
- no duplicate timestamps in the supplied sample
- no blank usage values in the supplied sample
- no negative usage values in the supplied sample
- total sample usage: 850.67 kWh

## Supported file types
- `.csv`
- `.xlsx`

For the first prototype, Excel import can read the first worksheet.

## Preferred input columns
External preferred names:
- `timestamp`
- `kWh`

To make the prototype easier to use, common alternatives may be accepted, for example:
- timestamp alternatives: `date`, `datetime`, `time`
- usage alternatives: `usage`, `usage_kwh`, `kwh`, `consumption`, `consumption_kwh`

After import, data should be normalised internally to:
- `timestamp`
- `usage_kwh`

## Validation rules
The importer should check:
1. a file has been selected;
2. the file is CSV or Excel;
3. the file can be opened;
4. at least one record exists;
5. a timestamp/date column exists;
6. a usage/kWh column exists;
7. timestamps can be converted to valid date/time values;
8. usage values are numeric;
9. electricity usage is not negative;
10. duplicate timestamps are flagged rather than silently double-counted.

Missing time periods may be accepted for the prototype, but the user should be warned when gaps are detected.

## Daily vs hourly data
Daily data can support:
- Flat Rate calculations
- Tiered calculations
- daily usage charts

Hourly data can support:
- Flat Rate calculations
- Tiered calculations
- Time-of-Use calculations
- hourly/daily usage charts

Time-of-Use analysis requires timestamps with time-of-day information. Daily-only data must not be used to invent Peak / Off-Peak / Shoulder allocation.

## Normalised output
The importer should return clean data similar to:

```text
timestamp            usage_kwh
2025-01-01 00:00:00  0.25
2025-01-01 01:00:00  0.42
```

The output should be sorted by timestamp and ready for tariff calculations, bill comparison and visualisation.

## User-friendly errors
Examples:
- “Please upload a CSV or Excel (.xlsx) file.”
- “We could not find a date or timestamp column.”
- “We could not find an electricity usage (kWh) column.”
- “Some electricity usage values are not valid numbers.”
- “Electricity usage cannot contain negative values.”
- “Some dates or times could not be read.”
- “Time-of-Use analysis requires hourly data with timestamps.”

## Acceptance criteria
The feature is ready when valid daily/hourly CSV and Excel data can be read, converted into the normalised structure, and invalid/missing data produces clear errors. The supplied sample must be read correctly and return the known sample checks above.

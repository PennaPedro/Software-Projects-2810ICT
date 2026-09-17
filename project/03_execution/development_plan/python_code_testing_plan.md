# Python Code Structure and Testing Plan

**Status:** Planning complete; implementation To Do.

## Planned source structure
```text
src/
├── main.py
└── xpower/
    ├── __init__.py
    ├── data_import.py
    ├── tariffs.py
    ├── billing.py
    ├── visualisation.py
    └── ui.py
```

## Module responsibilities
- `main.py` — application entry point
- `data_import.py` — CSV/Excel reading, validation and normalisation
- `tariffs.py` — Flat Rate, Time-of-Use and Tiered tariff calculations
- `billing.py` — bill breakdown, comparison, savings and suggestions
- `visualisation.py` — usage trends and bill charts
- `ui.py` — user-facing interface and error messages

## Core assessed functions
The planned three main functions are:
```text
calculate_flat_rate(...)
calculate_tou_tariff(...)
calculate_tiered_tariff(...)
```

These directly match the required tariff models and naturally cover parameters, return values and conditional logic.

### Flat Rate
Expected inputs:
- total kWh
- rate per kWh
- fixed supply fee

Expected output:
- total bill (with breakdown available to the billing layer)

Reference example from the assignment case study:
- 300 kWh × $0.25 + $10 fixed fee = $85

### Time-of-Use
Uses timestamped hourly usage and Peak / Off-Peak / Shoulder rates. Conditional logic will determine which rate applies to each record.

Reference example from the assignment case study:
- Peak = $40
- Shoulder = $30
- Off-Peak = $12
- fixed fee = $10
- total = $92

### Tiered Tariff
Calculates consumption progressively across thresholds.

Reference example from the assignment case study:
- first 100 kWh × $0.20 = $20
- next 200 kWh × $0.30 = $60
- remaining 50 kWh × $0.40 = $20
- fixed fee = $10
- total = $110

## Testing structure
```text
tests/
├── test_data_import.py
├── test_tariffs.py
└── test_billing.py
```

The current project plan uses `pytest` and `pytest-html` for simple unit testing and submission evidence.

Each implemented assessment function must have:
- positive test cases
- negative test cases
- clear test names
- a final 100% pass rate

Planned test command:
```bash
pytest -v
```

Planned HTML report command:
```bash
pytest --html=report.html --self-contained-html
```

## Example test names
```text
test_flat_rate_valid_bill
test_flat_rate_rejects_negative_usage
test_tou_applies_peak_rate
test_tou_rejects_invalid_timestamp
test_tiered_valid_three_tiers
test_tiered_rejects_negative_usage
```

## Coding rules
- use meaningful `snake_case` names;
- keep calculations separate from UI code;
- validate inputs before calculation;
- use short docstrings for public functions;
- keep production code in `src/` and tests in `tests/`;
- do not duplicate tariff formulas across modules.

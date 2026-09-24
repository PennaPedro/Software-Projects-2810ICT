# Requirements Traceability Matrix

**Status:** Done

This matrix links the approved XPower requirements to the related use case, system component, implementation or test evidence, and current project status.

## Functional Requirements

| ID | Requirement | Use Case / Design | Implementation / Evidence | Verification | Status |
|---|---|---|---|---|---|
| FR-01 | Upload electricity usage data from CSV or Excel files. | UC01 - Upload Electricity Data / Input & Interface | `src/xpower/data_import.py` | CSV and Excel import tests in `tests/test_data_import.py` | Implemented |
| FR-02 | Support daily and hourly electricity usage data. | UC01 - Upload Electricity Data | `src/xpower/data_import.py` | Daily and hourly data tests | Implemented |
| FR-03 | Validate uploaded data and show clear messages for invalid data. | UC01 - Upload Electricity Data | Data Import & Validation / `data_import.py` | Missing columns, invalid timestamp, negative usage, duplicate and unsupported file tests | Implemented |
| FR-04 | Calculate a bill using Flat Rate. | UC03 - Calculate Electricity Bill | Flat Rate / `src/xpower/tariffs.py` | `test_flat_bill_example` and negative-units test | Implemented |
| FR-05 | Calculate a bill using Time-of-Use with Peak, Shoulder and Off-Peak rates. | UC03 - Calculate Electricity Bill | Time-of-Use / `tariffs.py` | `test_tou_bill_assignment_example` | Implemented |
| FR-06 | Allow Time-of-Use periods and rates to be defined. | UC02 - Configure Tariff | `time_slot(...)` and `tou_bill(...)` | Custom peak-period and TOU tests | Implemented |
| FR-07 | Calculate a bill using Tiered tariff thresholds and rates. | UC03 - Calculate Electricity Bill | Tiered / `tariffs.py` | `test_tiered_bill_example` and negative-units test | Implemented |
| FR-08 | Include an optional fixed fee in bill calculations. | UC02 / UC03 | Flat, TOU and Tiered tariff functions | Assignment-example tariff tests include fixed fees | Implemented |
| FR-09 | Show a breakdown of electricity usage and costs for the selected tariff. | UC05 - View Usage, Bill and Savings Results / Visualisation & Bill Breakdown | TOU breakdown exists in `tariffs.py`; `billing.py` and `visualisation.py` are planned | TOU breakdown test completed; full result display test planned | Partly Implemented |
| FR-10 | Compare the cost of different tariff options. | UC04 - Compare Tariffs / Bill Comparison & Savings | `src/xpower/billing.py` | Comparison test planned | To Do |
| FR-11 | Identify possible savings between tariff options. | UC04 / UC05 / Bill Comparison & Savings | `billing.py` | Savings calculation test planned | To Do |
| FR-12 | Provide simple cost-saving suggestions. | UC05 / Cost-Saving Suggestions | Billing & Results design | Suggestion behaviour test planned | To Do |
| FR-13 | Display electricity usage over time using a line chart. | UC05 / Visualisation & Bill Breakdown | `src/xpower/visualisation.py` | Visualisation check planned | To Do |
| FR-14 | Display bill information using a bar chart or pie chart. | UC05 / Visualisation & Bill Breakdown | `visualisation.py` | Visualisation check planned | To Do |
| FR-15 | Allow the user to view results for a selected period. | UC05 / User Interface | `src/xpower/ui.py` | UI / integration test planned | To Do |

## Non-Functional Requirements

| ID | Requirement | Use Case / Design | Implementation / Evidence | Verification | Status |
|---|---|---|---|---|---|
| NFR-01 | The interface should be simple and usable without technical knowledge. | All user-facing use cases / UI Wireframes | Figma UI wireframes and `src/xpower/ui.py` | Team usability check planned | Designed |
| NFR-02 | Electricity calculations should be accurate based on the tariff settings. | UC03 / Tariff Calculation | `src/xpower/tariffs.py` | Flat = $85, TOU = $92 and Tiered = $110 assignment-example tests | Implemented |
| NFR-03 | Invalid input should show a clear error instead of crashing the program. | UC01, UC02 and UC03 | Data validation and tariff validation | Negative and invalid-input unit tests | Partly Implemented |
| NFR-04 | Main functions should be separated into simple Python modules for testing and maintenance. | High-Level Architecture | `data_import.py`, `tariffs.py`, `billing.py`, `visualisation.py`, `ui.py` | Module structure review and unit tests | In Progress |

## Status Notes

- **Implemented** - the related functionality and current unit-test evidence are present in the repository.
- **Partly Implemented / In Progress** - part of the requirement is working, but another related component still needs development.
- **Designed** - the design artefact is complete, but the coded feature is not complete yet.
- **To Do** - the requirement is traced to a planned component but still needs implementation and testing.

The matrix should be reviewed again near the end of the project so the remaining **To Do** items can be updated with their final implementation and test evidence.

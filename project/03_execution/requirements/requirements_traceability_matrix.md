# Requirements Traceability Matrix

**Status:** Updated - Sprint 3

This matrix links the approved XPower requirements to the related use case, system component, implementation or test evidence, and current project status.

## Functional Requirements

| ID | Requirement | Use Case / Design | Implementation / Evidence | Verification | Status |
|---|---|---|---|---|---|
| FR-01 | Upload electricity usage data from CSV or Excel files. | UC01 - Upload Electricity Data / Input & Interface | `src/xpower/data_import.py`, `src/xpower/ui.py` | CSV and Excel import tests in `tests/test_data_import.py`; end-to-end integration test | Implemented |
| FR-02 | Support daily and hourly electricity usage data. | UC01 - Upload Electricity Data | `src/xpower/data_import.py` | Daily and hourly data tests in `tests/test_data_import.py` | Implemented |
| FR-03 | Validate uploaded data and show clear messages for invalid data. | UC01 - Upload Electricity Data | Data Import & Validation / `data_import.py`; UI error messages in `ui.py` | Missing columns, invalid timestamp, negative usage, duplicate and unsupported-file tests; negative integration test | Implemented |
| FR-04 | Calculate a bill using Flat Rate. | UC03 - Calculate Electricity Bill | `flat_bill(...)` in `src/xpower/tariffs.py` | `test_flat_bill_example` and negative-units test | Implemented |
| FR-05 | Calculate a bill using Time-of-Use with Peak, Shoulder and Off-Peak rates. | UC03 - Calculate Electricity Bill | `tou_bill(...)` in `src/xpower/tariffs.py` | `test_tou_bill_assignment_example`; integration test | Implemented |
| FR-06 | Allow Time-of-Use periods and rates to be defined. | UC02 - Configure Tariff | Configurable TOU fields in `src/xpower/ui.py`; `time_slot(...)` and `tou_bill(...)` | Custom peak-period test and manual UI flow test | Implemented |
| FR-07 | Calculate a bill using Tiered tariff thresholds and rates. | UC03 - Calculate Electricity Bill | `tiered_bill(...)` in `src/xpower/tariffs.py` | `test_tiered_bill_example`, negative-units test and integration test | Implemented |
| FR-08 | Include an optional fixed fee in bill calculations. | UC02 / UC03 | Flat, TOU and Tiered tariff functions; fixed-fee fields in `ui.py` | Tariff tests include fixed fees; manual UI flow test | Implemented |
| FR-09 | Show a breakdown of electricity usage and costs for the selected tariff. | UC05 - View Usage, Bill and Savings Results / Visualisation & Bill Breakdown | TOU returns Peak, Shoulder and Off-Peak usage/cost breakdown in `tariffs.py`; UI currently shows tariff totals | TOU breakdown test confirms detailed usage and cost values | Partly Implemented |
| FR-10 | Compare the cost of different tariff options. | UC04 - Compare Tariffs / Bill Comparison & Savings | `compare_tariffs(...)` in `src/xpower/billing.py`; comparison table in `ui.py` | Billing comparison tests and integration test | Implemented |
| FR-11 | Identify possible savings between tariff options. | UC04 / UC05 / Bill Comparison & Savings | `calculate_savings(...)` in `src/xpower/billing.py`; savings shown in `ui.py` | Savings unit tests and integration test | Implemented |
| FR-12 | Provide simple cost-saving suggestions. | UC05 / Cost-Saving Suggestions | `cost_saving_suggestion(...)` in `src/xpower/billing.py`; suggestion shown in `ui.py` | Suggestion unit tests and integration test | Implemented |
| FR-13 | Display electricity usage over time using a line chart. | UC05 / Visualisation & Bill Breakdown | `usage_line_chart(...)` in `src/xpower/visualisation.py`; chart button in `ui.py` | Visualisation tests and integration test | Implemented |
| FR-14 | Display bill information using a bar chart or pie chart. | UC05 / Visualisation & Bill Breakdown | `bill_comparison_chart(...)` in `src/xpower/visualisation.py`; chart button in `ui.py` | Bar-chart visualisation tests and integration test | Implemented |
| FR-15 | Allow the user to view results for a selected period. | UC05 / User Interface | Not implemented in the current prototype | No current test evidence | To Do |

## Non-Functional Requirements

| ID | Requirement | Use Case / Design | Implementation / Evidence | Verification | Status |
|---|---|---|---|---|---|
| NFR-01 | The interface should be simple and usable without technical knowledge. | All user-facing use cases / UI Wireframes | Figma UI wireframes and four-step Tkinter interface in `src/xpower/ui.py` | Manual end-to-end UI walkthrough completed successfully | Implemented |
| NFR-02 | Electricity calculations should be accurate based on the tariff settings. | UC03 / Tariff Calculation | `src/xpower/tariffs.py` | Flat = $85, TOU = $92 and Tiered = $110 assignment-example tests; full integration flow passes | Implemented |
| NFR-03 | Invalid input should show a clear error instead of crashing the program. | UC01, UC02 and UC03 | Data-import validation, tariff validation and Tkinter error message boxes | Negative unit tests plus invalid-file integration test | Implemented |
| NFR-04 | Main functions should be separated into simple Python modules for testing and maintenance. | High-Level Architecture | `data_import.py`, `tariffs.py`, `billing.py`, `visualisation.py`, `ui.py` | Module structure review; 41 automated tests pass | Implemented |

## Final Status Notes

- **Implemented** - the related functionality is present in the prototype and supported by current test or manual verification evidence.
- **Partly Implemented** - part of the requirement is working, but the full user-facing behaviour is not complete.
- **To Do** - the requirement is documented and traced, but is not implemented in the current prototype.
- The final automated test suite currently passes **41 tests out of 41**.
- FR-09 remains partly implemented because detailed TOU usage/cost data exists in the calculation layer, but the UI currently presents tariff totals rather than a full selected-tariff breakdown.
- FR-15 remains outside the current prototype implementation because the UI does not include a selected-period filter.

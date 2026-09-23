# Consolidated Requirements

**Status:** Done

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | The system must allow the user to upload electricity usage data from CSV or Excel files. |
| FR-02 | The system must support daily and hourly electricity usage data. |
| FR-03 | The system must validate uploaded data and show clear messages when the file or data is invalid. |
| FR-04 | The system must calculate an electricity bill using a Flat Rate tariff. |
| FR-05 | The system must calculate an electricity bill using a Time-of-Use tariff with Peak, Shoulder and Off-Peak rates. |
| FR-06 | The system must allow Time-of-Use periods and rates to be defined. |
| FR-07 | The system must calculate an electricity bill using a Tiered tariff with different usage thresholds and rates. |
| FR-08 | The system must include an optional fixed fee when calculating electricity bills. |
| FR-09 | The system must show a breakdown of electricity usage and costs for the selected tariff. |
| FR-10 | The system must compare the cost of the different tariff options. |
| FR-11 | The system must identify possible savings between tariff options. |
| FR-12 | The system must provide simple cost-saving suggestions to the user. |
| FR-13 | The system must display electricity usage over time using a line chart. |
| FR-14 | The system must display bill information using a bar chart or pie chart. |
| FR-15 | The system must allow the user to view results for a selected period. |

## Non-Functional Requirements

| ID | Requirement |
|---|---|
| NFR-01 | The user interface should be simple and easy to use without technical knowledge. |
| NFR-02 | Electricity calculations should produce accurate results based on the tariff settings provided by the user. |
| NFR-03 | Invalid input should produce a clear error message rather than causing the program to crash. |
| NFR-04 | The prototype should keep the main functions separated into simple Python modules so the code can be tested and maintained easily. |

## Project Constraints

- The project must be completed within **5 weeks**.
- The available project budget is **$10,000**.
- The system is a working prototype and does not need to connect to XPower's real billing systems.

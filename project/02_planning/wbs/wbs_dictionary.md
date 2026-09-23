# WBS Dictionary

**Status:** Draft – Ready for Team Review

This WBS Dictionary describes every work package in the XPower Work Breakdown Structure (`project/02_planning/wbs/wbs.md`).

**How to read this dictionary**
- **Responsible, Duration, Schedule and Predecessors** come from the approved baseline in `project/02_planning/schedule/activity_schedule.md`.
- **Successors** are the work packages that list this package as a predecessor in the schedule.
- **Effort** = duration × number of people responsible.
- **Schedule** uses working project days: Days 1–5 = Week 1, 6–10 = Week 2, 11–15 = Week 3, 16–20 = Week 4, 21–25 = Week 5.
- Items marked **To confirm** are not yet decided by the team.

## Summary

| WBS ID | Work Package | Responsible | Duration | Project Days |
|---|---|---|---:|---|
| 1.1.1 | Project Charter | Pedro | 2 | 1–2 |
| 1.1.2 | Stakeholder Register | Pedro | 2 | 1–2 |
| 1.1.3 | WBS and WBS Dictionary | Mohit | 3 | 3–5 |
| 1.1.4 | Project Schedule and Gantt Chart | Pedro + Mohit | 2 | 6–7 |
| 1.1.5 | Risk Register | Lakshay | 2 | 6–7 |
| 1.1.6 | Quality Metrics Plan | Dev | 2 | 6–7 |
| 1.1.7 | Weekly Status Reports | Whole Team | 21 | 5–25 |
| 1.2.1 | Consolidated Requirements List | Dev + Lakshay | 3 | 3–5 |
| 1.2.2 | Use Case Diagram | Pedro | 2 | 6–7 |
| 1.2.3 | Use Case Descriptions | Pedro + Lakshay | 3 | 6–8 |
| 1.2.4 | Requirements Traceability Matrix | Mohit + Dev | 2 | 9–10 |
| 1.3.1 | High-Level Architecture Diagram | Mohit + Dev | 3 | 9–11 |
| 1.3.2 | Tariff Configuration Data Model | Mohit + Pedro | 2 | 6–7 |
| 1.3.3 | User Interface Wireframes | Dev | 2 | 9–10 |
| 1.4.1 | CSV/Excel Data Import and Validation | Dev + Lakshay | 4 | 6–9 |
| 1.4.2 | Flat Rate Calculation Function | Mohit + Pedro | 3 | 8–10 |
| 1.4.3 | Time-of-Use Calculation Function | Mohit + Lakshay | 4 | 10–13 |
| 1.4.4 | Tiered Calculation Function | Mohit + Pedro | 3 | 8–10 |
| 1.4.5 | Tariff Comparison, Savings and Cost-Saving Suggestions Module | Lakshay + Pedro | 3 | 14–16 |
| 1.4.6 | Selected-Period Usage and Bill Visualisation and Reporting | Dev | 3 | 17–19 |
| 1.4.7 | User Interface | Dev + Pedro | 5 | 11–15 |
| 1.4.8 | Bill Calculation and Breakdown Module | To confirm | To confirm | To confirm |
| 1.5.1 | Positive and Negative Unit Test Case Specification | Lakshay | 3 | 11–13 |
| 1.5.2 | Test Code, Execution Results and 100% Pass Evidence | Lakshay + Dev | 4 | 17–20 |
| 1.5.3 | Defect Log and Resolution Record | Whole Team | 2 | 21–22 |
| 1.6.1 | Consolidated Submission Document | Pedro | 5 | 21–25 |
| 1.6.2 | Source Code ZIP Archive | Lakshay | 2 | 23–24 |
| 1.6.3 | Individual Lessons Learned Reports | Each Member | 3 | 21–23 |

---

# 1.1 Project Management Deliverables

Documents used to plan, control and report on the project.

## 1.1.1 Project Charter

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Pedro |
| **Description** | Formal document that authorises the project and sets out its purpose, objectives, scope, stakeholders, constraints and success criteria. |
| **Deliverables** | `project/01_initiation/project_charter.md` |
| **Activities** | Define purpose and objectives; define in-scope and out-of-scope items; list constraints (5 weeks, $10,000); define success criteria; team review. |
| **Acceptance Criteria** | Charter covers purpose, objectives, scope, stakeholders, constraints and success criteria, and has been reviewed by the team. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 1–2 (Week 1) |
| **Predecessors** | None |
| **Successors** | 1.1.3, 1.1.5, 1.1.7, 1.2.1 |

## 1.1.2 Stakeholder Register

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Pedro |
| **Description** | List of the people and groups affected by the project, with their interests and influence. |
| **Deliverables** | `project/01_initiation/stakeholder_register.md` |
| **Activities** | Identify stakeholders (XPower sponsor, household customers, development team, XPower tariff/billing representative); record each stakeholder's role, interest and influence. |
| **Acceptance Criteria** | All key stakeholders are listed with their role, main interest and level of influence. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 1–2 (Week 1) |
| **Predecessors** | None |
| **Successors** | 1.2.1 |

## 1.1.3 WBS and WBS Dictionary

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Mohit |
| **Description** | Breaks the project into deliverable-based work packages and describes each package in this dictionary. |
| **Deliverables** | `project/02_planning/wbs/wbs.md`; this dictionary; WBS diagram export `project/02_planning/wbs/evidence/wbs_diagram.png` (from FigJam) |
| **Activities** | Decompose the project into deliverables; number the work packages; build the WBS diagram in FigJam; write the dictionary entries; team review. |
| **Acceptance Criteria** | Every deliverable in the scope appears in the WBS; every work package has a dictionary entry; the diagram and text use the same IDs. |
| **Duration / Effort** | 3 days / 3 person-days |
| **Schedule** | Days 3–5 (Week 1) |
| **Predecessors** | 1.1.1 |
| **Successors** | 1.1.4 |

## 1.1.4 Project Schedule and Gantt Chart

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Pedro + Mohit |
| **Description** | Activity schedule with owners, durations and dependencies for each work package, shown as a Gantt chart. |
| **Deliverables** | `project/02_planning/schedule/activity_schedule.md`; `gantt_chart.xlsx`; `evidence/gantt_chart.png` |
| **Activities** | Estimate durations; assign owners; set dependencies; build the Gantt chart; get team approval of the baseline. |
| **Acceptance Criteria** | Every WBS work package is scheduled within the 25 working days; the team has approved the baseline; the Gantt screenshot is saved for the report. |
| **Duration / Effort** | 2 days / 4 person-days |
| **Schedule** | Days 6–7 (Week 2) |
| **Predecessors** | 1.1.3 |
| **Successors** | None |

## 1.1.5 Risk Register

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Lakshay |
| **Description** | Identifies project risks and records how each will be managed. |
| **Deliverables** | `project/02_planning/risks/risk_register.md` |
| **Activities** | Identify risks; rate probability and impact; assign an owner; define mitigation and response actions. |
| **Acceptance Criteria** | At least four risks, each with probability, impact, owner, mitigation and response. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 6–7 (Week 2) |
| **Predecessors** | 1.1.1, 1.2.1 |
| **Successors** | None |

## 1.1.6 Quality Metrics Plan

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Dev |
| **Description** | Defines how the quality of the prototype and documents will be measured. |
| **Deliverables** | `project/02_planning/quality/quality_metrics.md` |
| **Activities** | Choose metrics (e.g. unit test pass rate, calculation accuracy against the case study examples); set a target for each; define how and by whom each is measured. |
| **Acceptance Criteria** | At least four metrics, each with a target, a measurement method and a responsible person. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 6–7 (Week 2) |
| **Predecessors** | 1.2.1 |
| **Successors** | None |

## 1.1.7 Weekly Status Reports

| Field | Details |
|---|---|
| **Parent** | 1.1 Project Management Deliverables |
| **Responsible** | Whole Team |
| **Description** | Regular reporting of progress, issues and next steps throughout the project, supported by the Sprint records. |
| **Deliverables** | Sprint records in `agile/` (Sprint goal, backlog, daily scrum, review and retrospective for Sprints 1–5) |
| **Activities** | Hold daily scrums; update the Sprint backlog; complete a Sprint review and retrospective each week. |
| **Acceptance Criteria** | A status record exists for each week of the project. |
| **Duration / Effort** | 21 days (ongoing, whole team) |
| **Schedule** | Days 5–25 (Weeks 1–5) |
| **Predecessors** | 1.1.1 |
| **Successors** | None |

---

# 1.2 Requirements Specification

Defines what the prototype must do.

## 1.2.1 Consolidated Requirements List

| Field | Details |
|---|---|
| **Parent** | 1.2 Requirements Specification |
| **Responsible** | Dev + Lakshay |
| **Description** | Single list of the functional and non-functional requirements for the prototype, including the CSV/Excel data requirements. |
| **Deliverables** | `project/03_execution/requirements/consolidated_requirements.md`; `data_import_requirements.md` |
| **Activities** | Analyse the case study; analyse the tutor-provided sample data; list and number each requirement; team review. |
| **Acceptance Criteria** | Covers data import, the three tariffs, bill breakdown, comparison, savings, visualisation and UI; each requirement has a unique ID. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 3–5 (Week 1) |
| **Predecessors** | 1.1.1, 1.1.2 |
| **Successors** | 1.1.5, 1.1.6, 1.2.2, 1.2.3, 1.3.2, 1.3.3, 1.4.1 |

## 1.2.2 Use Case Diagram

| Field | Details |
|---|---|
| **Parent** | 1.2 Requirements Specification |
| **Responsible** | Pedro |
| **Description** | UML diagram showing the actors (e.g. household customer) and the main things they can do with the system. |
| **Deliverables** | Use case diagram image in `project/03_execution/use_cases/evidence/` |
| **Activities** | Identify actors and use cases from the requirements; draw the diagram; team review. |
| **Acceptance Criteria** | Diagram shows all main use cases (upload data, calculate bill, compare tariffs, view charts, etc.) and matches the requirements. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 6–7 (Week 2) |
| **Predecessors** | 1.2.1 |
| **Successors** | 1.2.4, 1.3.1, 1.3.3 |

## 1.2.3 Use Case Descriptions

| Field | Details |
|---|---|
| **Parent** | 1.2 Requirements Specification |
| **Responsible** | Pedro + Lakshay |
| **Description** | Detailed written descriptions of the main use cases. |
| **Deliverables** | `project/03_execution/use_cases/use_case_descriptions.md` |
| **Activities** | For each use case, write the actor, preconditions, main flow, alternative/error flows and postconditions. |
| **Acceptance Criteria** | At least four detailed use case descriptions, consistent with the use case diagram. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 6–8 (Week 2) |
| **Predecessors** | 1.2.1 |
| **Successors** | 1.2.4, 1.3.1 |

## 1.2.4 Requirements Traceability Matrix

| Field | Details |
|---|---|
| **Parent** | 1.2 Requirements Specification |
| **Responsible** | Mohit + Dev |
| **Description** | Table linking each requirement to its use case, code module and test case. |
| **Deliverables** | `project/03_execution/requirements/requirements_traceability_matrix.md` |
| **Activities** | Map each requirement to a use case, module and test; identify gaps. |
| **Acceptance Criteria** | Every requirement is traced to at least one use case and one test case. |
| **Duration / Effort** | 2 days / 4 person-days |
| **Schedule** | Days 9–10 (Week 2) |
| **Predecessors** | 1.2.2, 1.2.3 |
| **Successors** | 1.6.1 |

---

# 1.3 System Design Package

Defines how the prototype will be built.

## 1.3.1 High-Level Architecture Diagram

| Field | Details |
|---|---|
| **Parent** | 1.3 System Design Package |
| **Responsible** | Mohit + Dev |
| **Description** | Diagram showing the main parts of the system (UI, data import, tariff calculations, billing, visualisation) and how data flows between them. |
| **Deliverables** | `project/03_execution/architecture/architecture_notes.md`; diagram image in `architecture/evidence/` |
| **Activities** | Identify components from the planned module structure; draw the data flow; team review. |
| **Acceptance Criteria** | Diagram shows every module in `src/xpower/` and matches the use cases. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 9–11 (Weeks 2–3) |
| **Predecessors** | 1.2.2, 1.2.3 |
| **Successors** | 1.6.1 |

## 1.3.2 Tariff Configuration Data Model

| Field | Details |
|---|---|
| **Parent** | 1.3 System Design Package |
| **Responsible** | Mohit + Pedro |
| **Description** | Defines how tariff settings are stored and passed to the calculation functions: flat rate, Time-of-Use rates and time bands, tier thresholds and rates, and fixed supply fees. |
| **Deliverables** | Data model definition (location **to confirm**, e.g. in `architecture_notes.md`) |
| **Activities** | Define the fields for each tariff type; confirm the Peak / Shoulder / Off-Peak hours; confirm the tier thresholds; agree default values from the case study. |
| **Acceptance Criteria** | All three tariffs can be described by the model; the rates, time bands and thresholds are agreed by the team. |
| **Duration / Effort** | 2 days / 4 person-days |
| **Schedule** | Days 6–7 (Week 2) |
| **Predecessors** | 1.2.1 |
| **Successors** | 1.4.2, 1.4.3, 1.4.4 |

## 1.3.3 User Interface Wireframes

| Field | Details |
|---|---|
| **Parent** | 1.3 System Design Package |
| **Responsible** | Dev |
| **Description** | Simple screen layouts showing how users upload data, choose tariffs and view results. |
| **Deliverables** | Wireframes in `project/03_execution/ui_design/wireframes/`; `ui_requirements.md` |
| **Activities** | Sketch each screen from the use cases; review with the team for ease of use. |
| **Acceptance Criteria** | A wireframe exists for each main use case, and the design is usable without technical knowledge. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 9–10 (Week 2) |
| **Predecessors** | 1.2.1, 1.2.2 |
| **Successors** | 1.4.7 |

---

# 1.4 Software Prototype

The working Python prototype.

## 1.4.1 CSV/Excel Data Import and Validation

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Dev + Lakshay |
| **Description** | Reads household usage data from a CSV or Excel (`.xlsx`) file, validates it and returns clean data (`timestamp`, `usage_kwh`) sorted by time. |
| **Deliverables** | `src/xpower/data_import.py` |
| **Activities** | Read CSV and the first Excel worksheet; detect timestamp and usage columns (including common alternative names); validate file type, empty files, dates, numeric and non-negative usage, duplicates; warn about time gaps; normalise the output. |
| **Acceptance Criteria** | Valid files are read and normalised; invalid data gives a clear error message; the sample file returns 720 hourly records totalling 850.67 kWh with no duplicates or negative values. |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Days 6–9 (Week 2) |
| **Predecessors** | 1.2.1 |
| **Successors** | 1.4.3, 1.4.6, 1.4.7, 1.5.1 |

## 1.4.2 Flat Rate Calculation Function

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Mohit + Pedro |
| **Description** | `calculate_flat_rate(...)` charges every kWh at the same rate and adds a fixed supply fee. |
| **Deliverables** | `calculate_flat_rate(...)` in `src/xpower/tariffs.py` |
| **Activities** | Define inputs (total kWh, rate, fixed fee); validate inputs; implement and document the calculation. |
| **Acceptance Criteria** | 300 kWh × $0.25 + $10 fixed fee = **$85.00**; negative or invalid inputs are rejected with a clear error. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 8–10 (Week 2) |
| **Predecessors** | 1.3.2 |
| **Successors** | 1.4.5, 1.5.1 |

## 1.4.3 Time-of-Use Calculation Function

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Mohit + Lakshay |
| **Description** | `calculate_tou_tariff(...)` charges each hourly record at the Peak, Shoulder or Off-Peak rate depending on the time of day, then adds the fixed fee. |
| **Deliverables** | `calculate_tou_tariff(...)` in `src/xpower/tariffs.py` |
| **Activities** | Assign each record to its time band; calculate cost per band; add the fixed fee; return the total and a breakdown by band. |
| **Acceptance Criteria** | Peak $40 + Shoulder $30 + Off-Peak $12 + $10 fixed fee = **$92.00**; daily-only data is rejected with “Time-of-Use analysis requires hourly data with timestamps.” |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Days 10–13 (Weeks 2–3) |
| **Predecessors** | 1.3.2, 1.4.1 |
| **Successors** | 1.4.5, 1.5.2 |

## 1.4.4 Tiered Calculation Function

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Mohit + Pedro |
| **Description** | `calculate_tiered_tariff(...)` charges usage progressively, so each block of kWh is charged at its own rate, then adds the fixed fee. |
| **Deliverables** | `calculate_tiered_tariff(...)` in `src/xpower/tariffs.py` |
| **Activities** | Define the tier thresholds and rates (from 1.3.2); calculate usage within each tier; add the fixed fee; return the total and a breakdown by tier. |
| **Acceptance Criteria** | 100 kWh × $0.20 + 200 kWh × $0.30 + 50 kWh × $0.40 + $10 fixed fee = **$110.00**; invalid inputs are rejected with a clear error. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 8–10 (Week 2) |
| **Predecessors** | 1.3.2 |
| **Successors** | 1.4.5, 1.5.2 |

## 1.4.5 Tariff Comparison, Savings and Cost-Saving Suggestions Module

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Lakshay + Pedro |
| **Description** | Compares the bill under all three tariffs, identifies the cheapest option, calculates the possible saving and gives simple cost-saving suggestions. |
| **Deliverables** | Comparison and savings functions in `src/xpower/billing.py` |
| **Activities** | Run all three tariff calculations on the same data; rank the results; calculate the savings against the current or most expensive tariff; generate suggestions (e.g. moving usage out of Peak hours). |
| **Acceptance Criteria** | The cheapest tariff and the saving amount are correct for known test data; suggestions are clear to a non-technical user. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Days 14–16 (Weeks 3–4) |
| **Predecessors** | 1.4.2, 1.4.3, 1.4.4 |
| **Successors** | 1.4.6, 1.5.2 |

## 1.4.6 Selected-Period Usage and Bill Visualisation and Reporting

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Dev |
| **Description** | Charts and a summary report of usage and bills for a period the user selects. |
| **Deliverables** | `src/xpower/visualisation.py` (usage line chart; bill breakdown bar or pie chart) |
| **Activities** | Filter data by the selected period; plot usage over time; plot the bill breakdown and tariff comparison; label the charts clearly. |
| **Acceptance Criteria** | Charts display correctly for the sample data and a selected period, with titles, axis labels and units. |
| **Duration / Effort** | 3 days / 3 person-days |
| **Schedule** | Days 17–19 (Week 4) |
| **Predecessors** | 1.4.1, 1.4.5 |
| **Successors** | None |

## 1.4.7 User Interface

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Dev + Pedro |
| **Description** | The screens users interact with to upload data, choose tariffs and view results and charts. |
| **Deliverables** | `src/xpower/ui.py`; `src/main.py` (entry point) |
| **Activities** | Build the screens from the wireframes; connect them to the import, tariff and billing modules; show user-friendly error messages. |
| **Acceptance Criteria** | A user can complete each main use case without technical knowledge; errors are shown as clear messages rather than crashes. |
| **Duration / Effort** | 5 days / 10 person-days |
| **Schedule** | Days 11–15 (Week 3) |
| **Predecessors** | 1.3.3, 1.4.1 |
| **Successors** | 1.5.2 |

## 1.4.8 Bill Calculation and Breakdown Module

| Field | Details |
|---|---|
| **Parent** | 1.4 Software Prototype |
| **Responsible** | To confirm (not yet in the schedule) |
| **Description** | Produces an itemised bill for the selected tariff: usage charges (per band or tier where applicable), fixed supply fee and total. |
| **Deliverables** | Bill breakdown functions in `src/xpower/billing.py` |
| **Activities** | Take the tariff calculation results; build an itemised breakdown; format amounts to two decimal places for display and charts. |
| **Acceptance Criteria** | The breakdown items add up to the total bill for each tariff and match the case study examples ($85, $92 and $110). |
| **Duration / Effort** | To confirm |
| **Schedule** | To confirm |
| **Predecessors** | To confirm (expected: 1.4.2, 1.4.3, 1.4.4) |
| **Successors** | To confirm (expected: 1.4.5, 1.4.6) |

---

# 1.5 Test Evidence Package

Proves that the prototype works correctly.

## 1.5.1 Positive and Negative Unit Test Case Specification

| Field | Details |
|---|---|
| **Parent** | 1.5 Test Evidence Package |
| **Responsible** | Lakshay |
| **Description** | Written test cases describing inputs and expected results for each assessed function. |
| **Deliverables** | `project/04_testing/test_plan.md`; `project/04_testing/test_case_matrix.md` |
| **Activities** | Write positive cases (valid inputs, expected results) and negative cases (invalid inputs, expected errors) for each function. |
| **Acceptance Criteria** | Each of `calculate_flat_rate`, `calculate_tou_tariff` and `calculate_tiered_tariff` has at least one positive and one negative test case. |
| **Duration / Effort** | 3 days / 3 person-days |
| **Schedule** | Days 11–13 (Week 3) |
| **Predecessors** | 1.4.1, 1.4.2 |
| **Successors** | 1.5.2 |

## 1.5.2 Test Code, Execution Results and 100% Pass Evidence

| Field | Details |
|---|---|
| **Parent** | 1.5 Test Evidence Package |
| **Responsible** | Lakshay + Dev |
| **Description** | Automated `pytest` tests built from the test case specification, run to produce evidence that all tests pass. |
| **Deliverables** | `tests/test_data_import.py`, `tests/test_tariffs.py`, `tests/test_billing.py`; HTML test report and 100% pass screenshot in `project/04_testing/evidence/` |
| **Activities** | Write the tests; run `pytest -v`; log and fix failures; generate the report with `pytest --html=report.html --self-contained-html`; capture the screenshot. |
| **Acceptance Criteria** | All tests pass (100% pass rate); the HTML report and screenshot are saved. |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Days 17–20 (Week 4) |
| **Predecessors** | 1.5.1, 1.4.3, 1.4.4, 1.4.5, 1.4.7 |
| **Successors** | 1.5.3, 1.6.1, 1.6.3 |

## 1.5.3 Defect Log and Resolution Record

| Field | Details |
|---|---|
| **Parent** | 1.5 Test Evidence Package |
| **Responsible** | Whole Team |
| **Description** | Record of every defect found during testing and how it was resolved. |
| **Deliverables** | `project/04_testing/defect_log.md` |
| **Activities** | Log each defect with its ID, description, severity and owner; fix and re-test; record the resolution. |
| **Acceptance Criteria** | Every defect found is logged and closed, or has an agreed reason for staying open. |
| **Duration / Effort** | 2 days / 8 person-days |
| **Schedule** | Days 21–22 (Week 5) |
| **Predecessors** | 1.5.2 |
| **Successors** | 1.6.2 |

---

# 1.6 Project Closeout Package

Final submission and project close.

## 1.6.1 Consolidated Submission Document

| Field | Details |
|---|---|
| **Parent** | 1.6 Project Closeout Package |
| **Responsible** | Pedro |
| **Description** | The final report that combines all project deliverables into one document. |
| **Deliverables** | Final report in `submission/report/` and `submission/final/` |
| **Activities** | Compile all documents and screenshots; add the group contribution table on the first page; check against `submission/checklist.md`; team review. |
| **Acceptance Criteria** | Every item in the submission checklist is included and the document opens correctly. |
| **Duration / Effort** | 5 days / 5 person-days |
| **Schedule** | Days 21–25 (Week 5) |
| **Predecessors** | 1.2.4, 1.3.1, 1.5.2 |
| **Successors** | None |

## 1.6.2 Source Code ZIP Archive

| Field | Details |
|---|---|
| **Parent** | 1.6 Project Closeout Package |
| **Responsible** | Lakshay |
| **Description** | ZIP file containing the final source and test code for submission. |
| **Deliverables** | Source code ZIP in `submission/final/` |
| **Activities** | Collect all source and test `.py` files; exclude the report and any personal upload data; check that the ZIP opens and the tests run. |
| **Acceptance Criteria** | The ZIP contains all source and test `.py` files, does not include the final report, and opens correctly. |
| **Duration / Effort** | 2 days / 2 person-days |
| **Schedule** | Days 23–24 (Week 5) |
| **Predecessors** | 1.5.3 |
| **Successors** | None |

## 1.6.3 Individual Lessons Learned Reports

| Field | Details |
|---|---|
| **Parent** | 1.6 Project Closeout Package |
| **Responsible** | Each Member (Mohit, Dev, Pedro, Lakshay) |
| **Description** | Each team member's reflection on what went well, what did not and what they would do differently. |
| **Deliverables** | `project/05_closing/lessons_learned/mohit.md`, `dev.md`, `pedro.md`, `lakshay.md` |
| **Activities** | Each member writes their own reflection on the project. |
| **Acceptance Criteria** | One completed report per team member. |
| **Duration / Effort** | 3 days / 12 person-days |
| **Schedule** | Days 21–23 (Week 5) |
| **Predecessors** | 1.5.2 |
| **Successors** | None |

---

## Review and sign-off

| Reviewer | Date | Comments |
|---|---|---|
| | | |

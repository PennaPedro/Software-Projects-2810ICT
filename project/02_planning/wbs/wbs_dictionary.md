# WBS Dictionary

**Status:** Draft – Ready for Team Review

The assignment requires WBS Dictionary entries for a minimum of four selected work packages. The four work packages below were chosen because they are the core deliverables of the prototype: getting the data in, calculating two of the required tariffs, and proving the calculations work.

| WBS ID | Work Package | Responsible |
|---|---|---|
| 1.4.1 | CSV/Excel Data Import and Validation | Dev + Lakshay |
| 1.4.2 | Flat Rate Calculation Function | Mohit + Pedro |
| 1.4.3 | Time-of-Use Calculation Function | Mohit + Lakshay |
| 1.5.2 | Test Code, Execution Results and 100% Pass Evidence | Lakshay + Dev |

Responsible, durations, project days and predecessors are taken from the approved baseline in `project/02_planning/schedule/activity_schedule.md`. Project days are working days: Days 1–5 = Week 1, 6–10 = Week 2, 11–15 = Week 3, 16–20 = Week 4 and 21–25 = Week 5. Effort = duration × number of people responsible.

---

## 1.4.1 CSV/Excel Data Import and Validation

| Field | Details |
|---|---|
| **WBS ID** | 1.4.1 |
| **Work Package Name** | CSV/Excel Data Import and Validation |
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Dev + Lakshay |
| **Description** | Build the Python function that lets a household customer upload electricity usage data from a CSV or Excel (`.xlsx`) file. The function checks the file, finds the timestamp and usage columns, validates the values and returns clean data in a standard format (`timestamp`, `usage_kwh`) sorted by time, ready for the tariff calculations and charts. |
| **Deliverables** | `src/xpower/data_import.py` with the import and validation function; clear, user-friendly error messages for invalid files. |
| **Activities** | 1. Read CSV files and the first worksheet of Excel files.<br>2. Detect the timestamp and usage columns, including common alternative names (e.g. `date`, `usage`, `consumption`).<br>3. Validate the data: file type, empty files, missing columns, invalid dates, non-numeric or negative usage, duplicate timestamps.<br>4. Warn the user when time gaps are found.<br>5. Normalise the output to `timestamp` / `usage_kwh`.<br>6. Check the result using the tutor-provided sample file. |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Project Days 6–9 (Week 2) |
| **Predecessors** | 1.2.1 Consolidated Requirements List |
| **Successors** | 1.4.3 Time-of-Use Calculation Function, 1.4.6 Visualisation and Reporting, 1.4.7 User Interface, 1.5.1 Unit Test Case Specification |
| **Resources** | Python, pandas, openpyxl; sample file `data/sample/sample_usage_data_month.csv`; requirements in `project/03_execution/requirements/data_import_requirements.md` |
| **Acceptance Criteria** | • Valid CSV and Excel files are read and converted to the normalised structure.<br>• Invalid or missing data produces a clear error message instead of crashing.<br>• The sample file returns the known checks: 720 hourly records, no duplicates, no negative values and a total of 850.67 kWh. |
| **Assumptions / Constraints** | Only `.csv` and `.xlsx` are supported. Excel import reads the first worksheet only. Daily-only data cannot be used for Time-of-Use. |
| **Risks** | Customer files may use unexpected column names or date formats. *Response:* accept common column-name alternatives and show a clear message explaining the expected format. |

---

## 1.4.2 Flat Rate Calculation Function

| Field | Details |
|---|---|
| **WBS ID** | 1.4.2 |
| **Work Package Name** | Flat Rate Calculation Function |
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Mohit + Pedro |
| **Description** | Build `calculate_flat_rate(...)`, which calculates a household electricity bill where every kWh is charged at the same rate, plus a fixed supply fee. This is the simplest tariff and the baseline the other tariffs are compared against. |
| **Deliverables** | `calculate_flat_rate(...)` in `src/xpower/tariffs.py` with a docstring and input validation. |
| **Activities** | 1. Define the inputs (total kWh, rate per kWh, fixed supply fee) and the return value.<br>2. Validate the inputs (no negative or non-numeric values).<br>3. Implement the calculation: total kWh × rate + fixed fee.<br>4. Return the total, with the breakdown available to the billing module (1.4.8).<br>5. Check the result against the case study example. |
| **Duration / Effort** | 3 days / 6 person-days |
| **Schedule** | Project Days 8–10 (Week 2) |
| **Predecessors** | 1.3.2 Tariff Configuration Data Model |
| **Successors** | 1.4.5 Tariff Comparison and Savings, 1.5.1 Unit Test Case Specification |
| **Resources** | Python; tariff rates from the Tariff Configuration Data Model (1.3.2); case study reference example |
| **Acceptance Criteria** | • Returns the correct bill for the case study example: 300 kWh × $0.25 + $10 fixed fee = **$85.00**.<br>• Rejects invalid inputs such as negative usage or a negative rate with a clear error.<br>• Passes its positive and negative unit tests. |
| **Assumptions / Constraints** | The rate and fixed fee are supplied as inputs rather than hard-coded. The fixed fee is charged once per billing period. |
| **Risks** | Rounding differences in currency values. *Response:* round the final bill to two decimal places and test with known values. |

---

## 1.4.3 Time-of-Use Calculation Function

| Field | Details |
|---|---|
| **WBS ID** | 1.4.3 |
| **Work Package Name** | Time-of-Use Calculation Function |
| **Parent** | 1.4 Software Prototype |
| **Responsible** | Mohit + Lakshay |
| **Description** | Build `calculate_tou_tariff(...)`, which charges each usage record at a Peak, Shoulder or Off-Peak rate depending on the time of day, then adds the fixed supply fee. It uses conditional logic to decide which rate applies to each hourly record. |
| **Deliverables** | `calculate_tou_tariff(...)` in `src/xpower/tariffs.py` with a docstring and input validation; a cost breakdown by Peak / Shoulder / Off-Peak. |
| **Activities** | 1. Define the Peak, Shoulder and Off-Peak time bands and rates (from 1.3.2).<br>2. Validate that the data has timestamps with time-of-day information.<br>3. Assign each hourly record to its time band.<br>4. Calculate the cost for each band and add the fixed fee.<br>5. Return the total and the breakdown by band.<br>6. Check the result against the case study example. |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Project Days 10–13 (Weeks 2–3) |
| **Predecessors** | 1.3.2 Tariff Configuration Data Model, 1.4.1 CSV/Excel Data Import and Validation |
| **Successors** | 1.4.5 Tariff Comparison and Savings, 1.5.2 Test Code and Pass Evidence |
| **Resources** | Python, pandas; normalised hourly data from 1.4.1; tariff rates and time bands from 1.3.2; case study reference example |
| **Acceptance Criteria** | • Matches the case study example: Peak $40 + Shoulder $30 + Off-Peak $12 + $10 fixed fee = **$92.00**.<br>• Each record is charged at the correct rate for its time of day.<br>• Daily-only data is rejected with the message “Time-of-Use analysis requires hourly data with timestamps.”<br>• Passes its positive and negative unit tests. |
| **Assumptions / Constraints** | Requires hourly (timestamped) data. The exact Peak / Shoulder / Off-Peak hours are **to be confirmed** in the Tariff Configuration Data Model (1.3.2). |
| **Risks** | Time bands being wrongly defined, or records on a band boundary (e.g. exactly at the start of Peak) being charged at the wrong rate. *Response:* confirm the bands with the team and write boundary unit tests. |

---

## 1.5.2 Test Code, Execution Results and 100% Pass Evidence

| Field | Details |
|---|---|
| **WBS ID** | 1.5.2 |
| **Work Package Name** | Test Code, Execution Results and 100% Pass Evidence |
| **Parent** | 1.5 Test Evidence Package |
| **Responsible** | Lakshay + Dev |
| **Description** | Write and run automated `pytest` unit tests from the test case specification (1.5.1) for the main prototype functions, and produce evidence that all tests pass for the final submission. |
| **Deliverables** | Test files in `tests/` (`test_data_import.py`, `test_tariffs.py`, `test_billing.py`); an HTML test report; a screenshot showing a 100% pass rate stored in `project/04_testing/evidence/`. |
| **Activities** | 1. Write positive tests (valid inputs give the expected results).<br>2. Write negative tests (invalid inputs are rejected with clear errors).<br>3. Run the tests with `pytest -v`.<br>4. Log any failures in the Defect Log (1.5.3) and re-test once fixed.<br>5. Generate the HTML report with `pytest --html=report.html --self-contained-html`.<br>6. Capture the 100% pass screenshot for the report. |
| **Duration / Effort** | 4 days / 8 person-days |
| **Schedule** | Project Days 17–20 (Week 4) |
| **Predecessors** | 1.5.1 Unit Test Case Specification, 1.4.3 Time-of-Use Function, 1.4.4 Tiered Function, 1.4.5 Tariff Comparison and Savings, 1.4.7 User Interface |
| **Successors** | 1.5.3 Defect Log and Resolution Record, 1.6.1 Consolidated Submission Document, 1.6.3 Individual Lessons Learned Reports |
| **Resources** | Python, pytest, pytest-html; test case specification (1.5.1); case study reference examples (Flat Rate $85, Time-of-Use $92, Tiered $110) |
| **Acceptance Criteria** | • Each assessed function (`calculate_flat_rate`, `calculate_tou_tariff`, `calculate_tiered_tariff`) has at least one positive and one negative test.<br>• Test names are clear (e.g. `test_flat_rate_valid_bill`, `test_tiered_rejects_negative_usage`).<br>• All tests pass (100% pass rate).<br>• The HTML report and screenshot are saved as evidence. |
| **Assumptions / Constraints** | Testing depends on the functions being finished on schedule. Only automated unit testing is in scope; there is no user acceptance testing with real customers. |
| **Risks** | Late completion of the functions leaves too little time for testing and fixing. *Response:* write tests as each function is finished, not only in Week 4. |

---

## Review and sign-off

| Reviewer | Date | Comments |
|---|---|---|
| | | |

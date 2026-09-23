# Quality Metrics

**Status:** Done

| Metric Name | Definition | Measurement Method | Acceptance Criteria |
|---|---|---|---|
| **Unit Test Pass Rate** | Measures whether the implemented Python functions are working correctly based on the automated tests. | Run the full test suite using `python -m pytest -v` and check how many tests pass. | **100% of automated tests should pass.** |
| **Tariff Calculation Accuracy** | Measures whether Flat Rate, Time-of-Use and Tiered tariff calculations return the correct electricity bill. | Compare the calculated results against the assignment examples for each tariff. | Flat Rate should return **$85**, Time-of-Use **$92**, and Tiered **$110** for the provided examples. |
| **Data Import Accuracy** | Measures whether CSV and Excel electricity data is imported correctly without losing or changing valid records. | Import the provided sample data and check the number of records, total usage, duplicates and negative values. | The sample should contain **720 records**, total **850.67 kWh**, with no duplicates or negative usage values. |
| **Invalid Input Handling** | Measures whether the system handles incorrect files or values without crashing. | Test invalid file types, missing columns, invalid timestamps, negative usage and invalid tariff settings. | Invalid inputs should produce a **clear error message** instead of causing the program to crash. |
| **User Task Completion** | Measures whether a user can complete the main system tasks without technical knowledge. | Ask team members to test uploading data, selecting a tariff and viewing the result without additional instructions. | Users should be able to complete the main tasks without assistance. |

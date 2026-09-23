# Risk Register

**Status:** Done

| ID | Risk | Probability | Impact | Owner | Mitigation | Response |
|---|---|---|---|---|---|---|
| R1 | Tariff calculations may produce incorrect results. | Medium | High | Mohit + Pedro | Check calculations against the assignment examples and use unit tests. | Fix the calculation and run the tests again before merging. |
| R2 | Uploaded CSV or Excel files may contain invalid or unexpected data. | High | Medium | Dev + Lakshay | Validate file type, columns, timestamps and usage values during import. | Show a clear error message and ask the user to correct the file. |
| R3 | Team tasks may be delayed or branches may become out of date. | Medium | High | Pedro | Keep the Sprint backlog updated and regularly sync branches with `main`. | Reassign or prioritise delayed work and resolve branch differences before merging. |
| R4 | Different system modules may not work correctly when connected together. | Medium | High | Dev + Lakshay | Keep modules simple and test them individually before integration. | Identify the failing module, fix the issue and re-test the integrated system. |
| R5 | The project may run short of time because it must be completed within 5 weeks. | Medium | High | Whole Team | Follow the project schedule and complete high-priority features first. | Reduce non-essential work and focus on the assignment requirements needed for submission. |

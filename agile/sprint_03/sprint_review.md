# Sprint 3 Review

**Status:** Complete

## Sprint 3 Outcome

Sprint 3 focused on completing the remaining XPower prototype features, connecting the modules into a working application, and completing final testing.

All **10 Sprint 3 backlog tasks were completed**.

The Sprint 3 goal was achieved. The prototype now supports electricity data import, tariff configuration, Flat Rate, Time-of-Use and Tiered calculations, bill comparison, savings calculation, cost-saving suggestions, visualisations and a working Tkinter user interface.

## Completed Work

| Sprint 3 Item | Evidence in Repository | Status |
|---|---|---|
| Bill Comparison | `src/xpower/billing.py` | Done |
| Savings Calculation | `src/xpower/billing.py` | Done |
| Cost-Saving Suggestions | `src/xpower/billing.py` | Done |
| Usage and Bill Visualisations | `src/xpower/visualisation.py` | Done |
| User Interface from Wireframes | `src/xpower/ui.py` | Done |
| Module Integration | `tests/test_integration.py` and working UI flow | Done |
| Positive and Negative Tests | `tests/test_billing.py`, `tests/test_visualisation.py`, `tests/test_integration.py` | Done |
| Full Test Suite | 41 automated tests passed | Done |
| Requirements Traceability Matrix Update | `project/03_execution/requirements/requirements_traceability_matrix.md` | Done |
| Sprint 3 Review | `agile/sprint_03/sprint_review.md` | Done |

## Testing Result

The final automated test suite contains **41 tests** covering:

- CSV and Excel data import and validation;
- Flat Rate, Time-of-Use and Tiered tariff calculations;
- bill comparison;
- savings calculation;
- cost-saving suggestions;
- electricity usage and bill visualisations; and
- the main end-to-end integration flow.

All **41 tests passed**, giving the implemented automated test suite a **100% pass rate**.

The user interface was also tested manually from data upload through tariff configuration, bill comparison, savings results and chart display.

## Review Notes

The main modules are now connected and the prototype can complete the intended customer flow:

```text
Upload Electricity Data
        ↓
Configure Tariffs
        ↓
Calculate Flat / TOU / Tiered Bills
        ↓
Compare Tariffs
        ↓
Show Savings and Suggestion
        ↓
Display Usage and Bill Charts
```

The updated Requirements Traceability Matrix records the final implementation status.

Most requirements are implemented. Two scope items remain incomplete in the current prototype:

- **FR-09** is partly implemented because detailed Time-of-Use usage and cost breakdown data is produced by the calculation layer, but the UI currently presents the main tariff totals rather than a complete selected-tariff breakdown.
- **FR-15** is not implemented because the current UI does not include a selected-period filter.

These limitations are documented in the RTM and can be considered when the final assignment submission is reviewed.

## Sprint Review Result

Sprint 3 is considered **complete**.

The main prototype development, integration and testing work is finished. The project is ready for the final assignment review, evidence collection and submission preparation.

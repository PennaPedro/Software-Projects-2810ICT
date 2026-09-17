# Project Charter

**Project:** XPower Household Tariff Analysis Prototype  
**Status:** Draft for Team Review  
**Project Duration:** 5 weeks  
**Budget Constraint:** $10,000  
**Prepared by:** Development Team (Mohit, Dev, Pedro, Lakshay)

## 1. Project Purpose
XPower wants a simple Household Tariff Analysis software prototype that helps household customers understand and compare electricity costs. The system should allow users to upload electricity consumption data, calculate bills under different tariff schemes, compare costs and savings, view usage and bill information visually, receive cost-saving suggestions, and use the system through a simple and friendly interface.

## 2. Project Objectives
The project aims to:

1. Build a working software prototype within the 5-week project period and the $10,000 budget constraint.
2. Support CSV and Excel electricity usage files containing daily or hourly consumption data.
3. Support the three required tariff models: Flat Rate, Time-of-Use, and Tiered Tariffs.
4. Calculate electricity bills for a selected duration and provide a clear breakdown of fixed fees and energy costs.
5. Compare tariff schemes and clearly show cost differences and possible savings.
6. Provide usage and bill visualisations, including a line chart for electricity usage and a bar or pie chart for bill breakdown.
7. Provide a simple user interface so customers can upload data and run analyses without technical knowledge.
8. Implement and test at least three Python functions, including functions with parameters, return values and conditional logic, supported by positive and negative unit tests with a 100% pass rate.
9. Complete the required project management documentation and closing activities for the group project.

## 3. High-Level Scope

### In Scope
- Import household electricity consumption data from CSV and Excel files.
- Validate and prepare daily or hourly electricity usage data for analysis.
- Flat Rate tariff calculation.
- Time-of-Use tariff calculation using Peak, Off-Peak and Shoulder periods.
- Tiered tariff calculation using consumption thresholds.
- Bill calculation including fixed supply fees and energy charges.
- Comparison of tariff costs and savings.
- Cost-saving suggestions based on the analysis.
- Electricity usage trend visualisation.
- Bill breakdown visualisation.
- A simple, user-friendly prototype interface.
- At least three Python functions used as the basis for unit testing.
- Positive and negative unit testing with 100% passing test results.
- Required project management documentation, evidence and closing reports.

### Out of Scope / Prototype Boundaries
The assignment requires a working prototype rather than a complete production electricity-billing platform. Unless the team later agrees otherwise, the following are treated as outside the current prototype scope:

- Live connection to XPower production billing systems.
- Live smart-meter or retailer API integration.
- Processing real customer payments.
- Production deployment, hosting, monitoring or operational support beyond prototype demonstration.
- Production-grade customer authentication, security certification or regulatory compliance implementation.

These boundaries are team scope decisions for keeping the project achievable within the given five-week duration and budget.

## 4. Major Deliverables

| Deliverable | Description |
|---|---|
| Project Charter and Stakeholder Register | Defines the project purpose, scope, objectives, constraints and key stakeholders. |
| Planning Package | WBS, WBS Dictionary, project schedule/Gantt chart, Risk Register and Quality Metrics. |
| Requirements and Design Package | Consolidated requirements, Use Case Diagram, at least four Use Case Descriptions, architecture design and supporting design information. |
| Software Prototype | Data import, tariff calculations, bill comparison, visualisation and user interface components required for the prototype. |
| Test Evidence Package | Python functions, positive and negative unit tests, defect records and evidence showing a 100% pass rate. |
| Final Submission Package | Consolidated group project document, source-code ZIP and individual Lessons Learned Reports. |

## 5. Key Stakeholders

| Stakeholder | Role / Interest | Influence |
|---|---|---|
| XPower Project Sponsor / Client | Requests the prototype and expects delivery within the project constraints and required features. | High |
| Household Customers | End users who need a simple, accurate and easy-to-use tariff analysis tool. | High |
| Development Team — Mohit, Dev, Pedro, Lakshay | Plans, designs, develops, tests and delivers the project. | High |
| XPower Tariff / Billing Representative | Supports validation of tariff and billing rules used by the prototype. | Medium–High |

Detailed stakeholder information is maintained in `stakeholder_register.md`.

## 6. Project Constraints
- Project duration is limited to **5 weeks**.
- Project budget is limited to **$10,000**.
- The project is a group project and contribution should be shared fairly across team members.
- The final submission must include the required project management, software and testing evidence.
- The assignment only requires at least three Python functions rather than implementation of the entire production system.
- Unit testing must include positive and negative cases and achieve a **100% pass rate**.

## 7. Project Assumptions
The following assumptions are used for planning and will be reviewed if project conditions change:

- Users will provide electricity usage data in CSV or Excel format.
- Tariff rates, time periods and tier thresholds will be supplied by the user rather than retrieved from a live external service.
- The supplied assignment requirements are sufficient for developing and demonstrating the prototype.
- Team members will communicate regularly and complete the tasks assigned to them during the five-week project period.
- Prototype data used for development and testing will not contain real customer personal or billing information.

## 8. High-Level Milestones

| Project Stage | Target Focus |
|---|---|
| Week 1 | Project foundation, charter, stakeholders, WBS, requirements analysis and initial prototype planning. |
| Week 2 | Core planning documents and early tariff/data-import development. |
| Week 3 | Requirements/design work and continued tariff, comparison and interface development. |
| Week 4 | Integration, visualisation, unit testing and defect resolution. |
| Week 5 | Final testing, evidence, documentation, Lessons Learned and submission preparation. |

Detailed activities, owners, durations and dependencies are maintained in the approved project schedule.

## 9. High-Level Risks
The detailed Risk Register will be completed during project planning. Initial risks include:

- Incorrect or inconsistent CSV/Excel input formats may cause import or analysis errors.
- Incorrect tariff rules or calculation logic may produce inaccurate bill results.
- Integration between data import, tariff calculations, visualisation and the UI may take longer than planned.
- Limited five-week delivery time may create schedule pressure if tasks are delayed.
- Uneven team availability or communication problems may affect contribution and delivery.

## 10. Success Criteria
The project will be considered successful when:

- The prototype demonstrates the main XPower requirements relevant to the agreed project scope.
- CSV/Excel household electricity usage data can be processed for analysis.
- Flat Rate, Time-of-Use and Tiered calculations operate correctly for the implemented scenarios.
- Users can compare bills and identify cost differences or savings.
- Required usage and bill visualisations can be demonstrated.
- The interface is simple enough for a non-technical user to upload data and run the analysis.
- At least three required Python functions are implemented and tested.
- Positive and negative unit tests achieve a 100% pass rate.
- Required project management documents, diagrams, screenshots and closing reports are completed.
- The project is completed within the five-week duration and planned $10,000 budget constraint.

## 11. Approval and Review
This charter establishes the initial project direction and will be reviewed by the development team before being treated as the approved baseline.

| Review Item | Status |
|---|---|
| Project scope reviewed by team | Pending Team Review |
| Objectives reviewed by team | Pending Team Review |
| Constraints confirmed against assignment brief | Confirmed |
| Stakeholders identified | Complete |
| Final charter approval | Pending Team Review |

Any significant change to project scope, schedule or agreed responsibilities should be discussed by the team and reflected in the relevant project documents rather than changed silently.

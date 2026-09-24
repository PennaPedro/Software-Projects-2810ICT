# High-Level Architecture

**Status:** Done

The XPower prototype uses a simple three-part architecture so the main system flow is easy to understand.

## 1. Input & Interface

This part handles the customer interaction and electricity usage data.

- **Household Customer** uses the User Interface.
- **CSV / Excel Files** provide the household electricity usage data.
- **Data Import & Validation** checks the uploaded file and prepares valid usage data for the tariff calculations.
- The User Interface also provides the tariff settings entered by the customer.

## 2. Tariff Calculation

This part calculates the electricity bill using the three required tariff models:

- **Flat Rate**
- **Time-of-Use**
- **Tiered**

Each calculation receives the validated electricity usage data and returns a bill result.

The diagram uses one simplified **Tariff settings** connection to keep the architecture clear. These settings represent the configurable values used by the tariff calculations, including rates, time periods, thresholds and fixed fees.

## 3. Billing & Results

The calculated bill results are passed to **Bill Comparison & Savings**.

This component:

- compares the tariff results;
- identifies possible savings;
- sends bill data to **Visualisation & Bill Breakdown**; and
- sends savings information to **Cost-Saving Suggestions**.

The results and suggestions are then displayed back to the customer through the User Interface.

## Architecture Diagram

The final High-Level Architecture Diagram is available in the project FigJam file:

https://www.figma.com/board/GLLgyMijJ5HL8sllGHBMCT?node-id=34-340

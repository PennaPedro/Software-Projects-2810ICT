# Use Case Descriptions

**Status:** Done

## Use Case 1 - Upload Electricity Data

| Field | Details |
|---|---|
| **Use Case ID** | UC01 |
| **Use Case Name** | Upload Electricity Data |
| **Actors** | Household Customer |
| **Description** | This use case allows the customer to upload household electricity usage data from a CSV or Excel file so it can be used for tariff calculations. |
| **Preconditions** | The customer has a CSV or Excel file containing electricity usage data. |
| **Trigger** | The customer selects the option to upload electricity usage data. |
| **Flow of Events** | 1. Customer selects the upload option. 2. System asks the customer to choose a CSV or Excel file. 3. Customer selects the file. 4. System reads and validates the data. 5. System converts the data into the required format. 6. System confirms that the data was loaded successfully. |
| **Alternate Flow** | If the file contains supported alternative column names, the system recognises and standardises them automatically. |
| **Postconditions** | The electricity usage data is loaded and ready for tariff calculations. |
| **Exceptions** | If the file type or data is invalid, the system displays a clear error message and the data is not loaded. |

## Use Case 2 - Configure Tariff

| Field | Details |
|---|---|
| **Use Case ID** | UC02 |
| **Use Case Name** | Configure Tariff |
| **Actors** | Household Customer |
| **Description** | This use case allows the customer to set or choose the tariff values used for bill calculations, such as flat rate, peak rate, off-peak rate, shoulder rate, tier thresholds and fixed fee. |
| **Preconditions** | The customer has already uploaded valid electricity usage data or is preparing to calculate a bill. |
| **Trigger** | The customer chooses to configure the tariff settings. |
| **Flow of Events** | 1. Customer opens the tariff configuration section. 2. System displays the available tariff options. 3. Customer enters or selects tariff values. 4. System stores the tariff settings. 5. System confirms that the tariff configuration has been saved. |
| **Alternate Flow** | The customer may use default tariff values instead of manually entering custom values. |
| **Postconditions** | The selected tariff configuration is saved and ready to be used in bill calculations. |
| **Exceptions** | If invalid tariff values are entered, the system displays an error message and asks the customer to correct them. |

## Use Case 3 - Calculate Electricity Bill

| Field | Details |
|---|---|
| **Use Case ID** | UC03 |
| **Use Case Name** | Calculate Electricity Bill |
| **Actors** | Household Customer |
| **Description** | This use case allows the customer to calculate an electricity bill using the uploaded usage data and selected tariff settings. |
| **Preconditions** | Valid electricity usage data has been uploaded and tariff settings are available. |
| **Trigger** | The customer selects the option to calculate the electricity bill. |
| **Flow of Events** | 1. Customer chooses a tariff type. 2. System retrieves the uploaded usage data. 3. System applies the selected tariff settings. 4. System calculates the bill. 5. System displays the final bill amount. |
| **Alternate Flow** | The customer may calculate the bill using Flat Rate, Time-of-Use or Tiered tariff settings. |
| **Postconditions** | The electricity bill is calculated and displayed to the customer. |
| **Exceptions** | If required data is missing, the system displays an error and the bill is not calculated. |

## Use Case 4 - Compare Tariffs

| Field | Details |
|---|---|
| **Use Case ID** | UC04 |
| **Use Case Name** | Compare Tariffs |
| **Actors** | Household Customer |
| **Description** | This use case allows the customer to compare electricity bill results across different tariff types to identify the most suitable option. |
| **Preconditions** | Electricity usage data has been uploaded and the tariff settings are available. |
| **Trigger** | The customer selects the option to compare tariffs. |
| **Flow of Events** | 1. Customer selects the compare tariffs option. 2. System calculates the bill using each tariff type. 3. System compares the results. 4. System displays the costs for each tariff. 5. System highlights the cheaper option and possible savings. |
| **Alternate Flow** | The customer may compare only selected tariff types instead of all available tariff types. |
| **Postconditions** | The tariff comparison results are displayed and the customer can see possible savings. |
| **Exceptions** | If bill calculations cannot be completed, the system displays an error and the comparison is not shown. |

## Use Case 5 - View Usage, Bill and Savings Results

| Field | Details |
|---|---|
| **Use Case ID** | UC05 |
| **Use Case Name** | View Usage, Bill and Savings Results |
| **Actors** | Household Customer |
| **Description** | This use case allows the customer to view electricity usage charts, bill breakdowns and savings suggestions after calculations are completed. |
| **Preconditions** | Electricity usage data has been uploaded and bill calculations have been completed. |
| **Trigger** | The customer opens the results or visualisation section. |
| **Flow of Events** | 1. Customer opens the results section. 2. System displays the electricity bill breakdown. 3. System shows usage and bill charts. 4. System presents tariff comparison results if available. 5. System shows possible savings suggestions. |
| **Alternate Flow** | The customer may choose to view only the bill breakdown, only the charts, or only the savings suggestions. |
| **Postconditions** | The customer can view and understand their electricity usage, bill results and possible savings. |
| **Exceptions** | If no calculation results are available, the system informs the customer that results cannot yet be displayed. |

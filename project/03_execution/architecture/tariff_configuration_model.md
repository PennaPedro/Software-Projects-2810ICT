# Tariff Configuration Data Model

**Status:** Done

The tariff configuration defines the values used by the Flat Rate, Time-of-Use and Tiered electricity calculations.

## Flat Rate

| Setting | Description | Example / Default |
|---|---|---|
| Rate | Cost charged for each kWh used | $0.25/kWh |
| Fixed Fee | Optional fixed charge added to the bill | $10.00 |

The Flat Rate bill is calculated using:

**Total = electricity usage × rate + fixed fee**

Example:

300 kWh × $0.25 + $10 = **$85.00**

The current implementation uses:

`flat_bill(units, rate, fee=0)`

---

## Time-of-Use Tariff

| Setting | Default |
|---|---:|
| Peak Rate | $0.40/kWh |
| Shoulder Rate | $0.25/kWh |
| Off-Peak Rate | $0.15/kWh |
| Peak Period | 18:00–22:00 |
| Off-Peak Period | 22:00–07:00 |
| Shoulder Period | All other times |
| Fixed Fee | Optional |

Each hourly electricity record is placed into Peak, Shoulder or Off-Peak using its timestamp.

The time periods and rates can be changed by the user instead of being permanently fixed in the calculation.

The current implementation uses:

`time_slot(...)`

and

`tou_bill(...)`

The assignment example produces:

- Peak: $40
- Shoulder: $30
- Off-Peak: $12
- Fixed Fee: $10
- **Total: $92.00**

---

## Tiered Tariff

| Tier | Usage Range | Default Rate |
|---|---|---:|
| Tier 1 | First 100 kWh | $0.20/kWh |
| Tier 2 | 101–300 kWh | $0.30/kWh |
| Tier 3 | Above 300 kWh | $0.40/kWh |

A fixed fee can also be added to the final bill.

The current implementation uses:

`tiered_bill(...)`

Example for 350 kWh:

- First 100 kWh × $0.20 = $20
- Next 200 kWh × $0.30 = $60
- Remaining 50 kWh × $0.40 = $20
- Fixed Fee = $10
- **Total: $110.00**

## Configuration Rules

- Rates must not be negative.
- Electricity usage must not be negative.
- Time-of-Use hours must be valid hours between 0 and 23.
- Tariff settings should be supplied to the calculation functions so they can be changed without changing the source code.
- Final bill values are rounded to two decimal places.

"""Tariff calculation module.

Implements:
- flat_bill(...)
- tiered_bill(...)
- time_slot(...)

Status: Done.
"""
def flat_bill(units, rate, fee=0):
    if units<0 or rate<0:
        return "Error : units and rate must not be negative"

    total=(units*rate)+fee
    return round(total,2)


def tiered_bill(units,
                 t1_limit=100, t1_rate=0.20,
                 t2_limit=300, t2_rate=0.30,
                 t3_rate=0.40,
                 fee=0):
    if units<0:
        return "Error : units must not be negative"

    if units<=t1_limit:
        cost=units*t1_rate
    elif units<=t2_limit:
        cost=(t1_limit*t1_rate)+((units-t1_limit)*t2_rate)
    else:
        cost=(t1_limit*t1_rate)+((t2_limit-t1_limit)*t2_rate)+((units-t2_limit)*t3_rate)

    return round(cost+fee,2)


def time_slot(hour):
    if not isinstance(hour,int) or hour<0 or hour>23:
        return "Error : hour must be an integer between 0 and 23"
      
    if 18<=hour<22:
        return "Peak"
    elif hour>=22 or hour<7:
        return "Off-Peak"
    else:
        return "Shoulder"


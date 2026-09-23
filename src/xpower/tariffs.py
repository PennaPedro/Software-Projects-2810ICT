"""Tariff calculation module.

Implements:
- flat_bill(...)
- tiered_bill(...)
- time_slot(...)
- tou_bill(...)

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


def time_slot(hour,
              peak_start=18, peak_end=22,
              off_peak_start=22, off_peak_end=7):
    hours=[hour,peak_start,peak_end,off_peak_start,off_peak_end]

    if any(not isinstance(value,int) or value<0 or value>23 for value in hours):
        return "Error : hour values must be integers between 0 and 23"

    if peak_start<peak_end:
        is_peak=peak_start<=hour<peak_end
    else:
        is_peak=hour>=peak_start or hour<peak_end

    if off_peak_start<off_peak_end:
        is_off_peak=off_peak_start<=hour<off_peak_end
    else:
        is_off_peak=hour>=off_peak_start or hour<off_peak_end

    if is_peak:
        return "Peak"
    elif is_off_peak:
        return "Off-Peak"
    else:
        return "Shoulder"


def tou_bill(data,
             peak_rate=0.40, shoulder_rate=0.25, off_peak_rate=0.15,
             fee=0,
             peak_start=18, peak_end=22,
             off_peak_start=22, off_peak_end=7):
    if peak_rate<0 or shoulder_rate<0 or off_peak_rate<0 or fee<0:
        return "Error : rates and fee must not be negative"

    if "timestamp" not in data.columns or "usage_kwh" not in data.columns:
        return "Error : data must contain timestamp and usage_kwh columns"

    usage={"Peak":0,"Shoulder":0,"Off-Peak":0}

    for _,row in data.iterrows():
        if row["usage_kwh"]<0:
            return "Error : usage must not be negative"

        slot=time_slot(
            row["timestamp"].hour,
            peak_start,peak_end,
            off_peak_start,off_peak_end
        )

        if slot.startswith("Error"):
            return slot

        usage[slot]+=row["usage_kwh"]

    costs={
        "Peak":round(usage["Peak"]*peak_rate,2),
        "Shoulder":round(usage["Shoulder"]*shoulder_rate,2),
        "Off-Peak":round(usage["Off-Peak"]*off_peak_rate,2)
    }

    total=costs["Peak"]+costs["Shoulder"]+costs["Off-Peak"]+fee

    return {
        "usage_kwh":{
            "Peak":round(usage["Peak"],2),
            "Shoulder":round(usage["Shoulder"],2),
            "Off-Peak":round(usage["Off-Peak"],2)
        },
        "costs":costs,
        "fixed_fee":round(fee,2),
        "total":round(total,2)
    }

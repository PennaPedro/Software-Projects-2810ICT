"""Bill comparison and savings functions for XPower.

This module compares the calculated tariff results,
finds the cheapest option and provides a simple
cost-saving suggestion.
"""


def _get_total(result):
    """Return the total cost from a tariff result."""

    # Flat Rate and Tiered currently return a number.
    if isinstance(result, (int, float)):
        return float(result)

    # Time-of-Use currently returns a dictionary
    # containing the final total.
    if isinstance(result, dict) and "total" in result:
        return float(result["total"])

    return None


def compare_tariffs(flat_result, tou_result, tiered_result):
    """Compare Flat Rate, Time-of-Use and Tiered bill results."""

    flat_total = _get_total(flat_result)
    tou_total = _get_total(tou_result)
    tiered_total = _get_total(tiered_result)

    if flat_total is None or tou_total is None or tiered_total is None:
        return "Error : invalid tariff result"

    if flat_total < 0 or tou_total < 0 or tiered_total < 0:
        return "Error : bill totals must not be negative"

    bills = {
        "Flat Rate": round(flat_total, 2),
        "Time-of-Use": round(tou_total, 2),
        "Tiered": round(tiered_total, 2),
    }

    cheapest_tariff = min(bills, key=bills.get)
    most_expensive_tariff = max(bills, key=bills.get)

    return {
        "bills": bills,
        "cheapest_tariff": cheapest_tariff,
        "cheapest_cost": bills[cheapest_tariff],
        "most_expensive_tariff": most_expensive_tariff,
        "most_expensive_cost": bills[most_expensive_tariff],
    }


def calculate_savings(comparison):
    """Calculate the maximum saving between tariff options."""

    if not isinstance(comparison, dict) or "bills" not in comparison:
        return "Error : invalid comparison result"

    bills = comparison["bills"]

    if not bills:
        return "Error : no bill results available"

    lowest = min(bills.values())
    highest = max(bills.values())

    return round(highest - lowest, 2)


def cost_saving_suggestion(comparison):
    """Return a simple suggestion based on the cheapest tariff."""

    if not isinstance(comparison, dict):
        return "Error : invalid comparison result"

    if "cheapest_tariff" not in comparison or "cheapest_cost" not in comparison:
        return "Error : comparison result is incomplete"

    tariff = comparison["cheapest_tariff"]
    cost = comparison["cheapest_cost"]

    return (
        f"{tariff} is the lowest-cost option at ${cost:.2f}. "
        "Consider this tariff if it suits your household usage."
    )
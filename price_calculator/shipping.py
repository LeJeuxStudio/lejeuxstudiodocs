''''
FS (fast ship): 7-9 days, 10CNY/kg
SS (slow ship): 12-25 days, 1400CNY/m^3
AL (airline): 3-5 days, 20CNY/kg
UPS: 3-4 days, 25CNY/kg
'''

from currency import get_currency

SHIPPING_OPT = {
    "FS": {
        "DAYS": [7,9],
        "PRICE": 10,
        "UNIT": "kg"
    },
    "SS": {
        "DAYS": [12,25],
        "PRICE": 1400,
        "UNIT": "m3"
    },
    "AL": {
        "DAYS": [3,5],
        "PRICE": 20,
        "UNIT": "kg"
    },
    "UPS": {
        "DAYS": [3,4],
        "PRICE": 25,
        "UNIT": "kg"
    }
}

def get_shipping_cost(unit, len, width, height, weight, shipping):
    total_weight = 0.0
    total_dimension = 0.0

    if shipping in ["FS", "AL", "UPS"]:
        weight *= 0.001
        total_weight = unit * weight
        return total_weight * SHIPPING_OPT.get(shipping).get("PRICE") * get_currency()

    len *= 0.01
    width *= 0.01
    height *= 0.01
    total_dimension = unit * len * width * height
    return total_dimension * SHIPPING_OPT.get(shipping).get("PRICE") * get_currency()



''''
Small Seller: sell <50 items per month as for 100 yen/item.
Big Seller: sell >=50 items per month as for 4900 yen/month.
'''

PLAN_OPT = {
    "SMALL": {
        "ITEMS": 49,
        "PRICE": 100
    },
    "BIG": {
        "items": 50,
        "PRICE": 4900
    }
}

def get_plan_cost(plan):
    if plan == "SMALL":
        return PLAN_OPT.get("SMALL").get("PRICE")
    return PLAN_OPT.get("BIG").get("PRICE") / PLAN_OPT.get("BIG").get("items")
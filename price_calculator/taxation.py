''''
Consumption Tax: 10% of the total value of goods (TVG)
                 Not needed if TVG is less than 10,000 yen
Import Duty: Recorded in another file as for the relationship
             between different products and their corresponding
             taxation
Sale Tax: 10% of the TVG
'''
TAX = {
    "CONSUMPTION_TAX": 0.1,
    "IMPORT_TAX": 0.1,
    "SALE_TAX": 0.1
}

IMPORT_TAX = {
    "Coffee": 0.15,
    "Furniture": 0.03,
    "Games": 0.03,
    "Paper": 0,
    "Rubber": 0,
    "Tableware": 0.03,
    "Tea": 0.15,
    "Toys": 0.03,
    "Others": 0.05
}

def get_total_tax(unit_price, unit, category):
    import_tax = 0.1
    for k in IMPORT_TAX:
        if k == category:
            import_tax = IMPORT_TAX.get(k)

    if unit_price * unit < 10000:
        return unit_price * (import_tax)
    return unit_price * (TAX.get("CONSUMPTION_TAX") + import_tax)
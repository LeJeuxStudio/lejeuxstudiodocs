from taxation import get_total_tax
from shipping import get_shipping_cost
from plan import get_plan_cost
from fba import get_fba_cost
from currency import get_currency

# def calculate(input_dict):
def calculate(input_dict):

    unit_price = float(input_dict.get("unit_price").get())
    unit = int(input_dict.get("unit").get())
    delivery = float(input_dict.get("delivery").get())
    len = float(input_dict.get("len").get())
    width = float(input_dict.get("width").get())
    height = float(input_dict.get("height").get())
    weight = float(input_dict.get("weight").get())
    category = input_dict.get("category").get()
    shipping = input_dict.get("shipping").get()
    upc = float(input_dict.get("upc").get())
    plan = input_dict.get("plan").get()
    commission = float(input_dict.get("commission").get())

    print(unit_price)
    print(unit)
    print(delivery)
    print(len)
    print(width)
    print(height)
    print(weight)
    print(category)
    print(shipping)
    print(upc)
    print(plan)
    print(commission)

    # unit_price = 40.0
    # unit = 100
    # delivery = 44
    # len = 23.0
    # width = 23.0
    # height = 23.0
    # weight = 6
    # category = "Others"
    # shipping = "FS"
    # upc = 0.02
    # plan = "SMALL"
    # commission = 10

    cny_to_jpy = get_currency()
    unit_price *= cny_to_jpy
    delivery *= cny_to_jpy
    upc *= cny_to_jpy

    # first calculate the cost include the cost of purchasing the items (COP),
    # UPC, shipping to Japan, tax, plan, commission

    tax_cost = get_total_tax(unit_price, unit, category)
    shipping_cost = get_shipping_cost(unit, len, width, height, weight, shipping) / unit
    plan_cost = get_plan_cost(plan)
    fba_cost = get_fba_cost(len, width, height, weight)

    total_cost = unit_price + delivery + tax_cost + shipping_cost + plan_cost + fba_cost

    selling_price = 2 * total_cost / (commission * 0.01 + 1)

    return round(selling_price, 2)

# print(calculate())
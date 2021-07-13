from tkinter import *
from tkinter import ttk

from calculator import calculate
from shipping import SHIPPING_OPT
from plan import PLAN_OPT
from taxation import IMPORT_TAX
from currency import get_currency

TITLE = "Selling Price Calculator"

def init():

    window = Tk()
    window.title(TITLE)
    window.geometry('330x360')

    unit_price = StringVar()
    unit = StringVar()
    delivery = StringVar()
    len = StringVar()
    width = StringVar()
    height = StringVar()
    weight = StringVar()
    category = StringVar()
    shipping = StringVar()
    upc = StringVar()
    plan = StringVar()
    commission = StringVar()

    input_dict = {
        "unit_price": unit_price,
        "unit": unit,
        "delivery": delivery,
        "len": len,
        "width": width,
        "height": height,
        "weight": weight,
        "category": category,
        "shipping": shipping,
        "upc": upc,
        "plan": plan,
        "commission": commission
    }

    Label(window, text="Unit Price (CNY)").grid(row=0, column=0)
    Entry(window, textvariable=unit_price, justify=RIGHT).grid(row=0, column=1)

    Label(window, text="Units").grid(row=1, column=0)
    Entry(window, textvariable=unit, justify=RIGHT).grid(row=1, column=1)

    Label(window, text="Delivery (CNY)").grid(row=2, column=0)
    Entry(window, textvariable=delivery, justify=RIGHT).grid(row=2, column=1)

    Label(window, text="Length (CM)").grid(row=3, column=0)
    Entry(window, textvariable=len, justify=RIGHT).grid(row=3, column=1)

    Label(window, text="Width (CM)").grid(row=4, column=0)
    Entry(window, textvariable=width, justify=RIGHT).grid(row=4, column=1)

    Label(window, text="Height (CM)").grid(row=5, column=0)
    Entry(window, textvariable=height, justify=RIGHT).grid(row=5, column=1)

    Label(window, text="Weight (G)").grid(row=6, column=0)
    Entry(window, textvariable=weight, justify=RIGHT).grid(row=6, column=1)

    Label(window, text="Category").grid(row=7, column=0)
    ttk.Combobox(window, width=19, textvariable=category, values= \
        list(IMPORT_TAX.keys())).grid(row=7, column=1)

    Label(window, text="Shipping Method").grid(row=8, column=0)
    ttk.Combobox(window, width = 19, textvariable = shipping, values=\
        list(SHIPPING_OPT.keys())).grid(row=8, column=1)

    Label(window, text="UPC price (CNY)").grid(row=9, column=0)
    Entry(window, textvariable=upc, justify=RIGHT).grid(row=9, column=1)

    Label(window, text="Plan").grid(row=10, column=0)
    ttk.Combobox(window, width = 19, textvariable = plan, values=\
        list(PLAN_OPT.keys())).grid(row=10, column=1)

    Label(window, text="Commission (%)").grid(row=11, column=0)
    Entry(window, textvariable=commission, justify=RIGHT).grid(row=11, column=1)

    Button(window, text="Submit", command=lambda: end(input_dict)).grid(row=12, column=1)

    window.mainloop()

def end(input_dict):

    window = Tk()
    window.title(TITLE)
    window.geometry('350x200')

    selling_price = calculate(input_dict)
    sp_cny = round(selling_price / get_currency(), 2)

    text_1 = "To be profitable"
    text_2 = "The selling price needs to be higher than {} JPN".format(selling_price)
    text_3 = "which is {} in RMB".format(sp_cny)

    Label(window, text=text_1, width=250, anchor='w').grid(row=0, column=0)
    Label(window, text=text_2, width=250, anchor='w').grid(row=1, column=0)
    Label(window, text=text_3, width=250, anchor='w').grid(row=2, column=0)

    window.mainloop()
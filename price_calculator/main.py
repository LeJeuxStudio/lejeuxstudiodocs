''''
Selling Price Calculator for selling products on Amazon Japan

Selling Price should be calculated based on the Return on Investment (ROI).

ROI is a performance measure used to evaluate the efficiency or
profitability of an investment.

ROI = Profit / Invest

How to read ROI?
    Higher ROI indicates a more profitable investment.
    * ROI >= 100% & 20% <= Profit <= 30% would be a good indication

This calculator aims to provide users with a profitable selling
price based on ROI and Profit.

The list of factors below presents the variables that help to decide
a profitable selling price.

1. Buy products from factory or seller
    Unit Price: in CNY
    Unit: the num of items to purchase
    Len, Width, Height: in cm
    Weight: in g
2. Choose the method of shipment (MOS)
   Note: this part should be extensible. e.g. In the future, we
   may have requirements of comparing different companies and
   different ways of shipment to find out the most valuable MOS.
    FS (fast ship): 7-9 days, 10CNY/kg
    SS (slow ship): 12-25 days, 1400CNY/m^3
    AL (airline): 3-5 days, 20CNY/kg
    UPS: 3-4 days, 25CNY/kg
3. UPC code
    UPC: 0.2 CNY/variety
4. Taxation
    Consumption Tax: 10% of the total value of goods (TVG)
                     Not needed if TVG is less than 10,000 yen
    Import Duty: Recorded in another file as for the relationship
                 between different products and their corresponding
                 taxation
    Sale Tax: 10% of the TVG
5. Plan on Amazon
    Small Seller: sell <50 items per month as for 100 yen/item.
    Big Seller: sell >=50 items per month as for 4900 yen/month.
6. Commissions on Amazon
    Commission fee: commission fee required by Amazon based on
                    product category
                    * Should be input by user
7. FBA fee on Amazon
    FBA fee: basically the shipping fee from Amazon Storagment Place
    to consumer's destinated address.
             Recorded in another file for the relationship between
             product's weight and dimension and its corresponding
             shipping fee. As for now, only small products info are
             recorded.

TODO: To be more comprehensive, it would be encouraging to take more
      factors into consideration. e.g. potential duration for storage,
      potential percentage for return, etc.

Note: the exchange rate is decided/queried based on the
      real-time currency from forex-python library.
'''

import user_input

user_input.init()
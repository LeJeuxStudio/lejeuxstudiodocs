'''
FBA fee: basically the shipping fee from Amazon Storagment Place
         to consumer's destinated address.
         mass in g, length in cm
'''

FBA_OPT = {
    "SMALL_LIGHT":{
        "dimension": 35 * 30 * 3.3,
        "weight": 1000,
        "price": 198,
        "key_word": "within"
    },
    "SMALL":{
        "dimension": 25 + 18 + 2,
        "weight": 250,
        "price": 282,
        "key_word": "less than"
    },
    "STANDARD_1":{
        "dimension": 33 + 24 + 2.8,
        "weight": 1000,
        "price": 381,
        "key_word": "less than"
    },
    "STANDARD_2":{
        "dimension": 60,
        "weight": 2000,
        "price": 421,
        "key_word": "less than"
    },
    "STANDARD_3":{
        "dimension": 80,
        "weight": 5000,
        "price": 467,
        "key_word": "less than"
    },
    "STANDARD_4":{
        "dimension": 100,
        "weight": 9000,
        "price": 548,
        "key_word": "less than"
    }
}

def get_fba_cost(len, width, height, weight):
    dimension_product = len * width * height
    dimension_sum = len + width + height
    for v in FBA_OPT.values():
        if v.get("key_word") == "within":
            if dimension_product < v.get("dimension") and weight < v.get("weight"):
                return v.get("price")
        else:
            if dimension_sum < v.get("dimension") and weight < v.get("weight"):
                return v.get("price")
    return 9999

# print(get_fba_cost(21,12,2.5,172))
# print(get_fba_cost(29,27,87,3500))
# print(get_fba_cost(125,85,34,18000))

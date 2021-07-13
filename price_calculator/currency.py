from forex_python.converter import CurrencyRates

def get_currency():
    currency = CurrencyRates()
    return currency.get_rate('CNY', 'JPY')
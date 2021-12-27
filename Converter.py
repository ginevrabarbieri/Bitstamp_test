import pandas as pd
from currency_converter import CurrencyConverter


def curr_converter(price, default_currency, output_currency):
    c = CurrencyConverter()
    default_currency = default_currency.upper()
    output_currency = output_currency.upper()
    converted_price = c.convert(price, default_currency, output_currency)
    return converted_price


def convert_table(output_currency):
    df = pd.read_csv('CryptoTable.csv')
    df['last'] = curr_converter(df._get_value(0, 'last'), "usd", output_currency)
    df['open'] = curr_converter(df._get_value(0, 'open'), "usd", output_currency)
    df.to_csv(r'CryptoTable.csv', index=False, header=True)

def converter(price, default_currency, output_currency):
    c = CurrencyConverter()
    converted_price = c.convert(price, default_currency, output_currency)
    return converted_price

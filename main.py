'''
This is the main file where we created
the interaction between users and the
bitstamp API.
We used argparse module to configure
positional and optional arguments.

There are two positional argument:
crypto and currency which reprepsent
respectively cryptocurrency and currency
selected by the user

Additionally, the user can specify 
which information to display, such as
last price, daily change, volume or
hourly chart
'''
from get_value import get_data
from get_value import get_price
from get_value import get_volume
from get_value import get_price
from get_value import get_change
from get_graph import get_price_chart

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
<<<<<<< HEAD


======
parser.add_argument("crypto", help="Specify the cryptocurrency code")
parser.add_argument("currency", help="Specify the currency code")
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know")
print(args.crypto, args.currency, args.specific_data)
>>>>>>> dave
get_price_chart("btcusd")
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

crypto_list = ["btc", "eth", "gbp", "ada" , "xrp", "uni", "ltc", "link", "matic", "xlm", 
                "ftt", "bch", "aave", "axs", "algo", "comp", "snx", "hbar", "chz", "cel", 
                "enj", "bat", "mkr", "zrx", "audio", "skl", "yfi" , "sushi", "alpha", "storj", 
                "sxp", "grt", "uma", "omg", "knc", "crv", "sand", "fet", "rgt", "slp", "eurt", 
                "usdt", "usdc", "dai", "pax", "eth2", "gusd"]

parser.add_argument("crypto", help="Specify the cryptocurrency code", 
			choices = crypto_list)
parser.add_argument("currency", help="Specify the currency code")
parser.add_argument("-sd","--specific_data", help="Specify which information you want to know",
			choices=["price", "volume", "change", "chart"])

args = parser.parse_args()
print(args.crypto, args.currency, args.specific_data)

value = args.crypto + args.currency
get_data(value)

if args.specific_data == "price":
    print("{} value in {} is {}".format(args.crypto, args.currency, get_price()))
elif args.specific_data == "volume":
    print("{} 24h volume is {}".format(args.crypto, get_volume()))
elif args.specific_data == "change":
    print("{} daily change is {} %".format(args.crypto, get_change()))
else:
    get_price_chart(value)
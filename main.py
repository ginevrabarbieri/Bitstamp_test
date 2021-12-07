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

import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("crypto")
parser.add_argument("currency")
parser.add_argument("-sd","--specific_data")
print(args.crypto, args.currency, args.specific_data)
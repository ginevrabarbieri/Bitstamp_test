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
args = parser.parse_args()
print(args.crypto, args.currency, args.specific_data)
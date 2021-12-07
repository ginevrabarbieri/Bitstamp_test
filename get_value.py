import requests
import json
import pandas as pd

bitstamp_URL = 'https://www.bitstamp.net/api/v2/ticker/%s/'

"""We generate a csv file with the bitstamp API by using
    the values inputted by the user"""

def get_data(value):
    #request data from API
	r = requests.get(bitstamp_URL % value)
    #create a json file that store API data
	file_json = json.loads(r.text)
    #convert the json file to a dataframe
	df = pd.DataFrame(file_json, index=[0])
    #create a csv file that contains API data
	df.to_csv (r'CryptoTable.csv', index = False, header=True)

def get_price():
    df = pd.read_csv('CryptoTable.csv')
    last_price = df._get_value(0, 'last')
    return last_price

def get_volume():
    df = pd.read_csv('CryptoTable.csv')
    volume = df._get_value(0, 'volume')
    return volume

def get_change():
    df = pd.read_csv('CryptoTable.csv')
    open_price = df._get_value(0, 'open')
    last_price = df._get_value(0, 'last')
    return (last_price-open_price)/last_price*100

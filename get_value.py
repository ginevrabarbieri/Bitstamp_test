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

'''This function create the variable last_price (which is the last price of the cryptocurrency selected) 
in order to return the last price value'''
def get_price():
    df = pd.read_csv('CryptoTable.csv')
    last_price = df._get_value(0, 'last')
    return last_price

'''This function create the variable volume (which is the daily volume of the cryptocurrency selected) 
in order to return the volume value'''
def get_volume():
    df = pd.read_csv('CryptoTable.csv')
    volume = df._get_value(0, 'volume')
    return volume

'''This function create the variable open_price (which is the first daily price of the cryptocurrency selected) and then 
create the variable last_price (which is the last price of the cryptocurrency selected) in ordet to return the change in price'''
def get_change():
    df = pd.read_csv('CryptoTable.csv')
    open_price = df._get_value(0, 'open')
    last_price = df._get_value(0, 'last')
    return (last_price-open_price)/last_price*100

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import csv 
from datetime import datetime

bitstamp_URL = 'https://www.bitstamp.net/api/v2/transactions/%s/'

def get_price_chart(currency="btcusd"):
    # Request data from API
    r = requests.get(bitstamp_URL % currency)
    # Create the file json that store API datas
    file_json = json.loads(r.text)
    # Converting the file json to a dataframe
    df = pd.DataFrame(file_json)
    # Creating the csv file that contains the data
    df.to_csv (r'Price.csv', index = False, header=True)
    #Read the csv file
    price_df = pd.read_csv("price.csv")
    
    """The dataframe expresses data and time using the timestamp. We want to convert it in simply date and 
    time and put them in different columns, to better manage data."""
    dates = []
    for date in price_df['date']:
        date = int(date)  
        date = datetime.utcfromtimestamp(date).strftime('%d-%m-%Y %H:%M:%S')
        dates.append(date)
    price_df['Date and time'] = dates
    price_df['Date'], price_df['Time'] = price_df['Date and time'].str.split(' ', 1).str
    price_df = price_df.drop(['Date and time', 'date'], axis = 1)
    
    """Since the graph will display an entire hour of variation of prices, minute by minute, we want to
    select only some important time-references to make the graph more readable."""
    timing= price_df['Time'].tolist()
    values =[] 
    for n in range (1,len(price_df)+1, int(len(price_df)/6)):
        values.append(timing[n])
    date=price_df['Date'][0]
    
    plot = plt.figure(figsize=(15, 7))
    plot =plt.plot('Time','price', data=price_df)
    plot =plt.title('Price of btcusd for '+ date)
    plot =plt.xticks(values, values)
    return plot

get_price_chart("btcusd")
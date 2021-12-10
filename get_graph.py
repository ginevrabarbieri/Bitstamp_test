import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import csv 
from datetime import datetime
#from converter import curr_converter, convert_table


bitstamp_URL = "https://www.bitstamp.net/api/v2/transactions/%s/"

def get_file(value):
    """---"""
    r = requests.get(bitstamp_URL % value)
    file_json = json.loads(r.text)
    df = pd.DataFrame(file_json)
    df.to_csv (r"Price.csv", index = False, header=True)
    df_price = pd.read_csv("Price.csv")
    df_price = df_price.sort_values(by=["date"], ascending=True)
    return df_price

def date_adjustment(df):
    """The dataframe expresses data and time using timestamp. We want to convert it in simply date and 
    time and put them in different columns, to better manage data."""
    dates = []
    for date in df["date"]:
        date = int(date)  
        date = datetime.fromtimestamp(date).strftime("%d-%m-%Y %H:%M:%S")
        dates.append(date)
    df["Date and time"] = dates
    df[["Date", "Time"]] = df["Date and time"].str.split(" ", n=1, expand=True)
    df = df.drop(["Date and time", "date"], axis = 1)
    return(df)

def get_price_chart(df, value):
    """Since the graph will display an entire hour of variation of prices, minute by minute, we want to
    select only some important time-references to make the graph more readable."""
    timing = df["Time"].tolist()
    time_values =[] 
    # division for 6, we want to consider more or less every 10 minutes
    for n in range (0, len(df)+1, int(len(df)/6)):
        time_values.append(timing[n])
    date=df["Date"][0]
    plot = plt.figure(figsize=(15, 7))
    plot = plt.plot("Time","price", data=df)
    plot = plt.title("Price of " + value + " for "+ date)
    plot = plt.xticks(time_values, time_values)
    plot = plt.show()
    return plot


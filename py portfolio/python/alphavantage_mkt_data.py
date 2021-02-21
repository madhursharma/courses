# -*- coding: utf-8 -*-
"""
This is API to get mkt data from alphavantage.co
Created on Mon Oct 26 16:40:37 2020

@author: msharma
"""
#import json
import alphavantage_mkt_data as mkt_data
import requests
import pandas as pd

def get_stock(ticker="GOOGL", format="pandas"):
    """
    

    """
    function="TIME_SERIES_DAILY"
    url = 'function=TIME_SERIES_DAILY_ADJUSTED&symbol={}'.format(ticker)
    response=get_data(url)
    #print(response.json())
    return response



def get_data(url, format='txt' , *args):
    key = 'G7MRDC02QFMP47BN'
    base_url = "https://www.alphavantage.co/query?"
    url = base_url + "apikey={}".format(key) + "&" + url
    url = url.format(*args)
    response = requests.get(url)
    res = None
    if format == 'json' :
        res = response.json() 
    elif format == 'pandas':
        res = pd.Series(response.json())
    else: res = response.content
    #return response
    return res
    

ds1 = get_stock(ticker='AAPL', format="pandas")
ds2 = get_stock(ticker="GOOGL", format="pandas")
    
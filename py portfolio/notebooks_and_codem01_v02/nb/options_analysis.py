# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 23:26:43 2020

@author: msharma
"""
import pandas as pd
import scipy as sc
import numpy as np

import requests
import json 
def price_option_bs(spot, k, iv30, days, rf=0.0, rd=0.0):
    '''
    Calculate the Black-Scholes price of the options
    d1 = [ ln(S/K) + (r + (iv30**2)/2) * T ] / (iv30 * sqrt(T))  
    d2= d1 - iv30 * sqrt (T) 
    
    Price of European call
    c = Norm(d1) * S - Norm(d2) * K * exp(-rT)
    p = Norm(-d2) * K *exp(-rT) - Norm(-d1) * S
    price = 
    Parameters
    ----------
    spot : pandas.Dataframe
        Current spot price of the underlying stock.
    k : pandas.Dataframe
        Strike price of the option.
    iv30 : float
        volatility of the option is it's stddev. Usually daily vol is used. Convert to 
        annual sqrt(daysToExp/30).
    days : pandas.Dataframe
        no of days to expiration.
    rf : float(), optional
        Risk free rate (annualized). The default is 0.0.
    rd : pandas.Dataframe, optional
        divident rate(annualized). The default is 0.0.

    Returns
    -------
    (,)
    '''
    #convert traded days to year
    t = days/255.0
    #TODO: adjust the 
    d1 = sc.log(np.divide(spot, k)) + np.multiply((rf + vol/2), t)
    d1 = d1 / np.sqrt(vol * t)
    d2 = d1 - np.sqrt(vol * t)
    c = spot * np.norm(d1) + np.norm(d2) * k * np.exp(-rf * t)
    p = np.norm(-d2) * k * np.exp(-rf * t) - np.norm(-d1) * spot
    return (c, p)

def get_data(ticker='AAPL'):
    #Get real time data from Alpha Vantage
    key = 'G7MRDC02QFMP47BN'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
    response = requests.get(url)
    #print(response.json())
    return response
    
#print (get_data().json())

def test_option_data():
    spot_price = 108.22
    d = pd.read_csv("E:\\GitHub\\coursera\\courses\\py portfolio\\notebooks_and_codem01_v02\\nb\\data\\aapl_options.csv",
                header='infer', sep=';', parse_dates=True)
    #Parse dates
    d["SpotDt"] = pd.to_datetime(d['Spot Date'], format="%m/%d/%y")
    d["ExpDt"] = pd.to_datetime(d['Expiration Date'], format="%m/%d/%y")
    #Override Spot Date
    currDate = datetime.datetime.strptime("09/25/20", "%m/%d/%y")
    d["SpotDt"] = currDate
    #Add days to expiration
    d['Days2Exp'] = d['ExpDt'] - d['SpotDt']
    d['Spot Price'] = spot_price
    d['PriceDiff'] = np.subtract (d['Strike'] , spot_price)
    
    
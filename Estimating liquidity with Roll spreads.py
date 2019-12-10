# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:48:42 2019

@author: Dell
"""

'''
ROll Spread measure liquidaity where:
     Liquidity is defined as how quickly we can dispose of our asset without losing its
     intrinsic value.
Determining Roll spread observation using ROLL(1985)
Here estimates are based on serial covariance in price changes
Formula:
        ROLL Spread-2*root(-covariance(change in closing price of day and day-1,closing \
        price of day-1))
        %spread=roll spread/average share price in estimation period
        
'''

#lets test the roll spread for IBM
#lets import the modules well be using
import yfinance as yf
import scipy as sp

#download data
data=yf.download('IBM',start='2013-9-1',end='2013-11-11')
'''
Key note is that roll spread is appropriate for high frequency data
However for purposes of demonstration we'll use historical data from IBM

'''
#determine change in prices
returns=sp.diff(data['Adj Close'])
#find covariance matrix
covariance=sp.cov(returns[:-1],returns[1:])

if covariance[0,1]<0:#cov[0.1] defines a matrix of row 1 and column 0
    print("Roll spread for IBM is", round(2*sp.sqrt(-covariance[0,1]),3))
else:
    print("Cov is positive for IBM ", round(covariance[0,1],3))
    
'''
When roll value is positive, Roll's model
would fail. In a real world, it could occur for many cases. Usually, practitioners
adopt two approaches: when the spread is negative, we just ignore those cases or use
other methods to estimate spread. The second approach is to add a negative sign in
front of a positive covariance.
'''
    

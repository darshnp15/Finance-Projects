import yfinance as yf
import pandas as pd
import numpy as np

stockList = ["INTU", "SAP"]
print("prgmde")

riskFreeRate = 0.0409
marketRate = 0.10

for i in stockList:
    stock = yf.Ticker(i)
    
    intrinsicValue = 0
    k = riskFreeRate + stock.info['beta']*(marketRate-riskFreeRate)
    counter = 1
    for ii in stock.dividends:
        intrinsicValue = intrinsicValue + (ii/((1+k)**counter))
        counter = counter + 1

    '''
    earningsReport = stock.earnings_dates['Reported EPS']
    reportedEPS = 0
    for j in earningsReport:
        if np.isnan(j):
            continue
        else:
            reportedEPS = j
            break
    '''
    PVGO = stock.info['currentPrice'] - stock.info['forwardEps']/k

    print(i, " Intrinsic Value: ", intrinsicValue)
    print(i, " Payout Ratio: ", stock.info['payoutRatio'])
    print(i, " Price to Book Ratio: ", stock.info['priceToBook'])
    print(i, " Debt to Equity Ratio: ", stock.info['debtToEquity'])
    print(i, " Return on Equity: ", stock.info['returnOnEquity'])
    print(i, " Present Value of Growth Opportunities: ", PVGO)
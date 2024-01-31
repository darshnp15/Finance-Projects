import yfinance, numpy, pandas, pandas_datareader

myFile = open("all_tickers.txt", "r")
fileData = myFile.read()
tickerList = fileData.split("\n")
myFile.close()

tickerAmount = len(tickerList)

for i in tickerList:
    stock = yfinance.Ticker(i)

    try:
        stock.info
        print(i)
    except:
        tickerList.remove(i)
        print("===============")
        print(i)
        print("===============")
        pass

with open('allTickersEditted.txt', 'w') as f:
    for line in tickerList:
        f.write(line)
        f.write('\n')
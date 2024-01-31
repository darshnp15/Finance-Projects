import yfinance, pandas, multiprocessing, time

def getEPS(ticker):
    stock = yfinance.Ticker(ticker)

    try:
        EPSList[ticker] = stock.info['trailingEps']
    except KeyError:
        EPSList[ticker] = float('nan')
        pass

    print("=========================")
    print("index:", tickerList.index(ticker))
    print("value:", EPSList[ticker])
    print("=========================")

myFile = open("allTickersEditted.txt", "r")
fileData = myFile.read()
tickerList = fileData.split("\n")
myFile.close()

tickerAmount = len(tickerList)
#print(tickerAmount)
EPSList = dict.fromkeys(range(7250))

if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in tickerList:
        p = multiprocessing.Process(target=getEPS, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))

#quickSort(PEGRatioList, 0, tickerAmount-1)

df = pandas.DataFrame(data=EPSList, index=[0])
df = (df.T)
#print (df)
df.to_excel('trailingEPSs.xlsx')
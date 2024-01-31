import requests

# Set your Alpha Vantage API key
API_KEY = "L9XPCRRYM47IP5F1"

# Endpoint URL for earnings per share (EPS) data
#url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol=YOUR_SYMBOL&apikey={API_KEY}"
url = f"https://www.alphavantage.co/query?function=APO&symbol=YOUR_SYMBOL&interval=monthly&series_type=close&fastperiod=10&matype=1&apikey={API_KEY}"

'''
# Read the list of S&P 500 stocks into a string
myFile = open("S&P500_tickers.txt", "r")
fileData = myFile.read()
sp_500_symbols = fileData.split("\n")
myFile.close()
'''
# List to store EPS data for each stock
eps_data = []

current_url = url.replace("YOUR_SYMBOL", "AAPL")
response = requests.get(current_url)
data = response.json()
print(data)

'''
# Iterate through the list of S&P 500 stock symbols
for symbol in sp_500_symbols:
    # Replace 'YOUR_SYMBOL' with the current stock symbol
    current_url = url.replace("YOUR_SYMBOL", symbol)
    
    # Make the API call
    response = requests.get(current_url)
    
    # Parse the response JSON
    data = response.json()
    
    # Extract the EPS data from the response
    eps = data["earnings"]["quarterlyEarnings"]
    
    # Append the EPS data to the list
    eps_data.append(eps)

# Print the EPS data for all stocks
for eps in eps_data:
    print(eps)
'''
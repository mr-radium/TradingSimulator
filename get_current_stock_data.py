import requests
import json

# URL (http://localhost:3000/nse/get_quote_info?companyName=ONGC)

def get_current_stock_data_nse(stock):

    stock = stock.upper()

    print("Please wait while we are fetching your request...")

    # If there's "&" symbol in the the stocky symbol it will replace it with "%26"
    if "&" in stock:
        stock = stock.replace("&", "%26")

    # If there's "'" symbol in the the stocky symbol it will replace it with "%27"
    if "'" in stock:
        stock = stock.replace("'", "%27")

    res = requests.get('http://localhost:3000/nse/get_quote_info?companyName=' + stock)
    
    stock_info = json.loads(res.text)

    market_status = json.loads(requests.get('http://localhost:3000/get_market_status').text)
    
    if len(stock_info["data"]) == 0:
        print("")
        print("Sorry, we can't find the status of the following stock symbol.")

    elif market_status["status"] == "closed":
        print("")
        print("Company Name: " + stock_info["data"][0]["companyName"])
        print("Symbol: " + stock_info["data"][0]["symbol"])
        print("")
        print("Current Price: " + stock_info["data"][0]["lastPrice"])
        print("Total Sell Quantity: " + stock_info["data"][0]["totalSellQuantity"])
        print("Open Price: " + stock_info["data"][0]["open"] + " | Day High: " + stock_info["data"][0]["dayHigh"] + " | Day Low: " + stock_info["data"][0]["dayLow"] + " | Close Price: " + stock_info["data"][0]["lastPrice"])
        print("")
        print("Last Updated: " + stock_info["lastUpdateTime"])

    else:
        print("")
        print("Company Name: " + stock_info["data"][0]["companyName"])
        print("Symbol: " + stock_info["data"][0]["symbol"])
        print("")
        print("Current Price: " + stock_info["data"][0]["lastPrice"])
        print("Total Sell Quantity: " + stock_info["data"][0]["totalSellQuantity"])
        print("Open Price: " + stock_info["data"][0]["open"] + " | Day High: " + stock_info["data"][0]["dayHigh"] + " | Day Low: " + stock_info["data"][0]["dayLow"])
        print("")
        print("Last Updated: " + stock_info["lastUpdateTime"])
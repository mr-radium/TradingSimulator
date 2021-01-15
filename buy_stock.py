import requests
import json

# Import functions form other files
from utilities import un_comma
from get_current_stock_data import get_current_stock_data_nse

def buy_stock(stock, quantity):
    stock = stock.upper()

    if "&" in stock:
        stock = stock.replace("&", "%26")
    
    if " " in stock:
        stock = stock.replace(" ", "%20")
        
    # First it would get the stock data from NSE
    get_current_stock_data_nse(stock)

    res = requests.get("http://localhost:3000/nse/get_quote_info?companyName=" + stock)
    stock_info = json.loads(res.text)
        
    # This will get the data from profile.json and store it in a variable
    profile = open('profile.json',)
    profile_data = json.loads(profile.read())
    profile.close()
    
    try:
        # Now it would overwrite the current-balence with the new balence and then it would overwrite 
        # the varibale to profile.json
        if un_comma(profile_data["current-balence"]) - un_comma(stock_info["data"][0]["lastPrice"]) * un_comma(quantity) < 0:
            print("")
            print("You don't have enough money buy the following stock.")

        else:
            profile_data["current-balence"] = str(un_comma(profile_data["current-balence"]) - (un_comma(stock_info["data"][0]["lastPrice"])) * un_comma(quantity)) 
            trades_len = len(profile_data["trades"])
            profile_data["trades"].append(
                {
                    "trade-id": str(trades_len),
                    "trade-status": "bought",
                    "trade-company": stock_info["data"][0]["symbol"],
                    "trade-price": stock_info["data"][0]["lastPrice"],
                    "trade-quantity": quantity,
                    "total-trade-price": str((un_comma(stock_info["data"][0]["lastPrice"])) * un_comma(quantity))
                }
            )
            profile_data["bought"].append(
                {
                    "bought-id": str(trades_len),
                    "bought-company": stock_info["data"][0]["symbol"],
                    "bought-price": stock_info["data"][0]["lastPrice"],
                    "bought-quantity": quantity,
                    "total-trade-price": str((un_comma(stock_info["data"][0]["lastPrice"])) * un_comma(quantity))
                }
            )
            profile_data["portfolio"].append(
                {
                    "bought-id": str(trades_len),
                    "bought-company": stock_info["data"][0]["symbol"],
                    "bought-price": stock_info["data"][0]["lastPrice"],
                    "bought-quantity": quantity,
                    "total-trade-price": str((un_comma(stock_info["data"][0]["lastPrice"])) * un_comma(quantity))
                }
            )

            profile_edit = open('profile.json', 'w')
            profile_edit.write(json.dumps(profile_data, indent = 4))
            profile_edit.close()

            print("")
            print("Bought " + quantity + " " +  stock_info["data"][0]["symbol"] + " stocks at each of ₹" + stock_info["data"][0]["lastPrice"])
            print("Total price deducted from your current balence: ₹" +  str((un_comma(stock_info["data"][0]["lastPrice"])) * un_comma(quantity)))
            print("Your current balence: ₹" + profile_data["current-balence"])
    except:
        pass
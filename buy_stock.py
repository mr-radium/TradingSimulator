import requests
import json

# Import functions form other files
from utilities import un_comma
from get_current_stock_data import get_current_stock_data_nse

def buy_stock(stock, quantity):
    stock = stock.upper()
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
        if float(profile_data["current-balence"]) - un_comma(stock_info["data"][0]["lastPrice"]) * float(quantity) < 0:
            print("Sorry you don't have enough money buy the following stock.")
            profile_data["current-balence"] = str(float(profile_data["current-balence"]) - un_comma(stock_info["data"][0]["lastPrice"]) * float(quantity))

        else:
            trades_len = len(profile_data["trades"])
            profile_data["trades"].append(
                {
                    "trade-id": str(trades_len),
                    "trade-status": "buy",
                    "trade-company": stock_info["data"][0]["symbol"],
                    "trade-price": stock_info["data"][0]["lastPrice"],
                    "trade-quantity": quantity,
                    "total-trade-price": str((un_comma(stock_info["data"][0]["lastPrice"])) * float(quantity))
                }
            )
            profile_data["bought"].append(
                {
                    "brought-id": str(trades_len),
                    "brought-company": stock_info["data"][0]["symbol"],
                    "brought-price": stock_info["data"][0]["lastPrice"],
                    "brought-quantity": quantity,
                    "total-trade-price": str((un_comma(stock_info["data"][0]["lastPrice"])) * float(quantity))
                }
            )

            profile_edit = open('profile.json', 'w')
            profile_edit.write(json.dumps(profile_data, indent = 4))
            profile_edit.close()

            print("Brought " + stock_info["data"][0]["symbol"] + " at the quantity of" + quantity)

    except:
        print("Sorry but the stock of your symbol does'nt exist.")
        print("")
        print("You could use our symbol searcher for help!")
        print("For that just type the company name or symbol followed by ls")
        print("For example- 'ls Bharat Petroleum' or 'ls BPCL'")
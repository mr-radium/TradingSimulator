import requests
import json


from get_current_stock_data import get_current_stock_data_nse

def buy_stock(stock):
    
    get_current_stock_data_nse(stock)
    stock = stock.upper()
    res = requests.get("http://localhost:3000/nse/get_quote_info?companyName=" + stock)
    stock_info = json.loads(res.text)

    profile = open('profile.json', "r")
    profile_data = json.loads(profile)
    print(int(stock_info["data"][0]["lastPrice"]) - int(profile_data["current-balence"]))

    profile.close()

    
    
import requests
import json

# Import functions form other files
from utilities import un_comma
from get_current_stock_data import get_current_stock_data_nse

def buy_stock(stock):
    # First it would get the stock data from NSE
    get_current_stock_data_nse(stock)
    stock = stock.upper()
    res = requests.get("http://localhost:3000/nse/get_quote_info?companyName=" + stock)
    stock_info = json.loads(res.text)
        
    # This will get the data from profile.json and store it in a variable
    profile = open('profile.json',)
    profile_data = json.load(profile)
    profile.close()
    
    # Now it would overwrite the current-balence with the new balence and then it would overwrite 
    # the varibale to profile.json
    profile_data["current-balence"] = str(float(profile_data["current-balence"]) - un_comma(stock_info["data"][0]["lastPrice"]))
    profile_edit = open('profile.json', 'w')
    profile_edit.write(json.dumps(profile_data))
    profile_edit.close()
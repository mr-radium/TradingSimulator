import requests
import json

def sell_stock(stock):
    stock = stock.upper()

    if "&" in stock:
        stock = stock.replace("&", "%26")
    
    profile_data = json.loads(open('profile.json',).read())
    portfolio_length = len(profile_data["portfolio"])

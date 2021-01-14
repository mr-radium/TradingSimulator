import requests
import json

def sell_stock(stock):
    stock = stock.upper()

    if "&" in stock:
        stock = stock.replace("&", "%26")
    
    if " " in stock:
        stock = stock.replace(" ", "%20")
    
    profile_data = json.loads(open("profile.json",).read())
    portfolio_lenght = len(profile_data["portfolio"])


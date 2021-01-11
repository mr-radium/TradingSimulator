import requests
import json

def sell_stock(stock):
    stock = stock.upper()
    
    if "&" in keywords:
        keywords = keywords.replace("&", "%26")
    
    if " " in keywords:
        keywords = keywords.replace(" ", "%20")
    
    profile_data = json.loads(open("profile.json",).read())
    portfolio_lenght = len(profile_data["portfolio"])

    i = 0
    while i < portfolio_lenght:
        if stock in profile_data["portfolio"][i]["bought-company"]:
            print("found it")
            i += 1
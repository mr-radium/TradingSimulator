import requests
import json

def sell_stock(stock):
    stock = stock.upper()

    if "&" in stock:
        stock = stock.replace("&", "%26")
    
    

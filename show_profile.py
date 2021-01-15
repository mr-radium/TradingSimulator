import json
import requests
from utilities import un_comma

def show_profile():
    profile_data = json.loads(open('profile.json',).read())
    portfolio_lenght = len(profile_data["portfolio"])


    print("")
    print(profile_data["username"] + ',')
    print("Current Balence: " + profile_data["current-balence"])
    print("")
    print("Portfolio")

    i = 0
    while i < portfolio_lenght:

        stock = profile_data["portfolio"][i]["bought-company"]
        res = requests.get("http://localhost:3000/nse/get_quote_info?companyName=" + stock)
        stock_info = json.loads(res.text)

        bought_price = un_comma(profile_data["portfolio"][i]["bought-price"])
        bought_quantity = un_comma(profile_data["portfolio"][i]["bought-quantity"])
        total_bought_price = bought_price * bought_quantity

        if un_comma(profile_data["portfolio"][i]["bought-price"]) < un_comma(stock_info["data"][0]["lastPrice"]):
            print("")
            print(profile_data["portfolio"][i]["bought-company"])
            print("Bought Price: ₹" + profile_data["portfolio"][i]["bought-price"])
            print("Quantity: " + profile_data["portfolio"][i]["bought-quantity"])

            # This variable limits the amount of digits after the decimal            
            limited_float_profit = "{:.2f}".format(un_comma(stock_info["data"][0]["lastPrice"]) * bought_quantity - total_bought_price)

            # This thing prints the profit in green color  
            print("\033[32m" + "+" + limited_float_profit)
            print("\033[39m")

        if un_comma(profile_data["portfolio"][i]["bought-price"]) > un_comma(stock_info["data"][0]["lastPrice"]):
            print("")
            print(profile_data["portfolio"][i]["bought-company"])
            print("Bought Price: ₹" + profile_data["portfolio"][i]["bought-price"])
            print("Quantity: " + profile_data["portfolio"][i]["bought-quantity"])

            # This variable limits the amount of digits after the decimal
            limited_float_loss = "{:.2f}".format(total_bought_price - un_comma(stock_info["data"][0]["lastPrice"]) * bought_quantity)    

            # This thing prints the loss in red color  
            print("\033[31m" + "-" + limited_float_loss)
            print("\033[39m")

        if un_comma(profile_data["portfolio"][i]["bought-price"]) == un_comma(stock_info["data"][0]["lastPrice"]):
            print("")
            print(profile_data["portfolio"][i]["bought-company"])
            print("Bought Price: ₹" + profile_data["portfolio"][i]["bought-price"])
            print("Quantity: " + profile_data["portfolio"][i]["bought-quantity"])

            # This thing prints the profit in green color  
            print("\033[32m" + "+00")
            print("\033[39m")
        i += 1



        
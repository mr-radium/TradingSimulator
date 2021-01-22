import json
import requests
from utilities import un_comma

def show_profile():
    profile_data = json.loads(open('profile.json',).read())
    portfolio_length = len(profile_data["portfolio"])
    portfolio_value = 0.0
    portfolio_profit = 0.0
    portfolio_loss = 0.0

    print("")
    print(profile_data["username"] + ',')
    print("Current Balence: " + profile_data["current-balence"])
    print("")
    print("Portfolio")

    i = 0
    while i < portfolio_length:

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

            portfolio_value += float(limited_float_profit)
            portfolio_profit += float(limited_float_profit)

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

            portfolio_value -= float(limited_float_loss)
            portfolio_loss += float(limited_float_loss)

            # This thing prints the loss in red color  
            print("\033[31m" + "-" + limited_float_loss)
            print("\033[39m")

        if un_comma(profile_data["portfolio"][i]["bought-price"]) == un_comma(stock_info["data"][0]["lastPrice"]):
            print("")
            print(profile_data["portfolio"][i]["bought-company"])
            print("Bought Price: ₹" + profile_data["portfolio"][i]["bought-price"])
            print("Quantity: " + profile_data["portfolio"][i]["bought-quantity"])

            # This thing prints the profit in green color  
            print("\033[32m" + "+0.00")
            print("\033[39m")

      
        i += 1

    if "-" in str(portfolio_value):
        portfolio_value = str(portfolio_value).replace("-", "")
        print("\033[31m" + "Portfolio Value: -₹" + str(portfolio_value))
    else:
        print("\033[32m" + "Portfolio Value: +₹" + str(portfolio_value))

    print("\033[32m" + "Portfolio Profit: ₹" + str(portfolio_profit))
    print("\033[31m" + "Portfolio Loss: ₹" + str(portfolio_loss))
    print("\033[39m")
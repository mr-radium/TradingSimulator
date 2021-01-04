import requests
import json

# res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=BAC&interval=5min&apikey=FLB281YD66I569JV')
# print(res.text)

def sym_search(keywords):
    res = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + keywords + '&apikey=FLB281YD66I569JV')
    print("Please wait while we are fetching your requests.")
    print(res.text)

task = input("What do you want to do: ")

if "ls" in task:
    try:
        keywords = input("Enter the Keywoards: ")
        sym_search(keywords)
    except:
        print("Something might be wrong!")
        print("Please check your internet connection and try again")
    


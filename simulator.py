import requests
import json

# res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=BAC&interval=5min&apikey=FLB281YD66I569JV')
# print(res.text)

def write_datafile(write_text):
    datafile = open("datafile.json", "w")
    datafile.write(write_text)
    datafile.close()

def sym_search(keywords):
    # Fetching Request Message
    print("Please wait while we are fetching your request...")

    # Requesting Data
    res = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + keywords + '&apikey=FLB281YD66I569JV')

    # Converting Data to JSON
    data = json.loads(res.text)

    # Number of Results
    results = len(data["bestMatches"])

    # Writing Data to a JSON File (Not Mandatory)
    # write_datafile(res.text)

    # Printing the Data in Formal Form
    print("")
    print("There are "  + str(results) + " best macthes for yor request!")
    print(data["bestMatches"]["1. symbol"])
    print(data["bestMatches"]["2. name"])
    print(data["bestMatches"]["3. type"])
    print(data["bestMatches"]["4. region"])
    print(data["bestMatches"]["5. marketOpen"])
    print(data["bestMatches"]["6. marketClose"])
    print(data["bestMatches"]["7. timezone"])
    print(data["bestMatches"]["8. currency"])
    print(data["bestMatches"]["9. matchScore"])


task = input("What do you want to do: ")

if "ls" in task:
    try:
        keywords = input("Enter the Keywords: ")
        sym_search(keywords)
    except:
        print("Something might be wrong!")
        print("Please check your internet connection and try again")

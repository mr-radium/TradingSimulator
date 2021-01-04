import requests
import json


def print_data(times):

    # Printing the Data in Formal Form
    print('')
    print("Symbol: " + data["bestMatches"][times]["1. symbol"])
    print("Name: " + data["bestMatches"][times]["2. name"])
    print("Type: " + data["bestMatches"][times]["3. type"])
    print("Region: " + data["bestMatches"][times]["4. region"])
    print("Market Open: " + data["bestMatches"][times]["5. marketOpen"])
    print("Market Close: " + data["bestMatches"][times]["6. marketClose"])
    print("TimeZone: " + data["bestMatches"][times]["7. timezone"])
    print("Currency: " + data["bestMatches"][times]["8. currency"])
    print("Match Score: "  + data["bestMatches"][times]["9. matchScore"])

def sym_search(keywords):
    # Fetching Request Message
    print("Please wait while we are fetching your request...")

    # Requesting Data
    res = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + keywords + '&apikey=FLB281YD66I569JV')

    # Converting Data to JSON
    global data
    data = json.loads(res.text)

    # Number of Results
    global results
    results = len(data["bestMatches"])

    # This is for telling the user the number of results
    print("")
    print("There are "  + str(results) + " best macthes for yor request!")

    # This prints the search result using a while loop 
    i = 0
    while i < results:
        print_data(i)
        i += 1



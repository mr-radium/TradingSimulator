import requests
import json


def print_data(times):

    # Printing the Data in Formal Form
    print('')
    print("Name: " + data[times]["name"])
    print("Symbol: " + data[times]["symbol"])

def sym_search(keywords):

    if "&" in keywords:
        keywords = keywords.replace("&", "%26")
    
    if " " in keywords:
        keywords = keywords.replace(" ", "%20")
        
    # Fetching Request Message
    print("Please wait while we are fetching your request...")

    # Requesting Data
    res = requests.get('http://localhost:3000/nse/search_stocks?keyword=' + keywords)

    # Converting Data to JSON
    global data
    data = json.loads(res.text)

    # Number of Results
    global results
    results = len(data)

    # This is for telling the user the number of results
    print("")
    print("There are "  + str(results) + " best macthes for yor request!")

    # This prints the search result using a while loop 
    i = 0
    while i < results:
        print_data(i)
        i += 1



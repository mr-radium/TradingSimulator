# Importing the functions from the symbol_seacher file
import os
from symbol_searcher import sym_search
from symbol_searcher import print_data
from get_current_stock_data import get_current_stock_data_nse


if __name__ == "__main__":
    task = input("Enter you request: ")
    
# If "ls" in task it would do symbol searching
    if "ls" in task:

        try:
            keywords = task.replace("ls ", "")
            sym_search(keywords)
        except:
            print("Something might be wrong!")
            print("Please check your internet connection and try again.")

# If "status" in task it would get the data of the given stock
    if "status" in task:
        try:
            stock = task.replace("status ", "")
            get_current_stock_data_nse(stock)

        except:
            print("Something might be wrong!")
            print("Please check your internet connection and try again.")

    if "-s" in task:
        try:
            stock = task.replace("-s ", "")
            get_current_stock_data_nse(stock)

        except:
            print("Something might be wrong!")
            print("Please check your internet connection and try again.")

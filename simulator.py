from symbol_searcher import sym_search
from symbol_searcher import print_data
from get_current_stock_data import get_current_stock_data_nse
from buy_stock import buy_stock
from show_profile import show_profile


if __name__ == "__main__":
    while True:
            
        task = input("Enter you request: ")
        
    # If "ls" in task it would do symbol searching
        if "ls" in task:

            try:
                keywords = task.replace("ls ", "")
                sym_search(keywords)
                print()
            except:
                print("Something might be wrong!")
                print("Please check your internet connection and try again.")
                print()

    # If "status" in task it would get the data of the given stock
        if "status" in task:
            try:
                stock = task.replace("status ", "")
                get_current_stock_data_nse(stock)
                print()

            except:
                print("Something might be wrong!")
                print("Please check your internet connection and try again.")
                print()

        if "-s" in task:
            try:
                stock = task.replace("-s ", "")
                get_current_stock_data_nse(stock)
                print()

            except:
                print("Something might be wrong!")
                print("Please check your internet connection and try again.")
                print()

    # If "buy" in task it will buy the stock.
    # The quantity should be assigned followed by "-"
    # Example: "buy ONGC -100"
        if "buy" in task:
            try:
                arranged_task = task.split()
                stock = arranged_task[1]
                print()
                try:
                    quantity = arranged_task[2].replace("-", "")
                    buy_stock(stock, quantity)
                    print()
                except:
                    print("")
                    print("Please assign a quantity at last followed by '-'")
                    print("For example- 'buy ONGC -400' or buy 'buy BURGERKING -25'")
                    print()
            except:
                print("Something might be wrong!")
                print("Please check your internet connection and try again.")
                print()

        if "-i" in task:
            show_profile()
            print()

        if "-q" in task:
            exit(code=0)
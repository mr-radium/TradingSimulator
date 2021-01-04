# Importing the functions from the symbol_seacher file
from symbol_searcher import sym_search
from symbol_searcher import print_data


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
                
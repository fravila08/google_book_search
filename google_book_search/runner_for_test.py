# This file is an exact replica of runner.py, except we don't call the 'running_book_search' function at the end of the
# file in order to allow test_book.py to run test properly
from classes.search import Searcher
searcher= Searcher(name='Francisco')
runner=True
menu="1. Add a book to my list!\n2. View my list of books!\n6. EXIT    "
print(f"Welcome to {searcher.Name}'s google book search program!")   
def running_book_search():
    print(menu)
    user_choice=input("Please choose option '1', '2', or '6' from the Menu above:  ")
    if user_choice=='1':
        searcher.search_and_add_book_to_store()
        return running_book_search()
    elif user_choice == '2':
        searcher.Reading_List.see_my_book_list()
        return running_book_search()
    elif user_choice== '6':
        print("\nThank you please come again soon!\n")
        return True
    else:
        print("\n***incorrect input please enter a number between 1 and 6***\n")
        return running_book_search()

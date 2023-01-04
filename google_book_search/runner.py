from classes.search import Searcher


def running_book_search():
    searcher= Searcher(name='Francisco')
    runner=True
    menu="1. Add a book to my list!\n2. View my list of books!\n6. EXIT    "
    
    
    
    print(f"Welcome to {searcher.Name}'s google book search program!")   
    while (runner):
        print(menu)
        user_choice=input("Please choose option '1', '2', or '6' from the Menu above:  ")
        if(user_choice=='1'):
            searcher.search_and_add_book_to_store()
        elif user_choice == '2':
            searcher.Reading_List.see_my_book_list()
        elif (user_choice== '6'):
            print("\nThank you please come again soon!\n")
            return True
        else:
            print("\n***incorrect input please enter a number between 1 and 6***\n")
            




running_book_search()
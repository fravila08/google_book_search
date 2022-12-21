from classes.searcher import Searcher


def running_book_search():
    searcher= Searcher(name='Francisco')
    runner=True
    menu="""
1. Add a book to my list!
2. View my list of books!

6. EXIT    
    """
    
    
    
    print(f"Welcome to {searcher.Name}s google book search program!")   
    while (runner):
        print(menu)
        user_choice=input('type a number(1-6) to select an option:  ')
        if(user_choice=='1'):
            searcher.search_for_a_book_title()
        elif user_choice == '2':
            searcher.see_my_book_list()
        elif (user_choice== '6'):
            print("\nThank you please come again soon!\n")
            runner=False
        else:
            print("\n***incorrect input please enter a number between 1 and 6***\n")
    




running_book_search()
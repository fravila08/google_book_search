from classes.search import Searcher
from rich import print
from rich.console import Console
console=Console()


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
        console.print("\nThank you, please come again soon!\n", style="bold cyan")
        return True
    else:
        searcher.b_inpt()
        return running_book_search()

running_book_search()
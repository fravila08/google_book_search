from .book import Book
from .reading_list import Reading_List
import requests
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich import print
from dotenv import load_dotenv
import os
load_dotenv()
my_theme=Theme({"success":"bold green", "error":"bold red"})
console=Console(theme=my_theme)

class Searcher:
    
    def __init__(self, name):
        self.Name= name
        self.Key= os.environ['API_key']#Will grab the google api key from the .env
        self.Reading_List= Reading_List()
        
    def b_inpt(self):
        console.print("***Incorrect input please enter 'Y' or 'N'***", style="error")
        
    def search_for_a_book(self, book_title):
        response= requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book_title}+intitle:{book_title}&key={self.Key}")
        response=response.json()
        book_results=[]
        try:
            for book in range(5):
                book_authors=', '.join(response['items'][book]['volumeInfo']['authors'])
                book_title=response['items'][book]['volumeInfo']['title']
                book_publisher=response['items'][book]['volumeInfo']['publisher']
                book_results.append(Book(**{'title': book_title, 'author':book_authors, 'publisher': book_publisher}))
        except:
            pass
        return book_results

    
    def confirm_book(self):
        confirmation=input("Would you like to add this book to your reading list? (Enter Y/N)\n")
        if confirmation.upper()=='Y':
            #when the user confirms we will add the book to the users Reading List
            return True
        elif confirmation.upper()=="N":
            return False
        else:
            #b_inpt method starts on line 21
            self.b_inpt()
            return self.confirm_book()
        
    
    def select_a_book(self, books):
        nums=list(range(1,len(books)+1))
        nums=[str(i) for i in nums]
        choice=input(f"Choose a number between 1-{len(books)}:\nEnter '6' to search again\n")
        if choice=='6':
            return "restart_search"
        elif choice in nums:
            my_book=books[int(choice)-1]
            console.print(f"\nYou selected: [yellow]{my_book}[/]")
            #confirm_book method starts in line 39 and returns a boolean variable
            confirm=self.confirm_book()
            if confirm:
                console.print(f"\n:thumbs_up: {self.Reading_List.add_a_book_to_reading_list(my_book)}\n", style="success")
                return len(self.Reading_List.Book_list)
            else:
                return self.select_a_book(books)
        else:
            #b_inpt starts on line 21
            self.b_inpt()
            return self.select_a_book(books)
    
    
    def search_and_add_book_to_store(self):
        user_book= input("\nEnter the title of the book you are looking for:\nEnter '6' to return to main menu\n")
        if user_book=='6':
            #we can exit this method and go back to the main menu
            pass
        else:
            #search_for_a_book method begins in line 24
            my_results=self.search_for_a_book(user_book)
            if len(my_results)<1:
                console.print("**There's no results for what you've entered**", style="error")
                return self.search_and_add_book_to_store()
            else:
                table=Table(title="Book Results")
                table.add_column("#")
                table.add_column("Title")
                table.add_column("Author/s")
                table.add_column("Publisher")
                for i in range(len(my_results)):
                    table.add_row(str(i+1), my_results[i].Title, my_results[i].Author, my_results[i].Publisher)
                console.print(table)
                #select_a_book method starts in line 52
                selection=self.select_a_book(my_results)
                if selection=="restart_search":
                    return self.search_and_add_book_to_store()
        return True                
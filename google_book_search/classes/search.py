from .book import Book
from .reading_list import Reading_List
import requests
from dotenv import load_dotenv
import os
load_dotenv()


class Searcher:
    
    def __init__(self, name):
        self.Name= name
        self.Key= os.environ['API_key']#Will grab the google api key from the .env
        self.Reading_List= Reading_List()
        
        
    def search_for_a_book(self, book_title):
        response= requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book_title}+intitle:{book_title}&key={self.Key}")
        response=response.json()
        book_results=[]
        try:
            for book in range(5):
                book_authors=response['items'][book]['volumeInfo']['authors']
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
            print("***Incorrect input please enter 'Y' or 'N'***")
            return self.confirm_book()
        
    
    def select_a_book(self, books):
        nums=list(range(1,len(books)+1))
        nums=[str(i) for i in nums]
        choice=input(f"Choose a number between 1-{len(books)}:\nEnter '6' to search again\n")
        if choice=='6':
            return "restart_search"
        elif choice in nums:
            my_book=books[int(choice)-1]
            print(f"\nYou selected: {my_book}")
            confirm=self.confirm_book()
            if confirm:
                print(self.Reading_List.add_a_book_to_reading_list(my_book))
                return len(self.Reading_List.Book_list)
            else:
                return self.select_a_book(books)
        else:
            print("***Incorrect Input***")
            return self.select_a_book(books)
    
    
    def search_and_add_book_to_store(self):
        user_book= input("\nEnter the title of the book you are looking for:\nEnter '6' to return to main menu\n")
        if user_book=='6':
            #we can exit this method and go back to the main menu
            pass
        else:
            #the following method begins in line 17
            my_results=self.search_for_a_book(user_book)
            if len(my_results)<1:
                print("**There's no results for what you've entered**")
                return self.search_and_add_book_to_store()
            else:
                for i in range(len(my_results)):
                    print(f"{i+1}. {my_results[i]}")
                #select_a_book method starts in line 44
                selection=self.select_a_book(my_results)
                if selection=="restart_search":
                    return self.search_and_add_book_to_store()
        return True                
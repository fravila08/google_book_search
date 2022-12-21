from .guest import Guest
from .book import Book
import requests
from dotenv import load_dotenv
import os
load_dotenv()


class Searcher():
    
    def __init__(self, name):
        self.Name= name
        self.Key= os.environ['API_key']#Will grab the google api key from the .env
        self.Guest= Guest() 
        
    def search_for_a_book_title(self):
        search_runner=True
        #the while loops will allow our queries to come up in case the user places invalid input 
        while(search_runner):
            user_book= input("Enter the title of the book you are looking for:\nEnter '6' to return to main menu\n")
            if user_book=='6':
                #we can kill the program and go back to the main menu
                search_runner=False
                
                
            else:
                book_choice_runner=True
                try:
                    response= requests.get(f"https://www.googleapis.com/books/v1/volumes?q={user_book}+intitle:{user_book}&key={self.Key}")
                    response=response.json()
                    my_books=[]    
                    for book in range(5):
                        book_authors=response['items'][book]['volumeInfo']['authors']
                        book_title=response['items'][book]['volumeInfo']['title']
                        book_publisher=response['items'][book]['volumeInfo']['publisher']
                        my_books.append(Book(**{'title': book_title, 'author':book_authors, 'publisher': book_publisher}))
                        book_authors = ", ".join(book_authors)
                        print(f"{book + 1}: Title: {book_title} Author: {book_authors} Publisher: {book_publisher}")
                except :
                    #if there isn't a total of 5 books available in the search we still want to print the books that did come back from the api call
                    #otherwise we could let the user know there was no results and set book_choice_runner to false to unable the program to continue
                    #further down the line
                    if len(my_books)>0:
                        pass
                    else:
                        print("**There's no results for what you've entered**")
                        book_choice_runner=False
                book_choice=None
                while book_choice_runner:
                    choices=[]
                    # we will create an array of acceptable input by iterating through the range of my_books. We don't want to set it all the way to 5 
                    #because we could get less than 5 books in return
                    for i in range(len(my_books)):
                        choices.append(str(i+1))
                    user_book_choice= input(f"\nChoose a book by entering the respective number:(Enter 1-{len(my_books)})\nEnter '6' to cancel\n")
                    
                    #here we ensure it's a valid input
                    if user_book_choice in choices:
                        book_choice=int(user_book_choice)-1
                        book_choice_runner=False
                    elif user_book_choice == '6':
                        book_choice_runner=False
                    else:
                        print(f"**Incorrect input please enter a number betwenn 1-{len(my_books)}**")
                if book_choice is not None:
                    chosen_book=my_books[book_choice]
                    #we grab the selected book by the index and display it to the user for confirmation
                    print("You selecter:")
                    print(chosen_book)
                    
                    confirmation_runner=True
                    while confirmation_runner:
                        confirmation=input("\nIs this the book you are looking for? (Enter Y/N)\n")
                        if confirmation.upper()=='Y':
                            #when the user confirms we will add the book to the users Reading List
                            print(self.Guest.add_a_book_to_reading_list(chosen_book))
                            confirmation_runner=False
                            search_runner=False
                        elif confirmation.upper()=="N":
                            confirmation_runner=False
                        else:
                            print("** Incorrect input place input 'Y' or 'N' **")
        return True      
                
    def see_my_book_list(self):
        self.Guest.view_reading_list()
        
    
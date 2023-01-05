from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich import print


my_theme=Theme({"success":"bold green", "error":"bold red"})
console=Console(theme=my_theme)

class Reading_List:
    def __init__(self):
        self.Book_list= []
        
    def add_a_book_to_reading_list(self, book):
        #each user will have their own list to add their books to
        self.Book_list.append(book)
        return f"{book.Title} has been added to your reading list!"
    
    def see_my_book_list(self):
        if len(self.Book_list)>0:
            table=Table(title="Your Reading List")
            table.add_column("Title")
            table.add_column("Author/s")
            table.add_column("Publisher")
            for book in self.Book_list:
                table.add_row(book.Title, book.Author, book.Publisher)
            console.print(table)
        else:
            console.print("\nYou currently don't have any books\n", style="error")
        return len(self.Book_list)
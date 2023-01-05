class Reading_List:
    def __init__(self):
        self.Book_list= []
        
    def add_a_book_to_reading_list(self, book):
        #each user will have their own list to add their books to
        self.Book_list.append(book)
        return f"\n@@{book.Title} has been added to your reading list!@@\n"
    
    def see_my_book_list(self):
        if len(self.Book_list)>0:
            print("\n@@@@@@@@@@@@@@@@@@@\nYour Reading List:\n---------------------------------------------------")
            for book in self.Book_list:
                print(book)
            print("---------------------------------------------------\n@@@@@@@@@@@@@@@@@@@\n")
        else:
            print("\nYou currently don't have any books\n")
        return len(self.Book_list)
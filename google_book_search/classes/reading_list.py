class Reading_List:
    def __init__(self):
        self.Reading_list= []
        
    def add_a_book_to_reading_list(self, book):
        #each user will have their own list to add their books to
        self.Reading_list.append(book)
        return f"\n@@{book.Title} has been added to your reading list!@@\n"
    
    def see_my_book_list(self):
        if len(self.Reading_list)>0:
            print("\n@@@@@@@@@@@@@@@@@@@\nYour Reading List:\n---------------------------------------------------")
            for book in self.Reading_list:
                print(book)
            print("---------------------------------------------------\n@@@@@@@@@@@@@@@@@@@\n")
        else:
            print("\nYou currently don't have any books\n")
        return len(self.Reading_list)
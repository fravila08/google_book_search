class Guest():
    def __init__(self, name="GUEST", reading_list=[]):
        self.Name= name
        self.Reading_List= reading_list
        
    def view_reading_list(self):
        #if the list is not empty we could iterate throught the list of books and print each instance 
        #through its dunder method
        if len(self.Reading_List)>0:
            print("\nYour Reading List: \n@@@@")
            for book in self.Reading_List:
                print(book)
            print("@@@@")
            return len(self.Reading_List)
        else:
            print("\nYou currently don't have any books\n")
            
    def add_a_book_to_reading_list(self, book):
        #each user will have their own list to add their books to
        self.Reading_List.append(book)
        return f"\n@@{book.Title} has been added to your reading list!@@"
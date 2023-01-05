import pytest
from classes.search import Searcher
from classes.book import Book
from runner_for_test import running_book_search


class TestClass:
    searcher=Searcher(name='test')
    books= [
            Book(**{'title':'Beyond the Gates of Fire', 'author':["Christopher Matthew"], 'publisher':"Casemate Publishers"}),
            Book(**{'title':'Fractured Fairy Tales', 'author':['A.J. Jacobs'], 'publisher':'Bantam'}),
            Book(**{'title':'Tooth Fairy', 'author':['A.J. Jacobs'], 'publisher':'Bantam'})
            ]

    return_for_adding_book= "\n@@Beyond the Gates of Fire has been added to your reading list!@@\n"
    
    def test_search_for_a_book(self):
        #Will test the google api and ensure an array of 5 books is returned
        assert len(self.searcher.search_for_a_book("Python for Dummies")) == 5
    
    def test_search_for_a_book_partial(self):
        #Sends a title that will not return 5 books to ensure the program 
        #can continue running for the user
        books_returned=len(self.searcher.search_for_a_book("Fairy tale"))
        assert books_returned > 0 and books_returned < 5
    
    def test_search_for_a_book_no_results(self):
        #Will make an API call that will return 0 results
        books_returned=len(self.searcher.search_for_a_book("aygf232agdyiuf"))
        assert books_returned == 0
    
    def test_confirmation_y(self, monkeypatch):
        #this will take in incorrect input and then place in the correct option to ensure the confirmation
        #function works correctly with 'y' || 'Y' and returns True
        responses=iter(["adjfaudhf","y"])
        monkeypatch.setattr('builtins.input',lambda _: next(responses))
        assert self.searcher.confirm_book()==True
    
    def test_confirmation_n(self, monkeypatch):
        #this will take in incorrect input and then place in the correct option to ensure the confirmation
        #function works correctly with 'n' || 'N' and returns False
        responses=iter(["adjfaudhf","n"])
        monkeypatch.setattr('builtins.input',lambda _: next(responses))
        assert self.searcher.confirm_book()==False

    def test_adding_a_book_to_list(self):
        #ensures a book can be added to the reading list and 
        #returns a confirmation msg for the user
        assert self.searcher.Reading_List.add_a_book_to_reading_list(self.books[0]) == self.return_for_adding_book
    
    def test_ensuring_book_will_print_correctly(self):
        assert self.books[0].__str__() == "Title: Beyond the Gates of Fire Author/s: Christopher Matthew Publisher: Casemate Publishers."
    
    def test_view_reading_list_through_len(self):
        #there's already one book inside of the Reading List so we will just add the other and confirm there's two books in there
        self.searcher.Reading_List.add_a_book_to_reading_list(self.books[1])
        assert self.searcher.Reading_List.see_my_book_list() == 2
        
    def test_selecting_a_book_correct_input(self, monkeypatch):
        #ensures user can select a book from a list of Book instances and add
        #it to the users reading list
        responses=iter(["3","Y"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert self.searcher.select_a_book(self.books) == 3
    
    def test_selecting_a_book_incorrect_input(self, monkeypatch):
        responses=iter(["aufhaiud","3","fuahdf","Y"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert self.searcher.select_a_book(self.books) == 4
          
    def test_finding_and_adding_a_book_correct_input(self, monkeypatch):
        responses=iter(["Gates of Fire",'3','Y'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        #although this test is not testing for a return value it is testing that input
        #triggers the correct functionality
        assert self.searcher.search_and_add_book_to_store()== True
        
    def test_finding_and_adding_a_book_incorrect_input(self, monkeypatch):
        responses=iter(["ajdfaudf","Gates of Fire","haudifaud",'3',"suhadfaiu",'Y'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        #although this test is not testing for a return value it is testing that input
        #triggers the correct functionality and handles incorrect input as well
        assert self.searcher.search_and_add_book_to_store()== True
           
    def test_entire_program_incorrect_input(self, monkeypatch):
        #this test will runs through the entire program from start to finish.
        #it takes in edge cases by taking in incorrect input and then taking in
        #correct input. Tests every function in the program and ensures it runs 
        #successfully
        responses=iter(["auifadfh","1","ajdfaudf","Gates of Fire","haudifaud",'3',"suhadfaiu",'Y',"auhfuad","2","6"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert running_book_search()==True
    
    def test_entire_program_correct_input(self, monkeypatch):
        #this test will runs through the entire program from start to finish.
        #Tests every function in the program and ensures it runs successfully.
        responses=iter(["1","Gates of Fire",'3','Y',"2","6"])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert running_book_search()==True
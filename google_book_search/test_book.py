import pytest
from classes.search import Searcher
from classes.book import Book


class TestClass:
    searcher=Searcher(name='test')
    books= [
            Book(**{'title':'Beyond the Gates of Fire', 'author':["Christopher Matthew"], 'publisher':"Casemate Publishers"}),
            Book(**{'title':'Fractured Fairy Tales', 'author':['A.J. Jacobs'], 'publisher':'Bantam'}),
            Book(**{'title':'Tooth Fairy', 'author':['A.J. Jacobs'], 'publisher':'Bantam'})
            ]

    return_for_adding_book= "\n@@Beyond the Gates of Fire has been added to your reading list!@@\n"
    
    
    def test_confirmation_y(self, monkeypatch):
        responses=iter(["adjfaudhf","y"])
        monkeypatch.setattr('builtins.input',lambda _: next(responses))
        assert self.searcher.confirm_book()==True
        
    
    def test_confirmation_n(self, monkeypatch):
        responses=iter(["adjfaudhf","n"])
        monkeypatch.setattr('builtins.input',lambda _: next(responses))
        assert self.searcher.confirm_book()==False
    
    def test_adding_a_book_to_list(self):
        assert self.searcher.Reading_List.add_a_book_to_reading_list(self.books[0]) == self.return_for_adding_book
    
        
    def test_ensuring_book_will_print_correctly(self):
        assert self.books[0].__str__() == "Title: Beyond the Gates of Fire Author/s: Christopher Matthew Publisher: Casemate Publishers."
    
        
    def test_view_reading_list_through_len(self):
        #there's already one book inside of the Reading List so we will just add the other and confirm there's two books in there
        self.searcher.Reading_List.add_a_book_to_reading_list(self.books[1])
        assert self.searcher.Reading_List.see_my_book_list() == 2
        
        
    def test_selecting_a_book_correct_input(self, monkeypatch):
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
        #triggers the correct functionality
        assert self.searcher.search_and_add_book_to_store()== True
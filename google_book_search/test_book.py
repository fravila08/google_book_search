import pytest
from classes.searcher import Searcher
from classes.book import Book
from classes.guest import Guest


class TestClass:
    searcher=Searcher(name='test')
    guest=Guest()
    books= [
            Book(**{'title':'Beyond the Gates of Fire', 'author':["Christopher Matthew"], 'publisher':"Casemate Publishers"}),
            Book(**{'title':'Fractured Fairy Tales', 'author':['A.J. Jacobs'], 'publisher':'Bantam'})
            ]

    return_for_adding_book= "\n@@Beyond the Gates of Fire has been added to your reading list!@@"
    
    
    def test_adding_a_video_to_list(self):
        assert self.guest.add_a_book_to_reading_list(self.books[0]) == self.return_for_adding_book
    
        
    def test_ensuring_book_will_print_correctly(self):
        assert self.books[0].__str__() == "Title: Beyond the Gates of Fire Author/s: Christopher Matthew Publisher: Casemate Publishers."
    
        
    def test_view_reading_list_through_len(self):
        #there's already one book inside of the Reading List so we will just add the other and confirm there's two books in there
        self.guest.add_a_book_to_reading_list(self.books[1])
        assert self.guest.view_reading_list() == 2
        
        
    def test_finding_and_adding_a_book(self, monkeypatch):
        responses=iter(["Gates of Fire",'3','Y'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        #although this test is not testing for a return value it is testing that input
        #triggers the correct functionality
        assert self.searcher.search_for_a_book_title()== True
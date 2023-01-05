class Book:
    def __init__(self, title, author, publisher):
        self.Title= title
        self.Author = author
        self.Publisher = publisher
        
    def __str__(self):
        return f"{self.Title} authored by {self.Author} and published by {self.Publisher}."
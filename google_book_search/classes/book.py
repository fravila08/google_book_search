class Book:
    def __init__(self, title, author, publisher):
        self.Title= title
        self.Author = author
        self.Publisher = publisher
        
    def __str__(self):
        return f"Title: {self.Title} Author/s: {', '.join(self.Author)} Publisher: {self.Publisher}."
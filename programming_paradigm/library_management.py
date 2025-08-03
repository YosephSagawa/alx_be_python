class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return True
                else:
                    return False
                
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return True
                else:
                    return False
                
    def list_available_books(self):
        available_books = {}
        for book in self._books:
            if not book._is_checked_out:
                available_books.update({book.title: book.author})
                for title, author in available_books.items():
                    print(f"{title} by {author}")
                

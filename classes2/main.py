class Book:
    def __init__(self, title: str, author: str, contents_book: str):
        self.title = title
        self.author = author
        self.contents_book = contents_book
        self.available = True

    def __str__(self):
        return f'{self.title} by {self.author} | Availability: {self.available} \n ||| {self.contents_book} |||'

class LibraryCatalog:
    def __init__(self):
        # Once we learn sets, we'll use those instead in cases where index doesn't matter.
        self.books: list[Book] = []

    def __str__(self):
        outstr = ""
        outstr += " " + '-' * 15 + '\n'
        outstr += f" Library System. Contains {len(self.books)} books.\n"

        for book in self.books:
            outstr += book.__str__() + '\n'

        outstr += " " + '-'*15 + '\n'
        return outstr

    def add_book(self, title, author, contents_book) -> None:
        self.books.append(Book(title, author, contents_book))

    def borrow_book(self, title, author) -> Book | None:
        for book in self.books:
            if book.title == title and book.author == author and book.available:
                book.available = False
                return book

        print("Book not found or already borrowed")
        return None

    def return_book(self, book: Book) -> None:
        if book in self.books and book.available:
            print("Book not returned, book is available")
        elif book in self.books and not book.available:
            book.available = True
        elif book not in self.books:
            print("Book not returned, book not found")

    def search_available_books_by_title(self, title) -> list[Book]:
        bookresults = []

        for book in self.books:
            if title in book.title and book.available:
                bookresults.append(book)

        return bookresults

    def search_available_books_by_author(self, author) -> list[Book]:
        bookresults = []

        for book in self.books:
            if author in book.author and book.available:
                bookresults.append(book)

        return bookresults

    def search_available_books_by_content(self, content) -> list[Book]:
        bookresults = []

        for book in self.books:
            if content in book.contents_book and book.available:
                bookresults.append(book)

        return bookresults

    def search_books_by_title(self, title) -> list[Book]:
        bookresults = []

        for book in self.books:
            if title in book.title:
                bookresults.append(book)

        return bookresults

    def search_books_by_author(self, author) -> list[Book]:
        bookresults = []

        for book in self.books:
            if author in book.author:
                bookresults.append(book)

        return bookresults

    def search_books_by_content(self, content) -> list[Book]:
        bookresults = []

        for book in self.books:
            if content in book.contents_book:
                bookresults.append(book)

        return bookresults

"""

Library Catalog:

Design a class for managing a library catalog
 with features like adding books, searching by title or author, and checking availability.

"""


class Book:
    def __init__(self, title: str, author: str, contents_book: str):
        self.title = title
        self.author = author
        self.contents_book = contents_book
        self.available = True

    def __str__(self):
        return f'{self.title} by {self.author} | Availability: {self.available} \n ||| {self.contents_book} |||'

def test_all():
    print("Creating library catalog. ")
    library = LibraryCatalog()
    print(library)

    print("\nAdding books to library")
    library.add_book("Introduction to Python", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Java", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Python", "Sahan Wijetunga", "Python is cool. ")
    library.add_book("Data Science Essentials", "Jane Smith",
                     "Explore the fundamentals of data science with this essential guide.")
    library.add_book("Mystery Novel", "Agatha Christie",
                     "A thrilling mystery novel that will keep you on the edge of your seat.")
    library.add_book("Mystery Math Book", "Generic Name",
                     "A thrilling math novel.")
    print(library)

    math_book = library.borrow_book("Mystery Math Book", "Generic Name")
    print(f"Borrowed book: {math_book}")

    print("\nDisplaying books with \"novel\" in the content. ")
    available_books = library.search_books_by_content("novel")
    for book in available_books:
        print(book)

    print("\nDisplaying available books with title \"Introduction to Python\"")
    available_books = library.search_available_books_by_title("Introduction to Python")
    for book in available_books:
        print(book)

    print("\nBorrowing a book")
    borrowed_book = library.borrow_book("Introduction to Python", "John Doe")
    print("Borrowed Book:")
    print(borrowed_book)

    print("\nAttempting to borrow the same book again")
    duplicate_borrowed_book = library.borrow_book("Introduction to Python", "John Doe")
    print("Duplicate Borrowed Book:")
    print(duplicate_borrowed_book)

    print("\nReturning the book")
    library.return_book(borrowed_book)

    print("\nAttempting to return the same book again")
    library.return_book(borrowed_book)

    print("\nBorrowing a different book")
    library.borrow_book("Introduction to Python", "Sahan Wijetunga")

    print(library)

    print("\nDisplaying available books after return, by author \"John Doe\"")
    available_books_after_return = library.search_available_books_by_author("John Doe")
    for book in available_books_after_return:
        print(book)


def test_a():
    library = LibraryCatalog()
    library.add_book("Python", "Sahan", "Python is a cool programming language ... The end. ")
    library.add_book("Java", "Clark", "Java is also a programming language ... To be continued ... ")

    for book in library.books:
        print(book)


def test_b():
    library = LibraryCatalog()
    library.add_book("Python", "Sahan", "Python is a cool programming language ... The end. ")
    library.add_book("Java", "Clark", "Java is also a programming language ... To be continued ... ")
    borrowed_book = library.borrow_book("Python", "Sahan")
    if borrowed_book:
        print("Borrowed Book:")
        print(borrowed_book)


def test_c():
    library = LibraryCatalog()
    library.add_book("Python", "Sahan", "Python is a cool programming language ... The end. ")
    library.add_book("Java", "Clark", "Java is also a programming language ... To be continued ... ")
    borrowed_book = library.borrow_book("Python", "Sahan")
    print("Borrowed Book:")
    print(borrowed_book)
    print('-' * 10)

    library.return_book(borrowed_book)
    for book in library.books:
        print(book)
    library.return_book(borrowed_book)


def test_d():
    library = LibraryCatalog()
    library.add_book("Introduction to Python", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Java", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Python", "Sahan Wijetunga", "Python is cool. ")
    library.add_book("Data Science Essentials", "Jane Smith",
                     "Explore the fundamentals of data science with this essential guide.")
    library.add_book("Mystery Novel", "Agatha Christie",
                     "A thrilling mystery novel that will keep you on the edge of your seat.")
    library.add_book("Mystery Math Book", "Generic Name",
                     "A thrilling math novel.")

    search_result = library.search_available_books_by_title("Introduction to Python")
    for item in search_result:
        print(item)

    print('-' * 10)

    search_result = library.search_available_books_by_content("novel")
    for item in search_result:
        print(item)


def test_e():
    library = LibraryCatalog()
    library.add_book("Introduction to Python", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Java", "John Doe", "This is a comprehensive guide to Python programming.")
    library.add_book("Introduction to Python", "Sahan Wijetunga", "Python is cool. ")
    library.add_book("Data Science Essentials", "Jane Smith",
                     "Explore the fundamentals of data science with this essential guide.")
    library.add_book("Mystery Novel", "Agatha Christie",
                     "A thrilling mystery novel that will keep you on the edge of your seat.")
    library.add_book("Mystery Math Book", "Generic Name",
                     "A thrilling math novel.")
    print(library)


test_all()
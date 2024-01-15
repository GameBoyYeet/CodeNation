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
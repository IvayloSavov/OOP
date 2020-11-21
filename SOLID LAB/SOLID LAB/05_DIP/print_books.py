from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class AuthorFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.author


class Printer:
    def print(self, book: Book, formatter: Formatter):
        return formatter.format(book)
    # def get_book(self, book: Book):
    #     formatter = Formatter()
    #     formatted_book = formatter.format(book)
    #     return formatted_book
    #
    # def get_author(self, book):  # не е добре, затова ще предадем отговорността в ръцете на клиента
    #     formatter = AuthorFormatter()
    #     return formatter.format(book)


book = Book("Ivo", "Savov", "Lorem ipsum dolor sit amet")
printer = Printer()
print(printer.print(book, ContentFormatter()))



# old
# class Book:
#     def __init__(self, content: str):
#         self.content = content
#
#
# class Formatter:
#     def format(self, book: Book) -> str:
#         return book.content
#
#
# class Printer:
#     def get_book(self, book: Book):
#         formatter = Formatter()
#         formatted_book = formatter.format(book)
#         return formatted_book



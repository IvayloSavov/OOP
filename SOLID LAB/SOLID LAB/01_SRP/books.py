from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self, books: List[Book]):
        self.books = books

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

# Ако имаме pdf файл с книгата и при всеки потребител ще е на различна страница, а ако е физически turn_page
# ще си е при книгата.
# class BookReader:
#     def __int__(self, book):
#         self.book = book
#         self.page = page
#
#     def change_page(self, new_page):
#         self.page = new_page
        
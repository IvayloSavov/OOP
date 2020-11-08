class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int, library):
        book_is_found = any(True for u, books in library.books_available.items() if book_name in books)
        # if author in library.books_available and book_name in library.books_available[author]:
        if book_is_found:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username not in library.rented_books:
                library.rented_books[self.username] = {}
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        user_who_has_the_book = [user for user, books_in_user in library.rented_books.items() if book_name in books_in_user][0]
        return f'The book "{book_name}" is already rented and will be available in ' \
               f"{library.rented_books[user_who_has_the_book][book_name]} days!"

    def return_book(self, author: str, book_name: str, library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"
        self.books.remove(book_name)
        if author not in library.books_available.keys():
            library.books_available[author] = []
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)

    def info(self):
        return ", ".join(sorted(self.books))

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

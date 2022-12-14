from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    # db = "books"
    def __init__(self, data):
        self.id = data['id'],
        self.title = data['title'],
        self.num_pages = data['num_pages'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

# CREATE

    @classmethod
    def add_book(cls, data):
        query = """
        INSERT INTO books (title, num_pages, created_at, updated_at)
        VALUES %(title)s, %(num_pages)s, NOW(), NOW())
        ;"""
        return connectToMySQL('books').query_db(query, data)

# READ

    @classmethod
    def show_all_books(cls):
        query = "SELECT * FROM books;"
        books_from_db = connectToMySQL('books').query_db(query)
        all_books = []
        for book in books_from_db:
            all_books.append(cls(book))
        return all_books

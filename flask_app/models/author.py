# queries

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    # db = "books"

    def __init__(self, data):
        self.id = data['id'],
        self.name = data['name'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']
        self.favorite_books = []

# CREATE

    #creates new author.
    @classmethod
    def create_author(cls, data):
        query = """
        INSERT INTO authors (name)
        VALUES (%(name)s)
        ;"""
        return connectToMySQL('books').query_db(query, data)

# READ

    # pulls list of all authors.
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL('books').query_db(query)
        authors = []
        for auth in authors_from_db:
            authors.append(cls(auth))
        print(authors)
        return authors

    # pulls one author's favorite books. includes all columns from all tables.
    @classmethod
    def get_author_favorites(cls, data):
        query = """
        SELECT * 
        FROM authors
        LEFT JOIN favorites
        ON favorites.author_id = authors.id
        LEFT JOIN books
        ON favorites.book_id = books.id
        WHERE authors.id = %(id)s
        ;"""
        results = connectToMySQL('books').query_db(query, data)
        author_favorites = cls(results[0])
        for row in results:
            book_data = {
                'id' : row['books.id'],
                'title' : row['title'],
                'num_pages' : row['num_pages'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.updated_at']
            }
            author_favorites.favorite_books.append(book.Book(book_data))
        print(author_favorites)
        return author_favorites
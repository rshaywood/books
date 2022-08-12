# page directions

from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models import book

# CREATE

@app.route('/books/add', methods=['POST'])
def new_book():
    data = {
        'title': request.form['title'],
        'num_pages': request.form['num_pages']
    }
    book_id = book.Book.add_book(data)
    print("***********************", book_id)
    return redirect('/books/all_books')


# READ

@app.route('/books/all_books')
def display_all_books():
    all_books = book.Book.show_all_books()
    return render_template('all_books.html', all_books=all_books)
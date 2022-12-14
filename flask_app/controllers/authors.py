# page directions

from flask_app import app
from flask import render_template, redirect, flash, request, session
from flask_app.models import author

# CREATE

@app.route('/author/create', methods=['POST'])
def new_author():
    author.Author.create_author(request.form)
    return redirect('/')

# READ

@app.route('/')
def index():
    all_authors = author.Author.get_all_authors()
    return render_template('all_authors.html', all_authors = all_authors)

@app.route('/author/favorites/<int:id>')
def show_author_favorites(id):
    data = {'id': id}
    return render_template('author_favorites.html', faves = author.Author.get_author_favorites(data))
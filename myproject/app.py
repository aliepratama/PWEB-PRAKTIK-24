from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost:3306/db_books'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

db = SQLAlchemy(app)
from myproject.models.books import Books
migrate = Migrate(app, db)

from myproject.controllers.books import get_books, create_book, edit_book, delete_book as del_book


@app.route('/')
def index():
    return get_books()


@app.route('/add', methods=['POST'])
def add_book():
    return create_book()


@app.route('/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return del_book(book_id)


@app.route("/edit/<int:book_id>", methods=["PUT"])
def edit_buku(book_id):
    return edit_book(book_id)

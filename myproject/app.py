from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_books"
mysql = MySQL(app)

from myproject.controllers.books import get_books, create_book, edit_book, delete_book as del_book

@app.route('/')
def index():
    return get_books()


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    return create_book()


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    return del_book(book_id)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_buku(book_id):
    return edit_book(book_id)

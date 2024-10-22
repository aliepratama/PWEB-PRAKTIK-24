from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config['MYSQL_PORT'] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "db_books"
mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    if request.args.get('order') == 'asc':
        cur.execute("SELECT * FROM books ORDER BY created_at ASC")
    else:
        cur.execute("SELECT * FROM books ORDER BY created_at DESC")
    books = cur.fetchall()
    cur.close()
    return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO books(title, author) VALUES(%s, %s)",
            (title, author))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    return render_template('add_book.html')


@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('index'))


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_buku(book_id):
    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE books SET title = %s, author = %s WHERE id = %s",
            (new_title, new_author, book_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
        books = cur.fetchone()
        cur.close()
        if book_id in books:
            return render_template("edit.html",
                                   title=books[1],
                                   author=books[2])


if __name__ == '__main__':
    app.run(debug=True)

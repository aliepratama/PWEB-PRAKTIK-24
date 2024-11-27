from flask import render_template, request, redirect, url_for, Response
from myproject.models.books import get_all_books_asc, get_all_books_desc, insert_book, edit_book_by_id, delete_book_by_id, get_book_by_id


def get_books() -> str:
    """
    Mendapatkan buku-buku yang ada
    """
    if request.args.get('order') == 'asc':
        books = get_all_books_asc()
    else:
        books = get_all_books_desc()
    return render_template('index.html', books=books)


def edit_book(book_id: int) -> str | Response:
    """
    Edit buku berdasarkan id
    """
    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        edit_book_by_id(book_id, new_title, new_author)
        return redirect(url_for('index'))
    else:
        books = get_book_by_id(book_id)
        if book_id in books:
            return render_template("edit.html",
                                   title=books[1],
                                   author=books[2])


def delete_book(book_id: int) -> Response:
    """
    Menghapus buku berdasarkan id
    """
    delete_book_by_id(book_id)
    return redirect(url_for('index'))


def create_book() -> str | Response:
    """
    Menambahkan buku baru
    """
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        insert_book(title, author)
        return redirect(url_for('index'))
    return render_template('add_book.html')

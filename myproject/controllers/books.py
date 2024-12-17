from flask import request, Response
from myproject.app import db
from myproject.models.books import Books
from myproject.utils.res_wrapper import success_response, error_response


def get_books() -> str:
    """
    Mendapatkan buku-buku yang ada
    """
    # Mendapatkan seluruh data
    books = Books.query.all()
    # Cara 1
    temp = []
    for book in books:
        temp.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "created_at": book.created_at
        })
    # Cara 2
    books = list(map(lambda book: {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "created_at": book.created_at
    }, books))
    return success_response(data=books)


def edit_book(book_id: int) -> str | Response:
    """
    Edit buku berdasarkan id
    """
    if request.method == "PUT":
        if request.json.get("title") and request.json.get("author"):
            new_title = request.json['title']
            new_author = request.json['author']
            Books.query.filter_by(id=book_id).update({
                "title": new_title,
                "author": new_author
            })
            db.session.commit()
            return success_response(msg="Buku berhasil diubah", res_code=200)
        return error_response("Data tidak lengkap", res_code=400)
    return error_response("Method not allowed", res_code=405)


def delete_book(book_id: int) -> Response:
    """
    Menghapus buku berdasarkan id
    """
    if request.method == "DELETE":
        Books.query.filter_by(id=book_id).delete()
        db.session.commit()
        return success_response("Buku berhasil dihapus", res_code=200)
    return error_response("Method not allowed", res_code=405)


def create_book() -> str | Response:
    """
    Menambahkan buku baru
    """
    if request.method == 'POST':
        if request.json.get("title") and request.json.get("author"):
            title = request.json['title']
            author = request.json['author']
            new_book = Books(title=title, author=author)
            db.session.add(new_book)
            db.session.commit()
            return success_response("Data berhasil ditambah",
                                    data={
                                        "id": new_book.id,
                                        "title": new_book.title,
                                        "author": new_book.author,
                                        "created_at": new_book.created_at
                                    },
                                    res_code=201)
        return error_response("Data tidak lengkap", res_code=400)
    return error_response("Method not allowed", res_code=405)

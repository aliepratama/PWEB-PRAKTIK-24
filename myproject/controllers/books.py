from flask import request, Response
from myproject.models.books import get_all_books_asc, get_all_books_desc, insert_book, edit_book_by_id, delete_book_by_id
from myproject.utils.res_wrapper import success_response, error_response


def get_books() -> str:
    """
    Mendapatkan buku-buku yang ada
    """
    if request.args.get('order') == 'asc':
        books = get_all_books_asc()
    else:
        books = get_all_books_desc()
    # Melakukan mapping data
    books = map(lambda book: {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "created_at": book[3]
    }, books)
    books = list(books)
    return success_response(data=books)


def edit_book(book_id: int) -> str | Response:
    """
    Edit buku berdasarkan id
    """
    if request.method == "PUT":
        if request.json.get("title") and request.json.get("author"):
            new_title = request.json['title']
            new_author = request.json['author']
            edit_book_by_id(book_id, new_title, new_author)
            return success_response(msg="Buku berhasil diubah", res_code=200)
        return error_response("Data tidak lengkap", res_code=400)
    return error_response("Method not allowed", res_code=405)


def delete_book(book_id: int) -> Response:
    """
    Menghapus buku berdasarkan id
    """
    if request.method == "DELETE":
        delete_book_by_id(book_id)
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
            insert_book(title, author)
            return success_response("Data berhasil ditambah", res_code=201)
        return error_response("Data tidak lengkap", res_code=400)
    return error_response("Method not allowed", res_code=405)

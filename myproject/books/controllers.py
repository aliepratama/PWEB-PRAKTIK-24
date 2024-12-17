from flask import request, Response
from ..models import Books
from ..utils.res_wrapper import success_response, error_response


def books_wrapper(book: Books) -> dict[str, str | int]:
    """
    Wrapper untuk data buku
    """
    return {"id": book.id, "title": book.title, 
            "author": book.author, "created_at": book.created_at}


def get_book(id: int) -> Response:
    """
    Mendapatkan buku berdasarkan id
    """
    # Mendapatkan data buku berdasarkan id
    book = Books.get_by_id(id)
    if book:
        return success_response(data=books_wrapper(book))
    return error_response("Buku tidak ditemukan", res_code=404)


def get_books() -> Response:
    """
    Mendapatkan buku-buku yang ada
    """
    # Mendapatkan metode sorting dari params
    order = request.args.get('order')
    books = Books.get_all(sort_by=order)
    # Melakukan mapping data
    books = map(books_wrapper, books)
    books = list(books)
    return success_response(data=books)


def edit_book(book_id: int) -> Response:
    """
    Edit buku berdasarkan id
    """
    # Memeriksa apakah data title dan author ada
    if request.json.get("title") and request.json.get("author"):
        new_title = request.json['title']
        new_author = request.json['author']
        # Mengupdate data buku
        book = Books.update(book_id, new_title, new_author)
        return success_response(data=books_wrapper(book), 
                                msg="Buku berhasil diubah", 
                                res_code=200)
    # Jika data tidak lengkap
    return error_response("Data tidak lengkap", res_code=400)


def delete_book(book_id: int) -> Response:
    """
    Menghapus buku berdasarkan id
    """
    # Menghapus data buku
    book = Books.delete(book_id)
    return success_response(f"Buku {book.title} berhasil dihapus", 
                            res_code=200)


def create_book() -> str | Response:
    """
    Menambahkan buku baru
    """
    # Memeriksa apakah data title dan author ada
    if request.json.get("title") and request.json.get("author"):
        title = request.json['title']
        author = request.json['author']
        # Menambahkan data buku baru
        new_book = Books.insert(title, author)
        return success_response("Data berhasil ditambah", 
                                data=books_wrapper(new_book),
                                res_code=201)
    # Jika data tidak lengkap
    return error_response("Data tidak lengkap", res_code=400)

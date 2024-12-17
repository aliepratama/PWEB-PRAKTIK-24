from flask import request
from myproject.books.controllers import get_book, get_books, create_book, edit_book, delete_book as del_book
from myproject.books import books
from ..utils.res_wrapper import error_response


@books.route('/', methods=['GET', 'POST'])
def books_route():
    if request.method == 'POST':
        return create_book()
    elif request.method == 'GET':
        return get_books()
    return error_response(msg="Method not allowed", res_code=405)


@books.route('/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
def book_route(book_id: int):
    if request.method == 'GET':
        return get_book(book_id)
    elif request.method == 'DELETE':
        return del_book(book_id)
    elif request.method == 'PUT':
        return edit_book(book_id)
    return error_response(msg="Method not allowed", res_code=405)

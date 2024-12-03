from myproject.app import mysql


def get_book_by_id(id: int) -> tuple[any]:
    """
    Mengambil buku berdasarkan id
    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books WHERE id = %s", (id,))
    books = cur.fetchone()
    cur.close()
    return books


def get_all_books_asc() -> tuple[tuple[any]]:
    """
    Mengambil semua buku yang ada, diurutkan berdasarkan created_at secara ascending
    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books ORDER BY created_at ASC")
    books = cur.fetchall()
    cur.close()
    return books


def get_all_books_desc() -> tuple[tuple[any]]:
    """
    Mengambil semua buku yang ada, diurutkan berdasarkan created_at secara descending
    """
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM books ORDER BY created_at DESC")
    books = cur.fetchall()
    cur.close()
    return books


def insert_book(title: str, author: str) -> None:
    """
    Menambahkan buku dengan title dan author
    """
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO books(title, author) VALUES(%s, %s)",
        (title, author))
    mysql.connection.commit()
    cur.close()

def edit_book_by_id(id: int, title: str, author: str) -> None:
    """
    Mengedit buku berdasarkan id
    """
    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE books SET title = %s, author = %s WHERE id = %s",
        (title, author, id))
    mysql.connection.commit()
    cur.close()


def delete_book_by_id(id: int) -> None:
    """
    Menghapus buku berdasarkan id
    """
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

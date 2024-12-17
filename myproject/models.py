from . import db


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    @staticmethod
    def get_by_id(id: int) -> 'Books':
        return Books.query.filter_by(id=id).first()

    @staticmethod
    def get_all(sort_by: str) -> list['Books']:
        if sort_by == 'asc':
            return Books.query.order_by(Books.created_at.asc()).all()
        return Books.query.order_by(Books.created_at.desc()).all()

    @staticmethod
    def insert(title: str, author: str) -> 'Books':
        book = Books(title=title, author=author)
        db.session.add(book)
        db.session.commit()
        return book

    @staticmethod
    def update(id: int, title: str, author: str) -> 'Books':
        book = Books.query.filter_by(id=id)
        book.update({
            "title": title,
            "author": author
        })
        db.session.commit()
        return book.first()

    @staticmethod
    def delete(id: int) -> 'Books':
        book = Books.query.filter_by(id=id)
        temp = book.first()
        book.delete()
        db.session.commit()
        return temp

    def __repr__(self) -> str:
        return f'<Book {self.title}>'

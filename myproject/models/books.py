from myproject.app import db


class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f'<Book {self.title}>'

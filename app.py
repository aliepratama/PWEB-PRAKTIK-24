from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

with app.app_context():
    db = SQLAlchemy(app)
    from models import Users, Candidates, Votes
    migrate = Migrate(app, db)


@app.route('/')
def index():
    """
    Berikan seluruh data kandidat yang ada beserta jumlah vote yang didapat
    """
    pass


@app.route('/users', methods=['GET', 'POST', 'PUT'])
def users():
    """
    Method GET: Berikan detail user dan vote yang telah dilakukan
    Method POST: Registrasi user baru
    Method PUT: Update password user
    """
    pass


@app.route('/vote/<int:candidate_id>', methods=['GET', 'POST'])
def vote(candidate_id):
    """
    Method GET: Berikan detail kandidat yang dipilih
    Method POST: Lakukan vote (1 user hanya bisa vote 1 kali)
    """
    pass


if __name__ == '__main__':
    app.run(debug=True)

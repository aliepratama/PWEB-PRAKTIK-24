from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

with app.app_context():
    db = SQLAlchemy(app)
    from models import Users, Events, Bookings
    migrate = Migrate(app, db)


@app.route('/')
def index():
    """
    Berikan seluruh data event yang ada beserta jumlah peserta yang didapat
    """
    pass


@app.route('/users', methods=['GET', 'POST', 'PUT'])
def users():
    """
    Method GET: Berikan detail user dan tiket event yang sudah dibeli
    Method POST: Registrasi user baru
    Method PUT: Update password user
    """
    pass


@app.route('/booking/<int:event_id>', methods=['GET', 'POST'])
def booking(event_id):
    """
    Method GET: Berikan detail event yang dipilih
    Method POST: Lakukan pembelian tiket (tiket hanya bisa dibeli ketika acara masih tersedia dan kuota user masih cukup)
    """
    pass

if __name__ == '__main__':
    app.run(debug=True)

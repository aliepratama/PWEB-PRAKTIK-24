from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.events import get_events, get_event_by_id
from models.bookings import get_bookings_by_user_id, add_booking, display_bookings_by_user_id
from models.users import get_users, get_user_by_id, add_user
from utils.date import check_valid_date

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    return render_template('index.html', events=get_events())


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mendapatkan data dari form login
        email = request.form['surel']
        password = request.form['kata_sandi']
        # Mencari user berdasarkan email
        for user in get_users():
            # Jika email ditemukan
            if user['mail'] == email:
                # Mengecek password
                if not check_password_hash(user['password'], password):
                    flash('Kata sandi salah')
                    return redirect(url_for('login'))
                # Menyimpan id user ke session
                session['id'] = user['id']
                return redirect(url_for('dashboard'))
        flash('Email tidak ditemukan')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Mendapatkan data dari form register
        email = request.form['surel']
        password = request.form['kata_sandi']
        password_conf = request.form['ulang_kata_sandi']
        # Mengecek apakah email dan password sudah diisi
        if not email or not password or not password_conf:
            flash('Email dan kata sandi harus diisi')
            return redirect(url_for('register'))
        # Mengecek password sudah sesuai
        if password != password_conf:
            flash('Kata sandi tidak sama')
            return redirect(url_for('register'))
        # Melakukan hashing password
        hashed_password = generate_password_hash(password)
        # Menambahkan user baru ke model
        add_user(email, hashed_password)
        flash('Registrasi berhasil, silakan login')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    # Mendapatkan id user dari session
    if 'id' not in session:
        return redirect(url_for('login'))
    # Mendapatkan data user berdasarkan id
    cur_booking = display_bookings_by_user_id(session['id'])
    return render_template('dashboard.html',
                           events=get_events(),
                           user=get_user_by_id(session['id']),
                           bookings=cur_booking)


@app.route('/booking/<int:event_id>')
def booking(event_id):
    # Mendapatkan id user dari session
    if 'id' not in session:
        return redirect(url_for('login'))
    # Mendapatkan data user berdasarkan id
    cur_booking = get_bookings_by_user_id(session['id'])
    # Mendapatkan data event berdasarkan id
    event = get_event_by_id(event_id)
    # Mengecek kuota pembelian dan tanggal
    if len(cur_booking) > 3 or get_user_by_id(session['id'])['quota'] == 0:
        flash('Kuota pembelian sudah habis')
        return redirect(url_for('dashboard'))
    # Mengecek apakah event sudah berakhir
    if not check_valid_date(event['date']):
        flash('Acara sudah selesai')
        return redirect(url_for('dashboard'))
    # Melakukan pembelian tiket
    add_booking(session['id'], event_id)
    flash('Suara berhasil diberikan')
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    # Membersihkan session
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

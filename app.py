from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.candidates import candidates
from models.votes import votes
from models.users import users

app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
    # Melakukan deep copy agar data asli tidak berubah
    new_candidates = candidates.copy()
    # Memastikan bahwa data awal kosong
    for candidate in new_candidates:
        candidate['vote_count'] = 0
    # Menghitung jumlah suara yang diterima oleh masing-masing kandidat
    for vote in votes:
        new_candidates[vote['vote'] - 1]['vote_count'] += 1
    return render_template('index.html', candidates=new_candidates)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Mengambil data dari form login
        email = request.form['email']
        password = request.form['password']
        # Mencari user berdasarkan email
        for user in users:
            # Mengecek email yang sesuai
            if user['mail'] == email:
                # Mengecek apakah password sesuai
                if not check_password_hash(user['password'], password):
                    flash('Kata sandi salah')
                    return redirect(url_for('login'))
                session['id'] = user['id']
                return redirect(url_for('dashboard'))
        flash('Email tidak ditemukan')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Mengambil data dari form register
        email = request.form['email']
        password = request.form['password']
        password_conf = request.form['conf_password']
        # Mengecek apakah email dan password sudah diisi
        if not email or not password or not password_conf:
            flash('Email dan kata sandi harus diisi')
            return redirect(url_for('register'))
        # Mengecek apakah password dan konfirmasi password sesuai
        if password != password_conf:
            flash('Kata sandi tidak sama')
            return redirect(url_for('register'))
        # Melakukan hashing password
        hashed_password = generate_password_hash(password)
        # Membuat user baru
        new_user = {'id': len(users) + 1, 'mail': email,
                    'password': hashed_password}
        users.append(new_user)
        flash('Registrasi berhasil, silakan login')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    # Mengecek apakah user sudah login
    if 'id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', candidates=candidates)


@app.route('/vote/<int:candidate_id>')
def vote(candidate_id):
    # Mengecek apakah user sudah login
    if 'id' not in session:
        return redirect(url_for('login'))
    # Mengecek apakah user sudah memberikan suara
    for vote in votes:
        if vote['user_id'] == session['id']:
            flash('Anda sudah memberikan suara')
            return redirect(url_for('dashboard'))
    # Menambahkan suara ke kandidat yang dipilih
    votes.append({
        'id': len(votes) + 1,
        'user_id': users[session['id'] - 1],
        'vote': candidate_id})
    flash('Suara berhasil diberikan')
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    # Menghapus session
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

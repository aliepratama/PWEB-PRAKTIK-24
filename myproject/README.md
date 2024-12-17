![logo2](https://github.com/user-attachments/assets/425e7307-6204-4fa3-adf2-0606088e06de)

# Pemrograman Web Praktik
### Dosen Pengampu: Endang Anggiratih, S.T., M.Cs.
### Asisten Dosen: Ali Pratama

Mata kuliah yang mengimplementasi konsep dasar web services menggunakan framework Flask

1. Kelas: IX
- Jadwal: 07:00 – 10:30
- Ruangan: K1-LK2.1

2. Kelas: X
- Jadwal: 12:50 – 16:20
- Ruangan: K1-LK1.1


### Instalasi
Instalasi modul yang digunakan
```shell
python -m venv myenv
myenv\scripts\activate.bat
pip install -r requirements.txt
```
Membuat database `db_books` pada mysql
```mysql
CREATE DATABASE db_books;
```
Inisialisasi database migration
```shell
flask db init
```
Mencatat skema pertama
```shell
flask db migrate -m "create table books"
```
Mengaplikasikan skema pertama
```shell
flask db upgrade
```
Menjalankan aplikasi
```shell
flask run
```
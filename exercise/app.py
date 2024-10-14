from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

list_buku = [
    {
        "id": 1,
        "title": "Malin kundang",
        "author": "zuhair"
    },
    {
        "id": 2,
        "title": "Doel si anak betawi",
        "author": "bagas"
    },
]


@app.route("/")
def tampil_buku():
    return render_template('home.html', books=list_buku)


@app.route("/tambah", methods=["GET", "POST"])
def tambah_buku():
    if request.method == "POST":
        new_id = len(list_buku) + 1
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        list_buku.append({
            "id": new_id,
            "title": new_title,
            "author": new_author
        })
        return redirect(url_for('tampil_buku'))
    return render_template("tambah.html")


@app.route('/hapus/<int:book_id>')
def delete_book(book_id):
    global list_buku
    list_buku = [buku for buku in list_buku if buku['id'] != book_id]
    return redirect(url_for('tampil_buku'))


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_buku(book_id):
    if request.method == "POST":
        new_title = request.form.get("title")
        new_author = request.form.get("author")
        for buku in list_buku:
            if buku["id"] == book_id:
                buku["title"] = new_title
                buku["author"] = new_author
        return redirect(url_for('tampil_buku'))
    for buku in list_buku:
        if buku["id"] == book_id:
            return render_template("edit.html",
                                   title=buku["title"],
                                   author=buku["author"])


if __name__ == "__main__":
    app.run()

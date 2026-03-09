"""
Main application Web Routing menggunakan Flask.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import os

from models.book import Book, EBook
from database.db_manager import DatabaseManager

app = Flask(__name__)
app.secret_key = "kunci_rahasia_untuk_flash_messages"

# Inisiasi database
db = DatabaseManager('library.db')
db.init_db()

@app.route('/')
def index():
    """Route utama untuk menampilkan halaman daftar buku dan form."""
    raw_books = db.get_all_books()
    processed_books = []
    
    # Pengulangan (for) untuk memproses data dari db ke object OOP (Polymorphism)
    for b in raw_books:
        # Array (Dictionary) mapping dengan method OOP
        if b['type'] == 'EBook':
            # instansiasi EBook
            obj = EBook(b['id'], b['title'], b['author'], b['year'], b['price'])
        else:
            # instansiasi printed book
            obj = Book(b['id'], b['title'], b['author'], b['year'], b['price'])
        
        processed_books.append({
            'id': obj.id_book,
            'details': obj.get_details(),
            'type': b['type']
        })
        
    return render_template('index.html', books=processed_books)

@app.route('/add', methods=['POST'])
def add_book():
    """Route untuk menangani penambahan buku baru."""
    title = request.form.get('title')
    author = request.form.get('author')
    year_str = request.form.get('year')
    price_str = request.form.get('price')
    book_type = request.form.get('type')
    
    # Struktur Kontrol Percabangan (if..elif..else)
    if not title or not author:
        flash("Error: Judul dan Penulis wajib diisi!", "danger")
    elif not year_str.isdigit() or not price_str.isdigit():
        flash("Error: Tahun dan Harga harus berupa angka bulat!", "danger")
    else:
        year = int(year_str)
        price = int(price_str)
        db.add_book(title, author, year, price, book_type)
        flash("Sukses: Buku berhasil ditambahkan!", "success")
        
    return redirect(url_for('index'))

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    """Route untuk mengedit data buku."""
    book = db.get_book_by_id(book_id)
    if not book:
        flash("Error: Buku tidak ditemukan!", "danger")
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year_str = request.form.get('year')
        price_str = request.form.get('price')
        book_type = request.form.get('type')

        if not title or not author:
            flash("Error: Judul dan Penulis wajib diisi!", "danger")
        elif not year_str.isdigit() or not price_str.isdigit():
            flash("Error: Tahun dan Harga harus berupa angka bulat!", "danger")
        else:
            year = int(year_str)
            price = int(price_str)
            db.update_book(book_id, title, author, year, price, book_type)
            flash("Sukses: Data buku berhasil diperbarui!", "success")
            return redirect(url_for('index'))

    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    """Route untuk menghapus buku."""
    book = db.get_book_by_id(book_id)
    if book:
        db.delete_book(book_id)
        flash("Sukses: Buku berhasil dihapus!", "success")
    else:
        flash("Error: Buku tidak ditemukan!", "danger")
        
    return redirect(url_for('index'))

@app.route('/export')
def export_data():
    """Route untuk ekspor ke file CSV."""
    filename = "export_buku.csv"
    db.export_to_csv(filename)
    flash(f"Data sukses diekspor ke file {filename}!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Jalankan server
    print("Sistem Toko Buku berjalan di http://127.0.0.1:5000")
    app.run(debug=True, host='127.0.0.1', port=5000)

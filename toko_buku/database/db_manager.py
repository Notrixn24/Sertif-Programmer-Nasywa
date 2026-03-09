"""
Modul untuk mengelola koneksi database SQLite dan ekspor data menggunakan pandas.
"""
import sqlite3
import pandas as pd

class DatabaseManager:
    """
    Kelas untuk menangani operasi Database SQLite dan File Export/Import CSV menggunakan Pandas.
    """
    def __init__(self, db_name: str = "library.db"):
        # Encapsulation dengan attribute private
        self.__db_name = db_name
        
    def init_db(self):
        """Membuat tabel jika belum ada di database."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS books') # Drop old table since we need a new schema
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                price INTEGER,
                type TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def add_book(self, title: str, author: str, year: int, price: int, book_type: str):
        """Prosedur menambahkan buku ke dalam database."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO books (title, author, year, price, type)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, author, year, price, book_type))
        conn.commit()
        conn.close()

    def get_book_by_id(self, book_id: int) -> dict | None:
        """Mengambil data satu buku berdasarkan ID."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, year, price, type FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'year': row[3],
                'price': row[4],
                'type': row[5]
            }
        return None

    def update_book(self, book_id: int, title: str, author: str, year: int, price: int, book_type: str):
        """Prosedur mengupdate data buku."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, year = ?, price = ?, type = ?
            WHERE id = ?
        ''', (title, author, year, price, book_type, book_id))
        conn.commit()
        conn.close()

    def delete_book(self, book_id: int):
        """Prosedur menghapus buku berdasarkan ID."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

    def get_all_books(self) -> list:
        """Mengambil semua data buku (return list of dictionaries)."""
        conn = sqlite3.connect(self.__db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, author, year, price, type FROM books")
        rows = cursor.fetchall()
        conn.close()
        
        books_list = []
        # Pengulangan (Looping) ke-2: Menggunakan while loop untuk perulangan sesuai syarat.
        limit = len(rows)
        idx = 0
        while idx < limit:
            row = rows[idx]
            # Menggunakan struktur Dictionaries untuk mapping row data (Syarat Array/Dictionary)
            book_dict = {
                'id': row[0],
                'title': row[1],
                'author': row[2],
                'year': row[3],
                'price': row[4],
                'type': row[5]
            }
            # List (Array di Python)
            books_list.append(book_dict)
            idx += 1
            
        return books_list

    def export_to_csv(self, filename: str) -> None:
        """Fungsi khusus (library eksternal) untuk export data array / dictionary ke .csv menggunakan pandas."""
        books = self.get_all_books()
        if len(books) > 0:
            df = pd.DataFrame(books)
            df.to_csv(filename, index=False)
        else:
            # Jika tabel kosong, simpan csv dengan header
            df = pd.DataFrame(columns=['id', 'title', 'author', 'year', 'price', 'type'])
            df.to_csv(filename, index=False)

# Sertif-Programmer-Nasywa

Aplikasi ini adalah **Sistem Toko Buku Mini** berskala Web yang dibangun menggunakan bahasa pemrograman **Python (Flask Framework)**. Program ini dikembangkan secara khusus untuk memenuhi seluruh kriteria Ujian Praktik Sertifikasi Programmer.

## Fitur Utama & Pemenuhan Kriteria Ujian

Program ini telah menerapkan seluruh spesifikasi wajib dari soal ujian, dengan rincian sebagai berikut:

1. **Antarmuka (Interface) HTML**
   - Menggunakan HTML, CSS berdesain rapi (efek _glassmorphism_), serta input form lengkap dan tabel untuk interaksi pengguna.
   - Dipisahkan ke dalam file `index.html` dan `edit.html` di dalam folder `templates`.

2. **Logika, Tipe Data & Array**
   - **Tipe Data:** Menerapkan `str`, `int`, `float`, `list` (Array Python), dan `dict` (Array Asosiatif).
   - **Struktur Kontrol:**
     - Percabangan (`if..elif..else`) digunakan di `app.py` untuk memvalidasi input _form_.
     - Pengulangan `for` digunakan untuk memproses list ke Object, dan `while` digunakan saat _fetching database_ di `db_manager.py`.

3. **Fungsi & Pemrograman Berorientasi Objek (OOP) Lengkap**
   - **Fungsi/Prosedur:** Terdapat prosedur `add_book(...)` dan fungsi `get_all_books() -> list`.
   - **Enkapsulasi & Properties:** Atribut dibungkus secara _private_ (contoh: `self.__title`) dan diakses lewat _getter/setter_ `@property`.
   - **Inheritance (Pewarisan):** Class `EBook` (Buku Digital) diwariskan dari Class `Book`.
   - **Polymorphism (Polimorfisme):** Implementasi override method `get_details()` yang menghasilkan output berbeda pada anak kelasnya.
   - **Overloading:** Memanfaatkan implementasi Pythonic melalui mekanisme _Default Parameters_ pada konstruktor `__init__`.
   - **Interface:** Memanfaatkan modul abstrak (`abc.ABC`) pada antarmuka `IBookItem` (di `models/book.py`).

4. **Namespace dan Struktur File**
   - Proyek terdiri atas lebih dari 2 namespace (package/direktori kerja) menggunakan `__init__.py`:
     - Package `models/`
     - Package `database/`

5. **Penggunaan Database & Ekspor File Media**
   - **Database SQLite:** Penyimpanan permanen yang aman (`library.db`) menggunakan _library_ standar `sqlite3`.
   - **File Media Csv:** Kemampuan mengekspor seluruh data buku menjadi file `export_buku.csv` secara otomatis menggunakan external library `pandas`.

6. **Library Eksternal**
   - Menggunakan `Flask` (Web Framework).
   - Menggunakan `pandas` (Data Manipulation).

7. **Dokumentasi & Standar**
   - Mengikuti _Coding Guidelines_ resmi **PEP 8**.
   - Dilengkapi _Docstrings_ di setiap level (Module, Class, Function).

---

## Struktur Direktori

```text
toko_buku/
├── app.py                      # Main entry web routing (Flask)
├── requirements.txt            # Daftar pustaka eksternal
├── models/                     # Namespace: OOP Logic
│   ├── __init__.py
│   └── book.py                 # Class, Interface, Inheritance, Properties
├── database/                   # Namespace: Database Connection
│   ├── __init__.py
│   └── db_manager.py           # SQLite Queries & Pandas Export CSV
├── static/                     # Direktori File Media
│   └── wp12420099.jpg          # Background UI
└── templates/                  # Direktori HTML
    ├── index.html              # Antarmuka Utama & Tambah
    └── edit.html               # Antarmuka Edit
```

---

## Panduan Instalasi & Menjalankan Program

Penuhi langkah-langkah di bawah ini untuk menguji program secara lokal (Localhost):

### 1. Prasyarat Sistem

Pastikan sudah menginstal Python versi 3.8 ke atas pada perangkat/komputer.

### 2. Instalasi Library Eksternal

Direkomendasikan membuat _Virtual Environment_ terlebih dahulu (opsional). Kemudian pasang seluruh konfigurasi pustaka eksternalnya (_dependency_):

Buka _Command Prompt / Terminal_ di direktori root aplikasi (`toko_buku`) dan jalankan:

```bash
pip install -r requirements.txt
```

### 3. Menjalankan Server Web

Setelah instalasi selesai, cukup esekusi file _routing_ utamanya:

```bash
python app.py
```

### 4. Buka Aplikasi di Browser

Buka Web Browser, dan masuk ke tautan berikut:

> **http://127.0.0.1:5000** atau **http://localhost:5000**

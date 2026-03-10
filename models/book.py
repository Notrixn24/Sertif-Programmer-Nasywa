"""
Module untuk model Buku.
Mengimplementasikan Interface (ABC), OOP (Encapsulation, Inheritance, Polymorphism),
serta menggunakan default parameter.
"""

from abc import ABC, abstractmethod

class IBookItem(ABC):
    """
    Interface (Abstrak) untuk item buku.
    """
    @abstractmethod
    def get_details(self) -> str:
        """Mengembalikan representasi string dari detail buku."""
        pass

class Book(IBookItem):
    """
    Base class untuk Buku yang mengimplementasikan IBookItem.
    """
    def __init__(self, id_book: int, title: str, author: str, year: int = 2024, price: int = 0):
        # Attribute private (Encapsulation/Hak akses tipe data private)
        self.__id = id_book
        self.__title = title
        self.__author = author
        self.__year = year
        self.__price = price

    # Properties / Hak akses public dengan @property
    @property
    def id_book(self) -> int:
        return self.__id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        if value:
            self.__title = value

    @property
    def author(self) -> str:
        return self.__author

    @property
    def year(self) -> int:
        return self.__year

    @property
    def price(self) -> int:
        return self.__price

    def get_details(self) -> str:
        """
        Polymorphism: Impelementasi method dari interface.
        """
        # Format harga dengan pemisah ribuan
        formatted_price = f"Rp {self.price:,}".replace(',', '.')
        return f"'{self.title}' oleh {self.author} (Tahun {self.year}) - Harga: {formatted_price}"

class EBook(Book):
    """
    Class turunan (Inheritance) untuk buku elektronik.
    """
    def __init__(self, id_book: int, title: str, author: str, year: int = 2024, price: int = 0, file_size_mb: float = 1.0):
        # Overloading via default parameter year=2024, file_size_mb=1.0
        super().__init__(id_book, title, author, year, price)
        # Attribute private untuk file size
        self.__file_size_mb = file_size_mb

    @property
    def file_size_mb(self) -> float:
        return self.__file_size_mb

    def get_details(self) -> str:
        """
        Polymorphism (Overriding): Modifikasi (override) behavior method parent class.
        """
        base_details = super().get_details()
        return f"[E-Book] {base_details} - Ukuran File: {self.file_size_mb} MB"

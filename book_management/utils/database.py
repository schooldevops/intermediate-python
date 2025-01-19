import sqlite3
from contextlib import contextmanager
from typing import List, Optional
from models.book import Book

class DatabaseManager:
    def __init__(self, db_file: str):
        self.db_file = db_file
    
    @contextmanager
    def get_connection(self):
        conn = sqlite3.connect(self.db_file)
        try:
            yield conn
        finally:
            conn.close()
    
    def initialize_db(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    isbn TEXT UNIQUE NOT NULL,
                    published_date DATE,
                    quantity INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
    
    def add_book(self, book: Book) -> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO books (title, author, isbn, published_date, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (book.title, book.author, book.isbn,
                 book.published_date.strftime('%Y-%m-%d'),
                 book.quantity))
            conn.commit()
            return cursor.lastrowid
    
    def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM books WHERE isbn = ?', (isbn,))
            row = cursor.fetchone()
            if row:
                return Book(*row)
            return None

import unittest
from datetime import datetime
from models.book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            id=1,
            title="파이썬 프로그래밍",
            author="홍길동",
            isbn="ISBN-123456",
            published_date=datetime.now(),
            quantity=5
        )
    
    def test_book_creation(self):
        self.assertEqual(self.book.title, "파이썬 프로그래밍")
        self.assertEqual(self.book.author, "홍길동")
        self.assertEqual(self.book.quantity, 5)
    
    def test_to_dict(self):
        book_dict = self.book.to_dict()
        self.assertIsInstance(book_dict, dict)
        self.assertEqual(book_dict['title'], "파이썬 프로그래밍")
        self.assertEqual(book_dict['author'], "홍길동")

if __name__ == '__main__':
    unittest.main()

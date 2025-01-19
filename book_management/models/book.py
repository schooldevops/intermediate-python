from dataclasses import dataclass
from datetime import datetime

@dataclass
class Book:
    id: int
    title: str
    author: str
    isbn: str
    published_date: datetime
    quantity: int
    created_at: datetime = datetime.now()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'published_date': self.published_date.strftime('%Y-%m-%d'),
            'quantity': self.quantity,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

import tkinter as tk
from tkinter import ttk, messagebox
from models.book import Book
from utils.database import DatabaseManager
from utils.logger import logger
from datetime import datetime

class BookManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("도서 관리 시스템")
        self.db = DatabaseManager('database/books.db')
        self.db.initialize_db()
        
        self.setup_ui()
    
    def setup_ui(self):
        # 입력 프레임
        input_frame = ttk.LabelFrame(self.root, text="도서 정보 입력")
        input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        
        # 입력 필드
        ttk.Label(input_frame, text="제목:").grid(row=0, column=0, padx=5, pady=5)
        self.title_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.title_var).grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(input_frame, text="저자:").grid(row=1, column=0, padx=5, pady=5)
        self.author_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.author_var).grid(row=1, column=1, padx=5, pady=5)
        
        # 버튼
        ttk.Button(input_frame, text="도서 추가", command=self.add_book).grid(row=2, column=0, columnspan=2, pady=10)
    
    def add_book(self):
        try:
            book = Book(
                id=None,
                title=self.title_var.get(),
                author=self.author_var.get(),
                isbn=f"ISBN-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                published_date=datetime.now(),
                quantity=1
            )
            
            book_id = self.db.add_book(book)
            logger.info(f"도서 추가됨: {book.title} (ID: {book_id})")
            messagebox.showinfo("성공", "도서가 추가되었습니다.")
            
            # 입력 필드 초기화
            self.title_var.set("")
            self.author_var.set("")
            
        except Exception as e:
            logger.error(f"도서 추가 실패: {str(e)}")
            messagebox.showerror("오류", f"도서 추가 중 오류 발생: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookManagementApp(root)
    root.mainloop()

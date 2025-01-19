import unittest
from datetime import datetime

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.created_at = datetime.now()
    
    def change_email(self, new_email):
        if '@' not in new_email:
            raise ValueError("유효하지 않은 이메일 주소입니다.")
        self.email = new_email
    
    def get_info(self):
        return {
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("0으로 나눌 수 없습니다.")
        return x / y

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "test@example.com")
    
    def test_init(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertIsInstance(self.user.created_at, datetime)
    
    def test_change_email_valid(self):
        new_email = "new@example.com"
        self.user.change_email(new_email)
        self.assertEqual(self.user.email, new_email)
    
    def test_change_email_invalid(self):
        with self.assertRaises(ValueError):
            self.user.change_email("invalid-email")
    
    def test_get_info(self):
        info = self.user.get_info()
        self.assertIsInstance(info, dict)
        self.assertEqual(info['username'], self.user.username)
        self.assertEqual(info['email'], self.user.email)
        self.assertEqual(info['created_at'], self.user.created_at)

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)
    
    def test_divide(self):
        self.assertEqual(Calculator.divide(6, 2), 3)
        self.assertEqual(Calculator.divide(5, 2), 2.5)
        self.assertEqual(Calculator.divide(0, 5), 0)
        
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

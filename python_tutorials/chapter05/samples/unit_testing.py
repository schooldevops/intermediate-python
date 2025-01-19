import unittest
import pytest
from typing import List

# 테스트할 클래스
class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
    
    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("0으로 나눌 수 없습니다")
        return a / b
    
    def get_stats(self, numbers: List[float]) -> dict:
        if not numbers:
            raise ValueError("빈 리스트는 계산할 수 없습니다")
        return {
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }

# unittest를 사용한 테스트
class TestCalculator(unittest.TestCase):
    def setUp(self):
        """각 테스트 메서드 실행 전에 호출됨"""
        self.calc = Calculator()
    
    def test_add(self):
        """덧셈 테스트"""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.3, places=1)
    
    def test_divide(self):
        """나눗셈 테스트"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # 예외 테스트
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_stats(self):
        """통계 계산 테스트"""
        numbers = [1, 2, 3, 4, 5]
        stats = self.calc.get_stats(numbers)
        
        self.assertEqual(stats['sum'], 15)
        self.assertEqual(stats['average'], 3)
        self.assertEqual(stats['min'], 1)
        self.assertEqual(stats['max'], 5)
        
        # 빈 리스트 테스트
        with self.assertRaises(ValueError):
            self.calc.get_stats([])

# pytest를 사용한 테스트
def test_calculator_add():
    calc = Calculator()
    assert calc.add(3, 5) == 8
    assert calc.add(-1, 1) == 0
    assert abs(calc.add(0.1, 0.2) - 0.3) < 0.0001

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    
    with pytest.raises(ValueError):
        calc.divide(5, 0)

@pytest.mark.parametrize("numbers,expected", [
    ([1, 2, 3], {'sum': 6, 'average': 2, 'min': 1, 'max': 3}),
    ([0], {'sum': 0, 'average': 0, 'min': 0, 'max': 0}),
    ([1, 1, 1], {'sum': 3, 'average': 1, 'min': 1, 'max': 1}),
])
def test_calculator_stats(numbers, expected):
    calc = Calculator()
    assert calc.get_stats(numbers) == expected

def test_calculator_stats_empty():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.get_stats([])

if __name__ == '__main__':
    # unittest 테스트 실행
    unittest.main()

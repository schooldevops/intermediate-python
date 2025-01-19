"""
파이썬의 함수형 데이터 처리 예제
이 예제는 map, filter, reduce 등의 함수형 데이터 처리 기법과 
제너레이터, 이터레이터를 활용한 지연 평가를 보여줍니다.
"""

from typing import TypeVar, Callable, Iterator, Iterable, List, Any, Optional
from functools import reduce
from operator import add, mul
from dataclasses import dataclass
from datetime import datetime
import itertools
import operator

T = TypeVar('T')
R = TypeVar('R')

# 기본 함수형 데이터 처리 예제
def square(x: int) -> int:
    return x * x

def is_even(x: int) -> bool:
    return x % 2 == 0

def sum_list(numbers: List[int]) -> int:
    return reduce(add, numbers, 0)

# 커스텀 함수형 도구
def my_map(func: Callable[[T], R], iterable: Iterable[T]) -> Iterator[R]:
    """자체 구현 map 함수"""
    return (func(x) for x in iterable)

def my_filter(predicate: Callable[[T], bool], iterable: Iterable[T]) -> Iterator[T]:
    """자체 구현 filter 함수"""
    return (x for x in iterable if predicate(x))

def my_reduce(func: Callable[[T, T], T], iterable: Iterable[T], initial: Optional[T] = None) -> T:
    """자체 구현 reduce 함수"""
    iterator = iter(iterable)
    if initial is None:
        try:
            value = next(iterator)
        except StopIteration:
            raise ValueError("reduce() of empty sequence with no initial value")
    else:
        value = initial
    
    for element in iterator:
        value = func(value, element)
    return value

# 지연 평가 시퀀스
class LazySequence:
    """지연 평가를 사용하는 시퀀스 클래스"""
    def __init__(self, iterable: Iterable[T]):
        self._iterable = iterable
    
    def map(self, func: Callable[[T], R]) -> 'LazySequence[R]':
        return LazySequence(map(func, self._iterable))
    
    def filter(self, predicate: Callable[[T], bool]) -> 'LazySequence[T]':
        return LazySequence(filter(predicate, self._iterable))
    
    def reduce(self, func: Callable[[T, T], T], initial: Optional[T] = None) -> T:
        return reduce(func, self._iterable) if initial is None else reduce(func, self._iterable, initial)
    
    def take(self, n: int) -> List[T]:
        """시퀀스에서 처음 n개의 항목을 가져옴"""
        return list(itertools.islice(self._iterable, n))
    
    def __iter__(self) -> Iterator[T]:
        return iter(self._iterable)

# 데이터 처리 예제를 위한 모델
@dataclass
class Transaction:
    """금융 거래 데이터 모델"""
    date: datetime
    amount: float
    category: str
    description: str

class TransactionProcessor:
    """함수형 스타일로 거래 데이터를 처리하는 클래스"""
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
    
    def total_by_category(self, category: str) -> float:
        """특정 카테고리의 총 거래액 계산"""
        return sum(
            tx.amount for tx in self.transactions 
            if tx.category == category
        )
    
    def categories(self) -> set:
        """고유한 카테고리 목록"""
        return set(tx.category for tx in self.transactions)
    
    def filter_by_amount(self, min_amount: float) -> List[Transaction]:
        """최소 금액 이상의 거래 필터링"""
        return list(filter(
            lambda tx: tx.amount >= min_amount,
            self.transactions
        ))
    
    def transform_amounts(self, rate: float) -> List[Transaction]:
        """모든 거래 금액을 특정 비율로 변환"""
        return list(map(
            lambda tx: Transaction(
                tx.date, tx.amount * rate, 
                tx.category, tx.description
            ),
            self.transactions
        ))

def demonstrate_basic_operations():
    print("\nBasic Functional Operations Demonstration:")
    numbers = range(1, 6)
    
    # 내장 함수형 도구 사용
    squares = list(map(square, numbers))
    evens = list(filter(is_even, numbers))
    total = reduce(add, numbers)
    
    print(f"Original numbers: {list(numbers)}")
    print(f"Squares: {squares}")
    print(f"Even numbers: {evens}")
    print(f"Sum: {total}")

def demonstrate_custom_operations():
    print("\nCustom Functional Operations Demonstration:")
    numbers = range(1, 6)
    
    # 커스텀 함수형 도구 사용
    squares = list(my_map(square, numbers))
    evens = list(my_filter(is_even, numbers))
    total = my_reduce(add, numbers)
    
    print(f"Custom squares: {squares}")
    print(f"Custom evens: {evens}")
    print(f"Custom sum: {total}")

def demonstrate_lazy_evaluation():
    print("\nLazy Evaluation Demonstration:")
    # 무한 시퀀스 생성
    numbers = LazySequence(itertools.count(1))
    
    # 처리 체인 구성 (아직 실행되지 않음)
    result = numbers.map(square).filter(is_even).take(5)
    
    print(f"First 5 even square numbers: {result}")

def demonstrate_transaction_processing():
    print("\nTransaction Processing Demonstration:")
    # 샘플 거래 데이터 생성
    transactions = [
        Transaction(datetime.now(), 100.0, "food", "Grocery shopping"),
        Transaction(datetime.now(), 500.0, "rent", "Monthly rent"),
        Transaction(datetime.now(), 50.0, "food", "Restaurant"),
        Transaction(datetime.now(), 200.0, "utilities", "Electricity bill")
    ]
    
    processor = TransactionProcessor(transactions)
    
    # 다양한 데이터 처리 작업 수행
    food_total = processor.total_by_category("food")
    large_transactions = processor.filter_by_amount(200.0)
    converted = processor.transform_amounts(1.1)  # 10% 증가
    
    print(f"Total food expenses: ${food_total}")
    print(f"Large transactions: {len(large_transactions)}")
    print(f"Categories: {processor.categories()}")

def main():
    print("Functional Data Processing Demonstrations")
    
    demonstrate_basic_operations()
    demonstrate_custom_operations()
    demonstrate_lazy_evaluation()
    demonstrate_transaction_processing()

if __name__ == "__main__":
    main()

"""
파이썬에서의 순수 함수와 불변성 예제
이 예제는 순수 함수의 특성과 불변 데이터 구조의 활용을 보여줍니다.
"""

from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from datetime import datetime
import functools
import copy

# 순수 함수 예제
def add_numbers(a: int, b: int) -> int:
    """순수 함수: 동일한 입력에 대해 항상 동일한 출력을 반환"""
    return a + b

def calculate_total(prices: List[float]) -> float:
    """순수 함수: 외부 상태에 의존하지 않음"""
    return sum(prices)

# 비순수 함수 예제
total_price = 0

def add_to_total(price: float) -> float:
    """비순수 함수: 전역 변수를 수정"""
    global total_price
    total_price += price
    return total_price

def get_current_time() -> str:
    """비순수 함수: 외부 상태(시간)에 의존"""
    return datetime.now().strftime("%H:%M:%S")

# 불변 데이터 구조 예제
@dataclass(frozen=True)
class Point:
    """불변 데이터 클래스"""
    x: float
    y: float
    
    def move(self, dx: float, dy: float) -> 'Point':
        """새로운 Point 객체를 반환"""
        return Point(self.x + dx, self.y + dy)

class ImmutableList:
    """불변 리스트 구현"""
    def __init__(self, items: List[Any]):
        self._items = tuple(items)  # 튜플로 변환하여 불변성 보장
    
    def append(self, item: Any) -> 'ImmutableList':
        """새로운 ImmutableList 객체를 반환"""
        return ImmutableList(list(self._items) + [item])
    
    def remove(self, item: Any) -> 'ImmutableList':
        """새로운 ImmutableList 객체를 반환"""
        items = list(self._items)
        items.remove(item)
        return ImmutableList(items)
    
    def __getitem__(self, index: int) -> Any:
        return self._items[index]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)

# 방어적 복사 예제
class Configuration:
    """방어적 복사를 사용하는 설정 클래스"""
    def __init__(self, settings: Dict[str, Any]):
        self._settings = copy.deepcopy(settings)
    
    def get_setting(self, key: str) -> Any:
        """설정값의 복사본을 반환"""
        value = self._settings.get(key)
        return copy.deepcopy(value)
    
    def set_setting(self, key: str, value: Any) -> None:
        """설정값의 복사본을 저장"""
        self._settings[key] = copy.deepcopy(value)

# 캐싱과 메모이제이션 예제
@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    """메모이제이션을 사용한 피보나치 수열 계산"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def demonstrate_pure_functions():
    print("\nPure Functions Demonstration:")
    # 순수 함수 사용
    print(f"Adding numbers: {add_numbers(5, 3)}")
    print(f"Calculating total: {calculate_total([1.0, 2.0, 3.0])}")
    
    # 비순수 함수와 비교
    print(f"Adding to total: {add_to_total(5.0)}")
    print(f"Current time: {get_current_time()}")

def demonstrate_immutable_data():
    print("\nImmutable Data Structures Demonstration:")
    # Point 클래스 사용
    p1 = Point(1.0, 2.0)
    p2 = p1.move(2.0, 3.0)
    print(f"Original point: {p1}")
    print(f"Moved point: {p2}")
    
    # ImmutableList 사용
    immutable_list = ImmutableList([1, 2, 3])
    new_list = immutable_list.append(4)
    print(f"Original list: {immutable_list}")
    print(f"New list: {new_list}")

def demonstrate_defensive_copying():
    print("\nDefensive Copying Demonstration:")
    # Configuration 클래스 사용
    initial_settings = {"theme": "dark", "language": "en"}
    config = Configuration(initial_settings)
    
    # 원본 설정 수정
    initial_settings["theme"] = "light"
    
    # 설정값 확인
    print(f"Original settings: {initial_settings}")
    print(f"Config theme: {config.get_setting('theme')}")

def demonstrate_memoization():
    print("\nMemoization Demonstration:")
    # 피보나치 수열 계산
    start_time = datetime.now()
    result = fibonacci(30)
    end_time = datetime.now()
    
    print(f"Fibonacci(30) = {result}")
    print(f"Time taken: {end_time - start_time}")
    print(f"Cache info: {fibonacci.cache_info()}")

def main():
    print("Pure Functions and Immutability Demonstrations")
    
    demonstrate_pure_functions()
    demonstrate_immutable_data()
    demonstrate_defensive_copying()
    demonstrate_memoization()

if __name__ == "__main__":
    main()

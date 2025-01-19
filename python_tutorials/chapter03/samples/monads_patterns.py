"""
파이썬의 모나드와 함수형 패턴 예제
이 예제는 Maybe, Either, IO 모나드와 다양한 함수형 패턴을 보여줍니다.
"""

from typing import TypeVar, Generic, Callable, Any, Optional, Union, List
from dataclasses import dataclass
from abc import ABC, abstractmethod
import functools
import logging

T = TypeVar('T')
R = TypeVar('R')
E = TypeVar('E')  # Error type

# Maybe 모나드
class Maybe(Generic[T]):
    """Maybe 모나드 구현"""
    def __init__(self, value: Optional[T]):
        self._value = value
    
    @staticmethod
    def of(value: T) -> 'Maybe[T]':
        return Maybe(value)
    
    @staticmethod
    def empty() -> 'Maybe[Any]':
        return Maybe(None)
    
    def is_present(self) -> bool:
        return self._value is not None
    
    def map(self, func: Callable[[T], R]) -> 'Maybe[R]':
        if self.is_present():
            return Maybe.of(func(self._value))
        return Maybe.empty()
    
    def flat_map(self, func: Callable[[T], 'Maybe[R]']) -> 'Maybe[R]':
        if self.is_present():
            return func(self._value)
        return Maybe.empty()
    
    def or_else(self, default: T) -> T:
        return self._value if self.is_present() else default
    
    def __str__(self) -> str:
        return f"Maybe({self._value})"

# Either 모나드
class Either(Generic[E, T]):
    """Either 모나드 구현"""
    pass

class Left(Either[E, Any]):
    """Either의 왼쪽(에러) 케이스"""
    def __init__(self, error: E):
        self._error = error
    
    def map(self, _: Callable[[Any], Any]) -> 'Left[E, Any]':
        return self
    
    def flat_map(self, _: Callable[[Any], Either[E, Any]]) -> 'Left[E, Any]':
        return self
    
    def get_error(self) -> E:
        return self._error
    
    def __str__(self) -> str:
        return f"Left({self._error})"

class Right(Either[Any, T]):
    """Either의 오른쪽(성공) 케이스"""
    def __init__(self, value: T):
        self._value = value
    
    def map(self, func: Callable[[T], R]) -> Either[Any, R]:
        return Right(func(self._value))
    
    def flat_map(self, func: Callable[[T], Either[E, R]]) -> Either[E, R]:
        return func(self._value)
    
    def get(self) -> T:
        return self._value
    
    def __str__(self) -> str:
        return f"Right({self._value})"

# IO 모나드
class IO(Generic[T]):
    """IO 모나드 구현"""
    def __init__(self, effect: Callable[[], T]):
        self._effect = effect
    
    @staticmethod
    def of(value: T) -> 'IO[T]':
        return IO(lambda: value)
    
    def map(self, func: Callable[[T], R]) -> 'IO[R]':
        return IO(lambda: func(self._effect()))
    
    def flat_map(self, func: Callable[[T], 'IO[R]']) -> 'IO[R]':
        return IO(lambda: func(self._effect()).unsafe_perform_io())
    
    def unsafe_perform_io(self) -> T:
        return self._effect()

# 함수형 패턴 예제
class Validation(Generic[E, T]):
    """검증 결과를 나타내는 타입"""
    def __init__(self, errors: List[E], value: Optional[T] = None):
        self._errors = errors
        self._value = value
    
    @staticmethod
    def success(value: T) -> 'Validation[E, T]':
        return Validation([], value)
    
    @staticmethod
    def failure(error: E) -> 'Validation[E, T]':
        return Validation([error])
    
    def is_success(self) -> bool:
        return len(self._errors) == 0
    
    def map(self, func: Callable[[T], R]) -> 'Validation[E, R]':
        if self.is_success():
            return Validation.success(func(self._value))
        return Validation(self._errors)
    
    def get_errors(self) -> List[E]:
        return self._errors
    
    def get_value(self) -> Optional[T]:
        return self._value

# 실제 사용 예제
def divide(a: float, b: float) -> Either[str, float]:
    """나눗셈 연산을 Either 모나드로 감싸기"""
    try:
        if b == 0:
            return Left("Division by zero")
        return Right(a / b)
    except Exception as e:
        return Left(str(e))

def safe_get_config(config: dict, key: str) -> Maybe[str]:
    """설정값을 안전하게 가져오기"""
    return Maybe.of(config.get(key))

def read_file(path: str) -> IO[str]:
    """파일 읽기를 IO 모나드로 감싸기"""
    return IO(lambda: open(path).read())

def validate_user(name: str, age: int) -> Validation[str, dict]:
    """사용자 데이터 검증"""
    errors = []
    if not name:
        errors.append("Name cannot be empty")
    if age < 0:
        errors.append("Age cannot be negative")
    
    if errors:
        return Validation(errors)
    return Validation.success({"name": name, "age": age})

def demonstrate_maybe_monad():
    print("\nMaybe Monad Demonstration:")
    config = {"host": "localhost", "port": "8080"}
    
    # Maybe 모나드를 사용한 안전한 설정값 접근
    port = (safe_get_config(config, "port")
            .map(int)
            .map(lambda x: x + 1)
            .or_else(8080))
    
    print(f"Port: {port}")
    
    # 존재하지 않는 설정값 접근
    debug = (safe_get_config(config, "debug")
             .map(bool)
             .or_else(False))
    
    print(f"Debug mode: {debug}")

def demonstrate_either_monad():
    print("\nEither Monad Demonstration:")
    # Either 모나드를 사용한 에러 처리
    result1 = divide(10, 2)
    result2 = divide(10, 0)
    
    print(f"10 / 2 = {result1}")
    print(f"10 / 0 = {result2}")
    
    # 체이닝 연산
    result3 = (Right(10)
               .map(lambda x: x * 2)
               .flat_map(lambda x: divide(x, 4)))
    
    print(f"Chain result: {result3}")

def demonstrate_validation():
    print("\nValidation Pattern Demonstration:")
    # 유효한 데이터 검증
    valid_result = validate_user("John", 25)
    print(f"Valid user: {valid_result.get_value() if valid_result.is_success() else valid_result.get_errors()}")
    
    # 잘못된 데이터 검증
    invalid_result = validate_user("", -5)
    print(f"Invalid user errors: {invalid_result.get_errors()}")

def main():
    print("Monads and Functional Patterns Demonstrations")
    
    demonstrate_maybe_monad()
    demonstrate_either_monad()
    demonstrate_validation()

if __name__ == "__main__":
    main()

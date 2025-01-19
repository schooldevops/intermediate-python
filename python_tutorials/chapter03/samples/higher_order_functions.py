"""
파이썬의 고차 함수와 데코레이터 예제
이 예제는 함수를 인자로 받거나 함수를 반환하는 고차 함수와 데코레이터의 활용을 보여줍니다.
"""

from typing import Callable, List, Any, TypeVar, Dict
from functools import wraps
import time
import logging
from datetime import datetime

# 타입 변수 정의
T = TypeVar('T')
R = TypeVar('R')

# 기본 고차 함수 예제
def apply_twice(f: Callable[[T], T], x: T) -> T:
    """함수를 두 번 적용하는 고차 함수"""
    return f(f(x))

def create_multiplier(factor: int) -> Callable[[int], int]:
    """곱셈 함수를 반환하는 고차 함수"""
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

# 함수 합성 예제
def compose(f: Callable[[T], R], g: Callable[[Any], T]) -> Callable[[Any], R]:
    """두 함수를 합성하는 고차 함수"""
    return lambda x: f(g(x))

# 커링 예제
def curry_function(func: Callable) -> Callable:
    """함수를 커리화하는 고차 함수"""
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return lambda *more_args, **more_kwargs: curried(
            *(args + more_args),
            **{**kwargs, **more_kwargs}
        )
    return curried

# 데코레이터 예제
def timer_decorator(func: Callable) -> Callable:
    """함수의 실행 시간을 측정하는 데코레이터"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

def retry_decorator(max_attempts: int, delay: float = 1.0) -> Callable:
    """실패 시 재시도하는 데코레이터"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def validate_args(**validators: Callable) -> Callable:
    """함수 인자를 검증하는 데코레이터"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 위치 인자를 키워드 인자로 변환
            bound_args = func.__code__.co_varnames[:func.__code__.co_argcount]
            all_args = {**dict(zip(bound_args, args)), **kwargs}
            
            # 각 인자 검증
            for param, validator in validators.items():
                if param in all_args:
                    value = all_args[param]
                    if not validator(value):
                        raise ValueError(
                            f"Invalid value for parameter {param}: {value}"
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 실제 사용 예제
@timer_decorator
def slow_function(n: int) -> int:
    """시간이 걸리는 함수"""
    time.sleep(n)
    return n * n

@retry_decorator(max_attempts=3)
def unreliable_function() -> str:
    """가끔 실패하는 함수"""
    if time.time() % 2 > 1:
        raise ConnectionError("Random failure")
    return "Success!"

@validate_args(age=lambda x: 0 <= x <= 150, name=lambda x: len(x) > 0)
def create_user(name: str, age: int) -> Dict[str, Any]:
    """사용자 정보를 생성하는 함수"""
    return {"name": name, "age": age}

def demonstrate_higher_order_functions():
    print("\nHigher-Order Functions Demonstration:")
    # apply_twice 예제
    double = lambda x: x * 2
    print(f"Applying double twice to 3: {apply_twice(double, 3)}")
    
    # create_multiplier 예제
    triple = create_multiplier(3)
    print(f"Triple 4: {triple(4)}")
    
    # 함수 합성 예제
    add_one = lambda x: x + 1
    square = lambda x: x * x
    square_then_add_one = compose(add_one, square)
    print(f"Square 3 then add one: {square_then_add_one(3)}")

def demonstrate_currying():
    print("\nCurrying Demonstration:")
    @curry_function
    def add_three_numbers(a: int, b: int, c: int) -> int:
        return a + b + c
    
    # 다양한 방식으로 호출
    print(f"Normal call: {add_three_numbers(1, 2, 3)}")
    print(f"Curried call: {add_three_numbers(1)(2)(3)}")
    print(f"Partial call: {add_three_numbers(1, 2)(3)}")

def demonstrate_decorators():
    print("\nDecorators Demonstration:")
    # timer_decorator 예제
    result = slow_function(1)
    print(f"Slow function result: {result}")
    
    # retry_decorator 예제
    try:
        result = unreliable_function()
        print(f"Unreliable function result: {result}")
    except ConnectionError as e:
        print(f"Final failure: {e}")
    
    # validate_args 예제
    try:
        user = create_user("John", 30)
        print(f"Valid user created: {user}")
        
        # 잘못된 데이터로 시도
        user = create_user("", -5)
    except ValueError as e:
        print(f"Validation error: {e}")

def main():
    print("Higher-Order Functions and Decorators Demonstrations")
    
    demonstrate_higher_order_functions()
    demonstrate_currying()
    demonstrate_decorators()

if __name__ == "__main__":
    main()

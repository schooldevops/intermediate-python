"""
파이썬의 일급 객체로서의 함수를 설명하는 예제
이 예제는 함수를 변수에 할당하고, 인자로 전달하며, 반환값으로 사용하는 방법을 보여줍니다.
"""

from typing import Callable, List, Any

def create_multiplier(factor: int) -> Callable[[int], int]:
    """
    주어진 factor로 숫자를 곱하는 함수를 반환합니다.
    """
    def multiplier(x: int) -> int:
        return x * factor
    return multiplier

def apply_operation(numbers: List[int], operation: Callable[[int], int]) -> List[int]:
    """
    리스트의 각 요소에 주어진 operation을 적용합니다.
    """
    return [operation(num) for num in numbers]

def create_logger(prefix: str) -> Callable[..., None]:
    """
    로깅 함수를 생성하여 반환합니다.
    """
    def logger(*args: Any) -> None:
        print(f"{prefix}:", *args)
    return logger

def demonstrate_function_assignment():
    print("\nFunction Assignment Demonstration:")
    # 함수를 변수에 할당
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"Double 5: {double(5)}")  # 10
    print(f"Triple 5: {triple(5)}")  # 15

def demonstrate_function_as_argument():
    print("\nFunction as Argument Demonstration:")
    numbers = [1, 2, 3, 4, 5]
    double = create_multiplier(2)
    
    # 함수를 인자로 전달
    doubled_numbers = apply_operation(numbers, double)
    print(f"Original numbers: {numbers}")
    print(f"Doubled numbers: {doubled_numbers}")

def demonstrate_function_factories():
    print("\nFunction Factory Demonstration:")
    # 다양한 로거 생성
    debug_logger = create_logger("DEBUG")
    error_logger = create_logger("ERROR")
    
    debug_logger("Debug message")
    error_logger("Error message")

def higher_order_function_example():
    print("\nHigher Order Function Demonstration:")
    def compose(f: Callable, g: Callable) -> Callable:
        """두 함수를 합성하는 고차 함수"""
        return lambda x: f(g(x))
    
    def square(x: int) -> int:
        return x * x
    
    def add_one(x: int) -> int:
        return x + 1
    
    # 함수 합성: (x^2 + 1)
    square_then_add = compose(add_one, square)
    # 함수 합성: ((x + 1)^2)
    add_then_square = compose(square, add_one)
    
    x = 5
    print(f"square_then_add({x}) = {square_then_add(x)}")
    print(f"add_then_square({x}) = {add_then_square(x)}")

def main():
    print("First-Class Functions Demonstration")
    demonstrate_function_assignment()
    demonstrate_function_as_argument()
    demonstrate_function_factories()
    higher_order_function_example()

if __name__ == "__main__":
    main()

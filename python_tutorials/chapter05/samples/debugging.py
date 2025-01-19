import logging
import functools
import time
import traceback
from typing import Any, Callable
import pdb

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 디버깅 데코레이터
def debug_function(func: Callable) -> Callable:
    """함수의 입력과 출력을 로깅하는 데코레이터"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"함수 '{func.__name__}' 호출")
        logger.debug(f"인자: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.debug(f"반환값: {result}")
            return result
        except Exception as e:
            logger.error(f"예외 발생: {str(e)}")
            logger.error(f"스택 트레이스:\n{traceback.format_exc()}")
            raise
    return wrapper

def performance_log(func: Callable) -> Callable:
    """함수의 실행 시간을 측정하는 데코레이터"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"함수 '{func.__name__}' 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

class ComplexCalculator:
    def __init__(self):
        self.cache = {}
    
    @debug_function
    def fibonacci(self, n: int) -> int:
        """피보나치 수열의 n번째 값을 계산"""
        if n < 0:
            raise ValueError("음수는 계산할 수 없습니다")
        
        if n in self.cache:
            logger.debug(f"캐시된 값 사용: fib({n})")
            return self.cache[n]
        
        if n <= 1:
            return n
        
        logger.debug(f"fib({n}) 계산 중...")
        result = self.fibonacci(n-1) + self.fibonacci(n-2)
        self.cache[n] = result
        return result
    
    @performance_log
    def complex_operation(self, x: float, y: float) -> float:
        """시간이 걸리는 복잡한 연산을 시뮬레이션"""
        logger.info(f"복잡한 연산 시작: x={x}, y={y}")
        time.sleep(0.1)  # 복잡한 연산 시뮬레이션
        result = (x ** 2 + y ** 2) ** 0.5
        logger.info(f"연산 결과: {result}")
        return result

def interactive_debugging_example():
    """대화형 디버깅 예제"""
    calculator = ComplexCalculator()
    numbers = [1, 2, 3, 4, 5]
    
    # 브레이크포인트 설정
    pdb.set_trace()
    
    total = 0
    for num in numbers:
        # 피보나치 수열 계산
        fib = calculator.fibonacci(num)
        # 복잡한 연산 수행
        result = calculator.complex_operation(fib, num)
        total += result
    
    return total

def main():
    try:
        # 기본 로깅 예제
        logger.debug("디버그 메시지")
        logger.info("정보 메시지")
        logger.warning("경고 메시지")
        
        # 계산기 객체 생성
        calculator = ComplexCalculator()
        
        # 피보나치 수열 계산
        for i in range(5):
            result = calculator.fibonacci(i)
            logger.info(f"fibonacci({i}) = {result}")
        
        # 복잡한 연산 수행
        calculator.complex_operation(3.14, 2.71)
        
        # 잘못된 입력으로 예외 발생
        calculator.fibonacci(-1)
    
    except Exception as e:
        logger.error(f"프로그램 실행 중 오류 발생: {str(e)}")
        logger.error(traceback.format_exc())
    
    # 대화형 디버깅 예제 실행
    # interactive_debugging_example()

if __name__ == '__main__':
    main()

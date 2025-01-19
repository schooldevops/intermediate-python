import cProfile
import pstats
import time
from memory_profiler import profile

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

@profile
def memory_intensive_function():
    # 메모리를 많이 사용하는 작업 시뮬레이션
    large_list = [i ** 2 for i in range(1000000)]
    return sum(large_list)

def time_comparison():
    n = 30
    
    # 재귀 버전 시간 측정
    start = time.time()
    fibonacci_recursive(n)
    recursive_time = time.time() - start
    
    # 반복 버전 시간 측정
    start = time.time()
    fibonacci_iterative(n)
    iterative_time = time.time() - start
    
    print(f"재귀 버전 실행 시간: {recursive_time:.4f}초")
    print(f"반복 버전 실행 시간: {iterative_time:.4f}초")

def main():
    # cProfile을 사용한 성능 프로파일링
    profiler = cProfile.Profile()
    profiler.enable()
    
    # 성능을 측정할 코드
    fibonacci_recursive(30)
    
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('cumulative')
    stats.print_stats()
    
    # 시간 비교
    time_comparison()
    
    # 메모리 사용량 측정
    memory_intensive_function()

if __name__ == "__main__":
    main()

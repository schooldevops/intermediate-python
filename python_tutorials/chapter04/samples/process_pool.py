from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
import time
import os

def cpu_bound_task(n):
    """CPU 집약적인 작업을 시뮬레이션하는 함수"""
    print(f"작업 시작 (PID: {os.getpid()}): {n}")
    result = sum(i * i for i in range(n))
    time.sleep(1)  # 추가 작업 시뮬레이션
    print(f"작업 완료 (PID: {os.getpid()}): {n}")
    return result

def process_pool_executor_example():
    """ProcessPoolExecutor를 사용한 병렬 처리 예제"""
    numbers = [10**6, 10**5, 10**7, 10**4, 10**6]
    
    print("ProcessPoolExecutor 사용")
    with ProcessPoolExecutor(max_workers=3) as executor:
        # submit 사용
        futures = [executor.submit(cpu_bound_task, num) for num in numbers]
        for future in futures:
            result = future.result()
            print(f"결과: {result}")
        
        # map 사용
        results = list(executor.map(cpu_bound_task, numbers))
        print(f"모든 결과: {results}")

def pool_callback(result):
    """Pool의 비동기 실행 완료 시 호출되는 콜백"""
    print(f"비동기 작업 완료, 결과: {result}")

def multiprocessing_pool_example():
    """multiprocessing.Pool을 사용한 병렬 처리 예제"""
    numbers = [10**6, 10**5, 10**7, 10**4, 10**6]
    
    print("\nmultiprocessing.Pool 사용")
    with mp.Pool(processes=3) as pool:
        # apply_async 사용
        for num in numbers:
            pool.apply_async(cpu_bound_task, (num,), callback=pool_callback)
        
        # 모든 비동기 작업이 완료될 때까지 대기
        pool.close()
        pool.join()
        
        # map 사용
        results = pool.map(cpu_bound_task, numbers)
        print(f"map 결과: {results}")

def main():
    process_pool_executor_example()
    multiprocessing_pool_example()

if __name__ == '__main__':
    main()

from concurrent.futures import ThreadPoolExecutor
import threading
import time
import random

def process_item(item):
    """시간이 걸리는 작업을 시뮬레이션하는 함수"""
    thread_name = threading.current_thread().name
    print(f"{thread_name} - 작업 시작: {item}")
    time.sleep(random.uniform(0.5, 2))  # 랜덤한 시간 동안 작업
    result = item * item
    print(f"{thread_name} - 작업 완료: {item}")
    return result

def process_completed(future):
    """작업 완료 시 호출되는 콜백 함수"""
    result = future.result()
    print(f"결과 처리 완료: {result}")

def main():
    items = list(range(1, 6))  # 처리할 작업 목록
    
    # ThreadPoolExecutor를 사용한 병렬 처리
    with ThreadPoolExecutor(max_workers=3) as executor:
        print("방법 1: submit() 사용")
        futures = []
        for item in items:
            future = executor.submit(process_item, item)
            future.add_done_callback(process_completed)
            futures.append(future)
        
        # 모든 작업 완료 대기
        for future in futures:
            future.result()
        
        print("\n방법 2: map() 사용")
        results = list(executor.map(process_item, items))
        print(f"모든 결과: {results}")

if __name__ == "__main__":
    main()

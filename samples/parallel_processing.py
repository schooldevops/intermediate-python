import threading
import multiprocessing
import time
import queue
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# 스레딩 예제
class ThreadingExample:
    def __init__(self):
        self.data = queue.Queue()
    
    def producer(self, items):
        for item in items:
            time.sleep(0.5)  # 작업 시뮬레이션
            self.data.put(item)
            print(f"생산: {item}")
    
    def consumer(self):
        while True:
            try:
                item = self.data.get(timeout=2)
                time.sleep(0.3)  # 작업 시뮬레이션
                print(f"소비: {item}")
                self.data.task_done()
            except queue.Empty:
                break
    
    def run_threading_example(self):
        items = list(range(5))
        
        # 스레드 생성
        producer_thread = threading.Thread(
            target=self.producer, args=(items,))
        consumer_thread = threading.Thread(
            target=self.consumer)
        
        # 스레드 시작
        producer_thread.start()
        consumer_thread.start()
        
        # 스레드 종료 대기
        producer_thread.join()
        consumer_thread.join()

# 멀티프로세싱 예제
def cpu_bound_task(n):
    """CPU 집약적인 작업 시뮬레이션"""
    count = 0
    for i in range(n):
        count += i * i
    return count

def run_multiprocessing_example():
    numbers = [10**6, 10**6, 10**6, 10**6]
    
    # 순차 실행
    start_time = time.time()
    results = [cpu_bound_task(n) for n in numbers]
    print(f"순차 실행 시간: {time.time() - start_time:.2f}초")
    
    # 멀티프로세싱 실행
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_bound_task, numbers))
    print(f"멀티프로세싱 실행 시간: {time.time() - start_time:.2f}초")

# ThreadPoolExecutor 예제
def io_bound_task(url):
    """I/O 작업 시뮬레이션"""
    time.sleep(1)  # 네트워크 요청 시뮬레이션
    return f"데이터 다운로드 완료: {url}"

def run_thread_pool_example():
    urls = [
        "http://example.com/1",
        "http://example.org/2",
        "http://example.net/3",
        "http://example.io/4"
    ]
    
    # ThreadPoolExecutor 사용
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(io_bound_task, url) for url in urls]
        for future in futures:
            print(future.result())
    print(f"스레드 풀 실행 시간: {time.time() - start_time:.2f}초")

if __name__ == "__main__":
    # 스레딩 예제 실행
    print("스레딩 예제 실행:")
    threading_example = ThreadingExample()
    threading_example.run_threading_example()
    
    print("\n멀티프로세싱 예제 실행:")
    run_multiprocessing_example()
    
    print("\n스레드 풀 예제 실행:")
    run_thread_pool_example()

"""
파이썬의 스레딩과 GIL에 대한 예제
이 예제는 스레드의 기본 사용법, 동기화 메커니즘, 그리고 GIL의 영향을 보여줍니다.
"""

import threading
import queue
import time
import random
from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from threading import Lock, Event, Condition, Semaphore

# 기본 스레드 예제
class CounterThread(threading.Thread):
    def __init__(self, name: str, count: int):
        super().__init__()
        self.name = name
        self.count = count
    
    def run(self):
        for i in range(self.count):
            print(f"Thread {self.name}: count {i}")
            time.sleep(0.1)

# 스레드 동기화 예제
class SharedCounter:
    def __init__(self):
        self._counter = 0
        self._lock = Lock()
    
    def increment(self):
        with self._lock:
            current = self._counter
            time.sleep(0.0001)  # 경쟁 상태 시뮬레이션
            self._counter = current + 1
    
    @property
    def value(self) -> int:
        return self._counter

# 생산자-소비자 패턴
@dataclass
class Task:
    id: int
    data: str

class ProducerConsumer:
    def __init__(self, queue_size: int = 5):
        self.queue: queue.Queue = queue.Queue(maxsize=queue_size)
        self.stop_event = Event()
    
    def producer(self):
        task_id = 0
        while not self.stop_event.is_set():
            try:
                task = Task(task_id, f"Task data {task_id}")
                self.queue.put(task, timeout=1)
                print(f"Produced task {task_id}")
                task_id += 1
                time.sleep(random.uniform(0.1, 0.5))
            except queue.Full:
                print("Queue is full, waiting...")
    
    def consumer(self, name: str):
        while not self.stop_event.is_set() or not self.queue.empty():
            try:
                task = self.queue.get(timeout=1)
                print(f"Consumer {name} processing task {task.id}")
                time.sleep(random.uniform(0.2, 0.7))
                self.queue.task_done()
            except queue.Empty:
                print(f"Consumer {name} waiting for tasks...")
    
    def run(self, num_consumers: int = 2, duration: int = 5):
        # 생산자 스레드 시작
        producer_thread = threading.Thread(target=self.producer)
        producer_thread.start()
        
        # 소비자 스레드들 시작
        consumer_threads = []
        for i in range(num_consumers):
            thread = threading.Thread(target=self.consumer, args=(f"Consumer-{i}",))
            thread.start()
            consumer_threads.append(thread)
        
        # 지정된 시간 동안 실행
        time.sleep(duration)
        self.stop_event.set()
        
        # 모든 스레드 종료 대기
        producer_thread.join()
        for thread in consumer_threads:
            thread.join()

# ThreadPoolExecutor 예제
class BatchProcessor:
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
    
    def process_item(self, item: int) -> int:
        time.sleep(0.1)  # 작업 시뮬레이션
        return item * item
    
    def process_batch(self, items: List[int]) -> List[int]:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self.process_item, items))
        return results

def demonstrate_basic_threading():
    print("\nBasic Threading Demonstration:")
    threads = [
        CounterThread("A", 3),
        CounterThread("B", 3)
    ]
    
    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()

def demonstrate_thread_synchronization():
    print("\nThread Synchronization Demonstration:")
    counter = SharedCounter()
    threads = []
    
    for _ in range(10):
        thread = threading.Thread(target=counter.increment)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"Final counter value: {counter.value}")

def demonstrate_producer_consumer():
    print("\nProducer-Consumer Pattern Demonstration:")
    pc = ProducerConsumer()
    pc.run(num_consumers=2, duration=3)

def demonstrate_thread_pool():
    print("\nThreadPool Demonstration:")
    processor = BatchProcessor()
    items = list(range(10))
    results = processor.process_batch(items)
    print(f"Processed results: {results}")

def main():
    print("Threading and GIL Demonstrations")
    
    demonstrate_basic_threading()
    demonstrate_thread_synchronization()
    demonstrate_producer_consumer()
    demonstrate_thread_pool()

if __name__ == "__main__":
    main()

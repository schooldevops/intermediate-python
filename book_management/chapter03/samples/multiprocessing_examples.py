"""
파이썬의 멀티프로세싱 예제
이 예제는 프로세스 생성, 프로세스 간 통신, 공유 상태 관리 등을 보여줍니다.
"""

import multiprocessing as mp
from multiprocessing import Process, Queue, Pipe, Value, Array, Lock, Pool
import time
import random
import os
from typing import List, Tuple, Any
from dataclasses import dataclass

# 기본 프로세스 예제
def worker_function(name: str):
    """기본 작업자 프로세스 함수"""
    print(f"Worker {name} starting (PID: {os.getpid()})")
    time.sleep(random.random())
    print(f"Worker {name} finished")

# CPU 집약적 작업 예제
def cpu_intensive_task(n: int) -> int:
    """CPU 집약적인 작업을 시뮬레이션"""
    count = 0
    for i in range(n):
        count += sum(i * i for i in range(1000))
    return count

# 프로세스 간 통신 예제
@dataclass
class WorkItem:
    id: int
    data: Any

def producer(queue: Queue):
    """작업 항목을 생성하여 큐에 추가"""
    for i in range(5):
        item = WorkItem(i, f"Data-{i}")
        queue.put(item)
        print(f"Produced: {item}")
        time.sleep(random.random())
    queue.put(None)  # 종료 신호

def consumer(queue: Queue):
    """큐에서 작업 항목을 가져와 처리"""
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consumed: {item}")
        time.sleep(random.random())

# 파이프 통신 예제
def pipe_sender(conn, msgs: List[str]):
    """파이프를 통해 메시지 전송"""
    for msg in msgs:
        conn.send(msg)
        time.sleep(random.random())
    conn.send(None)
    conn.close()

def pipe_receiver(conn):
    """파이프에서 메시지 수신"""
    while True:
        msg = conn.recv()
        if msg is None:
            break
        print(f"Received: {msg}")

# 공유 메모리 예제
class SharedCounter:
    def __init__(self):
        self.val = Value('i', 0)
        self.lock = Lock()
        
    def increment(self, n: int):
        with self.lock:
            for _ in range(n):
                self.val.value += 1
    
    @property
    def value(self) -> int:
        return self.val.value

# 프로세스 풀 예제
def process_chunk(chunk: List[int]) -> int:
    """데이터 청크를 처리"""
    return sum(x * x for x in chunk)

class DataProcessor:
    def __init__(self, num_processes: int = None):
        self.num_processes = num_processes or mp.cpu_count()
    
    def process_data(self, data: List[int]) -> int:
        chunk_size = len(data) // self.num_processes
        chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
        
        with Pool(processes=self.num_processes) as pool:
            results = pool.map(process_chunk, chunks)
        
        return sum(results)

def demonstrate_basic_processes():
    print("\nBasic Process Demonstration:")
    processes = []
    for i in range(3):
        p = Process(target=worker_function, args=(f"Worker-{i}",))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

def demonstrate_process_communication():
    print("\nProcess Communication Demonstration:")
    # 큐를 사용한 통신
    q = Queue()
    prod = Process(target=producer, args=(q,))
    cons = Process(target=consumer, args=(q,))
    
    prod.start()
    cons.start()
    prod.join()
    cons.join()
    
    # 파이프를 사용한 통신
    parent_conn, child_conn = Pipe()
    messages = ["Hello", "World", "From", "Pipe"]
    
    sender = Process(target=pipe_sender, args=(parent_conn, messages))
    receiver = Process(target=pipe_receiver, args=(child_conn,))
    
    sender.start()
    receiver.start()
    sender.join()
    receiver.join()

def demonstrate_shared_memory():
    print("\nShared Memory Demonstration:")
    counter = SharedCounter()
    processes = []
    
    for _ in range(4):
        p = Process(target=counter.increment, args=(100,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    print(f"Final counter value: {counter.value}")

def demonstrate_process_pool():
    print("\nProcess Pool Demonstration:")
    processor = DataProcessor()
    data = list(range(1000000))
    
    start_time = time.time()
    result = processor.process_data(data)
    end_time = time.time()
    
    print(f"Result: {result}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

def main():
    print("Multiprocessing Demonstrations")
    print(f"Main process PID: {os.getpid()}")
    
    demonstrate_basic_processes()
    demonstrate_process_communication()
    demonstrate_shared_memory()
    demonstrate_process_pool()

if __name__ == "__main__":
    main()

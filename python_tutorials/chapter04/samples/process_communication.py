import multiprocessing as mp
import time
import random

def producer(queue):
    """데이터를 생성하여 큐에 넣는 프로세스"""
    for i in range(5):
        item = random.randint(1, 100)
        queue.put(item)
        print(f"생산: {item}")
        time.sleep(random.random())
    queue.put(None)  # 종료 신호

def consumer(queue):
    """큐에서 데이터를 가져와 처리하는 프로세스"""
    while True:
        item = queue.get()
        if item is None:  # 종료 신호 확인
            break
        print(f"소비: {item}")
        time.sleep(random.random())

def pipe_worker(conn, name):
    """파이프를 통해 통신하는 프로세스"""
    for i in range(3):
        msg = f"메시지 from {name}: {i}"
        conn.send(msg)
        print(f"전송: {msg}")
        if conn.poll():  # 수신할 데이터가 있는지 확인
            print(f"수신: {conn.recv()}")
        time.sleep(random.random())
    conn.close()

def main():
    # Queue를 사용한 통신
    print("Queue 예제 시작")
    queue = mp.Queue()
    
    # 생산자와 소비자 프로세스 생성
    prod = mp.Process(target=producer, args=(queue,))
    cons = mp.Process(target=consumer, args=(queue,))
    
    prod.start()
    cons.start()
    prod.join()
    cons.join()
    
    # Pipe를 사용한 통신
    print("\nPipe 예제 시작")
    conn1, conn2 = mp.Pipe()
    
    # 두 프로세스 생성
    p1 = mp.Process(target=pipe_worker, args=(conn1, "Process-1"))
    p2 = mp.Process(target=pipe_worker, args=(conn2, "Process-2"))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()

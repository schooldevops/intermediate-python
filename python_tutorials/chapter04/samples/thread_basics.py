import threading
import time

def worker(thread_name, sleep_time):
    """작업을 수행하는 스레드 함수"""
    print(f"{thread_name} 시작")
    time.sleep(sleep_time)
    print(f"{thread_name} 종료")

def main():
    # 일반 스레드 생성
    thread1 = threading.Thread(target=worker, args=("Thread-1", 2))
    
    # 데몬 스레드 생성
    thread2 = threading.Thread(target=worker, args=("Thread-2", 3), daemon=True)
    
    # 스레드 시작
    thread1.start()
    thread2.start()
    
    # 메인 스레드에서 작업
    print("메인 스레드 작업 중...")
    
    # 일반 스레드가 종료될 때까지 대기
    thread1.join()
    
    # 데몬 스레드는 메인 스레드가 종료되면 함께 종료됨
    print("프로그램 종료")

if __name__ == "__main__":
    main()

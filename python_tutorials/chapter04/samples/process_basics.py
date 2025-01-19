import multiprocessing as mp
import time
import os

def worker(name):
    """작업을 수행하는 프로세스 함수"""
    print(f"프로세스 {name} 시작 (PID: {os.getpid()})")
    time.sleep(2)
    print(f"프로세스 {name} 종료 (PID: {os.getpid()})")

class WorkerProcess(mp.Process):
    """프로세스 클래스를 상속받은 사용자 정의 프로세스"""
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(f"사용자 정의 프로세스 {self.name} 시작 (PID: {os.getpid()})")
        time.sleep(3)
        print(f"사용자 정의 프로세스 {self.name} 종료 (PID: {os.getpid()})")

def main():
    print(f"메인 프로세스 시작 (PID: {os.getpid()})")
    
    # 일반 프로세스 생성
    process1 = mp.Process(target=worker, args=('Process-1',))
    
    # 사용자 정의 프로세스 생성
    process2 = WorkerProcess('Process-2')
    
    # 프로세스 시작
    process1.start()
    process2.start()
    
    # 프로세스 종료 대기
    process1.join()
    process2.join()
    
    print(f"메인 프로세스 종료 (PID: {os.getpid()})")

if __name__ == '__main__':
    main()

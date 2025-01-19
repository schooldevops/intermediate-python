import threading
import time
import random

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
        
    def withdraw(self, amount):
        """출금 작업 - Lock을 사용한 동기화"""
        with self.lock:
            if self.balance >= amount:
                time.sleep(0.1)  # 트랜잭션 처리 시간 시뮬레이션
                self.balance -= amount
                return True
            return False
            
    def deposit(self, amount):
        """입금 작업 - Lock을 사용한 동기화"""
        with self.lock:
            time.sleep(0.1)  # 트랜잭션 처리 시간 시뮬레이션
            self.balance += amount
            return True

def perform_transactions(account):
    """여러 거래를 수행하는 함수"""
    for _ in range(5):
        if random.random() < 0.5:
            amount = random.randint(1, 100)
            if account.withdraw(amount):
                print(f"출금: {amount}, 잔액: {account.balance}")
        else:
            amount = random.randint(1, 100)
            if account.deposit(amount):
                print(f"입금: {amount}, 잔액: {account.balance}")
        time.sleep(random.random())

def main():
    # 계좌 생성
    account = BankAccount(1000)
    print(f"초기 잔액: {account.balance}")
    
    # 여러 스레드에서 거래 실행
    threads = []
    for i in range(3):
        thread = threading.Thread(target=perform_transactions, args=(account,))
        threads.append(thread)
        thread.start()
    
    # 모든 스레드 종료 대기
    for thread in threads:
        thread.join()
    
    print(f"최종 잔액: {account.balance}")

if __name__ == "__main__":
    main()

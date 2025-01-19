class BankAccount:
    def __init__(self, owner, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("초기 잔액은 음수가 될 수 없습니다")
        self._owner = owner    # protected 변수
        self.__balance = initial_balance  # private 변수
    
    @property
    def owner(self):
        return self._owner
        
    @property 
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        self.__validate_amount(amount)
        self.__balance = amount
        
    def deposit(self, amount):
        self.__validate_amount(amount)
        self.__balance += amount
        return self.__get_balance_message()
        
    def withdraw(self, amount):
        self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("잔액이 부족합니다")
        self.__balance -= amount
        return self.__get_balance_message()
        
    def __validate_amount(self, amount):
        if amount < 0:
            raise ValueError("금액은 음수가 될 수 없습니다")
            
    def __get_balance_message(self):
        return f"현재 잔액: {self.__balance}원"

def main():
    # 기본 테스트
    try:
        # 계좌 생성 테스트
        account = BankAccount("홍길동", 10000)
        print(f"계좌 소유자: {account.owner}")
        print(f"초기 잔액: {account.balance}원")
        
        # 잔액 변경 테스트
        account.balance = 20000
        print(f"잔액 변경 후: {account.balance}원")
        
        # 입금 테스트
        print(account.deposit(5000))
        
        # 출금 테스트
        print(account.withdraw(3000))
        
        # 에러 테스트
        print("\n--- 에러 테스트 ---")
        
        # 음수 입금 시도
        print("음수 입금 시도:")
        account.deposit(-1000)
    except ValueError as e:
        print(f"예상된 에러 발생: {e}")
        
    try:
        # 잔액 초과 출금 시도
        print("\n잔액 초과 출금 시도:")
        account.withdraw(1000000)
    except ValueError as e:
        print(f"예상된 에러 발생: {e}")

if __name__ == "__main__":
    main() 
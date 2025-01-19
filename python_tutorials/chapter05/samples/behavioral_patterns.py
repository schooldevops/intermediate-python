from abc import ABC, abstractmethod
from typing import List, Dict

# 옵저버 패턴
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        self._observers.append(observer)
    
    def detach(self, observer: Observer):
        self._observers.remove(observer)
    
    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

class NewsAgency(Subject):
    def publish_news(self, news: str):
        self.notify(news)

class NewsSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, message: str):
        print(f"{self.name}이(가) 뉴스를 받았습니다: {message}")

# 전략 패턴
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: int) -> str:
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"신용카드로 {amount}원 결제"

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: int) -> str:
        return f"계좌이체로 {amount}원 결제"

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def execute_payment(self, amount: int) -> str:
        return self.strategy.pay(amount)

# 상태 패턴
class State(ABC):
    @abstractmethod
    def handle(self) -> str:
        pass

class OrderState(State):
    def handle(self) -> str:
        return "주문 완료"

class ShippingState(State):
    def handle(self) -> str:
        return "배송 중"

class DeliveredState(State):
    def handle(self) -> str:
        return "배송 완료"

class Order:
    def __init__(self):
        self.state = OrderState()
    
    def set_state(self, state: State):
        self.state = state
    
    def get_status(self) -> str:
        return self.state.handle()

# 템플릿 메서드 패턴
class DataMiner(ABC):
    def mine(self) -> str:
        data = self._extract()
        processed_data = self._transform(data)
        return self._load(processed_data)
    
    @abstractmethod
    def _extract(self) -> str:
        pass
    
    @abstractmethod
    def _transform(self, data: str) -> str:
        pass
    
    def _load(self, data: str) -> str:
        return f"데이터 저장: {data}"

class CSVDataMiner(DataMiner):
    def _extract(self) -> str:
        return "CSV 데이터 추출"
    
    def _transform(self, data: str) -> str:
        return f"{data} -> CSV 변환"

def behavioral_patterns_example():
    # 1. 옵저버 패턴 예제
    print("1. 옵저버 패턴:")
    news_agency = NewsAgency()
    subscriber1 = NewsSubscriber("구독자1")
    subscriber2 = NewsSubscriber("구독자2")
    
    news_agency.attach(subscriber1)
    news_agency.attach(subscriber2)
    news_agency.publish_news("새로운 뉴스가 있습니다!")
    
    # 2. 전략 패턴 예제
    print("\n2. 전략 패턴:")
    credit_card = PaymentContext(CreditCardPayment())
    bank_transfer = PaymentContext(BankTransferPayment())
    
    print(credit_card.execute_payment(50000))
    print(bank_transfer.execute_payment(30000))
    
    # 3. 상태 패턴 예제
    print("\n3. 상태 패턴:")
    order = Order()
    print(f"초기 상태: {order.get_status()}")
    
    order.set_state(ShippingState())
    print(f"배송 상태: {order.get_status()}")
    
    order.set_state(DeliveredState())
    print(f"최종 상태: {order.get_status()}")
    
    # 4. 템플릿 메서드 패턴 예제
    print("\n4. 템플릿 메서드 패턴:")
    csv_miner = CSVDataMiner()
    result = csv_miner.mine()
    print(result)

if __name__ == '__main__':
    behavioral_patterns_example()

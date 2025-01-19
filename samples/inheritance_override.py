class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start(self):
        return f"{self.brand} {self.model}의 시동을 겁니다"
        
    def info(self):
        return f"{self.year} {self.brand} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        
    def start(self):
        basic_start = super().start()
        return f"{basic_start} (배터리 충전량: {self.battery_capacity}%)"
        
    def charge(self):
        return f"{self.model}를 충전합니다"

def main():
    # 일반 자동차와 전기차 객체 생성
    normal_car = Vehicle("Toyota", "Camry", 2022)
    electric_car = ElectricCar("Tesla", "Model 3", 2023, 85)
    
    print("=== 일반 자동차 테스트 ===")
    print(f"차량 정보: {normal_car.info()}")
    print(f"시동 걸기: {normal_car.start()}")
    
    print("\n=== 전기차 테스트 ===")
    print(f"차량 정보: {electric_car.info()}")  # 상속받은 메서드 그대로 사용
    print(f"시동 걸기: {electric_car.start()}")  # 오버라이드된 메서드
    print(f"충전하기: {electric_car.charge()}")  # ElectricCar의 고유 메서드
    
    print("\n=== 상속 관계 확인 ===")
    print(f"전기차는 Vehicle의 인스턴스인가요? {isinstance(electric_car, Vehicle)}")
    print(f"일반 자동차는 ElectricCar의 인스턴스인가요? {isinstance(normal_car, ElectricCar)}")

if __name__ == "__main__":
    main() 
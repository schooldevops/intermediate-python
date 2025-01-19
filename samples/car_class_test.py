class Car:
    # 클래스 변수
    total_cars = 0
    
    # 생성자 메서드
    def __init__(self, brand, model, year):
        # 인스턴스 변수
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        Car.total_cars += 1
    
    # 인스턴스 메서드
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        return f"현재 속도: {self.speed}km/h"
    
    def brake(self, speed_decrease):
        self.speed = max(0, self.speed - speed_decrease)
        return f"현재 속도: {self.speed}km/h"
    
    # 특수 메서드 (매직 메서드)
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

def main():
    # 객체 생성과 메서드 호출
    my_car = Car("현대", "아반떼", 2023)
    print(my_car)  # 2023 현대 아반떼
    print(my_car.accelerate(30))  # 현재 속도: 30km/h
    print(my_car.brake(10))  # 현재 속도: 20km/h
    
    # 추가 테스트
    print(f"총 자동차 수: {Car.total_cars}")
    
    # 다른 자동차 인스턴스 생성
    another_car = Car("기아", "K5", 2022)
    print(another_car)
    print(another_car.accelerate(50))
    print(f"총 자동차 수: {Car.total_cars}")

if __name__ == "__main__":
    main() 
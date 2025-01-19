class MathUtils:
    # 수학 유틸리티 클래스를 정의합니다
    pi = 3.14159  # 원주율을 클래스 변수로 정의합니다
    
    @staticmethod  # 정적 메서드 데코레이터를 사용합니다
    def is_even(number):  # 숫자가 짝수인지 확인하는 정적 메서드입니다
        return number % 2 == 0  # 2로 나눈 나머지가 0이면 짝수입니다
    
    @classmethod  # 클래스 메서드 데코레이터를 사용합니다
    def circle_area(cls, radius):  # 원의 넓이를 계산하는 클래스 메서드입니다
        return cls.pi * radius * radius  # πr² 공식을 사용하여 원의 넓이를 계산합니다
    
    @classmethod  # 클래스 메서드 데코레이터를 사용합니다
    def update_pi(cls, new_pi):  # pi 값을 업데이트하는 클래스 메서드입니다
        cls.pi = new_pi  # 클래스 변수 pi를 새로운 값으로 업데이트합니다

def main():
    # 정적 메서드 테스트
    print("=== 정적 메서드 테스트 ===")
    print(f"4는 짝수인가요? {MathUtils.is_even(4)}")  # True
    print(f"7은 짝수인가요? {MathUtils.is_even(7)}")  # False
    
    # 클래스 메서드 테스트
    print("\n=== 클래스 메서드 테스트 ===")
    print(f"현재 파이 값: {MathUtils.pi}")
    print(f"반지름이 5인 원의 넓이: {MathUtils.circle_area(5):.2f}")
    
    # pi 값 업데이트 테스트
    print("\n=== pi 값 업데이트 테스트 ===")
    MathUtils.update_pi(3.14)
    print(f"새로운 파이 값: {MathUtils.pi}")
    print(f"업데이트된 pi로 계산한 반지름이 5인 원의 넓이: {MathUtils.circle_area(5):.2f}")

if __name__ == "__main__":
    main() 
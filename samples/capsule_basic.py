class Employee:
    def __init__(self, name, salary):
        self._name = name          # protected 속성
        self.__salary = salary     # private 속성
        
    def get_salary(self):
        return self.__salary
        
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("급여는 0보다 커야 합니다")
            
    def _internal_method(self):    # protected 메서드
        return "내부 처리 로직"
        
    def __private_method(self):    # private 메서드
        return "비공개 처리 로직"

def main():
    # 직원 객체 생성
    emp = Employee("홍길동", 3000000)
    
    print("=== 기본 접근 테스트 ===")
    print(f"이름 (protected): {emp._name}")  # protected 속성 접근 가능 (권장하지 않음)
    print(f"급여 (getter 사용): {emp.get_salary()}")  # getter 메서드를 통한 접근
    
    print("\n=== 급여 변경 테스트 ===")
    emp.set_salary(3500000)  # setter 메서드를 통한 수정
    print(f"변경된 급여: {emp.get_salary()}")
    
    print("\n=== 에러 테스트 ===")
    # private 속성 직접 접근 시도
    try:
        print(emp.__salary)  # AttributeError 발생
    except AttributeError as e:
        print(f"private 속성 직접 접근 에러: {e}")
    
    # 잘못된 급여 설정 시도
    try:
        emp.set_salary(-1000)  # ValueError 발생
    except ValueError as e:
        print(f"잘못된 급여 설정 에러: {e}")
    
    print("\n=== 네임 맹글링 테스트 ===")
    # 파이썬의 네임 맹글링을 통한 private 멤버 접근 (실제로는 사용하지 말 것)
    print(f"맹글링된 이름을 통한 접근: {getattr(emp, '_Employee__salary')}")
    
    print("\n=== protected 메서드 테스트 ===")
    print(f"Protected 메서드 호출: {emp._internal_method()}")
    
    # private 메서드 호출 시도
    try:
        emp.__private_method()
    except AttributeError as e:
        print(f"Private 메서드 직접 호출 에러: {e}")

if __name__ == "__main__":
    main() 
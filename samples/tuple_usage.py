def demonstrate_function_returns():
    print("=== 함수 반환값으로서의 튜플 ===")
    
    def get_coordinates():
        return (3, 4)
    
    def get_user_info():
        return "Alice", 25, "alice@email.com"  # 괄호 없이도 튜플 반환
    
    # 튜플 언패킹으로 받기
    x, y = get_coordinates()
    print(f"좌표: x = {x}, y = {y}")
    
    # 여러 값 언패킹
    name, age, email = get_user_info()
    print(f"사용자 정보: 이름 = {name}, 나이 = {age}, 이메일 = {email}")

def demonstrate_dictionary_usage():
    print("\n=== 딕셔너리와 함께 사용하기 ===")
    
    # 딕셔너리 메서드 반환값
    user = {'name': 'Bob', 'age': 30, 'email': 'bob@email.com'}
    
    # items() 메서드는 튜플의 시퀀스 반환
    print("--- items() 메서드 사용 ---")
    for key, value in user.items():
        print(f"키: {key}, 값: {value}")
    
    # 튜플을 키로 사용
    print("\n--- 튜플을 키로 사용 ---")
    locations = {
        (0, 0): 'origin',
        (1, 0): 'right',
        (0, 1): 'up',
        (1, 1): 'diagonal'
    }
    
    print(f"원점의 위치: {locations[(0, 0)]}")
    print(f"모든 위치:")
    for coords, description in locations.items():
        print(f"좌표 {coords}: {description}")

def demonstrate_data_structure():
    print("\n=== 데이터 구조로서의 튜플 ===")
    
    # 불변 레코드로 사용
    Student = tuple[str, int, float]  # Python 3.9+ type hint
    
    def create_student(name: str, age: int, gpa: float) -> Student:
        return (name, age, gpa)
    
    def print_student(student: Student):
        name, age, gpa = student
        print(f"학생: {name}, 나이: {age}, 평점: {gpa:.2f}")
    
    # 학생 레코드 생성 및 출력
    student1 = create_student("김철수", 20, 3.8)
    student2 = create_student("이영희", 22, 4.2)
    
    print_student(student1)
    print_student(student2)

def demonstrate_swap_variables():
    print("\n=== 변수 값 교환하기 ===")
    
    # 일반적인 방법
    a = 5
    b = 10
    print(f"교환 전: a = {a}, b = {b}")
    
    # 튜플을 사용한 변수 교환
    a, b = b, a
    print(f"교환 후: a = {a}, b = {b}")

def demonstrate_extended_unpacking():
    print("\n=== 확장된 언패킹 ===")
    
    numbers = (1, 2, 3, 4, 5, 6)
    
    # 첫 번째, 마지막 요소와 나머지 분리
    first, *middle, last = numbers
    print(f"첫 번째: {first}")
    print(f"중간 값들: {middle}")
    print(f"마지막: {last}")
    
    # 앞쪽 두 개와 나머지 분리
    head1, head2, *tail = numbers
    print(f"앞쪽 두 값: {head1}, {head2}")
    print(f"나머지 값들: {tail}")

def main():
    demonstrate_function_returns()
    demonstrate_dictionary_usage()
    demonstrate_data_structure()
    demonstrate_swap_variables()
    demonstrate_extended_unpacking()

if __name__ == "__main__":
    main() 
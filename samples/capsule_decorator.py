def validate_age(func):
    def wrapper(self, age):
        if 0 <= age <= 150:
            return func(self, age)
        raise ValueError("나이는 0-150 사이여야 합니다")
    return wrapper

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = self.__validate_age(age)
        
    @property
    def name(self):
        return self.__name
        
    @property
    def age(self):
        return self.__age
        
    @age.setter
    @validate_age
    def age(self, new_age):
        self.__age = new_age
        
    def __validate_age(self, age):
        if 0 <= age <= 150:
            return age
        raise ValueError("나이는 0-150 사이여야 합니다")

def main():
    print("=== 기본 생성 테스트 ===")
    try:
        # 정상적인 나이로 생성
        person = Person("홍길동", 25)
        print(f"이름: {person.name}")
        print(f"나이: {person.age}")
    except ValueError as e:
        print(f"생성 에러: {e}")
    
    print("\n=== 나이 변경 테스트 ===")
    try:
        # 유효한 나이로 변경
        person.age = 30
        print(f"변경된 나이: {person.age}")
    except ValueError as e:
        print(f"나이 변경 에러: {e}")
    
    print("\n=== 에러 테스트 ===")
    # 잘못된 초기 나이로 생성 시도
    try:
        invalid_person = Person("김철수", 200)
    except ValueError as e:
        print(f"잘못된 초기 나이 에러: {e}")
    
    # 잘못된 나이로 변경 시도
    try:
        person.age = -5
    except ValueError as e:
        print(f"잘못된 나이 변경 에러: {e}")
    
    print("\n=== 이름 변경 시도 테스트 ===")
    try:
        person.name = "김길동"  # name은 읽기 전용 프로퍼티
    except AttributeError as e:
        print(f"이름 변경 시도 에러: {e}")
    
    print("\n=== private 속성 접근 테스트 ===")
    try:
        print(person.__name)  # private 속성 직접 접근
    except AttributeError as e:
        print(f"private 속성 접근 에러: {e}")

if __name__ == "__main__":
    main() 
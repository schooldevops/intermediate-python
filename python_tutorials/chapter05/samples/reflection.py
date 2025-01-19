import inspect
from typing import Any

class Person:
    """예제를 위한 Person 클래스"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"안녕하세요, {self.name}입니다!"

def inspect_object(obj: Any) -> None:
    """객체의 속성과 메서드를 검사하는 함수"""
    print(f"\n{obj.__class__.__name__} 객체 검사:")
    
    # 객체의 모든 속성 출력
    print("\n1. 객체 속성:")
    for attr in dir(obj):
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            print(f"- {attr}: {value}")
    
    # 메서드 정보 출력
    print("\n2. 메서드 정보:")
    for name, method in inspect.getmembers(obj, inspect.ismethod):
        if not name.startswith('__'):
            signature = inspect.signature(method)
            print(f"- {name}{signature}")
            if method.__doc__:
                print(f"  독스트링: {method.__doc__}")

def dynamic_attribute_example():
    """동적 속성 조작 예제"""
    person = Person("홍길동", 30)
    
    # 동적으로 속성 추가
    setattr(person, 'job', '개발자')
    
    # 동적으로 속성 접근
    print(f"\n동적 속성 접근:")
    print(f"이름: {getattr(person, 'name')}")
    print(f"직업: {getattr(person, 'job')}")
    
    # 안전한 속성 접근
    hobby = getattr(person, 'hobby', '취미 정보 없음')
    print(f"취미: {hobby}")
    
    # 속성 존재 여부 확인
    print(f"\n속성 존재 여부:")
    print(f"'name' 속성 존재? {'name' in person.__dict__}")
    print(f"'hobby' 속성 존재? {'hobby' in person.__dict__}")

def main():
    # Person 인스턴스 생성
    person = Person("김철수", 25)
    
    # 리플렉션을 사용한 객체 검사
    inspect_object(person)
    
    # 동적 속성 조작 예제
    dynamic_attribute_example()

if __name__ == '__main__':
    main()

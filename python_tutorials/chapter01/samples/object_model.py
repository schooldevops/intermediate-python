"""
파이썬의 객체 모델을 설명하는 예제
이 예제는 파이썬의 변수가 실제로는 객체에 대한 참조라는 것을 보여줍니다.
"""

def demonstrate_object_identity():
    # 정수 객체 생성
    x = 300
    y = 300
    print("Large integers (300):")
    print(f"x == y: {x == y}")  # 값 비교
    print(f"x is y: {x is y}")  # 정체성 비교
    
    # 작은 정수는 인터닝됨 (-5 ~ 256)
    a = 5
    b = 5
    print("\nSmall integers (5):")
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")  # True - 인터닝됨
    
    # 문자열 인터닝
    str1 = "hello"
    str2 = "hello"
    str3 = "hel" + "lo"
    print("\nString interning:")
    print(f"str1 == str2: {str1 == str2}")
    print(f"str1 is str2: {str1 is str2}")  # True - 인터닝됨
    print(f"str1 is str3: {str1 is str3}")  # True - 컴파일 시점에 최적화

def demonstrate_mutable_immutable():
    # 불변 객체 (immutable)
    x = "hello"
    print(f"\nOriginal string: {x}")
    print(f"String id: {id(x)}")
    
    x = x + " world"  # 새로운 객체 생성
    print(f"Modified string: {x}")
    print(f"New string id: {id(x)}")
    
    # 가변 객체 (mutable)
    lst = [1, 2, 3]
    print(f"\nOriginal list: {lst}")
    print(f"List id: {id(lst)}")
    
    lst.append(4)  # 같은 객체 수정
    print(f"Modified list: {lst}")
    print(f"Same list id: {id(lst)}")

def main():
    print("Python Object Model Demonstration\n")
    demonstrate_object_identity()
    demonstrate_mutable_immutable()

if __name__ == "__main__":
    main()

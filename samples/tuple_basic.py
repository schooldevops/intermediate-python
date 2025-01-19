def demonstrate_tuple_creation():
    print("=== 튜플 생성 테스트 ===")
    # 다양한 튜플 생성 방법
    empty_tuple = ()
    single_tuple = (1,)  # 요소가 하나일 때는 콤마 필수
    numbers = (1, 2, 3, 4, 5)
    mixed = (1, "Python", 3.14, True, (1, 2, 3))
    
    print(f"빈 튜플: {empty_tuple}")
    print(f"단일 요소 튜플: {single_tuple}")
    print(f"숫자 튜플: {numbers}")
    print(f"혼합 튜플: {mixed}")
    
    # 괄호 없이 튜플 생성
    tuple_without_parentheses = 1, 2, 3, 4, 5
    print(f"괄호 없는 튜플: {tuple_without_parentheses}")
    
    # 다른 시퀀스로부터 튜플 생성
    tuple_from_list = tuple([1, 2, 3])
    tuple_from_string = tuple("Python")
    print(f"리스트로부터 생성: {tuple_from_list}")
    print(f"문자열로부터 생성: {tuple_from_string}")

def demonstrate_packing_unpacking():
    print("\n=== 패킹과 언패킹 테스트 ===")
    # 튜플 패킹
    coordinates = 12.5, 34.8
    print(f"패킹된 좌표: {coordinates}")
    
    # 튜플 언패킹
    x, y = coordinates
    print(f"언패킹된 좌표: x = {x}, y = {y}")
    
    # 확장된 언패킹
    numbers = (1, 2, 3, 4, 5)
    first, *rest, last = numbers
    print(f"첫 번째: {first}, 중간: {rest}, 마지막: {last}")
    
    # 다중 변수 할당
    a, b, c = 1, 2, 3
    print(f"다중 할당: a = {a}, b = {b}, c = {c}")

def demonstrate_tuple_operations():
    print("\n=== 튜플 연산 테스트 ===")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    # 연결
    concatenated = tuple1 + tuple2
    print(f"튜플 연결: {concatenated}")
    
    # 반복
    repeated = tuple1 * 3
    print(f"튜플 반복: {repeated}")
    
    # 멤버십 테스트
    print(f"3이 tuple1에 있나요? {3 in tuple1}")
    print(f"5가 tuple1에 있나요? {5 in tuple1}")

def demonstrate_immutability():
    print("\n=== 불변성 테스트 ===")
    tuple_test = (1, 2, [3, 4])
    print(f"원본 튜플: {tuple_test}")
    
    try:
        tuple_test[0] = 10  # 튜플 요소 직접 수정 시도
    except TypeError as e:
        print(f"튜플 수정 시도 에러: {e}")
    
    # 내부 가변 객체 수정
    tuple_test[2][0] = 30
    print(f"내부 리스트 수정 후: {tuple_test}")
    print("=> 튜플 내부의 가변 객체는 수정 가능")

def main():
    demonstrate_tuple_creation()
    demonstrate_packing_unpacking()
    demonstrate_tuple_operations()
    demonstrate_immutability()

if __name__ == "__main__":
    main() 
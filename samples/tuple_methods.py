def demonstrate_tuple_methods():
    print("=== 튜플 메서드 테스트 ===")
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"테스트 튜플: {numbers}")
    
    # count 메서드
    print(f"\n--- count() 메서드 ---")
    print(f"숫자 2의 개수: {numbers.count(2)}")
    print(f"숫자 4의 개수: {numbers.count(4)}")
    print(f"숫자 6의 개수: {numbers.count(6)}")  # 존재하지 않는 요소
    
    # index 메서드
    print(f"\n--- index() 메서드 ---")
    print(f"숫자 4의 위치: {numbers.index(4)}")
    print(f"숫자 2의 첫 번째 위치: {numbers.index(2)}")
    
    # index 메서드 범위 지정
    print(f"숫자 2의 위치 (인덱스 3부터 검색): {numbers.index(2, 3)}")
    
    try:
        numbers.index(6)  # 존재하지 않는 요소 검색
    except ValueError as e:
        print(f"존재하지 않는 값 검색 에러: {e}")

def demonstrate_builtin_functions():
    print("\n=== 내장 함수 테스트 ===")
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"테스트 튜플: {numbers}")
    
    # 기본 내장 함수
    print(f"\n--- 기본 내장 함수 ---")
    print(f"튜플 길이 (len): {len(numbers)}")
    print(f"최대값 (max): {max(numbers)}")
    print(f"최소값 (min): {min(numbers)}")
    print(f"합계 (sum): {sum(numbers)}")
    
    # 통계 계산
    average = sum(numbers) / len(numbers)
    print(f"평균값: {average:.2f}")

def demonstrate_advanced_operations():
    print("\n=== 고급 연산 테스트 ===")
    
    # 여러 자료형이 섞인 튜플
    mixed = (1, "hello", 3.14, True)
    print(f"혼합 튜플: {mixed}")
    
    try:
        print(f"최대값: {max(mixed)}")
    except TypeError as e:
        print(f"다른 타입 간 비교 에러: {e}")
    
    # 튜플 정렬
    numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3)
    sorted_numbers = tuple(sorted(numbers))
    print(f"\n원본 튜플: {numbers}")
    print(f"정렬된 튜플: {sorted_numbers}")
    print(f"내림차순 정렬: {tuple(sorted(numbers, reverse=True))}")

def demonstrate_tuple_operations():
    print("\n=== 튜플 연산 테스트 ===")
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    # 연결
    concatenated = tuple1 + tuple2
    print(f"튜플 연결 (+): {concatenated}")
    
    # 반복
    repeated = tuple1 * 3
    print(f"튜플 반복 (*): {repeated}")
    
    # 멤버십 테스트
    print(f"\n--- 멤버십 테스트 ---")
    print(f"3이 tuple1에 있나요? {3 in tuple1}")
    print(f"5가 tuple1에 있나요? {5 in tuple1}")

def main():
    demonstrate_tuple_methods()
    demonstrate_builtin_functions()
    demonstrate_advanced_operations()
    demonstrate_tuple_operations()

if __name__ == "__main__":
    main() 
def demonstrate_sorting():
    print("=== 정렬 테스트 ===")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"원본 리스트: {numbers}")
    
    # sorted() 함수 사용
    sorted_numbers = sorted(numbers)
    print(f"sorted() 결과 (새로운 리스트): {sorted_numbers}")
    print(f"원본 리스트 (변경되지 않음): {numbers}")
    
    # sort() 메서드 사용
    numbers.sort()
    print(f"sort() 후 (원본 리스트 변경됨): {numbers}")
    
    # reverse() 메서드 사용
    numbers.reverse()
    print(f"reverse() 후: {numbers}")
    
    # 내림차순 정렬
    numbers.sort(reverse=True)
    print(f"내림차순 정렬 후: {numbers}")

def demonstrate_search():
    print("\n=== 검색 테스트 ===")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"테스트 리스트: {numbers}")
    
    # count() 메서드
    print(f"숫자 5의 개수: {numbers.count(5)}")
    print(f"숫자 1의 개수: {numbers.count(1)}")
    
    # index() 메서드
    try:
        print(f"숫자 4의 첫 번째 위치: {numbers.index(4)}")
        print(f"숫자 1의 첫 번째 위치: {numbers.index(1)}")
        # 존재하지 않는 값 검색
        print(f"숫자 7의 위치: {numbers.index(7)}")
    except ValueError as e:
        print(f"검색 에러: {e}")

def demonstrate_calculations():
    print("\n=== 계산 테스트 ===")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"테스트 리스트: {numbers}")
    
    # 기본 계산
    print(f"리스트 길이: {len(numbers)}")
    print(f"모든 요소의 합: {sum(numbers)}")
    print(f"최대값: {max(numbers)}")
    print(f"최소값: {min(numbers)}")
    
    # 평균 계산
    average = sum(numbers) / len(numbers)
    print(f"평균값: {average:.2f}")

def demonstrate_advanced_usage():
    print("\n=== 고급 활용 테스트 ===")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    
    # 중복 제거 후 정렬
    unique_sorted = sorted(set(numbers))
    print(f"중복 제거 및 정렬: {unique_sorted}")
    
    # 사용자 정의 키를 사용한 정렬
    words = ['banana', 'apple', 'Cherry', 'date']
    print(f"원본 문자열 리스트: {words}")
    
    # 대소문자 구분 없이 정렬
    words.sort(key=str.lower)
    print(f"대소문자 구분 없이 정렬: {words}")

def main():
    demonstrate_sorting()
    demonstrate_search()
    demonstrate_calculations()
    demonstrate_advanced_usage()

if __name__ == "__main__":
    main() 
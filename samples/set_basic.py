def demonstrate_set_creation():
    print("=== 집합 생성 방법 ===")
    
    # 다양한 방법으로 집합 생성
    empty_set = set()  # 빈 집합 생성
    numbers = {1, 2, 3, 4, 5}  # 중괄호로 생성
    fruits = {'apple', 'banana', 'orange'}  # 문자열 집합
    
    # set() 생성자를 사용한 집합 생성
    from_list = set([1, 2, 3, 4, 5])
    from_tuple = set((1, 2, 3, 4, 5))
    from_string = set('hello')  # 문자열의 각 문자로 집합 생성
    
    print(f"빈 집합: {empty_set}")
    print(f"숫자 집합: {numbers}")
    print(f"과일 집합: {fruits}")
    print(f"리스트로부터 생성: {from_list}")
    print(f"튜플로부터 생성: {from_tuple}")
    print(f"문자열로부터 생성: {from_string}")

def demonstrate_duplicate_removal():
    print("\n=== 중복 제거 기능 ===")
    
    # 숫자 중복 제거
    numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
    print(f"중복이 제거된 숫자: {numbers_with_duplicates}")
    
    # 문자열 리스트의 중복 제거
    fruits_with_duplicates = ['apple', 'banana', 'apple', 'orange', 'banana']
    unique_fruits = set(fruits_with_duplicates)
    print(f"원본 리스트: {fruits_with_duplicates}")
    print(f"중복이 제거된 과일: {unique_fruits}")
    
    # 다시 리스트로 변환
    unique_fruits_list = list(unique_fruits)
    print(f"다시 리스트로 변환: {unique_fruits_list}")

def demonstrate_set_operations():
    print("\n=== 집합 조작 메서드 ===")
    fruits = {'apple', 'banana', 'orange'}
    print(f"초기 집합: {fruits}")
    
    # add() - 요소 추가
    fruits.add('grape')
    print(f"'grape' 추가 후: {fruits}")
    
    # update() - 여러 요소 추가
    fruits.update(['mango', 'kiwi'])
    print(f"'mango'와 'kiwi' 업데이트 후: {fruits}")
    
    # remove() - 요소 제거 (없으면 KeyError)
    fruits.remove('banana')
    print(f"'banana' 제거 후: {fruits}")
    
    try:
        fruits.remove('pear')
    except KeyError as e:
        print(f"존재하지 않는 요소 제거 시도 시 에러: {e}")
    
    # discard() - 요소 제거 (없어도 에러 없음)
    fruits.discard('melon')
    print(f"존재하지 않는 'melon' discard 후 (변화 없음): {fruits}")
    
    # pop() - 임의의 요소 제거 및 반환
    popped = fruits.pop()
    print(f"pop한 요소: {popped}")
    print(f"pop 후 집합: {fruits}")
    
    # clear() - 모든 요소 제거
    fruits.clear()
    print(f"clear 후: {fruits}")

def demonstrate_set_properties():
    print("\n=== 집합의 특성 ===")
    
    # 해시 가능한 객체만 포함 가능
    valid_set = {1, 'hello', (1, 2, 3)}  # 정상 동작
    print(f"유효한 집합: {valid_set}")
    
    try:
        invalid_set = {1, [2, 3], {4, 5}}  # 리스트와 집합은 해시 불가능
    except TypeError as e:
        print(f"해시 불가능한 객체 포함 시 에러: {e}")
    
    # 순서가 없음을 보여주기
    numbers = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3}
    print(f"순서가 없는 집합: {numbers}")

def main():
    demonstrate_set_creation()
    demonstrate_duplicate_removal()
    demonstrate_set_operations()
    demonstrate_set_properties()

if __name__ == "__main__":
    main() 
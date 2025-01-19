def demonstrate_list_creation():
    print("=== 리스트 생성 테스트 ===")
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "Python", 3.14, True, [1, 2, 3]]
    empty = []
    list_from_range = list(range(5))
    
    print(f"숫자 리스트: {numbers}")
    print(f"혼합 리스트: {mixed}")
    print(f"빈 리스트: {empty}")
    print(f"range로 생성한 리스트: {list_from_range}")

def demonstrate_list_operations():
    print("\n=== 리스트 조작 테스트 ===")
    numbers = [1, 2, 3, 4, 5]
    print(f"초기 리스트: {numbers}")
    
    # append 테스트
    numbers.append(6)
    print(f"append(6) 후: {numbers}")
    
    # insert 테스트
    numbers.insert(0, 0)
    print(f"insert(0, 0) 후: {numbers}")
    
    # extend 테스트
    numbers.extend([7, 8])
    print(f"extend([7, 8]) 후: {numbers}")
    
    # remove 테스트
    numbers.remove(0)
    print(f"remove(0) 후: {numbers}")
    
    # pop 테스트
    popped = numbers.pop()
    print(f"pop() 후: {numbers}")
    print(f"pop()으로 제거된 요소: {popped}")
    
    # clear 테스트
    numbers.clear()
    print(f"clear() 후: {numbers}")

def demonstrate_list_errors():
    print("\n=== 리스트 에러 테스트 ===")
    numbers = [1, 2, 3]
    
    # 존재하지 않는 값 제거 시도
    try:
        numbers.remove(10)
    except ValueError as e:
        print(f"존재하지 않는 값 제거 시도 에러: {e}")
    
    # 빈 리스트에서 pop 시도
    numbers.clear()
    try:
        numbers.pop()
    except IndexError as e:
        print(f"빈 리스트 pop 시도 에러: {e}")

def main():
    demonstrate_list_creation()
    demonstrate_list_operations()
    demonstrate_list_errors()

if __name__ == "__main__":
    main() 
import copy

def demonstrate_assignment():
    print("=== 단순 할당 테스트 ===")
    original = [1, [2, 3], 4]
    reference = original  # 참조만 복사
    
    print(f"원본: {original}")
    print(f"참조: {reference}")
    
    print("\n리스트 수정 후:")
    reference[0] = 9
    reference[1][0] = 8
    print(f"원본: {original}")
    print(f"참조: {reference}")
    print("=> 같은 객체를 참조하므로 둘 다 변경됨")

def demonstrate_shallow_copy():
    print("\n=== 얕은 복사 테스트 ===")
    original = [1, [2, 3], 4]
    
    # copy() 메서드를 사용한 얕은 복사
    shallow_copy1 = original.copy()
    # 슬라이싱을 사용한 얕은 복사
    shallow_copy2 = original[:]
    # list() 생성자를 사용한 얕은 복사
    shallow_copy3 = list(original)
    
    print("초기 상태:")
    print(f"원본: {original}")
    print(f"얕은 복사 1 (copy): {shallow_copy1}")
    print(f"얕은 복사 2 (slice): {shallow_copy2}")
    print(f"얕은 복사 3 (list): {shallow_copy3}")
    
    print("\n중첩된 리스트 수정 후:")
    shallow_copy1[1][0] = 8  # 중첩된 객체 수정
    print(f"원본: {original}")
    print(f"얕은 복사 1: {shallow_copy1}")
    print(f"얕은 복사 2: {shallow_copy2}")
    print(f"얕은 복사 3: {shallow_copy3}")
    print("=> 중첩된 객체는 참조가 복사되어 모두 영향 받음")

def demonstrate_deep_copy():
    print("\n=== 깊은 복사 테스트 ===")
    original = [1, [2, 3], 4]
    deep_copy = copy.deepcopy(original)
    
    print("초기 상태:")
    print(f"원본: {original}")
    print(f"깊은 복사: {deep_copy}")
    
    print("\n중첩된 리스트 수정 후:")
    deep_copy[1][0] = 8
    print(f"원본: {original}")
    print(f"깊은 복사: {deep_copy}")
    print("=> 완전히 독립된 복사본이 생성됨")

def demonstrate_copy_comparison():
    print("\n=== 복사 방식 비교 ===")
    original = [1, [2, 3], 4]
    reference = original
    shallow = original.copy()
    deep = copy.deepcopy(original)
    
    print("id 비교:")
    print(f"원본 id: {id(original)}")
    print(f"참조 id: {id(reference)}")
    print(f"얕은 복사 id: {id(shallow)}")
    print(f"깊은 복사 id: {id(deep)}")
    
    print("\n중첩된 객체의 id 비교:")
    print(f"원본 중첩 리스트 id: {id(original[1])}")
    print(f"얕은 복사 중첩 리스트 id: {id(shallow[1])}")
    print(f"깊은 복사 중첩 리스트 id: {id(deep[1])}")

def main():
    demonstrate_assignment()
    demonstrate_shallow_copy()
    demonstrate_deep_copy()
    demonstrate_copy_comparison()

if __name__ == "__main__":
    main() 
def demonstrate_basic_operations():
    print("=== 기본 집합 연산 ===")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"집합 1: {set1}")
    print(f"집합 2: {set2}")
    
    # 연산자를 이용한 집합 연산
    print("\n--- 연산자 사용 ---")
    print(f"합집합 (|): {set1 | set2}")
    print(f"교집합 (&): {set1 & set2}")
    print(f"차집합 (-): {set1 - set2}")
    print(f"대칭차집합 (^): {set1 ^ set2}")
    
    # 메서드를 이용한 집합 연산
    print("\n--- 메서드 사용 ---")
    print(f"합집합 (union): {set1.union(set2)}")
    print(f"교집합 (intersection): {set1.intersection(set2)}")
    print(f"차집합 (difference): {set1.difference(set2)}")
    print(f"대칭차집합 (symmetric_difference): {set1.symmetric_difference(set2)}")

def demonstrate_multiple_sets():
    print("\n=== 여러 집합 연산 ===")
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    set3 = {5, 6, 7, 8}
    
    print(f"집합 1: {set1}")
    print(f"집합 2: {set2}")
    print(f"집합 3: {set3}")
    
    # 여러 집합의 연산
    print("\n--- 여러 집합 연산 결과 ---")
    print(f"세 집합의 합집합: {set1.union(set2, set3)}")
    print(f"세 집합의 교집합: {set1.intersection(set2, set3)}")
    
    # 연쇄 연산
    print("\n--- 연쇄 연산 ---")
    print(f"(집합 1 ∪ 집합 2) - 집합 3: {set1.union(set2) - set3}")

def demonstrate_update_operations():
    print("\n=== 갱신 연산 ===")
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"원본 집합: {set1}")
    print(f"연산할 집합: {set2}")
    
    # 합집합 갱신
    temp_set = set1.copy()
    temp_set |= set2  # 또는 temp_set.update(set2)
    print(f"합집합 갱신 (|=): {temp_set}")
    
    # 교집합 갱신
    temp_set = set1.copy()
    temp_set &= set2  # 또는 temp_set.intersection_update(set2)
    print(f"교집합 갱신 (&=): {temp_set}")
    
    # 차집합 갱신
    temp_set = set1.copy()
    temp_set -= set2  # 또는 temp_set.difference_update(set2)
    print(f"차집합 갱신 (-=): {temp_set}")
    
    # 대칭차집합 갱신
    temp_set = set1.copy()
    temp_set ^= set2  # 또는 temp_set.symmetric_difference_update(set2)
    print(f"대칭차집합 갱신 (^=): {temp_set}")

def demonstrate_practical_examples():
    print("\n=== 실용적인 예제 ===")
    
    # 학생들의 과목 선택 예제
    math_students = {'Alice', 'Bob', 'Charlie', 'David'}
    physics_students = {'Bob', 'David', 'Eve', 'Frank'}
    chemistry_students = {'Charlie', 'Eve', 'Frank', 'George'}
    
    print("수강생 현황:")
    print(f"수학: {math_students}")
    print(f"물리: {physics_students}")
    print(f"화학: {chemistry_students}")
    
    # 분석
    all_students = math_students | physics_students | chemistry_students
    print(f"\n전체 학생 수: {len(all_students)}")
    
    math_and_physics = math_students & physics_students
    print(f"수학과 물리 모두 수강하는 학생: {math_and_physics}")
    
    only_math = math_students - (physics_students | chemistry_students)
    print(f"수학만 수강하는 학생: {only_math}")
    
    two_or_more = (math_students & physics_students) | \
                 (physics_students & chemistry_students) | \
                 (math_students & chemistry_students)
    print(f"두 과목 이상 수강하는 학생: {two_or_more}")

def main():
    demonstrate_basic_operations()
    demonstrate_multiple_sets()
    demonstrate_update_operations()
    demonstrate_practical_examples()

if __name__ == "__main__":
    main() 
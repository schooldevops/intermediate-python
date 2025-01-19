def demonstrate_subset_relations():
    print("=== 부분집합 관계 테스트 ===")
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    
    print(f"집합 A: {A}")
    print(f"집합 B: {B}")
    
    # 부분집합 확인
    print("\n--- 부분집합 테스트 ---")
    print(f"A.issubset(B): {A.issubset(B)}")  # True
    print(f"A <= B: {A <= B}")  # True (issubset 연산자)
    print(f"A < B: {A < B}")    # True (진부분집합 연산자)
    
    # 상위집합 확인
    print("\n--- 상위집합 테스트 ---")
    print(f"B.issuperset(A): {B.issuperset(A)}")  # True
    print(f"B >= A: {B >= A}")  # True (issuperset 연산자)
    print(f"B > A: {B > A}")    # True (진상위집합 연산자)
    
    # 같은 집합 테스트
    C = {1, 2, 3}
    print("\n--- 동일 집합 테스트 ---")
    print(f"A.issubset(C): {A.issubset(C)}")      # True
    print(f"A < C: {A < C}")                       # False (진부분집합 아님)
    print(f"A == C: {A == C}")                     # True

def demonstrate_disjoint_sets():
    print("\n=== 서로소 집합 테스트 ===")
    A = {1, 2, 3}
    B = {4, 5, 6}
    C = {1, 4, 7}
    
    print(f"집합 A: {A}")
    print(f"집합 B: {B}")
    print(f"집합 C: {C}")
    
    # 서로소 관계 확인
    print("\n--- 서로소 테스트 ---")
    print(f"A.isdisjoint(B): {A.isdisjoint(B)}")  # True (공통 원소 없음)
    print(f"A.isdisjoint(C): {A.isdisjoint(C)}")  # False (공통 원소 있음)
    print(f"B.isdisjoint(C): {B.isdisjoint(C)}")  # False (공통 원소 있음)

def demonstrate_practical_examples():
    print("\n=== 실용적인 예제 ===")
    
    # 권한 시스템 예제
    admin_permissions = {'read', 'write', 'delete', 'manage_users'}
    editor_permissions = {'read', 'write'}
    viewer_permissions = {'read'}
    
    print("권한 설정:")
    print(f"관리자 권한: {admin_permissions}")
    print(f"편집자 권한: {editor_permissions}")
    print(f"뷰어 권한: {viewer_permissions}")
    
    # 권한 검사
    print("\n권한 관계 확인:")
    print(f"뷰어는 편집자의 부분집합인가? {viewer_permissions.issubset(editor_permissions)}")
    print(f"편집자는 관리자의 부분집합인가? {editor_permissions.issubset(admin_permissions)}")
    print(f"관리자는 모든 편집자 권한을 포함하는가? {admin_permissions.issuperset(editor_permissions)}")

def demonstrate_set_hierarchy():
    print("\n=== 집합 계층 구조 테스트 ===")
    
    # 동물 분류 예제
    animals = {'dog', 'cat', 'bird', 'fish', 'snake', 'lizard'}
    mammals = {'dog', 'cat'}
    reptiles = {'snake', 'lizard'}
    pets = {'dog', 'cat', 'bird', 'fish'}
    wild = {'snake', 'lizard'}
    
    print("동물 분류:")
    print(f"전체 동물: {animals}")
    print(f"포유류: {mammals}")
    print(f"파충류: {reptiles}")
    print(f"애완동물: {pets}")
    print(f"야생동물: {wild}")
    
    # 관계 확인
    print("\n분류 관계:")
    print(f"모든 포유류는 동물인가? {mammals.issubset(animals)}")
    print(f"모든 파충류는 야생동물인가? {reptiles.issubset(wild)}")
    print(f"포유류와 파충류는 서로소인가? {mammals.isdisjoint(reptiles)}")
    print(f"애완동물과 야생동물은 서로소인가? {pets.isdisjoint(wild)}")

def main():
    demonstrate_subset_relations()
    demonstrate_disjoint_sets()
    demonstrate_practical_examples()
    demonstrate_set_hierarchy()

if __name__ == "__main__":
    main() 
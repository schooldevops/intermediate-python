def demonstrate_indexing():
    print("=== 인덱싱 테스트 ===")
    fruits = ["사과", "바나나", "오렌지", "포도", "망고"]
    
    print(f"전체 리스트: {fruits}")
    print(f"첫 번째 요소 (fruits[0]): {fruits[0]}")
    print(f"마지막 요소 (fruits[-1]): {fruits[-1]}")
    print(f"뒤에서 두 번째 요소 (fruits[-2]): {fruits[-2]}")
    
    # 인덱스 에러 테스트
    try:
        print(fruits[10])
    except IndexError as e:
        print(f"잘못된 인덱스 접근 에러: {e}")

def demonstrate_slicing():
    print("\n=== 슬라이싱 테스트 ===")
    fruits = ["사과", "바나나", "오렌지", "포도", "망고"]
    
    print(f"전체 리스트: {fruits}")
    print(f"fruits[1:3]: {fruits[1:3]}")    # 시작:끝 인덱스
    print(f"fruits[:3]: {fruits[:3]}")      # 처음부터 3번 인덱스 전까지
    print(f"fruits[2:]: {fruits[2:]}")      # 2번 인덱스부터 끝까지
    print(f"fruits[::2]: {fruits[::2]}")    # 2칸씩 건너뛰기
    
    # 고급 슬라이싱
    print("\n=== 고급 슬라이싱 테스트 ===")
    print(f"거꾸로 출력 (fruits[::-1]): {fruits[::-1]}")
    print(f"뒤에서 3개 (fruits[-3:]): {fruits[-3:]}")
    print(f"앞에서 3개 (fruits[:-2]): {fruits[:-2]}")

def demonstrate_slice_assignment():
    print("\n=== 슬라이스 할당 테스트 ===")
    fruits = ["사과", "바나나", "오렌지", "포도", "망고"]
    print(f"원본 리스트: {fruits}")
    
    # 슬라이스 교체
    fruits[1:3] = ["키위", "레몬"]
    print(f"fruits[1:3] = ['키위', '레몬'] 후: {fruits}")
    
    # 슬라이스 삭제
    fruits[1:3] = []
    print(f"fruits[1:3] = [] 후: {fruits}")
    
    # 슬라이스 확장
    fruits[1:1] = ["멜론", "수박"]
    print(f"fruits[1:1] = ['멜론', '수박'] 후: {fruits}")

def main():
    demonstrate_indexing()
    demonstrate_slicing()
    demonstrate_slice_assignment()

if __name__ == "__main__":
    main() 
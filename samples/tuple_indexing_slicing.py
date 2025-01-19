def demonstrate_indexing():
    print("=== 인덱싱 테스트 ===")
    colors = ("빨강", "주황", "노랑", "초록", "파랑")
    print(f"전체 튜플: {colors}")
    
    # 기본 인덱싱
    print(f"첫 번째 요소 (colors[0]): {colors[0]}")
    print(f"마지막 요소 (colors[-1]): {colors[-1]}")
    print(f"뒤에서 두 번째 요소 (colors[-2]): {colors[-2]}")
    
    # 인덱스 에러 테스트
    try:
        print(colors[10])
    except IndexError as e:
        print(f"잘못된 인덱스 접근 에러: {e}")

def demonstrate_slicing():
    print("\n=== 슬라이싱 테스트 ===")
    colors = ("빨강", "주황", "노랑", "초록", "파랑")
    print(f"전체 튜플: {colors}")
    
    # 기본 슬라이싱
    print(f"colors[1:3]: {colors[1:3]}")    # 시작:끝 인덱스
    print(f"colors[:3]: {colors[:3]}")      # 처음부터 3번 인덱스 전까지
    print(f"colors[2:]: {colors[2:]}")      # 2번 인덱스부터 끝까지
    
    # 스텝을 사용한 슬라이싱
    print("\n=== 고급 슬라이싱 테스트 ===")
    print(f"colors[::2]: {colors[::2]}")    # 2칸씩 건너뛰기
    print(f"colors[::-1]: {colors[::-1]}")  # 역순으로 출력
    print(f"colors[-3:]: {colors[-3:]}")    # 뒤에서 3개
    print(f"colors[:-2]: {colors[:-2]}")    # 뒤에서 2개 제외

def demonstrate_immutable_nature():
    print("\n=== 불변성 테스트 ===")
    colors = ("빨강", "주황", "노랑", "초록", "파랑")
    
    # 인덱싱으로 수정 시도
    try:
        colors[0] = "검정"
    except TypeError as e:
        print(f"튜플 수정 시도 에러: {e}")
    
    # 슬라이싱으로 수정 시도
    try:
        colors[1:3] = ("검정", "흰색")
    except TypeError as e:
        print(f"튜플 슬라이스 수정 시도 에러: {e}")

def demonstrate_tuple_methods():
    print("\n=== 튜플 메서드 테스트 ===")
    colors = ("빨강", "주황", "노랑", "초록", "파랑", "노랑")
    
    # index 메서드
    print(f"'노랑'의 첫 번째 위치: {colors.index('노랑')}")
    
    # count 메서드
    print(f"'노랑'의 등장 횟수: {colors.count('노랑')}")
    
    try:
        print(colors.index("검정"))
    except ValueError as e:
        print(f"존재하지 않는 값 검색 에러: {e}")

def main():
    demonstrate_indexing()
    demonstrate_slicing()
    demonstrate_immutable_nature()
    demonstrate_tuple_methods()

if __name__ == "__main__":
    main() 
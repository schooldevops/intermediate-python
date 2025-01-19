def demonstrate_basic_comprehension():
    print("=== 기본 리스트 컴프리헨션 테스트 ===")
    # 기본 형태
    squares = [x**2 for x in range(10)]
    print(f"0부터 9까지의 제곱수: {squares}")
    
    # 같은 동작을 하는 일반적인 for 문
    squares_traditional = []
    for x in range(10):
        squares_traditional.append(x**2)
    print(f"일반적인 for 문으로 만든 제곱수: {squares_traditional}")

def demonstrate_conditional_comprehension():
    print("\n=== 조건문을 포함한 리스트 컴프리헨션 테스트 ===")
    # if 조건문 포함
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print(f"짝수들의 제곱: {even_squares}")
    
    # if-else 포함
    numbers = [x if x > 0 else 0 for x in range(-5, 5)]
    print(f"음수를 0으로 바꾼 리스트: {numbers}")

def demonstrate_nested_comprehension():
    print("\n=== 중첩된 리스트 컴프리헨션 테스트 ===")
    # 2차원 행렬 생성
    matrix = [[i+j for j in range(3)] for i in range(3)]
    print("3x3 행렬:")
    for row in matrix:
        print(row)
    
    # 중첩 반복문을 한 줄로
    flattened = [i+j for i in range(3) for j in range(3)]
    print(f"평탄화된 행렬: {flattened}")

def demonstrate_practical_examples():
    print("\n=== 실용적인 예제 ===")
    # 문자열 처리
    words = ['hello', 'world', 'python', 'comprehension']
    upper_words = [word.upper() for word in words]
    print(f"대문자로 변환: {upper_words}")
    
    # 길이가 6자 이상인 단어만 선택
    long_words = [word for word in words if len(word) >= 6]
    print(f"길이가 6자 이상인 단어: {long_words}")
    
    # 단어 길이의 리스트
    word_lengths = {word: len(word) for word in words}
    print(f"각 단어의 길이: {word_lengths}")

def demonstrate_performance_tip():
    print("\n=== 성능 팁 ===")
    import time
    
    # 큰 리스트 생성 시간 비교
    start = time.time()
    squares_loop = []
    for i in range(10000):
        squares_loop.append(i**2)
    loop_time = time.time() - start
    
    start = time.time()
    squares_comp = [i**2 for i in range(10000)]
    comp_time = time.time() - start
    
    print(f"일반 루프 실행 시간: {loop_time:.6f}초")
    print(f"컴프리헨션 실행 시간: {comp_time:.6f}초")

def main():
    demonstrate_basic_comprehension()
    demonstrate_conditional_comprehension()
    demonstrate_nested_comprehension()
    demonstrate_practical_examples()
    demonstrate_performance_tip()

if __name__ == "__main__":
    main() 
def demonstrate_basic_comprehension():
    print("=== 기본 집합 컴프리헨션 ===")
    
    # 기본 제곱수 집합
    squares = {x**2 for x in range(10)}
    print(f"0부터 9까지의 제곱수: {squares}")
    
    # 문자열에서 고유 문자 추출
    text = "hello world"
    unique_chars = {char for char in text}
    print(f"문자열의 고유 문자: {unique_chars}")
    
    # 리스트에서 고유 요소 추출
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = {x for x in numbers}
    print(f"리스트의 고유 숫자: {unique_numbers}")

def demonstrate_conditional_comprehension():
    print("\n=== 조건부 집합 컴프리헨션 ===")
    
    # 단일 조건
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"짝수의 제곱: {even_squares}")
    
    # 범위 조건
    in_range = {x for x in range(100) if 20 <= x <= 30}
    print(f"20에서 30 사이의 숫자: {in_range}")
    
    # 복합 조건
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    long_words = {word for word in words if len(word) > 5}
    print(f"5글자보다 긴 단어: {long_words}")

def demonstrate_multiple_conditions():
    print("\n=== 다중 조건 집합 컴프리헨션 ===")
    
    # 두 개의 조건
    numbers = {x for x in range(100) if x % 2 == 0 if x % 3 == 0}
    print(f"2와 3의 공배수: {numbers}")
    
    # if-else 조건
    numbers = {x if x % 2 == 0 else -x for x in range(10)}
    print(f"짝수는 양수, 홀수는 음수: {numbers}")
    
    # 복합 조건식
    numbers = {x for x in range(100) if x % 2 == 0 and x % 3 == 0}
    print(f"2와 3의 공배수 (and 사용): {numbers}")

def demonstrate_nested_comprehension():
    print("\n=== 중첩 집합 컴프리헨션 ===")
    
    # 두 집합의 모든 조합
    A = {1, 2, 3}
    B = {'a', 'b'}
    combinations = {f"{num}{char}" for num in A for char in B}
    print(f"두 집합의 모든 조합: {combinations}")
    
    # 행렬의 모든 좌표
    coordinates = {(x, y) for x in range(3) for y in range(3)}
    print(f"3x3 격자의 모든 좌표: {coordinates}")

def demonstrate_practical_examples():
    print("\n=== 실용적인 예제 ===")
    
    # 이메일 도메인 추출
    emails = [
        "user1@gmail.com",
        "user2@yahoo.com",
        "user3@gmail.com",
        "user4@hotmail.com",
        "user5@gmail.com"
    ]
    domains = {email.split('@')[1] for email in emails}
    print(f"고유한 이메일 도메인: {domains}")
    
    # 단어 길이의 집합
    sentence = "the quick brown fox jumps over the lazy dog"
    word_lengths = {len(word) for word in sentence.split()}
    print(f"문장 내 단어 길이의 종류: {word_lengths}")
    
    # 숫자의 약수 집합
    number = 24
    factors = {i for i in range(1, number + 1) if number % i == 0}
    print(f"{number}의 약수: {factors}")

def main():
    demonstrate_basic_comprehension()
    demonstrate_conditional_comprehension()
    demonstrate_multiple_conditions()
    demonstrate_nested_comprehension()
    demonstrate_practical_examples()

if __name__ == "__main__":
    main() 
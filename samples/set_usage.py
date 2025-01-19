def demonstrate_duplicate_removal():
    print("=== 중복 제거 활용 ===")
    
    # 리스트에서 중복 제거
    numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique_numbers = list(set(numbers_list))
    print(f"원본 리스트: {numbers_list}")
    print(f"중복 제거된 리스트: {unique_numbers}")
    
    # 문자열에서 중복 문자 제거
    text = "mississippi"
    unique_chars = ''.join(sorted(set(text)))
    print(f"원본 문자열: {text}")
    print(f"중복이 제거된 문자들: {unique_chars}")
    
    # 여러 리스트에서 중복 제거
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    list3 = [5, 6, 7, 8]
    unique_combined = list(set(list1) | set(list2) | set(list3))
    print(f"세 리스트의 중복 없는 조합: {unique_combined}")

def demonstrate_membership_testing():
    print("\n=== 멤버십 테스트 활용 ===")
    
    # 사용자 인증 시스템
    valid_users = {'alice', 'bob', 'charlie'}
    active_sessions = {'bob', 'charlie'}
    
    def check_user(username):
        if username in valid_users:
            if username in active_sessions:
                return f"{username}은(는) 이미 로그인되어 있습니다."
            return f"{username}은(는) 유효한 사용자입니다."
        return f"{username}은(는) 유효하지 않은 사용자입니다."
    
    print(check_user('alice'))
    print(check_user('bob'))
    print(check_user('eve'))
    
    # 허용된 파일 확장자 검사
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif'}
    files = ['image.jpg', 'document.pdf', 'photo.png', 'script.js']
    
    for file in files:
        ext = '.' + file.split('.')[-1].lower()
        print(f"{file}: {'허용됨' if ext in allowed_extensions else '허용되지 않음'}")

def demonstrate_data_filtering():
    print("\n=== 데이터 필터링 활용 ===")
    
    # 숫자 필터링
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    evens = {x for x in numbers if x % 2 == 0}
    odds = {x for x in numbers if x % 2 == 1}
    
    print(f"모든 숫자: {numbers}")
    print(f"짝수: {evens}")
    print(f"홀수: {odds}")
    
    # 점수 기반 학생 분류
    scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'David': 95,
        'Eve': 88
    }
    
    high_scorers = {name for name, score in scores.items() if score >= 90}
    print(f"90점 이상 학생: {high_scorers}")

def demonstrate_set_operations_usage():
    print("\n=== 집합 연산 활용 ===")
    
    # 프로그래밍 언어 스킬 분석
    python_devs = {'Alice', 'Bob', 'Charlie'}
    java_devs = {'Bob', 'David', 'Eve'}
    js_devs = {'Charlie', 'Eve', 'Frank'}
    
    # 다중 언어 프로그래머 찾기
    multi_language = python_devs & java_devs & js_devs
    print(f"모든 언어를 다루는 개발자: {multi_language}")
    
    # 적어도 한 언어를 아는 개발자
    all_devs = python_devs | java_devs | js_devs
    print(f"전체 개발자: {all_devs}")
    
    # Python 전문가 (다른 언어는 모름)
    python_only = python_devs - (java_devs | js_devs)
    print(f"Python만 하는 개발자: {python_only}")

def main():
    demonstrate_duplicate_removal()
    demonstrate_membership_testing()
    demonstrate_data_filtering()
    demonstrate_set_operations_usage()

if __name__ == "__main__":
    main() 
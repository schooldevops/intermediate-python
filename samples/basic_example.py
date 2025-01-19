def basic_examples():
    '''
    파이썬 기본 문법에 대한 샘플을 알려준다. 
    '''
    # 1. 숫자형 (Numbers)
    integer_num = 42
    float_num = 3.14
    complex_num = 1 + 2j
    
    print("=== 숫자형 ===")
    print(f"정수: {integer_num}, 타입: {type(integer_num)}")
    print(f"실수: {float_num}, 타입: {type(float_num)}")
    print(f"복소수: {complex_num}, 타입: {type(complex_num)}")
    print()

    # 2. 문자열 (String)
    single_quote = 'Hello'
    double_quote = "Python"
    multi_line = """이것은
여러 줄의
문자열입니다."""
    
    print("=== 문자열 ===")
    print(f"작은따옴표: {single_quote}")
    print(f"큰따옴표: {double_quote}")
    print("여러 줄 문자열:")
    print(multi_line)
    print()

    # 3. 리스트 (List)
    my_list = [1, 2, 3, 4, 5]
    hello = "Hello, Python!"
    print("=== 리스트 ===")
    print(f"리스트: {my_list} {hello}")
    print(f"첫 번째 요소: {my_list[0]}")
    print(f"마지막 요소: {my_list[-1]}")
    my_list.append("새로운 항목")
    print(f"항목 추가 후: {my_list}")
    print()

    # 4. 튜플 (Tuple)
    my_tuple = (1, "Python", 3.14)
    print("=== 튜플 ===")
    print(f"튜플: {my_tuple}")
    print(f"두 번째 요소: {my_tuple[1]}")
    print()

    # 5. 딕셔너리 (Dictionary)
    my_dict = {
        "name": "Python",
        "version": 3.11,
        "is_fun": True,
        "features": ["easy", "powerful", "flexible"]
    }
    print("=== 딕셔너리 ===")
    print(f"딕셔너리: {my_dict}")
    print(f"이름: {my_dict['name']}")
    print(f"버전: {my_dict['version']}")
    my_dict["new_key"] = "새로운 값"
    print(f"새로운 키-값 추가 후: {my_dict}")
    print()

    # 6. 집합 (Set)
    my_set = {1, 2, 3, 3, 2, 1}  # 중복된 값은 자동으로 제거됨
    print("=== 집합 ===")
    print(f"집합: {my_set}")
    my_set.add(4)
    print(f"요소 추가 후: {my_set}")
    print()

    # 7. 불리언 (Boolean)
    is_python = True
    is_java = False
    print("=== 불리언 ===")
    print(f"is_python: {is_python}")
    print(f"is_java: {is_java}")
    print(f"논리 연산: {is_python and is_java}")

if __name__ == "__main__":
    basic_examples() 
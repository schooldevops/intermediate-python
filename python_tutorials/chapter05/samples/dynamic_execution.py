import ast
from typing import Any

def safe_eval(expr: str) -> Any:
    """안전한 eval 구현"""
    # 허용된 이름들의 집합
    allowed_names = {'True', 'False', 'None', 'abs', 'int', 'float', 'str'}
    
    # AST를 사용하여 표현식 파싱
    tree = ast.parse(expr, mode='eval')
    
    # 안전하지 않은 노드 검사
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id not in allowed_names:
            raise NameError(f"사용할 수 없는 이름입니다: {node.id}")
    
    # 컴파일 및 실행
    code = compile(tree, '<string>', 'eval')
    return eval(code)

def dynamic_code_examples():
    """동적 코드 실행 예제"""
    # 1. eval 예제
    print("1. eval 예제:")
    expressions = [
        "2 + 3 * 4",
        "abs(-42)",
        "str(123) + '456'",
    ]
    
    for expr in expressions:
        try:
            result = safe_eval(expr)
            print(f"표현식: {expr}")
            print(f"결과: {result}\n")
        except Exception as e:
            print(f"오류 발생: {e}\n")
    
    # 2. exec 예제
    print("2. exec 예제:")
    code = """
def greet(name):
    return f"안녕하세요, {name}님!"

message = greet("홍길동")
print(message)
"""
    print("실행할 코드:")
    print(code)
    print("\n실행 결과:")
    exec(code)
    
    # 3. compile 예제
    print("\n3. compile 예제:")
    # 여러 줄의 코드를 컴파일
    code = compile("""
for i in range(3):
    print(f"{i}번째 실행")
""", '<string>', 'exec')
    
    print("컴파일된 코드 실행 결과:")
    exec(code)

def main():
    try:
        dynamic_code_examples()
    except Exception as e:
        print(f"예제 실행 중 오류 발생: {e}")

if __name__ == '__main__':
    main()

from string import Template
import types
from typing import Any, Dict

def create_class_dynamically(class_name: str, attributes: Dict[str, Any]) -> type:
    """동적으로 클래스를 생성하는 함수"""
    def __init__(self):
        for key, value in attributes.items():
            setattr(self, key, value)
    
    return type(class_name, (), {
        '__init__': __init__,
        **attributes
    })

def create_function_dynamically(func_name: str, arg_names: list, body: str) -> types.FunctionType:
    """동적으로 함수를 생성하는 함수"""
    # 함수 코드 템플릿
    func_template = Template("""
def $func_name($args):
    $body
    """)
    
    # 함수 코드 생성
    func_code = func_template.substitute(
        func_name=func_name,
        args=', '.join(arg_names),
        body=body
    )
    
    # 함수 컴파일 및 생성
    namespace = {}
    exec(func_code, namespace)
    return namespace[func_name]

def template_example():
    """문자열 템플릿 예제"""
    print("1. 문자열 템플릿 예제:")
    
    # 간단한 템플릿
    template = Template("안녕하세요, ${name}님! 당신의 점수는 ${score}점입니다.")
    
    # 템플릿에 값 채우기
    result = template.substitute(name="홍길동", score=95)
    print(result)
    
    # 딕셔너리를 사용한 템플릿
    data = {'name': '김철수', 'score': 88}
    result = template.substitute(data)
    print(result)

def dynamic_class_example():
    """동적 클래스 생성 예제"""
    print("\n2. 동적 클래스 생성 예제:")
    
    # Student 클래스 동적 생성
    attributes = {
        'name': '홍길동',
        'grade': 3,
        'get_info': lambda self: f"{self.name} (학년: {self.grade})"
    }
    
    StudentClass = create_class_dynamically('Student', attributes)
    student = StudentClass()
    
    print(f"클래스 이름: {StudentClass.__name__}")
    print(f"인스턴스 정보: {student.get_info()}")

def dynamic_function_example():
    """동적 함수 생성 예제"""
    print("\n3. 동적 함수 생성 예제:")
    
    # 간단한 함수 생성
    greet = create_function_dynamically(
        'greet',
        ['name', 'age'],
        'return f"안녕하세요, {name}님! 당신은 {age}세입니다."'
    )
    
    # 생성된 함수 호출
    result = greet("홍길동", 25)
    print(result)
    
    # 수학 함수 생성
    calculate = create_function_dynamically(
        'calculate',
        ['x', 'y'],
        'return x * x + y * y'
    )
    
    # 생성된 함수 호출
    result = calculate(3, 4)
    print(f"3^2 + 4^2 = {result}")

def main():
    template_example()
    dynamic_class_example()
    dynamic_function_example()

if __name__ == '__main__':
    main()

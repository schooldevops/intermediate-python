"""
파이썬의 스코프와 네임스페이스를 설명하는 예제
이 예제는 LEGB 규칙과 변수의 스코프를 보여줍니다.
"""

# 전역 변수
global_var = "I'm a global variable"

def demonstrate_scope():
    # 지역 변수
    local_var = "I'm a local variable"
    
    print(f"Inside function - local: {local_var}")
    print(f"Inside function - global: {global_var}")

def demonstrate_nonlocal():
    outer_var = "I'm from outer function"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified by inner function"
        print(f"Inside inner function: {outer_var}")
    
    print(f"Before inner function call: {outer_var}")
    inner_function()
    print(f"After inner function call: {outer_var}")

def demonstrate_global():
    def modify_global():
        global global_var
        global_var = "Modified by function"
        print(f"Inside function: {global_var}")
    
    print(f"Before modification: {global_var}")
    modify_global()
    print(f"After modification: {global_var}")

class NamespaceDemo:
    # 클래스 변수
    class_var = "I'm a class variable"
    
    def __init__(self):
        # 인스턴스 변수
        self.instance_var = "I'm an instance variable"
    
    def demonstrate_namespace(self):
        # 메서드 지역 변수
        method_var = "I'm a method variable"
        print(f"\nInside method:")
        print(f"Class variable: {self.class_var}")
        print(f"Instance variable: {self.instance_var}")
        print(f"Method variable: {method_var}")

def main():
    print("Python Scope and Namespace Demonstration\n")
    
    print("1. Basic Scope Demonstration:")
    demonstrate_scope()
    
    print("\n2. Nonlocal Scope Demonstration:")
    demonstrate_nonlocal()
    
    print("\n3. Global Scope Demonstration:")
    demonstrate_global()
    
    print("\n4. Class Namespace Demonstration:")
    demo = NamespaceDemo()
    demo.demonstrate_namespace()
    
    # 클래스와 인스턴스 네임스페이스 비교
    print("\nNamespace Comparison:")
    print(f"Class namespace: {NamespaceDemo.__dict__.keys()}")
    print(f"Instance namespace: {demo.__dict__.keys()}")

if __name__ == "__main__":
    main()

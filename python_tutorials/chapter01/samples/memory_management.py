"""
파이썬의 메모리 관리와 가비지 컬렉션을 설명하는 예제
이 예제는 참조 카운팅과 순환 참조 처리를 보여줍니다.
"""

import gc
import weakref
import sys

class CircularRef:
    def __init__(self, name):
        self.name = name
        self.other = None
        print(f"Creating {self.name}")
    
    def __del__(self):
        print(f"Destroying {self.name}")

def demonstrate_reference_counting():
    print("\nReference Counting Demo:")
    x = CircularRef("Object X")
    print(f"Reference count: {sys.getrefcount(x) - 1}")  # -1 for the getrefcount argument
    
    # 참조 추가
    y = x
    print(f"Reference count after assignment: {sys.getrefcount(x) - 1}")
    
    # 참조 제거
    del y
    print(f"Reference count after deletion: {sys.getrefcount(x) - 1}")

def demonstrate_circular_reference():
    print("\nCircular Reference Demo:")
    # 순환 참조 생성
    x = CircularRef("Object A")
    y = CircularRef("Object B")
    x.other = y
    y.other = x
    
    # 참조 제거
    print("Removing references...")
    del x
    del y
    
    # 가비지 컬렉션 실행
    print("\nRunning garbage collection...")
    gc.collect()

def demonstrate_weak_references():
    print("\nWeak References Demo:")
    class ExpensiveObject:
        def __init__(self, name):
            self.name = name
        
        def __del__(self):
            print(f"{self.name} is being deleted")
    
    obj = ExpensiveObject("My Object")
    # 약한 참조 생성
    weak_ref = weakref.ref(obj)
    
    print(f"Object exists: {weak_ref() is not None}")
    del obj
    print(f"Object exists after deletion: {weak_ref() is not None}")

def main():
    print("Python Memory Management Demonstration")
    demonstrate_reference_counting()
    demonstrate_circular_reference()
    demonstrate_weak_references()

if __name__ == "__main__":
    main()

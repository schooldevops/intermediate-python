"""
파이썬의 매직 메서드와 그 활용을 설명하는 예제
이 예제는 연산자 오버로딩, 컨텍스트 매니저, 속성 접근 제어 등을 보여줍니다.
"""

from typing import Any, List, Dict
import math

class Vector:
    """
    2D 벡터 클래스 - 연산자 오버로딩 예제
    """
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self.x / scalar, self.y / scalar)
    
    def __abs__(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other: 'Vector') -> bool:
        return abs(self) < abs(other)

class DatabaseConnection:
    """
    데이터베이스 연결을 관리하는 컨텍스트 매니저 예제
    """
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.connected = False
    
    def __enter__(self) -> 'DatabaseConnection':
        self.connected = True
        print(f"Connected to database at {self.host}:{self.port}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.connected = False
        print("Disconnected from database")
        return False  # 예외를 상위로 전파
    
    def query(self, sql: str) -> List[Dict]:
        if not self.connected:
            raise RuntimeError("Not connected to database")
        print(f"Executing query: {sql}")
        return []  # 실제 구현에서는 쿼리 결과 반환

class ManagedAttributes:
    """
    속성 접근 제어를 위한 매직 메서드 예제
    """
    def __init__(self):
        self._internal = {}
    
    def __getattr__(self, name: str) -> Any:
        print(f"Getting attribute: {name}")
        return self._internal.get(name)
    
    def __setattr__(self, name: str, value: Any) -> None:
        if name == '_internal':
            super().__setattr__(name, value)
            return
        print(f"Setting attribute: {name} = {value}")
        self._internal[name] = value
    
    def __delattr__(self, name: str) -> None:
        if name == '_internal':
            super().__delattr__(name)
            return
        print(f"Deleting attribute: {name}")
        del self._internal[name]
    
    def __getitem__(self, key: str) -> Any:
        return self._internal[key]
    
    def __setitem__(self, key: str, value: Any) -> None:
        self._internal[key] = value

def demonstrate_vector_operations():
    print("\nVector Operations Demonstration:")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"|v1| = {abs(v1)}")
    print(f"v1 == v2: {v1 == v2}")
    print(f"v1 < v2: {v1 < v2}")

def demonstrate_context_manager():
    print("\nContext Manager Demonstration:")
    try:
        with DatabaseConnection("localhost", 5432) as db:
            db.query("SELECT * FROM users")
    except Exception as e:
        print(f"Error: {e}")

def demonstrate_managed_attributes():
    print("\nManaged Attributes Demonstration:")
    obj = ManagedAttributes()
    
    # 속성 설정
    obj.name = "John"
    obj.age = 30
    
    # 속성 접근
    print(f"Name: {obj.name}")
    print(f"Age: {obj.age}")
    
    # 딕셔너리 스타일 접근
    obj['score'] = 100
    print(f"Score: {obj['score']}")
    
    # 속성 삭제
    del obj.name
    try:
        print(obj.name)
    except KeyError:
        print("Name attribute was deleted")

def main():
    print("Magic Methods Demonstration")
    demonstrate_vector_operations()
    demonstrate_context_manager()
    demonstrate_managed_attributes()

if __name__ == "__main__":
    main()

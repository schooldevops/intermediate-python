"""
파이썬의 메타클래스 개념과 활용을 설명하는 예제
이 예제는 메타클래스의 동작 방식과 실제 사용 사례를 보여줍니다.
"""

from typing import Dict, Type, Any

class SingletonMeta(type):
    """
    싱글톤 패턴을 구현하는 메타클래스
    """
    _instances: Dict[Type, Any] = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class ValidatorMeta(type):
    """
    클래스 속성의 타입을 검증하는 메타클래스
    """
    def __new__(mcs, name, bases, namespace):
        # 클래스 속성의 타입 검증
        for key, value in namespace.items():
            if key.startswith('__'):
                continue
            if hasattr(value, 'validate'):
                namespace[f'_{key}'] = value
                namespace[key] = property(
                    fget=mcs._get_validator(key),
                    fset=mcs._set_validator(key)
                )
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def _get_validator(name):
        def getter(self):
            return getattr(self, f'_{name}')
        return getter
    
    @staticmethod
    def _set_validator(name):
        def setter(self, value):
            validator = getattr(self, f'_{name}')
            if validator.validate(value):
                setattr(self, f'_{name}_value', value)
            else:
                raise ValueError(f"Invalid value for {name}")
        return setter

class Field:
    """
    필드 검증을 위한 기본 클래스
    """
    def __init__(self, field_type):
        self.field_type = field_type
        self._value = None
    
    def validate(self, value):
        return isinstance(value, self.field_type)
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value
    
    def __set__(self, instance, value):
        if not self.validate(value):
            raise ValueError(f"Expected {self.field_type.__name__}, got {type(value).__name__}")
        self._value = value

# 싱글톤 패턴 예제
class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connected = False
    
    def connect(self):
        if not self.connected:
            print("Connecting to database...")
            self.connected = True
        else:
            print("Already connected")

# 타입 검증 예제
class User(metaclass=ValidatorMeta):
    name = Field(str)
    age = Field(int)
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def demonstrate_singleton():
    print("\nSingleton Pattern Demonstration:")
    db1 = Database()
    db2 = Database()
    
    print(f"Same instance? {db1 is db2}")
    db1.connect()
    db2.connect()

def demonstrate_validator():
    print("\nValidator Metaclass Demonstration:")
    try:
        user = User("John", 30)
        print(f"Valid user created: {user.name}, {user.age}")
        
        # 잘못된 타입 할당 시도
        user.age = "invalid"  # ValueError 발생
    except ValueError as e:
        print(f"Validation error: {e}")

# 메타클래스를 사용한 추상 베이스 클래스 예제
class InterfaceMeta(type):
    def __new__(mcs, name, bases, namespace):
        # 추상 메서드 검증
        for key, value in namespace.items():
            if getattr(value, "__isabstractmethod__", False):
                continue
            if key.startswith("abstract_"):
                raise TypeError(
                    f"Abstract method {key} in {name} is not implemented"
                )
        return super().__new__(mcs, name, bases, namespace)

class Interface(metaclass=InterfaceMeta):
    def abstract_method(self):
        raise NotImplementedError

class Implementation(Interface):
    def abstract_method(self):
        return "Implemented"

def main():
    print("Metaclass Demonstrations")
    demonstrate_singleton()
    demonstrate_validator()
    
    # 인터페이스 구현 테스트
    impl = Implementation()
    print(f"\nInterface implementation: {impl.abstract_method()}")

if __name__ == "__main__":
    main()

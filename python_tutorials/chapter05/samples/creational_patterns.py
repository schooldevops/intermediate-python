from abc import ABC, abstractmethod
from typing import Dict, Any
from copy import deepcopy

# 싱글톤 패턴
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {}

# 팩토리 메서드 패턴
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self) -> str:
        return "멍멍!"

class Cat(Animal):
    def speak(self) -> str:
        return "야옹!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        raise ValueError(f"알 수 없는 동물 유형: {animal_type}")

# 빌더 패턴
class Computer:
    def __init__(self):
        self.parts: Dict[str, str] = {}
    
    def __str__(self):
        return f"Computer parts: {self.parts}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def add_cpu(self, cpu: str) -> 'ComputerBuilder':
        self.computer.parts['CPU'] = cpu
        return self
    
    def add_ram(self, ram: str) -> 'ComputerBuilder':
        self.computer.parts['RAM'] = ram
        return self
    
    def add_storage(self, storage: str) -> 'ComputerBuilder':
        self.computer.parts['Storage'] = storage
        return self
    
    def build(self) -> Computer:
        return self.computer

# 프로토타입 패턴
class Prototype:
    def clone(self):
        return deepcopy(self)

class Document(Prototype):
    def __init__(self, content: str):
        self.content = content
    
    def __str__(self):
        return f"Document: {self.content}"

def creational_patterns_example():
    # 1. 싱글톤 패턴 예제
    print("1. 싱글톤 패턴:")
    singleton1 = Singleton()
    singleton1.data['key'] = 'value'
    
    singleton2 = Singleton()
    print(f"같은 인스턴스? {singleton1 is singleton2}")
    print(f"singleton2.data: {singleton2.data}")
    
    # 2. 팩토리 메서드 패턴 예제
    print("\n2. 팩토리 메서드 패턴:")
    factory = AnimalFactory()
    
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")
    
    print(f"강아지 소리: {dog.speak()}")
    print(f"고양이 소리: {cat.speak()}")
    
    # 3. 빌더 패턴 예제
    print("\n3. 빌더 패턴:")
    computer = ComputerBuilder()\
        .add_cpu("Intel i7")\
        .add_ram("16GB")\
        .add_storage("1TB SSD")\
        .build()
    
    print(computer)
    
    # 4. 프로토타입 패턴 예제
    print("\n4. 프로토타입 패턴:")
    original = Document("원본 문서")
    copy = original.clone()
    
    print(f"원본: {original}")
    print(f"복사본: {copy}")
    print(f"같은 인스턴스? {original is copy}")

if __name__ == '__main__':
    creational_patterns_example()

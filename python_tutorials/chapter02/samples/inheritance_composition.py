"""
파이썬의 상속과 구성 패턴을 설명하는 예제
이 예제는 다중 상속, Mixin 클래스, 구성 패턴의 활용을 보여줍니다.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

# 다중 상속 예제
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def speak(self) -> str:
        return "Some sound"

class Flyable:
    def fly(self) -> str:
        return f"{self.__class__.__name__} is flying"

class Swimmable:
    def swim(self) -> str:
        return f"{self.__class__.__name__} is swimming"

class Duck(Animal, Flyable, Swimmable):
    def speak(self) -> str:
        return "Quack!"

# Mixin 클래스 예제
class JSONSerializerMixin:
    def to_json(self) -> dict:
        return {
            key: value for key, value in self.__dict__.items()
            if not key.startswith('_')
        }

class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[{self.__class__.__name__}] {message}")

class User(JSONSerializerMixin, LoggerMixin):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# 구성 패턴 예제
class Engine:
    def start(self) -> str:
        return "Engine started"
    
    def stop(self) -> str:
        return "Engine stopped"

class Wheels:
    def __init__(self, count: int = 4):
        self.count = count
    
    def rotate(self) -> str:
        return f"{self.count} wheels rotating"

class Car:
    def __init__(self):
        self.engine = Engine()
        self.wheels = Wheels()
    
    def start(self) -> str:
        return self.engine.start()
    
    def drive(self) -> str:
        return self.wheels.rotate()

# 템플릿 메서드 패턴 예제
class DataMiner(ABC):
    def mine(self, path: str) -> str:
        data = self._extract(path)
        processed_data = self._transform(data)
        return self._load(processed_data)
    
    @abstractmethod
    def _extract(self, path: str) -> str:
        pass
    
    @abstractmethod
    def _transform(self, data: str) -> str:
        pass
    
    @abstractmethod
    def _load(self, data: str) -> str:
        pass

class CSVDataMiner(DataMiner):
    def _extract(self, path: str) -> str:
        return f"Extracting CSV data from {path}"
    
    def _transform(self, data: str) -> str:
        return f"Transforming CSV data: {data}"
    
    def _load(self, data: str) -> str:
        return f"Loading transformed data: {data}"

def demonstrate_multiple_inheritance():
    print("\nMultiple Inheritance Demonstration:")
    duck = Duck("Donald")
    print(duck.speak())
    print(duck.fly())
    print(duck.swim())

def demonstrate_mixins():
    print("\nMixin Classes Demonstration:")
    user = User("John", 30)
    print(f"JSON representation: {user.to_json()}")
    user.log("User created")

def demonstrate_composition():
    print("\nComposition Pattern Demonstration:")
    car = Car()
    print(car.start())
    print(car.drive())

def demonstrate_template_method():
    print("\nTemplate Method Pattern Demonstration:")
    miner = CSVDataMiner()
    result = miner.mine("data.csv")
    print(result)

def main():
    print("Inheritance and Composition Demonstrations")
    demonstrate_multiple_inheritance()
    demonstrate_mixins()
    demonstrate_composition()
    demonstrate_template_method()

if __name__ == "__main__":
    main()

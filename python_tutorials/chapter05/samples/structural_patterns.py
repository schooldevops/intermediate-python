from abc import ABC, abstractmethod
from typing import List

# 어댑터 패턴
class OldSystem:
    def specific_request(self) -> str:
        return "기존 시스템의 특별한 요청"

class NewSystem:
    def general_request(self) -> str:
        return "새로운 요청"

class SystemAdapter(NewSystem):
    def __init__(self, old_system: OldSystem):
        self.old_system = old_system
    
    def general_request(self) -> str:
        return f"어댑터를 통한 변환: {self.old_system.specific_request()}"

# 브리지 패턴
class Color(ABC):
    @abstractmethod
    def fill(self) -> str:
        pass

class Red(Color):
    def fill(self) -> str:
        return "빨간색"

class Blue(Color):
    def fill(self) -> str:
        return "파란색"

class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color
    
    @abstractmethod
    def draw(self) -> str:
        pass

class Circle(Shape):
    def draw(self) -> str:
        return f"{self.color.fill()} 원"

class Square(Shape):
    def draw(self) -> str:
        return f"{self.color.fill()} 사각형"

# 컴포지트 패턴
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Leaf(Component):
    def __init__(self, name: str):
        self.name = name
    
    def operation(self) -> str:
        return f"Leaf {self.name}"

class Composite(Component):
    def __init__(self, name: str):
        self.name = name
        self.children: List[Component] = []
    
    def add(self, component: Component):
        self.children.append(component)
    
    def operation(self) -> str:
        results = [f"Composite {self.name}"]
        for child in self.children:
            results.append(f"- {child.operation()}")
        return "\n".join(results)

# 데코레이터 패턴
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> int:
        pass
    
    @abstractmethod
    def description(self) -> str:
        pass

class SimpleCoffee(Coffee):
    def cost(self) -> int:
        return 3000
    
    def description(self) -> str:
        return "기본 커피"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self.coffee = coffee

class Milk(CoffeeDecorator):
    def cost(self) -> int:
        return self.coffee.cost() + 500
    
    def description(self) -> str:
        return f"{self.coffee.description()} + 우유"

def structural_patterns_example():
    # 1. 어댑터 패턴 예제
    print("1. 어댑터 패턴:")
    old_system = OldSystem()
    adapter = SystemAdapter(old_system)
    print(adapter.general_request())
    
    # 2. 브리지 패턴 예제
    print("\n2. 브리지 패턴:")
    red_circle = Circle(Red())
    blue_square = Square(Blue())
    print(red_circle.draw())
    print(blue_square.draw())
    
    # 3. 컴포지트 패턴 예제
    print("\n3. 컴포지트 패턴:")
    root = Composite("루트")
    branch1 = Composite("가지1")
    branch2 = Composite("가지2")
    leaf1 = Leaf("잎1")
    leaf2 = Leaf("잎2")
    leaf3 = Leaf("잎3")
    
    root.add(branch1)
    root.add(branch2)
    branch1.add(leaf1)
    branch1.add(leaf2)
    branch2.add(leaf3)
    
    print(root.operation())
    
    # 4. 데코레이터 패턴 예제
    print("\n4. 데코레이터 패턴:")
    coffee = SimpleCoffee()
    coffee_with_milk = Milk(coffee)
    coffee_with_double_milk = Milk(coffee_with_milk)
    
    print(f"{coffee.description()}: {coffee.cost()}원")
    print(f"{coffee_with_milk.description()}: {coffee_with_milk.cost()}원")
    print(f"{coffee_with_double_milk.description()}: {coffee_with_double_milk.cost()}원")

if __name__ == '__main__':
    structural_patterns_example()

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다")
        
    def introduce(self):
        return f"저는 {self.name}입니다"

class Flyable:
    def fly(self):
        return f"{self.name}가 날아갑니다"

class Swimmable:
    def swim(self):
        return f"{self.name}가 수영합니다"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "꽥꽥!"

def main():
    # 오리 객체 생성
    duck = Duck("도널드")
    
    print("=== 오리의 기본 행동 테스트 ===")
    print(duck.introduce())  # Animal 클래스에서 상속
    print(duck.speak())      # Duck 클래스에서 구현
    
    print("\n=== 오리의 다중 상속 능력 테스트 ===")
    print(duck.fly())        # Flyable 클래스에서 상속
    print(duck.swim())       # Swimmable 클래스에서 상속
    
    print("\n=== 클래스 정보 ===")
    print(f"Duck 클래스의 메서드 해결 순서(MRO):")
    for cls in Duck.__mro__:
        print(f"  - {cls.__name__}")

if __name__ == "__main__":
    main() 
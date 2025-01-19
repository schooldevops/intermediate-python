class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("하위 클래스에서 구현해야 합니다")
        
    def introduce(self):
        return f"저는 {self.name}입니다"

class Dog(Animal):
    def speak(self):
        return "멍멍!"
        
    def fetch(self):
        return f"{self.name}가 공을 가져옵니다"

class Cat(Animal):
    def speak(self):
        return "야옹!"
        
    def scratch(self):
        return f"{self.name}가 긁적긁적 합니다"

def main():
    # 동물 객체 생성
    dog = Dog("멍멍이")
    cat = Cat("야옹이")
    
    # 강아지 테스트
    print("=== 강아지 테스트 ===")
    print(dog.introduce())  # 상속받은 메서드
    print(dog.speak())      # 오버라이드된 메서드
    print(dog.fetch())      # Dog 클래스의 고유 메서드
    
    # 고양이 테스트
    print("\n=== 고양이 테스트 ===")
    print(cat.introduce())  # 상속받은 메서드
    print(cat.speak())      # 오버라이드된 메서드
    print(cat.scratch())    # Cat 클래스의 고유 메서드
    
    # NotImplementedError 테스트
    print("\n=== 추상 메서드 테스트 ===")
    try:
        generic_animal = Animal("동물")
        generic_animal.speak()
    except NotImplementedError as e:
        print(f"예상된 에러 발생: {e}")

if __name__ == "__main__":
    main() 
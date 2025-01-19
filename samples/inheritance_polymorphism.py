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

class Cat(Animal):
    def speak(self):
        return "야옹!"

class Duck(Animal):
    def speak(self):
        return "꽥꽥!"

def make_speak(animal):
    # 다형성: Animal을 상속받은 어떤 객체든 처리 가능
    print(f"{animal.name}의 소리: {animal.speak()}")

def process_animals(animals):
    # 여러 동물 객체들을 동일한 방식으로 처리
    for animal in animals:
        make_speak(animal)

def main():
    # 여러 동물 객체 생성
    dog = Dog("멍멍이")
    cat = Cat("야옹이")
    duck = Duck("도널드")
    
    print("=== 개별 동물 테스트 ===")
    make_speak(dog)
    make_speak(cat)
    make_speak(duck)
    
    print("\n=== 동물 리스트 처리 테스트 ===")
    animals = [dog, cat, duck]
    process_animals(animals)
    
    print("\n=== 다형성 에러 테스트 ===")
    try:
        # Animal 클래스를 직접 인스턴스화하면 NotImplementedError 발생
        generic_animal = Animal("미상의 동물")
        make_speak(generic_animal)
    except NotImplementedError as e:
        print(f"예상된 에러 발생: {e}")
    
    print("\n=== 타입 검사 ===")
    for animal in animals:
        print(f"{animal.name}는 Animal의 인스턴스인가요? {isinstance(animal, Animal)}")
        print(f"{animal.name}의 실제 타입: {type(animal).__name__}")

if __name__ == "__main__":
    main() 
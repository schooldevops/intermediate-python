# 파이썬 중급 및 고급 강좌 커리큘럼

## 중급 파이썬 강좌


### 01.강좌 개요 및 개발 환경 설정

- 학습 목표: 파이썬 개발 환경을 설정하고 기본적인 문법을 복습한다.

#### 파이썬 설치 및 IDE 설정

1. 파이썬 설치
   - [Python.org](https://www.python.org/downloads/)에서 최신 버전 다운로드 (3.x 버전 권장)
   - 설치 시 'Add Python to PATH' 옵션 체크
   - 설치 완료 후 터미널에서 `python --version` 명령어로 설치 확인

   macOS에서 Homebrew를 통한 설치:
   ```bash
   # Homebrew 설치 (이미 설치되어 있다면 생략)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Python 설치
   brew install python

   # Python 버전 확인
   python3 --version
   
   # Python 경로 확인
   which python3
   ```
   
   주의사항:
   - macOS의 경우 시스템 Python과 충돌을 피하기 위해 `python3` 명령어 사용
   - 필요한 경우 alias 설정으로 `python` 명령어 사용 가능:
     ```bash
     echo 'alias python=python3' >> ~/.zshrc  # zsh 사용시
     echo 'alias python=python3' >> ~/.bash_profile  # bash 사용시
     ```

2. 통합 개발 환경(IDE) 설정
   - PyCharm
     - JetBrains사의 전문적인 파이썬 IDE
     - Community Edition(무료) 또는 Professional Edition(유료) 선택
     - 디버깅, 코드 자동 완성 등 강력한 기능 제공
   
   - Visual Studio Code
     - Microsoft사의 무료 코드 에디터
     - Python Extension 설치 필요
     - 가볍고 확장성이 좋은 에디터
     - 다양한 플러그인 지원

3. 개발 환경 기본 설정
   - 가상환경 생성 및 활성화
     ```bash
     python -m venv venv
     source venv/bin/activate  # Windows: venv\Scripts\activate
     ```
   - 필수 패키지 설치
     ```bash
     pip install pytest
     pip install pylint
     pip install black
     ```

4. 코드 편집기 설정
   - 들여쓰기: 4칸 공백 사용
   - 자동 저장 활성화
   - 코드 포매터 설정 (Black 권장)
   - 린터 설정 (Pylint 권장)

#### 기본 문법 복습

1. 변수와 데이터 타입
   ```python
   # 숫자형
   integer_num = 10
   float_num = 3.14
   
   # 문자열
   text = "Hello Python"
   multi_line = """여러 줄의
   문자열 작성 가능"""
   
   # 불리언
   is_true = True
   is_false = False
   
   # 리스트, 튜플, 딕셔너리
   my_list = [1, 2, 3]  # 수정 가능
   my_tuple = (1, 2, 3)  # 수정 불가능
   my_dict = {'name': 'Python', 'version': 3.11}
   ```

2. 제어문
   ```python
   # if-elif-else 조건문
   score = 85
   if score >= 90:
       grade = 'A'
   elif score >= 80:
       grade = 'B'
   else:
       grade = 'C'

   # for 반복문
   for i in range(5):
       print(i)  # 0부터 4까지 출력
   
   # while 반복문
   count = 0
   while count < 3:
       print(count)
       count += 1
   ```

3. 함수 정의와 호출
   ```python
   # 기본 함수 정의
   def greet(name):
       return f"Hello, {name}!"

   # 기본값 매개변수
   def power(base, exponent=2):
       return base ** exponent

   # 가변 인자
   def sum_all(*args):
       return sum(args)

   # 함수 호출 예시
   print(greet("Python"))  # Hello, Python!
   print(power(3))  # 9
   print(sum_all(1, 2, 3, 4))  # 10
   ```

4. 리스트 컴프리헨션
   ```python
   # 기본 리스트 컴프리헨션
   squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
   
   # 조건부 리스트 컴프리헨션
   even_nums = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
   ```

5. 예외 처리
   ```python
   try:
       number = int(input("숫자를 입력하세요: "))
       result = 10 / number
   except ValueError:
       print("올바른 숫자를 입력하세요")
   except ZeroDivisionError:
       print("0으로 나눌 수 없습니다")
   else:
       print(f"결과: {result}")
   finally:
       print("프로그램 종료")
   ```

6. 클래스와 객체
   ```python
   class Dog:
       def __init__(self, name):
           self.name = name
           
       def bark(self):
           return f"{self.name}가 짖습니다!"

   # 객체 생성과 메서드 호출
   my_dog = Dog("멍멍이")
   print(my_dog.bark())  # 멍멍이가 짖습니다!
   ```

7. 모듈 임포트
   ```python
   # 기본 모듈 임포트
   import math
   print(math.pi)  # 3.141592...

   # 특정 함수만 임포트
   from random import randint
   print(randint(1, 6))  # 1부터 6 사이의 난수
   ```

8. 문자열 포매팅
   ```python
   name = "Python"
   version = 3.11
   
   # f-string (권장)
   print(f"Hello {name} {version}")
   
   # format() 메서드
   print("Hello {} {}".format(name, version))
   
   # % 연산자
   print("Hello %s %s" % (name, version))
   ```

#### 클래스와 객체

객체 지향 프로그래밍의 기본 개념과 파이썬에서의 구현 방법을 설명합니다.

1. 클래스 정의와 객체 생성

- car_class_test.py 참조 

   ```python
   class Car:
       # 클래스 변수
       total_cars = 0
       
       # 생성자 메서드
       def __init__(self, brand, model, year):
           # 인스턴스 변수
           self.brand = brand
           self.model = model
           self.year = year
           self.speed = 0
           Car.total_cars += 1
       
       # 인스턴스 메서드
       def accelerate(self, speed_increase):
           self.speed += speed_increase
           return f"현재 속도: {self.speed}km/h"
       
       def brake(self, speed_decrease):
           self.speed = max(0, self.speed - speed_decrease)
           return f"현재 속도: {self.speed}km/h"
       
       # 특수 메서드 (매직 메서드)
       def __str__(self):
           return f"{self.year} {self.brand} {self.model}"

   def main():
       # 객체 생성과 메서드 호출
       my_car = Car("현대", "아반떼", 2023)
       print(my_car)  # 2023 현대 아반떼
       print(my_car.accelerate(30))  # 현재 속도: 30km/h
       print(my_car.brake(10))  # 현재 속도: 20km/h
       
       # 추가 테스트
       print(f"총 자동차 수: {Car.total_cars}")
       
       # 다른 자동차 인스턴스 생성
       another_car = Car("기아", "K5", 2022)
       print(another_car)
       print(another_car.accelerate(50))
       print(f"총 자동차 수: {Car.total_cars}")

   if __name__ == "__main__":
       main()
   ```

2. 접근 제어와 프로퍼티

- class_access_test.py 참조 

   ```python
   class BankAccount:
       def __init__(self, owner, initial_balance=0):
           if initial_balance < 0:
               raise ValueError("초기 잔액은 음수가 될 수 없습니다")
           self._owner = owner    # protected 변수
           self.__balance = initial_balance  # private 변수
       
       @property
       def owner(self):
           return self._owner
           
       @property 
       def balance(self):
           return self.__balance
       
       @balance.setter
       def balance(self, amount):
           self.__validate_amount(amount)
           self.__balance = amount
           
       def deposit(self, amount):
           self.__validate_amount(amount)
           self.__balance += amount
           return self.__get_balance_message()
           
       def withdraw(self, amount):
           self.__validate_amount(amount)
           if amount > self.__balance:
               raise ValueError("잔액이 부족합니다")
           self.__balance -= amount
           return self.__get_balance_message()
           
       def __validate_amount(self, amount):
           if amount < 0:
               raise ValueError("금액은 음수가 될 수 없습니다")
               
       def __get_balance_message(self):
           return f"현재 잔액: {self.__balance}원"
   
   # 사용 예시
   account = BankAccount("홍길동", 10000)
   print(account.balance)  # 10000
   account.balance = 20000  
   print(account.deposit(5000))  # 현재 잔액: 25000원
   print(account.withdraw(3000))  # 현재 잔액: 22000원
   ```

3. 정적 메서드와 클래스 메서드

- class_static_test.py 참조 

   ```python
   class MathUtils:
       # 수학 유틸리티 클래스를 정의합니다
       pi = 3.14159  # 원주율을 클래스 변수로 정의합니다
       
       @staticmethod  # 정적 메서드 데코레이터를 사용합니다
       def is_even(number):  # 숫자가 짝수인지 확인하는 정적 메서드입니다
           return number % 2 == 0  # 2로 나눈 나머지가 0이면 짝수입니다
       
       @classmethod  # 클래스 메서드 데코레이터를 사용합니다
       def circle_area(cls, radius):  # 원의 넓이를 계산하는 클래스 메서드입니다
           return cls.pi * radius * radius  # πr² 공식을 사용하여 원의 넓이를 계산합니다
       
       @classmethod  # 클래스 메서드 데코레이터를 사용합니다
       def update_pi(cls, new_pi):  # pi 값을 업데이트하는 클래스 메서드입니다
           cls.pi = new_pi  # 클래스 변수 pi를 새로운 값으로 업데이트합니다
   
   # 정적 메서드와 클래스 메서드 사용 예시
   print(MathUtils.is_even(4))  # 정적 메서드를 호출하여 4가 짝수인지 확인합니다
   print(MathUtils.circle_area(5))  # 클래스 메서드를 호출하여 반지름이 5인 원의 넓이를 계산합니다
   ```

주요 개념:
- 클래스: 객체의 설계도
- 객체(인스턴스): 클래스를 기반으로 생성된 실체
- 인스턴스 변수: 각 객체마다 독립적으로 가지는 변수
- 클래스 변수: 클래스의 모든 인스턴스가 공유하는 변수
- 메서드: 클래스 내에 정의된 함수
- 생성자: 객체가 생성될 때 호출되는 특수 메서드
- 접근 제어: private(`__`), protected(`_`) 변수 지정
- 프로퍼티: getter/setter 메서드를 대체하는 파이썬의 방식
- 정적 메서드: 인스턴스 없이 호출 가능한 메서드
- 클래스 메서드: 클래스를 첫 번째 인자로 받는 메서드

#### 상속과 다형성

객체 지향 프로그래밍의 핵심 개념인 상속과 다형성의 구현 방법을 설명합니다.

1. 기본 상속

- inheritance_basic.py 참조 
   ```python
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
   
   # 상속 사용 예시
   dog = Dog("멍멍이")
   cat = Cat("야옹이")
   
   print(dog.introduce())  # 저는 멍멍이입니다
   print(dog.speak())      # 멍멍!
   print(dog.fetch())      # 멍멍이가 공을 가져옵니다
   
   print(cat.introduce())  # 저는 야옹이입니다
   print(cat.speak())      # 야옹!
   print(cat.scratch())    # 야옹이가 긁적긁적 합니다
   ```

2. 다중 상속

- inheritance_multiple.py 참조 

   ```python
   class Flyable:
       def fly(self):
           return f"{self.name}가 날아갑니다"
   
   class Swimmable:
       def swim(self):
           return f"{self.name}가 수영합니다"
   
   class Duck(Animal, Flyable, Swimmable):
       def speak(self):
           return "꽥꽥!"
   
   # 다중 상속 사용 예시
   duck = Duck("도널드")
   print(duck.speak())  # 꽥꽥!
   print(duck.fly())    # 도널드가 날아갑니다
   print(duck.swim())   # 도널드가 수영합니다
   ```

3. 메서드 오버라이딩과 super()

- inheritance_override.py 참조 

   ```python
   class Vehicle:
       def __init__(self, brand, model, year):
           self.brand = brand
           self.model = model
           self.year = year
           
       def start(self):
           return f"{self.brand} {self.model}의 시동을 겁니다"
           
       def info(self):
           return f"{self.year} {self.brand} {self.model}"
   
   class ElectricCar(Vehicle):
       def __init__(self, brand, model, year, battery_capacity):
           super().__init__(brand, model, year)
           self.battery_capacity = battery_capacity
           
       def start(self):
           basic_start = super().start()
           return f"{basic_start} (배터리 충전량: {self.battery_capacity}%)"
           
       def charge(self):
           return f"{self.model}를 충전합니다"
   
   # 메서드 오버라이딩 예시
   normal_car = Vehicle("Toyota", "Camry", 2022)
   electric_car = ElectricCar("Tesla", "Model 3", 2023, 85)
   
   print(normal_car.start())   # Toyota Camry의 시동을 겁니다
   print(electric_car.start()) # Tesla Model 3의 시동을 겁니다 (배터리 충전량: 85%)
   print(electric_car.charge()) # Model 3를 충전합니다
   ```

4. 다형성 활용

- inheritance_polymorphism.py 참조 

   ```python
   def make_speak(animal):
       # 다형성: Animal을 상속받은 어떤 객체든 처리 가능
       print(f"{animal.name}의 소리: {animal.speak()}")
   
   def process_animals(animals):
       # 여러 동물 객체들을 동일한 방식으로 처리
       for animal in animals:
           make_speak(animal)
   
   # 다형성 활용 예시
   dog = Dog("멍멍이")
   cat = Cat("야옹이")
   duck = Duck("도널드")
   
   animals = [dog, cat, duck]
   process_animals(animals)
   # 출력:
   # 멍멍이의 소리: 멍멍!
   # 야옹이의 소리: 야옹!
   # 도널드의 소리: 꽥꽥!
   ```

주요 개념:
- 상속: 기존 클래스의 속성과 메서드를 새로운 클래스가 재사용
- 다중 상속: 여러 클래스로부터 속성과 메서드를 상속
- 메서드 오버라이딩: 상속받은 메서드를 하위 클래스에서 재정의
- super(): 상위 클래스의 메서드를 호출
- 다형성: 같은 인터페이스를 통해 다양한 객체를 처리
- 추상화: 공통된 특성을 추출하여 상위 클래스로 정의

#### 캡슐화

객체의 속성과 메서드를 하나로 묶고, 실제 구현 내용의 일부를 외부에 감추어 은닉하는 방법을 설명합니다.

1. 기본적인 캡슐화

- capsule_basic.py 참조 

   ```python
   class Employee:
       def __init__(self, name, salary):
           self._name = name          # protected 속성
           self.__salary = salary     # private 속성
           
       def get_salary(self):
           return self.__salary
           
       def set_salary(self, new_salary):
           if new_salary > 0:
               self.__salary = new_salary
           else:
               raise ValueError("급여는 0보다 커야 합니다")
               
       def _internal_method(self):    # protected 메서드
           return "내부 처리 로직"
           
       def __private_method(self):    # private 메서드
           return "비공개 처리 로직"

   # 사용 예시
   emp = Employee("홍길동", 3000000)
   print(emp._name)         # protected 속성 접근 가능 (권장하지 않음)
   # print(emp.__salary)    # private 속성 직접 접근 불가 (AttributeError 발생)
   print(emp.get_salary())  # getter 메서드를 통한 접근
   emp.set_salary(3500000)  # setter 메서드를 통한 수정
   ```

2. 프로퍼티를 이용한 캡슐화

- capsule_property.py 참조 

   ```python
   class Product:
       def __init__(self, name, price):
           self._name = name
           self.__price = price
           self.__sales_count = 0
           
       @property
       def name(self):
           return self._name
           
       @property
       def price(self):
           return self.__price
           
       @price.setter
       def price(self, new_price):
           if new_price < 0:
               raise ValueError("가격은 음수가 될 수 없습니다")
           self.__price = new_price
           
       @property
       def total_sales(self):
           return self.__price * self.__sales_count
           
       def sell(self):
           self.__sales_count += 1
           self.__update_sales_record()
           
       def __update_sales_record(self):
           # 비공개 메서드: 판매 기록 업데이트 로직
           pass

   # 프로퍼티 사용 예시
   product = Product("노트북", 1200000)
   print(product.name)      # 프로퍼티를 통한 읽기
   print(product.price)     # 프로퍼티를 통한 읽기
   product.price = 1300000  # 프로퍼티를 통한 쓰기
   product.sell()
   print(product.total_sales)
   ```

3. 데코레이터를 활용한 캡슐화

- capsule_decorator.py 참조 

   ```python
   def validate_age(func):
       def wrapper(self, age):
           if 0 <= age <= 150:
               return func(self, age)
           raise ValueError("나이는 0-150 사이여야 합니다")
       return wrapper

   class Person:
       def __init__(self, name, age):
           self.__name = name
           self.__age = self.__validate_age(age)
           
       @property
       def name(self):
           return self.__name
           
       @property
       def age(self):
           return self.__age
           
       @age.setter
       @validate_age
       def age(self, new_age):
           self.__age = new_age
           
       def __validate_age(self, age):
           if 0 <= age <= 150:
               return age
           raise ValueError("나이는 0-150 사이여야 합니다")

   # 데코레이터를 활용한 캡슐화 예시
   person = Person("홍길동", 25)
   print(person.name)    # 프로퍼티를 통한 이름 접근
   print(person.age)     # 프로퍼티를 통한 나이 접근
   person.age = 30      # 검증된 나이 설정
   # person.age = 200   # ValueError 발생
   ```

주요 개념:
- 데이터 은닉: private(`__`) 및 protected(`_`) 멤버 사용
- 접근 제어: getter/setter 메서드 또는 프로퍼티를 통한 접근 제어
- 데이터 검증: setter에서 데이터 유효성 검사
- 캡슐화 이점: 
  - 데이터 보호
  - 유지보수성 향상
  - 데이터 무결성 보장
  - 구현 세부사항 숨김


### 03.고급 데이터 구조

- 학습 목표: 파이썬의 다양한 데이터 구조를 이해하고 활용한다.

#### 리스트

파이썬의 리스트는 순서가 있는 시퀀스 자료형으로, 다양한 타입의 요소들을 담을 수 있는 동적 배열입니다.

1. 리스트 기본 특징
   - 순서가 있는 데이터 구조
   - 중복된 값 허용
   - 다양한 자료형 혼합 가능
   - 크기 동적 변경 가능
   - 인덱싱과 슬라이싱 지원

2. 리스트 생성과 조작

- list_basic.py 참조 

   ```python
   # 리스트 생성
   numbers = [1, 2, 3, 4, 5]
   mixed = [1, "Python", 3.14, True, [1, 2, 3]]
   empty = []
   list_from_range = list(range(5))  # [0, 1, 2, 3, 4]

   # 리스트 조작
   numbers.append(6)        # 끝에 추가: [1, 2, 3, 4, 5, 6]
   numbers.insert(0, 0)     # 특정 위치에 추가: [0, 1, 2, 3, 4, 5, 6]
   numbers.extend([7, 8])   # 여러 요소 추가: [0, 1, 2, 3, 4, 5, 6, 7, 8]
   numbers.remove(0)        # 특정 값 제거: [1, 2, 3, 4, 5, 6, 7, 8]
   popped = numbers.pop()   # 마지막 요소 제거 및 반환
   numbers.clear()          # 모든 요소 제거
   ```

3. 리스트 인덱싱과 슬라이싱

- list_indexing_slicing.py 참조 

   ```python
   fruits = ["사과", "바나나", "오렌지", "포도", "망고"]
   
   # 인덱싱
   print(fruits[0])       # 첫 번째 요소: 사과
   print(fruits[-1])      # 마지막 요소: 망고
   
   # 슬라이싱
   print(fruits[1:3])     # ['바나나', '오렌지']
   print(fruits[:3])      # ['사과', '바나나', '오렌지']
   print(fruits[2:])      # ['오렌지', '포도', '망고']
   print(fruits[::2])     # ['사과', '오렌지', '망고']
   ```

4. 리스트 메서드와 내장 함수

- list_methods_functions.py 참조 

   ```python
   numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
   
   # 정렬
   sorted_numbers = sorted(numbers)  # 새로운 정렬된 리스트 반환
   numbers.sort()                    # 원본 리스트 정렬
   numbers.reverse()                 # 리스트 뒤집기
   
   # 검색과 계산
   count = numbers.count(5)          # 특정 값의 개수
   index = numbers.index(4)          # 특정 값의 첫 번째 위치
   total = sum(numbers)              # 모든 요소의 합
   length = len(numbers)             # 리스트 길이
   maximum = max(numbers)            # 최대값
   minimum = min(numbers)            # 최소값
   ```

5. 리스트 컴프리헨션

- list_comprehension.py 참조 

   ```python
   # 기본 형태
   squares = [x**2 for x in range(10)]
   
   # 조건문 포함
   even_squares = [x**2 for x in range(10) if x % 2 == 0]
   
   # 중첩 반복문
   matrix = [[i+j for j in range(3)] for i in range(3)]
   
   # if-else 포함
   numbers = [x if x > 0 else 0 for x in range(-5, 5)]
   ```

6. 리스트 복사

- list_copy.py 참조 

   ```python
   # 얕은 복사
   original = [1, [2, 3], 4]
   shallow_copy = original.copy()
   shallow_copy_2 = original[:]
   
   # 깊은 복사
   import copy
   deep_copy = copy.deepcopy(original)
   ```

주요 활용:
- 데이터 수집 및 저장
- 순차적 데이터 처리
- 스택/큐 구현
- 동적 데이터 관리
- 데이터 정렬 및 검색

#### 튜플(Tuple)

튜플은 불변(immutable)한 순서가 있는 시퀀스 자료형입니다. 리스트와 유사하지만 한번 생성된 후에는 수정할 수 없습니다.

1. 튜플의 특징
   - 순서가 있는 데이터 구조
   - 불변(immutable) 객체
   - 중복된 값 허용
   - 다양한 자료형 혼합 가능
   - 인덱싱과 슬라이싱 지원
   - 리스트보다 메모리 효율적

2. 튜플 생성과 기본 사용

- tuple_basic.py 참조 

   ```python
   # 튜플 생성
   empty_tuple = ()
   single_tuple = (1,)  # 요소가 하나일 때는 콤마 필수
   numbers = (1, 2, 3, 4, 5)
   mixed = (1, "Python", 3.14, True, (1, 2, 3))
   
   # 패킹과 언패킹
   coordinates = 12.5, 34.8  # 패킹
   x, y = coordinates       # 언패킹
   
   # 여러 변수 할당
   a, b, c = 1, 2, 3
   ```

3. 튜플 인덱싱과 슬라이싱

- tuple_indexing_slicing.py 참조 

   ```python
   colors = ("빨강", "주황", "노랑", "초록", "파랑")
   
   # 인덱싱
   print(colors[0])       # 첫 번째 요소: 빨강
   print(colors[-1])      # 마지막 요소: 파랑
   
   # 슬라이싱
   print(colors[1:3])     # ('주황', '노랑')
   print(colors[:3])      # ('빨강', '주황', '노랑')
   print(colors[2:])      # ('노랑', '초록', '파랑')
   ```

4. 튜플 메서드와 내장 함수

- tuple_methods.py 참조 

   ```python
   numbers = (1, 2, 3, 2, 4, 2, 5)
   
   # 메서드
   count = numbers.count(2)    # 특정 값의 개수: 3
   index = numbers.index(4)    # 특정 값의 첫 번째 위치: 4
   
   # 내장 함수
   length = len(numbers)       # 튜플 길이
   maximum = max(numbers)      # 최대값
   minimum = min(numbers)      # 최소값
   sum_all = sum(numbers)      # 모든 요소의 합
   ```

5. 튜플의 활용

- tuple_usage.py 참조 

   ```python
   # 함수에서 여러 값 반환
   def get_coordinates():
       return (3, 4)
   
   # 튜플 언패킹으로 받기
   x, y = get_coordinates()
   
   # 딕셔너리 메서드 반환값
   dict_items = {'a': 1, 'b': 2}.items()  # dict_items 객체는 튜플의 시퀀스
   
   # 튜플을 키로 사용
   locations = {(0, 0): 'origin', (1, 0): 'right', (0, 1): 'up'}
   ```

6. 네임드 튜플 사용

- tuple_named.py 참조 

   ```python
   from collections import namedtuple
   
   # 네임드 튜플 정의
   Point = namedtuple('Point', ['x', 'y'])
   Person = namedtuple('Person', 'name age job')
   
   # 네임드 튜플 생성
   p = Point(11, y=22)
   bob = Person('Bob', 30, 'developer')
   
   # 속성으로 접근
   print(p.x, p.y)           # 11 22
   print(bob.name, bob.job)  # Bob developer
   ```

주요 활용:
- 함수의 반환 값
- 불변성이 필요한 데이터
- 딕셔너리의 키
- 네임드 튜플로 간단한 클래스 대체
- 데이터 무결성 보장
- 메모리 효율적인 자료구조 구현

#### 집합(Set)

집합은 중복되지 않은 요소들의 순서 없는 컬렉션입니다. 수학의 집합 개념을 구현한 자료형입니다.

1. 집합의 특징
   - 중복된 값을 허용하지 않음
   - 순서가 없는 자료구조
   - 수정 가능(mutable)
   - 해시 가능한 객체만 포함 가능
   - 집합 연산 지원 (합집합, 교집합, 차집합 등)

2. 집합 생성과 기본 조작

- set_basic.py 참조 

   ```python
   # 집합 생성
   empty_set = set()
   numbers = {1, 2, 3, 4, 5}
   fruits = {'apple', 'banana', 'orange'}
   
   # 중복 제거
   numbers_with_duplicates = {1, 2, 2, 3, 3, 4, 4, 5, 5}
   print(numbers_with_duplicates)  # {1, 2, 3, 4, 5}
   
   # 집합 조작
   fruits.add('grape')            # 요소 추가
   fruits.remove('banana')        # 요소 제거 (없으면 KeyError)
   fruits.discard('melon')       # 요소 제거 (없어도 에러 없음)
   popped = fruits.pop()         # 임의의 요소 제거 및 반환
   fruits.clear()                # 모든 요소 제거
   ```

3. 집합 연산

- set_operations.py 참조 

   ```python
   set1 = {1, 2, 3, 4, 5}
   set2 = {4, 5, 6, 7, 8}
   
   # 집합 연산
   union = set1 | set2              # 합집합
   intersection = set1 & set2        # 교집합
   difference = set1 - set2          # 차집합
   symmetric_diff = set1 ^ set2      # 대칭차집합
   
   # 메서드를 이용한 연산
   union = set1.union(set2)
   intersection = set1.intersection(set2)
   difference = set1.difference(set2)
   symmetric_diff = set1.symmetric_difference(set2)
   ```

4. 집합 관계 연산

- set_relations.py 참조 

   ```python
   A = {1, 2, 3}
   B = {1, 2, 3, 4, 5}
   C = {6, 7, 8}
   
   # 부분집합과 상위집합 확인
   print(A.issubset(B))      # True: A는 B의 부분집합
   print(B.issuperset(A))    # True: B는 A의 상위집합
   
   # 서로소 집합 확인
   print(A.isdisjoint(C))    # True: A와 C는 서로소
   ```

5. 집합 컴프리헨션

- set_comprehension.py 참조 

   ```python
   # 기본 집합 컴프리헨션
   squares = {x**2 for x in range(10)}
   
   # 조건문을 포함한 집합 컴프리헨션
   even_squares = {x**2 for x in range(10) if x % 2 == 0}
   
   # 다중 조건
   numbers = {x for x in range(100) if x % 2 == 0 if x % 3 == 0}
   ```

6. 집합의 활용

- set_usage.py 참조 

   ```python
   # 중복 제거
   numbers_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
   unique_numbers = list(set(numbers_list))
   
   # 멤버십 테스트
   valid_users = {'alice', 'bob', 'charlie'}
   user = 'alice'
   if user in valid_users:
       print("유효한 사용자입니다")
   
   # 데이터 필터링
   numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
   evens = {x for x in numbers if x % 2 == 0}
   ```

주요 활용:
- 중복 제거
- 집합 연산 (합집합, 교집합, 차집합)
- 멤버십 테스트
- 고유 요소 관리
- 데이터 필터링
- 수학적 집합 연산 구현

#### 딕셔너리(Dictionary)

딕셔너리는 키(key)와 값(value)의 쌍으로 이루어진 자료구조입니다. 파이썬에서 가장 많이 사용되는 자료구조 중 하나로, 데이터를 효율적으로 저장하고 검색할 수 있습니다.

- dict_basic.py 참조

   ```python
   # 딕셔너리 생성
   student = {
       'name': '김철수',
       'age': 20,
       'grades': [90, 85, 88]
   }

   # 딕셔너리 접근
   print(student['name'])     # 김철수
   print(student.get('age'))  # 20

   # 딕셔너리 수정
   student['age'] = 21
   student['major'] = '컴퓨터공학'  # 새로운 키-값 추가

   # 딕셔너리 삭제
   del student['grades']

   # 딕셔너리 메서드
   print(student.keys())      # 모든 키 출력
   print(student.values())    # 모든 값 출력
   print(student.items())     # 모든 키-값 쌍 출력
   ```



#### 데이터 구조의 활용 예제

데이터 구조를 실제 상황에서 어떻게 활용하는지 살펴보겠습니다.

- data_structure_usage.py 참조

   ```python
   # 여러 데이터 구조를 조합한 학생 관리 시스템
   class StudentManagement:
       def __init__(self):
           self.students = {}  # 딕셔너리로 학생 정보 관리
           self.courses = set()  # 세트로 과목 관리
           self.grades = []  # 리스트로 성적 이력 관리

       def add_student(self, student_id, name):
           self.students[student_id] = {
               'name': name,
               'courses': set(),
               'grades': {}
           }

       def add_course(self, course_name):
           self.courses.add(course_name)

       def enroll_course(self, student_id, course_name):
           if course_name in self.courses:
               self.students[student_id]['courses'].add(course_name)
               return True
           return False

       def add_grade(self, student_id, course_name, grade):
           if course_name in self.students[student_id]['courses']:
               self.students[student_id]['grades'][course_name] = grade
               self.grades.append((student_id, course_name, grade))

   # 사용 예시
   manager = StudentManagement()
   manager.add_student("2024001", "김철수")
   manager.add_course("파이썬 프로그래밍")
   manager.enroll_course("2024001", "파이썬 프로그래밍")
   manager.add_grade("2024001", "파이썬 프로그래밍", 95)
   ```


### 04.예외 처리 및 파일 입출력

- 학습 목표: 예외 처리 방법과 파일 입출력 기능을 익힌다.

#### 예외 처리 구문

파이썬의 예외 처리 방법에 대해 알아보겠습니다.

- exception_handling.py 참조

   ```python
   def divide_numbers(a, b):
       try:
           result = a / b
           return result
       except ZeroDivisionError:
           print("0으로 나눌 수 없습니다.")
           return None
       except TypeError:
           print("숫자만 입력해주세요.")
           return None
       finally:
           print("계산이 완료되었습니다.")

   # 예외 처리 예시
   print(divide_numbers(10, 2))    # 정상 실행: 5.0
   print(divide_numbers(10, 0))    # ZeroDivisionError 발생
   print(divide_numbers(10, '2'))  # TypeError 발생

   # 사용자 정의 예외
   class InvalidAgeError(Exception):
       def __init__(self, age, message="나이는 0보다 커야 합니다."):
           self.age = age
           self.message = message
           super().__init__(self.message)

   def set_age(age):
       if age <= 0:
           raise InvalidAgeError(age)
       return age

   # 사용자 정의 예외 처리
   try:
       age = set_age(-5)
   except InvalidAgeError as e:
       print(f"에러 발생: {e.message}")
   ```


#### 파일 읽기 및 쓰기

파이썬에서 파일을 다루는 방법에 대해 알아보겠습니다.

- file_io.py 참조

   ```python
   # 텍스트 파일 쓰기
   with open('example.txt', 'w', encoding='utf-8') as f:
       f.write('안녕하세요!\n')
       f.write('파이썬 파일 입출력 예제입니다.\n')

   # 텍스트 파일 읽기
   with open('example.txt', 'r', encoding='utf-8') as f:
       # 전체 내용 읽기
       content = f.read()
       print(content)

   # 파일 한 줄씩 읽기
   with open('example.txt', 'r', encoding='utf-8') as f:
       for line in f:
           print(line.strip())

   # CSV 파일 다루기
   import csv

   # CSV 파일 쓰기
   with open('students.csv', 'w', newline='', encoding='utf-8') as f:
       writer = csv.writer(f)
       writer.writerow(['이름', '나이', '학과'])
       writer.writerow(['김철수', 20, '컴퓨터공학'])
       writer.writerow(['이영희', 21, '전자공학'])

   # CSV 파일 읽기
   with open('students.csv', 'r', encoding='utf-8') as f:
       reader = csv.reader(f)
       for row in reader:
           print(row)
   ```






### 05. 모듈과 패키지

- 학습 목표: 모듈과 패키지를 활용하여 코드의 재사용성을 높인다.

### 모듈 만들기

파이썬에서 모듈을 만들고 사용하는 방법을 알아보겠습니다.

- my_module.py 참조

   ```python
   # my_module.py
   def greet(name):
       return f"안녕하세요, {name}님!"

   def calculate_sum(numbers):
       return sum(numbers)

   class Calculator:
       def __init__(self):
           self.result = 0

       def add(self, x, y):
           self.result = x + y
           return self.result

       def subtract(self, x, y):
           self.result = x - y
           return self.result

   # 모듈 테스트용 코드
   if __name__ == "__main__":
       print(greet("김철수"))
       print(calculate_sum([1, 2, 3, 4, 5]))
   ```

- module_usage.py 참조

   ```python
   # 모듈 사용 예시
   import my_module
   from my_module import Calculator

   # 함수 사용
   print(my_module.greet("이영희"))
   numbers = [1, 2, 3, 4, 5]
   total = my_module.calculate_sum(numbers)
   print(f"합계: {total}")

   # 클래스 사용
   calc = Calculator()
   result1 = calc.add(10, 5)
   result2 = calc.subtract(20, 7)
   print(f"덧셈 결과: {result1}")
   print(f"뺄셈 결과: {result2}")
   ```

#### 패키지 구조 이해

파이썬 패키지의 구조와 사용법에 대해 알아보겠습니다.

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

- package_example.py 참조

   ```python
   # my_package/__init__.py
   from .module1 import greet
   from .module2 import calculate_sum
   
   # my_package/module1.py
   def greet(name):
       return f"안녕하세요, {name}님!"

   # my_package/module2.py
   def calculate_sum(numbers):
       return sum(numbers)

   # my_package/subpackage/__init__.py
   from .module3 import process_data

   # my_package/subpackage/module3.py
   def process_data(data):
       return [x * 2 for x in data]

   # 패키지 사용 예시
   from my_package import greet, calculate_sum
   from my_package.subpackage import process_data

   print(greet("김철수"))
   print(calculate_sum([1, 2, 3, 4, 5]))
   print(process_data([1, 2, 3, 4, 5]))
   ```

#### 고차 함수

고차 함수의 개념과 사용법을 알아보겠습니다.

- higher_order_functions.py 참조

   ```python
   # 함수를 인자로 받는 고차 함수
   def apply_operation(func, x, y):
       return func(x, y)

   def add(x, y):
       return x + y

   def multiply(x, y):
       return x * y

   # 고차 함수 사용
   result1 = apply_operation(add, 5, 3)      # 8
   result2 = apply_operation(multiply, 4, 2)  # 8

   # 함수를 반환하는 고차 함수
   def create_multiplier(factor):
       def multiplier(x):
           return x * factor
       return multiplier

   # 클로저 생성
   double = create_multiplier(2)
   triple = create_multiplier(3)

   print(double(5))  # 10
   print(triple(5))  # 15
   ```

#### 람다 함수

람다 함수의 사용법과 활용 예제를 알아보겠습니다.

- lambda_functions.py 참조

   ```python
   # 기본 람다 함수
   square = lambda x: x**2
   print(square(5))  # 25

   # 람다 함수를 인자로 사용
   numbers = [1, 2, 3, 4, 5]
   squared_numbers = list(map(lambda x: x**2, numbers))
   print(squared_numbers)  # [1, 4, 9, 16, 25]

   # 람다 함수를 정렬에 사용
   students = [
       {'name': '김철수', 'score': 85},
       {'name': '이영희', 'score': 92},
       {'name': '박민수', 'score': 78}
   ]

   # 점수를 기준으로 정렬
   sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
   for student in sorted_students:
       print(f"{student['name']}: {student['score']}")
   ```

#### map, filter, reduce

함수형 프로그래밍의 주요 함수들의 사용법을 알아보겠습니다.

- functional_programming.py 참조

   ```python
   from functools import reduce

   # map 예제: 모든 요소를 제곱
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x**2, numbers))
   print(squared)  # [1, 4, 9, 16, 25]

   # filter 예제: 짝수만 필터링
   even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   print(even_numbers)  # [2, 4]

   # reduce 예제: 모든 숫자의 곱 계산
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # 120

   # 실제 활용 예제
   # 학생들의 점수를 처리하는 예제
   scores = [
       {'name': '김철수', 'score': 85},
       {'name': '이영희', 'score': 92},
       {'name': '박민수', 'score': 78}
   ]

   # 점수만 추출
   scores_only = list(map(lambda x: x['score'], scores))

   # 80점 이상인 학생만 필터링
   passed_students = list(filter(lambda x: x['score'] >= 80, scores))

   # 총점 계산
   total_score = reduce(lambda x, y: x + y['score'], scores[1:], scores[0]['score'])

   # 평균 계산
   average_score = total_score / len(scores)

   print(f"점수 목록: {scores_only}")
   print(f"합격자 명단: {[student['name'] for student in passed_students]}")
   print(f"총점: {total_score}")
   print(f"평균: {average_score:.2f}")
   ```

### 06. 함수형 프로그래밍

- 학습 목표: 함수형 프로그래밍의 개념을 이해하고 적용한다.

#### 고차 함수

#### 람다 함수

#### map, filter, reduce





### 07. 데이터 처리 및 분석

- 학습 목표: 파이썬을 이용한 데이터 처리 기법을 익힌다.

#### NumPy 기초

#### Pandas를 이용한 데이터 분석





### 08. 웹 스크래핑

- 학습 목표: 웹에서 데이터를 추출하는 방법을 배운다.

#### BeautifulSoup 사용법

#### 웹 데이터 수집 실습





#### NumPy 기초

NumPy의 기본 사용법과 주요 기능을 알아보겠습니다.

- numpy_basics.py 참조

   ```python
   import numpy as np

   # 배열 생성
   arr1 = np.array([1, 2, 3, 4, 5])
   arr2 = np.zeros((3, 3))  # 3x3 영행렬
   arr3 = np.ones((2, 4))   # 2x4 1행렬
   arr4 = np.random.rand(3, 3)  # 3x3 랜덤 행렬

   # 배열 연산
   print(arr1 * 2)          # 모든 원소에 2를 곱함
   print(arr1 + arr1)       # 같은 크기의 배열끼리 덧셈
   print(np.sqrt(arr1))     # 제곱근 계산

   # 행렬 연산
   matrix1 = np.array([[1, 2], [3, 4]])
   matrix2 = np.array([[5, 6], [7, 8]])
   
   print(np.dot(matrix1, matrix2))  # 행렬 곱
   print(matrix1.T)                 # 전치 행렬

   # 통계 함수
   data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
   print(f"평균: {np.mean(data)}")
   print(f"표준편차: {np.std(data)}")
   print(f"최댓값: {np.max(data)}")
   print(f"최솟값: {np.min(data)}")

   # 배열 인덱싱과 슬라이싱
   arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
   print(arr[0, 1])     # 첫 번째 행, 두 번째 열의 원소
   print(arr[:, 1])     # 모든 행의 두 번째 열
   print(arr[1:, :2])   # 두 번째 행부터, 처음 두 열까지
   ```

#### Pandas를 이용한 데이터 분석

Pandas를 사용한 데이터 분석 방법을 알아보겠습니다.

- pandas_analysis.py 참조

   ```python
   import pandas as pd
   import numpy as np

   # DataFrame 생성
   data = {
       '이름': ['김철수', '이영희', '박민수', '최지은', '정대호'],
       '나이': [20, 21, 19, 22, 20],
       '성별': ['남', '여', '남', '여', '남'],
       '점수': [85, 92, 78, 95, 88]
   }
   df = pd.DataFrame(data)

   # 기본 정보 확인
   print("데이터프레임 정보:")
   print(df.info())
   print("\n기술 통계량:")
   print(df.describe())

   # 데이터 필터링
   print("\n90점 이상 학생:")
   high_scores = df[df['점수'] >= 90]
   print(high_scores)

   # 그룹화 및 집계
   print("\n성별 평균 점수:")
   gender_scores = df.groupby('성별')['점수'].mean()
   print(gender_scores)

   # 데이터 정렬
   print("\n점수 기준 내림차순 정렬:")
   sorted_df = df.sort_values(by='점수', ascending=False)
   print(sorted_df)

   # 새로운 열 추가
   df['학점'] = pd.cut(df['점수'], 
                    bins=[0, 60, 70, 80, 90, 100],
                    labels=['F', 'D', 'C', 'B', 'A'])
   print("\n학점 추가된 데이터:")
   print(df)

   # CSV 파일로 저장
   df.to_csv('student_grades.csv', index=False, encoding='utf-8')

   # CSV 파일 읽기
   df_read = pd.read_csv('student_grades.csv', encoding='utf-8')

   # 피벗 테이블
   pivot_table = pd.pivot_table(df, 
                              values='점수',
                              index='성별',
                              columns='학점',
                              aggfunc='count',
                              fill_value=0)
   print("\n성별/학점별 학생 수 피벗 테이블:")
   print(pivot_table)

   # 데이터 시각화 예제 (matplotlib 필요)
   import matplotlib.pyplot as plt

   plt.figure(figsize=(10, 6))
   df['점수'].hist(bins=10)
   plt.title('학생 점수 분포')
   plt.xlabel('점수')
   plt.ylabel('학생 수')
   plt.savefig('score_distribution.png')
   plt.close()
   ```

#### BeautifulSoup 사용법

웹 스크래핑을 위한 BeautifulSoup 사용법을 알아보겠습니다.

- web_scraping.py 참조

   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd

   # 웹 페이지 가져오기
   def fetch_webpage(url):
       try:
           response = requests.get(url)
           response.raise_for_status()  # 오류 발생 시 예외 발생
           return response.text
       except requests.RequestException as e:
           print(f"에러 발생: {e}")
           return None

   # BeautifulSoup 객체 생성
   url = 'https://example.com'
   html_content = fetch_webpage(url)
   if html_content:
       soup = BeautifulSoup(html_content, 'html.parser')

       # 제목 추출
       title = soup.find('h1').text
       print(f"페이지 제목: {title}")

       # 모든 링크 추출
       links = soup.find_all('a')
       for link in links:
           print(f"링크: {link.get('href')}")

       # 특정 클래스를 가진 요소 찾기
       articles = soup.find_all('div', class_='article')
       for article in articles:
           headline = article.find('h2').text
           content = article.find('p').text
           print(f"헤드라인: {headline}")
           print(f"내용: {content}")
   ```

#### 웹 데이터 수집 실습

실제 웹 사이트에서 데이터를 수집하고 처리하는 예제를 살펴보겠습니다.

- web_scraping_example.py 참조

   ```python
   import requests
   from bs4 import BeautifulSoup
   import pandas as pd
   import time

   class WebScraper:
       def __init__(self):
           self.headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
           }

       def get_page_content(self, url):
           try:
               response = requests.get(url, headers=self.headers)
               response.raise_for_status()
               return BeautifulSoup(response.text, 'html.parser')
           except Exception as e:
               print(f"에러 발생: {e}")
               return None

       def parse_product_info(self, soup):
           products = []
           items = soup.find_all('div', class_='product-item')
           
           for item in items:
               product = {
                   'name': item.find('h2', class_='product-name').text.strip(),
                   'price': item.find('span', class_='price').text.strip(),
                   'rating': item.find('div', class_='rating').text.strip(),
                   'url': item.find('a')['href']
               }
               products.append(product)
           
           return products

       def save_to_csv(self, data, filename):
           df = pd.DataFrame(data)
           df.to_csv(filename, index=False, encoding='utf-8')
           print(f"데이터가 {filename}에 저장되었습니다.")

   # 스크래퍼 사용 예시
   scraper = WebScraper()
   
   # 여러 페이지 스크래핑
   all_products = []
   base_url = "https://example.com/products?page={}"
   
   for page in range(1, 6):  # 1부터 5페이지까지 수집
       print(f"페이지 {page} 수집 중...")
       url = base_url.format(page)
       soup = scraper.get_page_content(url)
       
       if soup:
           products = scraper.parse_product_info(soup)
           all_products.extend(products)
           
           # 웹 서버 부하 방지를 위한 대기
           time.sleep(1)

   # 결과 저장
   scraper.save_to_csv(all_products, 'products.csv')

   # 데이터 분석
   df = pd.read_csv('products.csv')
   print("\n기본 통계:")
   print(df.describe())
   
   print("\n가격대별 제품 수:")
   print(df['price'].value_counts().sort_index())
   ```

#### Tkinter 기초

Tkinter를 사용한 GUI 프로그래밍의 기초를 알아보겠습니다.

- tkinter_basics.py 참조

   ```python
   import tkinter as tk
   from tkinter import ttk
   from tkinter import messagebox

   class BasicGUI:
       def __init__(self, master):
           self.master = master
           master.title("기본 GUI 예제")
           
           # 윈도우 크기 설정
           master.geometry("400x300")
           
           # 레이블
           self.label = tk.Label(master, text="안녕하세요!")
           self.label.pack(pady=10)
           
           # 입력 필드
           self.entry = tk.Entry(master)
           self.entry.pack(pady=10)
           
           # 버튼
           self.button = tk.Button(master, text="클릭!", command=self.button_click)
           self.button.pack(pady=10)
           
           # 체크박스
           self.check_var = tk.BooleanVar()
           self.checkbox = tk.Checkbutton(master, text="옵션 1", 
                                        variable=self.check_var)
           self.checkbox.pack(pady=10)
           
           # 라디오 버튼
           self.radio_var = tk.StringVar()
           self.radio1 = tk.Radiobutton(master, text="선택 1", 
                                      variable=self.radio_var, value="1")
           self.radio2 = tk.Radiobutton(master, text="선택 2", 
                                      variable=self.radio_var, value="2")
           self.radio1.pack()
           self.radio2.pack()
           
           # 콤보박스
           self.combo = ttk.Combobox(master, 
                                   values=["옵션 1", "옵션 2", "옵션 3"])
           self.combo.pack(pady=10)
           
           # 리스트박스
           self.listbox = tk.Listbox(master)
           for item in ["항목 1", "항목 2", "항목 3"]:
               self.listbox.insert(tk.END, item)
           self.listbox.pack(pady=10)

       def button_click(self):
           text = self.entry.get()
           if text:
               messagebox.showinfo("알림", f"입력한 텍스트: {text}")
           else:
               messagebox.showwarning("경고", "텍스트를 입력해주세요!")

   # GUI 실행
   if __name__ == "__main__":
       root = tk.Tk()
       gui = BasicGUI(root)
       root.mainloop()
   ```

#### 간단한 GUI 애플리케이션 만들기

실제 사용 가능한 GUI 애플리케이션을 만들어보겠습니다.

- calculator_gui.py 참조

   ```python
   import tkinter as tk
   from tkinter import messagebox

   class Calculator:
       def __init__(self, master):
           self.master = master
           master.title("계산기")
           
           # 계산기 디스플레이
           self.display = tk.Entry(master, width=30, justify='right')
           self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
           
           # 버튼 생성
           self.create_buttons()
           
           # 키보드 이벤트 바인딩
           master.bind('<Return>', lambda e: self.calculate())
           master.bind('<Escape>', lambda e: self.clear())

       def create_buttons(self):
           # 버튼 텍스트
           button_list = [
               '7', '8', '9', '/',
               '4', '5', '6', '*',
               '1', '2', '3', '-',
               '0', '.', '=', '+'
           ]
           
           # 버튼 생성 및 배치
           row = 1
           col = 0
           for button_text in button_list:
               cmd = lambda x=button_text: self.click(x)
               tk.Button(self.master, text=button_text, width=5,
                        command=cmd).grid(row=row, column=col, padx=2, pady=2)
               col += 1
               if col > 3:
                   col = 0
                   row += 1
           
           # Clear 버튼 추가
           tk.Button(self.master, text='C', width=5,
                    command=self.clear).grid(row=row, column=0, 
                                           columnspan=4, pady=5)

       def click(self, key):
           if key == '=':
               self.calculate()
           else:
               self.display.insert(tk.END, key)

       def calculate(self):
           try:
               result = eval(self.display.get())
               self.display.delete(0, tk.END)
               self.display.insert(tk.END, str(result))
           except Exception as e:
               messagebox.showerror("에러", "잘못된 수식입니다")
               self.display.delete(0, tk.END)

       def clear(self):
           self.display.delete(0, tk.END)

   # 애플리케이션 실행
   if __name__ == "__main__":
       root = tk.Tk()
       calculator = Calculator(root)
       root.mainloop()
   ```

#### 프로젝트 주제 선정

프로젝트 주제 선정 및 계획 수립 방법을 알아보겠습니다.

- project_planning.py 참조

   ```python
   class ProjectPlanner:
       def __init__(self):
           self.project_info = {
               'title': '',
               'description': '',
               'objectives': [],
               'requirements': [],
               'timeline': {}
           }
       
       def set_project_info(self, title, description):
           self.project_info['title'] = title
           self.project_info['description'] = description
       
       def add_objective(self, objective):
           self.project_info['objectives'].append(objective)
       
       def add_requirement(self, requirement):
           self.project_info['requirements'].append(requirement)
       
       def set_timeline(self, phase, duration):
           self.project_info['timeline'][phase] = duration
       
       def generate_project_plan(self):
           plan = f"""
           프로젝트 계획서
           
           1. 프로젝트 제목: {self.project_info['title']}
           
           2. 프로젝트 설명
           {self.project_info['description']}
           
           3. 프로젝트 목표
           """
           for i, obj in enumerate(self.project_info['objectives'], 1):
               plan += f"\n   {i}. {obj}"
           
           plan += "\n\n4. 요구사항"
           for i, req in enumerate(self.project_info['requirements'], 1):
               plan += f"\n   {i}. {req}"
           
           plan += "\n\n5. 타임라인"
           for phase, duration in self.project_info['timeline'].items():
               plan += f"\n   - {phase}: {duration}"
           
           return plan

   # 프로젝트 계획 예시
   planner = ProjectPlanner()
   planner.set_project_info(
       "도서 관리 시스템",
       "파이썬을 이용한 도서관 관리 시스템 개발"
   )
   
   # 목표 설정
   planner.add_objective("도서 대출/반납 기능 구현")
   planner.add_objective("회원 관리 시스템 구현")
   planner.add_objective("도서 검색 기능 구현")
   
   # 요구사항 정의
   planner.add_requirement("Python 3.8 이상")
   planner.add_requirement("SQLite 데이터베이스")
   planner.add_requirement("tkinter GUI 라이브러리")
   
   # 타임라인 설정
   planner.set_timeline("기획 및 설계", "1주차")
   planner.set_timeline("기본 기능 구현", "2-3주차")
   planner.set_timeline("GUI 개발", "4주차")
   planner.set_timeline("테스트 및 디버깅", "5주차")
   
   # 계획서 생성
   print(planner.generate_project_plan())
   ```

#### 제너레이터와 이터레이터

제너레이터와 이터레이터의 개념과 사용법을 알아보겠습니다.

- generator_iterator.py 참조

   ```python
   # 제너레이터 함수 정의
   def number_generator(n):
       for i in range(n):
           yield i

   # 피보나치 수열 제너레이터
   def fibonacci_generator(n):
       a, b = 0, 1
       for _ in range(n):
           yield a
           a, b = b, a + b

   # 커스텀 이터레이터 클래스
   class CountDown:
       def __init__(self, start):
           self.start = start
       
       def __iter__(self):
           return self
       
       def __next__(self):
           if self.start <= 0:
               raise StopIteration
           self.start -= 1
           return self.start + 1

   # 제너레이터 표현식
   squares = (x**2 for x in range(10))

   # 사용 예시
   def generator_examples():
       # 기본 제너레이터 사용
       print("숫자 제너레이터:")
       for num in number_generator(5):
           print(num, end=' ')
       print()

       # 피보나치 제너레이터 사용
       print("\n피보나치 수열:")
       for fib in fibonacci_generator(8):
           print(fib, end=' ')
       print()

       # 커스텀 이터레이터 사용
       print("\n카운트다운:")
       countdown = CountDown(5)
       for count in countdown:
           print(count, end=' ')
       print()

       # 제너레이터 표현식 사용
       print("\n제곱수:")
       for square in squares:
           print(square, end=' ')
       print()

   # 메모리 효율적인 큰 파일 처리 예제
   def process_large_file(filename):
       def line_generator(file):
           with open(file, 'r') as f:
               for line in f:
                   yield line.strip()

       for line in line_generator(filename):
           # 각 라인 처리
           process_line(line)

   def process_line(line):
       # 라인 처리 로직
       pass

   if __name__ == "__main__":
       generator_examples()
   ```

#### 데코레이터

파이썬 데코레이터의 개념과 활용법을 알아보겠습니다.

- decorators.py 참조

   ```python
   import time
   import functools

   # 기본 데코레이터
   def timer_decorator(func):
       @functools.wraps(func)
       def wrapper(*args, **kwargs):
           start_time = time.time()
           result = func(*args, **kwargs)
           end_time = time.time()
           print(f"{func.__name__} 실행 시간: {end_time - start_time:.4f}초")
           return result
       return wrapper

   # 매개변수를 받는 데코레이터
   def repeat(times):
       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kwargs):
               for _ in range(times):
                   result = func(*args, **kwargs)
               return result
           return wrapper
       return decorator

   # 클래스 데코레이터
   def singleton(cls):
       instances = {}
       @functools.wraps(cls)
       def get_instance(*args, **kwargs):
           if cls not in instances:
               instances[cls] = cls(*args, **kwargs)
           return instances[cls]
       return get_instance

   # 데코레이터 사용 예시
   @timer_decorator
   def factorial(n):
       return 1 if n <= 1 else n * factorial(n-1)

   @repeat(times=3)
   def greet(name):
       print(f"안녕하세요, {name}님!")

   @singleton
   class Database:
       def __init__(self):
           self.initialized = False
           
       def initialize(self):
           if not self.initialized:
               print("데이터베이스 초기화")
               self.initialized = True

   # 메서드 데코레이터
   class cached_property:
       def __init__(self, func):
           self.func = func
           self.attrname = None
           
       def __get__(self, obj, cls=None):
           if obj is None:
               return self
           if self.attrname is None:
               self.attrname = self.func.__name__
           try:
               return obj.__dict__[self.attrname]
           except KeyError:
               value = self.func(obj)
               obj.__dict__[self.attrname] = value
               return value

   # 실제 사용 예시
   class DataProcessor:
       def __init__(self, data):
           self.data = data
       
       @cached_property
       def processed_data(self):
           print("데이터 처리 중...")
           return [x * 2 for x in self.data]

   if __name__ == "__main__":
       # 팩토리얼 계산 및 시간 측정
       print(f"팩토리얼 결과: {factorial(10)}")
       
       # 반복 데코레이터 테스트
       greet("김철수")
       
       # 싱글톤 테스트
       db1 = Database()
       db2 = Database()
       print(f"같은 인스턴스?: {db1 is db2}")
       
       # 캐시된 프로퍼티 테스트
       processor = DataProcessor([1, 2, 3, 4, 5])
       print("첫 번째 접근:")
       print(processor.processed_data)
       print("두 번째 접근:")
       print(processor.processed_data)
   ```

#### async/await 구문

비동기 프로그래밍의 개념과 사용법을 알아보겠습니다.

- async_programming.py 참조

   ```python
   import asyncio
   import aiohttp
   import time

   # 기본 비동기 함수
   async def say_hello(delay, name):
       await asyncio.sleep(delay)
       print(f"{name}님, 안녕하세요!")
       return f"{name} 작업 완료"

   # 비동기 웹 요청 예제
   async def fetch_url(session, url):
       async with session.get(url) as response:
           return await response.text()

   async def fetch_all_urls(urls):
       async with aiohttp.ClientSession() as session:
           tasks = []
           for url in urls:
               tasks.append(asyncio.create_task(fetch_url(session, url)))
           responses = await asyncio.gather(*tasks)
           return responses

   # 비동기 파일 처리
   async def write_to_file(filename, content):
       await asyncio.to_thread(write_file_sync, filename, content)

   def write_file_sync(filename, content):
       with open(filename, 'w') as f:
           f.write(content)

   # 비동기 데이터베이스 작업 시뮬레이션
   class AsyncDatabase:
       def __init__(self):
           self.data = {}
       
       async def get(self, key):
           await asyncio.sleep(0.1)  # DB 접근 시뮬레이션
           return self.data.get(key)
       
       async def set(self, key, value):
           await asyncio.sleep(0.1)  # DB 쓰기 시뮬레이션
           self.data[key] = value
           return True

   # 실제 사용 예시
   async def main():
       # 기본 비동기 함수 실행
       print("비동기 함수 실행:")
       tasks = [
           say_hello(1, "김철수"),
           say_hello(2, "이영희"),
           say_hello(1, "박민수")
       ]
       results = await asyncio.gather(*tasks)
       print("결과:", results)
       
       # 비동기 웹 요청
       print("\n비동기 웹 요청:")
       urls = [
           "http://example.com",
           "http://example.org",
           "http://example.net"
       ]
       try:
           responses = await fetch_all_urls(urls)
           print(f"{len(responses)}개의 웹 페이지 다운로드 완료")
       except Exception as e:
           print(f"웹 요청 중 에러 발생: {e}")
       
       # 비동기 DB 작업
       print("\n비동기 DB 작업:")
       db = AsyncDatabase()
       await db.set("user1", {"name": "김철수", "age": 25})
       user = await db.get("user1")
       print("사용자 정보:", user)

   # 이벤트 루프 실행
   if __name__ == "__main__":
       start_time = time.time()
       asyncio.run(main())
       print(f"\n전체 실행 시간: {time.time() - start_time:.2f}초")
   ```

#### threading과 multiprocessing

파이썬의 병렬 처리 방법을 알아보겠습니다.

- parallel_processing.py 참조

   ```python
   import threading
   import multiprocessing
   import time
   import queue
   from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

   # 스레딩 예제
   class ThreadingExample:
       def __init__(self):
           self.data = queue.Queue()
       
       def producer(self, items):
           for item in items:
               time.sleep(0.5)  # 작업 시뮬레이션
               self.data.put(item)
               print(f"생산: {item}")
       
       def consumer(self):
           while True:
               try:
                   item = self.data.get(timeout=2)
                   time.sleep(0.3)  # 작업 시뮬레이션
                   print(f"소비: {item}")
                   self.data.task_done()
               except queue.Empty:
                   break
       
       def run_threading_example(self):
           items = list(range(5))
           
           # 스레드 생성
           producer_thread = threading.Thread(
               target=self.producer, args=(items,))
           consumer_thread = threading.Thread(
               target=self.consumer)
           
           # 스레드 시작
           producer_thread.start()
           consumer_thread.start()
           
           # 스레드 종료 대기
           producer_thread.join()
           consumer_thread.join()

   # 멀티프로세싱 예제
   def cpu_bound_task(n):
       """CPU 집약적인 작업 시뮬레이션"""
       count = 0
       for i in range(n):
           count += i * i
       return count

   def run_multiprocessing_example():
       numbers = [10**6, 10**6, 10**6, 10**6]
       
       # 순차 실행
       start_time = time.time()
       results = [cpu_bound_task(n) for n in numbers]
       print(f"순차 실행 시간: {time.time() - start_time:.2f}초")
       
       # 멀티프로세싱 실행
       start_time = time.time()
       with ProcessPoolExecutor() as executor:
           results = list(executor.map(cpu_bound_task, numbers))
       print(f"멀티프로세싱 실행 시간: {time.time() - start_time:.2f}초")

   # ThreadPoolExecutor 예제
   def io_bound_task(url):
       """I/O 작업 시뮬레이션"""
       time.sleep(1)  # 네트워크 요청 시뮬레이션
       return f"데이터 다운로드 완료: {url}"

   def run_thread_pool_example():
       urls = [
           "http://example.com/1",
           "http://example.org/2",
           "http://example.net/3",
           "http://example.io/4"
       ]
       
       # ThreadPoolExecutor 사용
       start_time = time.time()
       with ThreadPoolExecutor(max_workers=4) as executor:
           futures = [executor.submit(io_bound_task, url) for url in urls]
           for future in futures:
               print(future.result())
       print(f"스레드 풀 실행 시간: {time.time() - start_time:.2f}초")

   if __name__ == "__main__":
       # 스레딩 예제 실행
       print("스레딩 예제 실행:")
       threading_example = ThreadingExample()
       threading_example.run_threading_example()
       
       print("\n멀티프로세싱 예제 실행:")
       run_multiprocessing_example()
       
       print("\n스레드 풀 예제 실행:")
       run_thread_pool_example()
   ```


### 04.예외 처리 및 파일 입출력

- 학습 목표: 예외 처리 방법과 파일 입출력 기능을 익힌다.

#### 예외 처리 기본

1. try-except 구문
   ```python
   def divide_numbers(a, b):
       try:
           result = a / b
           return result
       except ZeroDivisionError:
           print("0으로 나눌 수 없습니다.")
           return None
       except TypeError:
           print("숫자만 입력해주세요.")
           return None
       finally:
           print("계산이 완료되었습니다.")

   # 예외 처리 테스트
   print(divide_numbers(10, 2))    # 정상 케이스
   print(divide_numbers(10, 0))    # 0으로 나누기 예외
   print(divide_numbers(10, '2'))  # 타입 예외
   ```

2. 사용자 정의 예외
   ```python
   class InvalidAgeError(Exception):
       def __init__(self, age, message="나이는 0보다 커야 합니다."):
           self.age = age
           self.message = message
           super().__init__(self.message)

   def verify_age(age):
       if age <= 0:
           raise InvalidAgeError(age)
       return f"입력된 나이는 {age}살 입니다."

   # 사용자 정의 예외 테스트
   try:
       print(verify_age(20))  # 정상 케이스
       print(verify_age(-5))  # 예외 발생
   except InvalidAgeError as e:
       print(f"에러 발생: {e.message}, 입력값: {e.age}")
   ```

#### 파일 입출력 활용

1. 텍스트 파일 처리
   ```python
   # 파일 쓰기
   with open('example.txt', 'w', encoding='utf-8') as f:
       f.write("안녕하세요.\n")
       f.write("파이썬 파일 입출력 예제입니다.\n")
       f.write("with 구문을 사용하면 자동으로 파일이 닫힙니다.\n")

   # 파일 읽기
   with open('example.txt', 'r', encoding='utf-8') as f:
       # 전체 읽기
       content = f.read()
       print("전체 내용:", content)

   with open('example.txt', 'r', encoding='utf-8') as f:
       # 한 줄씩 읽기
       for line in f:
           print("한 줄:", line.strip())
   ```

2. JSON 파일 처리
   ```python
   import json

   # JSON 데이터 생성
   data = {
       'name': '홍길동',
       'age': 30,
       'city': '서울',
       'hobbies': ['독서', '등산', '프로그래밍']
   }

   # JSON 파일로 저장
   with open('person.json', 'w', encoding='utf-8') as f:
       json.dump(data, f, ensure_ascii=False, indent=4)

   # JSON 파일 읽기
   with open('person.json', 'r', encoding='utf-8') as f:
       loaded_data = json.load(f)
       print("이름:", loaded_data['name'])
       print("취미:", ', '.join(loaded_data['hobbies']))
   ```

3. CSV 파일 처리
   ```python
   import csv

   # CSV 파일 쓰기
   with open('students.csv', 'w', newline='', encoding='utf-8') as f:
       writer = csv.writer(f)
       writer.writerow(['이름', '나이', '학년'])
       writer.writerows([
           ['김철수', 15, 1],
           ['이영희', 16, 2],
           ['박민수', 15, 1]
       ])

   # CSV 파일 읽기
   with open('students.csv', 'r', encoding='utf-8') as f:
       reader = csv.reader(f)
       header = next(reader)  # 헤더 읽기
       print("헤더:", header)
       
       for row in reader:
           print(f"{row[0]}는 {row[1]}살이고 {row[2]}학년입니다.")
   ```

4. 바이너리 파일 처리
   ```python
   # 이미지 파일 복사 예제
   def copy_image(source_path, target_path):
       try:
           with open(source_path, 'rb') as source:
               with open(target_path, 'wb') as target:
                   chunk_size = 4096
                   while True:
                       chunk = source.read(chunk_size)
                       if not chunk:
                           break
                       target.write(chunk)
           print("파일 복사가 완료되었습니다.")
       except FileNotFoundError:
           print("원본 파일을 찾을 수 없습니다.")
       except PermissionError:
           print("파일 접근 권한이 없습니다.")

   # 사용 예:
   # copy_image('original.jpg', 'copied.jpg')
   ```

### 05. 모듈과 패키지

- 학습 목표: 모듈과 패키지를 활용하여 코드의 재사용성을 높인다.

#### 모듈 생성과 사용

1. 사용자 정의 모듈 생성
   ```python
   # mymath.py
   def add(a, b):
       return a + b

   def subtract(a, b):
       return a - b

   def multiply(a, b):
       return a * b

   def divide(a, b):
       if b == 0:
           raise ValueError("0으로 나눌 수 없습니다.")
       return a / b

   # 모듈 테스트 코드
   if __name__ == "__main__":
       print("10 + 5 =", add(10, 5))
       print("10 - 5 =", subtract(10, 5))
       print("10 * 5 =", multiply(10, 5))
       print("10 / 5 =", divide(10, 5))
   ```

2. 모듈 사용 예제
   ```python
   # main.py
   import mymath
   from mymath import multiply, divide

   # 전체 모듈 import 사용
   result1 = mymath.add(10, 5)
   result2 = mymath.subtract(10, 5)

   # 특정 함수만 import 사용
   result3 = multiply(10, 5)
   result4 = divide(10, 5)

   print(f"덧셈: {result1}")
   print(f"뺄셈: {result2}")
   print(f"곱셈: {result3}")
   print(f"나눗셈: {result4}")
   ```

#### 패키지 구조 설계

1. 기본 패키지 구조
   ```
   my_package/
   ├── __init__.py
   ├── module1.py
   ├── module2.py
   └── subpackage/
       ├── __init__.py
       └── module3.py
   ```

2. 패키지 초기화 파일 (__init__.py)
   ```python
   # my_package/__init__.py
   from .module1 import *
   from .module2 import *
   from .subpackage.module3 import *

   __all__ = ['function1', 'function2', 'Class1', 'Class2']
   ```

3. 패키지 사용 예제
   ```python
   # 패키지 전체 import
   import my_package

   # 특정 모듈 import
   from my_package import module1
   from my_package.subpackage import module3

   # 특정 함수/클래스 import
   from my_package.module1 import function1
   from my_package.subpackage.module3 import Class1
   ```

### 06. 함수형 프로그래밍

- 학습 목표: 함수형 프로그래밍의 개념을 이해하고 적용한다.

#### 일급 함수(First-class Functions)

1. 함수를 변수에 할당
   ```python
   def greet(name):
       return f"안녕하세요, {name}님!"

   # 함수를 변수에 할당
   say_hello = greet
   print(say_hello("홍길동"))  # 출력: 안녕하세요, 홍길동님!
   ```

2. 함수를 인자로 전달
   ```python
   def apply_operation(x, y, operation):
       return operation(x, y)

   def add(x, y):
       return x + y

   def multiply(x, y):
       return x * y

   # 함수를 인자로 전달
   result1 = apply_operation(5, 3, add)      # 출력: 8
   result2 = apply_operation(5, 3, multiply) # 출력: 15
   ```

#### 람다 함수(Lambda Functions)

1. 기본 람다 함수
   ```python
   # 일반 함수
   def square(x):
       return x ** 2

   # 같은 기능의 람다 함수
   square_lambda = lambda x: x ** 2

   numbers = [1, 2, 3, 4, 5]
   squares = list(map(square_lambda, numbers))
   print(squares)  # 출력: [1, 4, 9, 16, 25]
   ```

2. 람다 함수의 활용
   ```python
   # 리스트 정렬에 람다 함수 사용
   students = [
       {'name': '홍길동', 'age': 20},
       {'name': '김철수', 'age': 18},
       {'name': '이영희', 'age': 19}
   ]

   # 나이순으로 정렬
   sorted_by_age = sorted(students, key=lambda x: x['age'])
   
   # 이름순으로 정렬
   sorted_by_name = sorted(students, key=lambda x: x['name'])
   ```

#### 고차 함수(Higher-order Functions)

1. map 함수
   ```python
   # 숫자 리스트의 각 요소를 제곱
   numbers = [1, 2, 3, 4, 5]
   squared = list(map(lambda x: x**2, numbers))
   print(squared)  # 출력: [1, 4, 9, 16, 25]

   # 여러 리스트에 대한 연산
   list1 = [1, 2, 3]
   list2 = [10, 20, 30]
   sums = list(map(lambda x, y: x + y, list1, list2))
   print(sums)  # 출력: [11, 22, 33]
   ```

2. filter 함수
   ```python
   # 짝수만 필터링
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   print(evens)  # 출력: [2, 4, 6, 8, 10]

   # 특정 조건의 딕셔너리 필터링
   products = [
       {'name': '노트북', 'price': 1200000},
       {'name': '마우스', 'price': 30000},
       {'name': '키보드', 'price': 150000}
   ]
   expensive = list(filter(lambda x: x['price'] > 100000, products))
   ```

3. reduce 함수
   ```python
   from functools import reduce

   # 리스트의 모든 요소 곱하기
   numbers = [1, 2, 3, 4, 5]
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # 출력: 120

   # 문자열 연결
   words = ['Hello', ' ', 'World', '!']
   sentence = reduce(lambda x, y: x + y, words)
   print(sentence)  # 출력: Hello World!
   ```

### 07. 데이터 처리 및 분석

- 학습 목표: 파이썬을 이용한 데이터 처리 기법을 익힌다.

#### Pandas를 이용한 데이터 처리

1. DataFrame 생성과 기본 조작
   ```python
   import pandas as pd
   import numpy as np

   # DataFrame 생성
   data = {
       '이름': ['홍길동', '김철수', '이영희', '박민수'],
       '나이': [20, 18, 19, 22],
       '성적': [85, 90, 95, 88]
   }
   df = pd.DataFrame(data)

   # 기본 정보 확인
   print(df.info())
   print("\n기술 통계량:")
   print(df.describe())
   ```

2. 데이터 필터링과 정렬
   ```python
   # 나이가 20세 이상인 학생
   adult_students = df[df['나이'] >= 20]

   # 성적순으로 정렬
   sorted_by_grade = df.sort_values('성적', ascending=False)

   # 조건부 필터링
   good_students = df[(df['성적'] >= 90) & (df['나이'] < 20)]
   ```

3. 그룹화와 집계
   ```python
   # 샘플 데이터 생성
   sales_data = pd.DataFrame({
       '제품': ['A', 'B', 'A', 'B', 'A', 'B'],
       '지역': ['서울', '서울', '부산', '부산', '인천', '인천'],
       '판매량': [100, 150, 200, 250, 300, 350],
       '가격': [1000, 2000, 1000, 2000, 1000, 2000]
   })

   # 제품별 총 판매량
   product_sales = sales_data.groupby('제품')['판매량'].sum()

   # 지역별, 제품별 평균 판매량
   region_product_sales = sales_data.groupby(['지역', '제품'])['판매량'].mean()
   ```

#### Numpy를 이용한 수치 계산

1. 배열 생성과 연산
   ```python
   import numpy as np

   # 배열 생성
   arr1 = np.array([1, 2, 3, 4, 5])
   arr2 = np.array([10, 20, 30, 40, 50])

   # 기본 연산
   print("합:", arr1 + arr2)
   print("곱:", arr1 * arr2)
   print("제곱:", arr1 ** 2)
   ```

2. 행렬 연산
   ```python
   # 행렬 생성
   matrix1 = np.array([[1, 2], [3, 4]])
   matrix2 = np.array([[5, 6], [7, 8]])

   # 행렬 곱
   matrix_product = np.dot(matrix1, matrix2)
   
   # 전치 행렬
   transposed = matrix1.T
   
   # 역행렬
   inverse = np.linalg.inv(matrix1)
   ```

3. 통계 함수
   ```python
   data = np.array([15, 23, 45, 38, 32, 55, 67, 44, 89, 76])

   print("평균:", np.mean(data))
   print("중앙값:", np.median(data))
   print("표준편차:", np.std(data))
   print("분산:", np.var(data))
   print("최소값:", np.min(data))
   print("최대값:", np.max(data))
   ```

### 08. 웹 스크래핑

- 학습 목표: 웹에서 데이터를 추출하는 방법을 배운다.

#### BeautifulSoup 사용법

1. 기본 HTML 파싱
   ```python
   import requests
   from bs4 import BeautifulSoup

   # 웹 페이지 가져오기
   url = "https://example.com"
   response = requests.get(url)
   
   # HTML 파싱
   soup = BeautifulSoup(response.text, 'html.parser')
   
   # 태그로 요소 찾기
   title = soup.find('title')
   paragraphs = soup.find_all('p')
   
   print("제목:", title.text)
   for p in paragraphs:
       print("단락:", p.text)
   ```

2. CSS 선택자 활용
   ```python
   # 클래스로 요소 찾기
   items = soup.find_all(class_='item')
   
   # ID로 요소 찾기
   header = soup.find(id='header')
   
   # CSS 선택자 사용
   links = soup.select('a.external-link')
   menu_items = soup.select('#navigation li')
   ```

3. 데이터 추출 및 저장
   ```python
   import pandas as pd

   def scrape_book_info(url):
       response = requests.get(url)
       soup = BeautifulSoup(response.text, 'html.parser')
       
       books = []
       for book in soup.find_all('div', class_='book-item'):
           title = book.find('h2').text.strip()
           author = book.find('span', class_='author').text.strip()
           price = book.find('span', class_='price').text.strip()
           
           books.append({
               'title': title,
               'author': author,
               'price': price
           })
       
       # DataFrame으로 변환
       df = pd.DataFrame(books)
       
       # CSV 파일로 저장
       df.to_csv('books.csv', index=False, encoding='utf-8')
       
       return df
   ```

#### Selenium을 이용한 동적 웹 스크래핑

1. Selenium 설정
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC

   # 웹드라이버 설정
   driver = webdriver.Chrome()
   
   # 페이지 로드
   driver.get("https://example.com")
   ```

2. 요소 찾기와 상호작용
   ```python
   # ID로 요소 찾기
   search_box = driver.find_element(By.ID, "search")
   
   # 검색어 입력
   search_box.send_keys("파이썬")
   
   # 버튼 클릭
   search_button = driver.find_element(By.CLASS_NAME, "search-button")
   search_button.click()
   
   # 요소가 로드될 때까지 대기
   results = WebDriverWait(driver, 10).until(
       EC.presence_of_all_elements_located((By.CLASS_NAME, "result-item"))
   )
   ```

3. 스크롤 처리
   ```python
   def scroll_to_bottom():
       # 이전 스크롤 높이
       last_height = driver.execute_script("return document.body.scrollHeight")
       
       while True:
           # 페이지 끝까지 스크롤
           driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
           
           # 로딩 대기
           time.sleep(2)
           
           # 새로운 스크롤 높이
           new_height = driver.execute_script("return document.body.scrollHeight")
           
           # 스크롤이 더 이상 되지 않으면 종료
           if new_height == last_height:
               break
               
           last_height = new_height
   ```

### 09. GUI 프로그래밍

- 학습 목표: 파이썬을 이용한 GUI 애플리케이션 개발 기초를 익힌다.

#### tkinter를 이용한 GUI 프로그래밍

1. 기본 창 만들기
   ```python
   import tkinter as tk
   from tkinter import messagebox

   # 메인 창 생성
   root = tk.Tk()
   root.title("내 첫 GUI 프로그램")
   root.geometry("400x300")

   # 레이블 추가
   label = tk.Label(root, text="안녕하세요!")
   label.pack()

   # 버튼 추가
   def button_click():
       messagebox.showinfo("알림", "버튼이 클릭되었습니다!")

   button = tk.Button(root, text="클릭하세요", command=button_click)
   button.pack()

   # 메인 루프 실행
   root.mainloop()
   ```

2. 입력 폼 만들기
   ```python
   class LoginForm:
       def __init__(self, root):
           self.root = root
           self.root.title("로그인")
           
           # 사용자 이름 입력
           self.username_label = tk.Label(root, text="사용자 이름:")
           self.username_label.pack()
           
           self.username_entry = tk.Entry(root)
           self.username_entry.pack()
           
           # 비밀번호 입력
           self.password_label = tk.Label(root, text="비밀번호:")
           self.password_label.pack()
           
           self.password_entry = tk.Entry(root, show="*")
           self.password_entry.pack()
           
           # 로그인 버튼
           self.login_button = tk.Button(root, text="로그인", command=self.login)
           self.login_button.pack()
       
       def login(self):
           username = self.username_entry.get()
           password = self.password_entry.get()
           
           if username == "admin" and password == "1234":
               messagebox.showinfo("성공", "로그인 성공!")
           else:
               messagebox.showerror("실패", "잘못된 사용자 이름 또는 비밀번호입니다.")

   # 사용 예:
   # root = tk.Tk()
   # login_form = LoginForm(root)
   # root.mainloop()
   ```

3. 메뉴와 대화상자
   ```python
   class NotepadApp:
       def __init__(self, root):
           self.root = root
           self.root.title("간단한 메모장")
           
           # 텍스트 영역
           self.text_area = tk.Text(root)
           self.text_area.pack(expand=True, fill='both')
           
           # 메뉴바 생성
           self.menu_bar = tk.Menu(root)
           self.root.config(menu=self.menu_bar)
           
           # 파일 메뉴
           self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
           self.menu_bar.add_cascade(label="파일", menu=self.file_menu)
           self.file_menu.add_command(label="새로 만들기", command=self.new_file)
           self.file_menu.add_command(label="저장", command=self.save_file)
           self.file_menu.add_separator()
           self.file_menu.add_command(label="종료", command=root.quit)
       
       def new_file(self):
           self.text_area.delete(1.0, tk.END)
       
       def save_file(self):
           from tkinter import filedialog
           
           file_path = filedialog.asksaveasfilename(
               defaultextension=".txt",
               filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
           )
           
           if file_path:
               with open(file_path, 'w', encoding='utf-8') as file:
                   file.write(self.text_area.get(1.0, tk.END))
               messagebox.showinfo("저장", "파일이 저장되었습니다.")

   # 사용 예:
   # root = tk.Tk()
   # notepad = NotepadApp(root)
   # root.mainloop()
   ```

### 프로젝트 및 실습

- 학습 목표: 중급 과정에서 배운 내용을 종합하여 프로젝트를 완성한다.

#### 도서 관리 시스템 만들기

1. 프로젝트 구조
   ```
   book_management/
   ├── README.md
   ├── requirements.txt
   ├── main.py
   ├── database/
   │   └── books.db
   ├── models/
   │   ├── __init__.py
   │   ├── book.py
   │   └── user.py
   ├── utils/
   │   ├── __init__.py
   │   ├── database.py
   │   └── logger.py
   └── tests/
       ├── __init__.py
       ├── test_book.py
       └── test_user.py
   ```

2. 데이터베이스 모델 (models/book.py)
   ```python
   from dataclasses import dataclass
   from datetime import datetime

   @dataclass
   class Book:
       id: int
       title: str
       author: str
       isbn: str
       published_date: datetime
       quantity: int
       created_at: datetime = datetime.now()
       
       def to_dict(self):
           return {
               'id': self.id,
               'title': self.title,
               'author': self.author,
               'isbn': self.isbn,
               'published_date': self.published_date.strftime('%Y-%m-%d'),
               'quantity': self.quantity,
               'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
           }
   ```

3. 데이터베이스 유틸리티 (utils/database.py)
   ```python
   import sqlite3
   from contextlib import contextmanager
   from typing import List, Optional
   from models.book import Book

   class DatabaseManager:
       def __init__(self, db_file: str):
           self.db_file = db_file
       
       @contextmanager
       def get_connection(self):
           conn = sqlite3.connect(self.db_file)
           try:
               yield conn
           finally:
               conn.close()
       
       def initialize_db(self):
           with self.get_connection() as conn:
               cursor = conn.cursor()
               cursor.execute('''
                   CREATE TABLE IF NOT EXISTS books (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       author TEXT NOT NULL,
                       isbn TEXT UNIQUE NOT NULL,
                       published_date DATE,
                       quantity INTEGER DEFAULT 0,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   )
               ''')
               conn.commit()
       
       def add_book(self, book: Book) -> int:
           with self.get_connection() as conn:
               cursor = conn.cursor()
               cursor.execute('''
                   INSERT INTO books (title, author, isbn, published_date, quantity)
                   VALUES (?, ?, ?, ?, ?)
               ''', (book.title, book.author, book.isbn,
                    book.published_date.strftime('%Y-%m-%d'),
                    book.quantity))
               conn.commit()
               return cursor.lastrowid
       
       def get_book_by_isbn(self, isbn: str) -> Optional[Book]:
           with self.get_connection() as conn:
               cursor = conn.cursor()
               cursor.execute('SELECT * FROM books WHERE isbn = ?', (isbn,))
               row = cursor.fetchone()
               if row:
                   return Book(*row)
               return None
   ```

4. 로깅 설정 (utils/logger.py)
   ```python
   import logging
   from datetime import datetime

   def setup_logger(name: str, log_file: str, level=logging.INFO):
       formatter = logging.Formatter(
           '%(asctime)s %(levelname)s [%(name)s] %(message)s'
       )
       
       handler = logging.FileHandler(log_file)
       handler.setFormatter(formatter)
       
       logger = logging.getLogger(name)
       logger.setLevel(level)
       logger.addHandler(handler)
       
       return logger

   # 로거 생성
   logger = setup_logger('book_management', 'app.log')
   ```

5. 메인 애플리케이션 (main.py)
   ```python
   import tkinter as tk
   from tkinter import ttk, messagebox
   from models.book import Book
   from utils.database import DatabaseManager
   from utils.logger import logger
   from datetime import datetime

   class BookManagementApp:
       def __init__(self, root):
           self.root = root
           self.root.title("도서 관리 시스템")
           self.db = DatabaseManager('database/books.db')
           self.db.initialize_db()
           
           self.setup_ui()
       
       def setup_ui(self):
           # 입력 프레임
           input_frame = ttk.LabelFrame(self.root, text="도서 정보 입력")
           input_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
           
           # 입력 필드
           ttk.Label(input_frame, text="제목:").grid(row=0, column=0, padx=5, pady=5)
           self.title_var = tk.StringVar()
           ttk.Entry(input_frame, textvariable=self.title_var).grid(row=0, column=1, padx=5, pady=5)
           
           ttk.Label(input_frame, text="저자:").grid(row=1, column=0, padx=5, pady=5)
           self.author_var = tk.StringVar()
           ttk.Entry(input_frame, textvariable=self.author_var).grid(row=1, column=1, padx=5, pady=5)
           
           # 버튼
           ttk.Button(input_frame, text="도서 추가", command=self.add_book).grid(row=2, column=0, columnspan=2, pady=10)
       
       def add_book(self):
           try:
               book = Book(
                   id=None,
                   title=self.title_var.get(),
                   author=self.author_var.get(),
                   isbn=f"ISBN-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                   published_date=datetime.now(),
                   quantity=1
               )
               
               book_id = self.db.add_book(book)
               logger.info(f"도서 추가됨: {book.title} (ID: {book_id})")
               messagebox.showinfo("성공", "도서가 추가되었습니다.")
               
               # 입력 필드 초기화
               self.title_var.set("")
               self.author_var.set("")
               
           except Exception as e:
               logger.error(f"도서 추가 실패: {str(e)}")
               messagebox.showerror("오류", f"도서 추가 중 오류 발생: {str(e)}")

   if __name__ == "__main__":
       root = tk.Tk()
       app = BookManagementApp(root)
       root.mainloop()
   ```

6. 테스트 코드 (tests/test_book.py)
   ```python
   import unittest
   from datetime import datetime
   from models.book import Book

   class TestBook(unittest.TestCase):
       def setUp(self):
           self.book = Book(
               id=1,
               title="파이썬 프로그래밍",
               author="홍길동",
               isbn="ISBN-123456",
               published_date=datetime.now(),
               quantity=5
           )
       
       def test_book_creation(self):
           self.assertEqual(self.book.title, "파이썬 프로그래밍")
           self.assertEqual(self.book.author, "홍길동")
           self.assertEqual(self.book.quantity, 5)
       
       def test_to_dict(self):
           book_dict = self.book.to_dict()
           self.assertIsInstance(book_dict, dict)
           self.assertEqual(book_dict['title'], "파이썬 프로그래밍")
           self.assertEqual(book_dict['author'], "홍길동")

   if __name__ == '__main__':
       unittest.main()
   ```

## 부록: 파이썬 설치 및 라이브러리 설치

### 파이썬 설치

#### 공식 웹사이트에서 파이썬 다운로드

1. Python.org 방문
   - [Python 공식 웹사이트](https://www.python.org/downloads/)에서 최신 버전 다운로드
   - Windows: "Download Python X.X.X" 버튼 클릭
   - macOS: macOS 인스톨러 다운로드

2. 설치 과정
   - Windows:
     - "Add Python X.X to PATH" 옵션 체크
     - "Install Now" 클릭
   - macOS:
     - 다운로드한 .pkg 파일 실행
     - 설치 마법사 따라하기

#### 설치 확인
```bash
# Python 버전 확인
python --version
# 또는
python3 --version

# Python 대화형 셸 실행
python
# 또는
python3
```

### 라이브러리 설치

#### pip를 이용한 라이브러리 설치 방법

1. pip 업그레이드
   ```bash
   # Windows
   python -m pip install --upgrade pip

   # macOS/Linux
   pip3 install --upgrade pip
   ```

2. 라이브러리 설치
   ```bash
   # 단일 패키지 설치
   pip install package_name

   # 특정 버전 설치
   pip install package_name==1.0.0

   # requirements.txt로 설치
   pip install -r requirements.txt
   ```

#### 가상 환경 설정 및 관리

1. venv 생성
   ```bash
   # 가상 환경 생성
   python -m venv myenv

   # 가상 환경 활성화
   # Windows
   myenv\Scripts\activate

   # macOS/Linux
   source myenv/bin/activate
   ```

2. 가상 환경 사용
   ```bash
   # 현재 설치된 패키지 목록 확인
   pip list

   # 패키지 목록 저장
   pip freeze > requirements.txt

   # 가상 환경 비활성화
   deactivate
   ```
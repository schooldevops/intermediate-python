
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


# 2. 제어문

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


# 3. 함수 정의와 호출

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


# 4. 리스트 컴프리헨션

# 기본 리스트 컴프리헨션
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# 조건부 리스트 컴프리헨션
even_nums = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


# 5. 예외 처리

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


# 6. 클래스와 객체

class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        return f"{self.name}가 짖습니다!"

# 객체 생성과 메서드 호출
my_dog = Dog("멍멍이")
print(my_dog.bark())  # 멍멍이가 짖습니다!


# 7. 모듈 임포트

# 기본 모듈 임포트
import math
print(math.pi)  # 3.141592...

# 특정 함수만 임포트
from random import randint
print(randint(1, 6))  # 1부터 6 사이의 난수


# 8. 문자열 포매팅
name = "Python"
version = 3.11

# f-string (권장)
print(f"Hello {name} {version}")

# format() 메서드
print("Hello {} {}".format(name, version))

# % 연산자
print("Hello %s %s" % (name, version))

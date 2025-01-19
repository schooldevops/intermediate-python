from collections import namedtuple

def demonstrate_basic_usage():
    print("=== 기본 네임드 튜플 사용법 ===")
    
    # 네임드 튜플 정의
    Point = namedtuple('Point', ['x', 'y'])
    Person = namedtuple('Person', 'name age job')  # 공백으로 구분된 문자열도 가능
    
    # 네임드 튜플 생성
    p1 = Point(11, y=22)  # 위치 인자와 키워드 인자 모두 사용 가능
    p2 = Point(x=33, y=44)  # 키워드 인자만 사용
    
    bob = Person('Bob', 30, 'developer')
    alice = Person(name='Alice', age=25, job='designer')
    
    # 속성으로 접근
    print(f"p1: x={p1.x}, y={p1.y}")
    print(f"p2: x={p2.x}, y={p2.y}")
    print(f"bob: 이름={bob.name}, 나이={bob.age}, 직업={bob.job}")
    print(f"alice: 이름={alice.name}, 나이={alice.age}, 직업={alice.job}")

def demonstrate_methods():
    print("\n=== 네임드 튜플 메서드 ===")
    
    Person = namedtuple('Person', 'name age job')
    bob = Person('Bob', 30, 'developer')
    
    # _asdict(): OrderedDict로 변환
    print(f"OrderedDict 변환: {bob._asdict()}")
    
    # _replace(): 새로운 값으로 대체
    bob2 = bob._replace(age=31, job='senior developer')
    print(f"원본: {bob}")
    print(f"수정본: {bob2}")
    
    # _fields: 필드 이름 튜플
    print(f"필드 이름들: {Person._fields}")
    
    # _make(): 이터러블로부터 새 인스턴스 생성
    data = ['Charlie', 35, 'manager']
    charlie = Person._make(data)
    print(f"이터러블로 생성: {charlie}")

def demonstrate_advanced_features():
    print("\n=== 고급 기능 ===")
    
    # 기본값 설정
    Employee = namedtuple('Employee', ['name', 'age', 'job', 'salary'], defaults=[0])
    emp1 = Employee('Dave', 28, 'programmer')  # salary는 기본값 0
    print(f"기본값 사용: {emp1}")
    
    # 필드 이름 중복 허용
    Point3D = namedtuple('Point3D', 'x y x y', rename=True)
    p = Point3D(1, 2, 3, 4)
    print(f"중복 필드 자동 변환: {p}")
    print(f"실제 필드 이름: {Point3D._fields}")

def demonstrate_practical_usage():
    print("\n=== 실용적인 예제 ===")
    
    # 데이터베이스 레코드 표현
    Record = namedtuple('Record', 'id name email created_at')
    
    def get_user_record(user_id):
        # 데이터베이스에서 데이터를 가져왔다고 가정
        return Record(
            id=user_id,
            name="John Doe",
            email="john@example.com",
            created_at="2024-01-01"
        )
    
    record = get_user_record(1)
    print(f"사용자 레코드: {record}")
    
    # CSV 데이터 처리
    SalesRecord = namedtuple('SalesRecord', 'date product price quantity')
    
    sales_data = [
        SalesRecord('2024-01-01', 'A', 1000, 3),
        SalesRecord('2024-01-01', 'B', 1500, 2),
        SalesRecord('2024-01-02', 'A', 1000, 1),
    ]
    
    # 데이터 분석
    total_sales = sum(record.price * record.quantity for record in sales_data)
    print(f"총 매출: {total_sales}")

def main():
    demonstrate_basic_usage()
    demonstrate_methods()
    demonstrate_advanced_features()
    demonstrate_practical_usage()

if __name__ == "__main__":
    main() 
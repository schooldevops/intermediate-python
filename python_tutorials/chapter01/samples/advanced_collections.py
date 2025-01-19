"""
파이썬의 고급 컬렉션 타입과 그 활용을 설명하는 예제
이 예제는 시퀀스, 매핑, 집합 타입의 고급 기능을 보여줍니다.
"""

from collections import defaultdict, Counter, namedtuple, deque
from typing import List, Dict, Set, DefaultDict
import heapq

def demonstrate_sequence_operations():
    print("\nSequence Operations Demonstration:")
    
    # 리스트 컴프리헨션과 제너레이터 표현식
    squares = [x**2 for x in range(10)]
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    
    print(f"Squares: {squares}")
    print(f"Even squares: {even_squares}")
    
    # 슬라이싱 고급 기능
    numbers = list(range(10))
    print(f"Original: {numbers}")
    print(f"Every second item: {numbers[::2]}")
    print(f"Reversed: {numbers[::-1]}")
    
    # deque 활용
    d = deque(range(5))
    print(f"\nOriginal deque: {d}")
    d.rotate(2)
    print(f"After rotating right by 2: {d}")
    d.rotate(-2)
    print(f"After rotating left by 2: {d}")

def demonstrate_mapping_operations():
    print("\nMapping Operations Demonstration:")
    
    # defaultdict 활용
    words = ["apple", "banana", "apple", "cherry", "date", "banana"]
    word_count: DefaultDict[str, int] = defaultdict(int)
    for word in words:
        word_count[word] += 1
    
    print("Word count using defaultdict:")
    print(dict(word_count))
    
    # Counter 활용
    counter = Counter(words)
    print("\nWord count using Counter:")
    print(dict(counter))
    print(f"Most common 2 items: {counter.most_common(2)}")
    
    # 딕셔너리 컴프리헨션
    square_dict = {x: x**2 for x in range(5)}
    print(f"\nSquare dictionary: {square_dict}")

def demonstrate_set_operations():
    print("\nSet Operations Demonstration:")
    
    # 집합 연산
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {a}")
    print(f"Set B: {b}")
    print(f"Union: {a | b}")
    print(f"Intersection: {a & b}")
    print(f"Difference (A-B): {a - b}")
    print(f"Symmetric Difference: {a ^ b}")
    
    # 집합 컴프리헨션
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"\nEven squares set: {even_squares}")

def demonstrate_heap_operations():
    print("\nHeap Operations Demonstration:")
    
    # 최소 힙
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    heap = []
    
    # 힙에 요소 추가
    for num in numbers:
        heapq.heappush(heap, num)
    
    print("Extracting from min heap:")
    while heap:
        print(heapq.heappop(heap), end=" ")
    print()
    
    # 최대 힙 (음수 값 활용)
    max_heap = []
    for num in numbers:
        heapq.heappush(max_heap, -num)
    
    print("\nExtracting from max heap:")
    while max_heap:
        print(-heapq.heappop(max_heap), end=" ")
    print()

def demonstrate_named_tuple():
    print("\nNamedTuple Demonstration:")
    
    # namedtuple 정의
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, 22)
    
    print(f"Point: {p}")
    print(f"X coordinate: {p.x}")
    print(f"Y coordinate: {p[1]}")  # 인덱스로도 접근 가능
    
    # 필드 이름 리스트
    print(f"Field names: {p._fields}")
    
    # _replace()로 새 튜플 생성
    p2 = p._replace(x=33)
    print(f"After replace: {p2}")

def main():
    print("Advanced Collections Demonstration")
    demonstrate_sequence_operations()
    demonstrate_mapping_operations()
    demonstrate_set_operations()
    demonstrate_heap_operations()
    demonstrate_named_tuple()

if __name__ == "__main__":
    main()

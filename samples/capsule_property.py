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

def main():
    # 상품 객체 생성
    product = Product("노트북", 1200000)
    
    print("=== 기본 속성 테스트 ===")
    print(f"상품명: {product.name}")      # 프로퍼티를 통한 읽기
    print(f"가격: {product.price}원")     # 프로퍼티를 통한 읽기
    
    print("\n=== 가격 변경 테스트 ===")
    product.price = 1300000  # 프로퍼티를 통한 쓰기
    print(f"변경된 가격: {product.price}원")
    
    print("\n=== 판매 및 매출 테스트 ===")
    print(f"초기 총 매출: {product.total_sales}원")
    product.sell()  # 판매 1회
    print(f"1회 판매 후 총 매출: {product.total_sales}원")
    product.sell()  # 판매 2회
    print(f"2회 판매 후 총 매출: {product.total_sales}원")
    
    print("\n=== 에러 테스트 ===")
    try:
        # name은 읽기 전용 프로퍼티
        product.name = "태블릿"
    except AttributeError as e:
        print(f"이름 변경 시도 에러: {e}")
    
    try:
        # 가격을 음수로 설정
        product.price = -100000
    except ValueError as e:
        print(f"잘못된 가격 설정 에러: {e}")
    
    try:
        # private 속성 직접 접근
        print(product.__price)
    except AttributeError as e:
        print(f"private 속성 접근 에러: {e}")

if __name__ == "__main__":
    main() 
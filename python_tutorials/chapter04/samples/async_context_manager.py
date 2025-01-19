import asyncio
from contextlib import asynccontextmanager

class AsyncResource:
    """비동기 리소스를 시뮬레이션하는 클래스"""
    async def __aenter__(self):
        print("리소스 획득 중...")
        await asyncio.sleep(1)  # 리소스 획득을 시뮬레이션
        print("리소스 획득 완료")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("리소스 해제 중...")
        await asyncio.sleep(1)  # 리소스 해제를 시뮬레이션
        print("리소스 해제 완료")

@asynccontextmanager
async def async_resource():
    """데코레이터를 사용한 비동기 컨텍스트 매니저"""
    try:
        print("리소스 설정 중...")
        await asyncio.sleep(1)
        yield "리소스"
    finally:
        print("리소스 정리 중...")
        await asyncio.sleep(1)

async def main():
    # 클래스 기반 비동기 컨텍스트 매니저 사용
    async with AsyncResource() as resource:
        print("리소스 사용 중...")
        await asyncio.sleep(1)
    
    # 데코레이터 기반 비동기 컨텍스트 매니저 사용
    async with async_resource() as resource:
        print(f"{resource} 사용 중...")
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())

"""
파이썬의 비동기 프로그래밍 예제
이 예제는 코루틴, 이벤트 루프, 비동기 컨텍스트 매니저 등을 보여줍니다.
"""

import asyncio
import aiohttp
import aiofiles
import time
from typing import List, Dict, Any
from dataclasses import dataclass
from contextlib import asynccontextmanager
import random

# 기본 코루틴 예제
async def hello_world():
    """기본 코루틴 함수"""
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# 동시 실행 예제
async def count_up(name: str, n: int):
    """숫자를 세는 코루틴"""
    for i in range(n):
        print(f"{name}: {i}")
        await asyncio.sleep(0.5)

# HTTP 요청 예제
@dataclass
class ApiResponse:
    status: int
    data: Dict[str, Any]

class AsyncHttpClient:
    """비동기 HTTP 클라이언트"""
    def __init__(self):
        self.session = None
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def get(self, url: str) -> ApiResponse:
        async with self.session.get(url) as response:
            return ApiResponse(
                status=response.status,
                data=await response.json()
            )

# 비동기 파일 처리 예제
class AsyncFileProcessor:
    """비동기 파일 처리기"""
    def __init__(self, filename: str):
        self.filename = filename
    
    async def write_lines(self, lines: List[str]):
        async with aiofiles.open(self.filename, 'w') as f:
            for line in lines:
                await f.write(f"{line}\n")
                await asyncio.sleep(0.1)  # 쓰기 작업 시뮬레이션
    
    async def read_lines(self) -> List[str]:
        lines = []
        async with aiofiles.open(self.filename, 'r') as f:
            async for line in f:
                lines.append(line.strip())
                await asyncio.sleep(0.1)  # 읽기 작업 시뮬레이션
        return lines

# 비동기 생산자-소비자 패턴
class AsyncQueue:
    """비동기 작업 큐"""
    def __init__(self, maxsize: int = 5):
        self.queue = asyncio.Queue(maxsize=maxsize)
    
    async def producer(self):
        for i in range(5):
            item = f"Item-{i}"
            await self.queue.put(item)
            print(f"Produced {item}")
            await asyncio.sleep(random.uniform(0.1, 0.5))
        
        # 종료 신호 전송
        await self.queue.put(None)
    
    async def consumer(self, name: str):
        while True:
            item = await self.queue.get()
            if item is None:
                self.queue.task_done()
                break
            
            print(f"Consumer {name} processing {item}")
            await asyncio.sleep(random.uniform(0.2, 0.7))
            self.queue.task_done()

# 비동기 컨텍스트 매니저
@asynccontextmanager
async def timer():
    """작업 시간을 측정하는 비동기 컨텍스트 매니저"""
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"Elapsed time: {end - start:.2f} seconds")

# 비동기 이터레이터
class AsyncRange:
    """비동기 범위 이터레이터"""
    def __init__(self, start: int, stop: int, delay: float = 0.1):
        self.start = start
        self.stop = stop
        self.delay = delay
        self.current = start
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        
        await asyncio.sleep(self.delay)
        value = self.current
        self.current += 1
        return value

async def demonstrate_basic_coroutines():
    print("\nBasic Coroutines Demonstration:")
    await hello_world()
    
    # 동시 실행
    tasks = [
        count_up("Counter A", 3),
        count_up("Counter B", 3)
    ]
    await asyncio.gather(*tasks)

async def demonstrate_http_client():
    print("\nHTTP Client Demonstration:")
    async with AsyncHttpClient() as client:
        response = await client.get('https://api.github.com/users/github')
        print(f"Status: {response.status}")
        print(f"Data: {response.data}")

async def demonstrate_file_processing():
    print("\nFile Processing Demonstration:")
    processor = AsyncFileProcessor("test.txt")
    
    # 파일 쓰기
    lines = [f"Line {i}" for i in range(5)]
    await processor.write_lines(lines)
    
    # 파일 읽기
    read_lines = await processor.read_lines()
    print("Read lines:", read_lines)

async def demonstrate_producer_consumer():
    print("\nProducer-Consumer Demonstration:")
    queue = AsyncQueue()
    
    # 생산자와 소비자 태스크 생성
    producer = asyncio.create_task(queue.producer())
    consumers = [
        asyncio.create_task(queue.consumer(f"Consumer-{i}"))
        for i in range(2)
    ]
    
    # 모든 태스크 완료 대기
    await producer
    await asyncio.gather(*consumers)

async def demonstrate_async_iteration():
    print("\nAsync Iteration Demonstration:")
    async for i in AsyncRange(0, 5):
        print(f"Value: {i}")

async def main():
    print("Async Programming Demonstrations")
    
    async with timer():
        await demonstrate_basic_coroutines()
        await demonstrate_producer_consumer()
        await demonstrate_async_iteration()
        
        try:
            await demonstrate_http_client()
        except Exception as e:
            print(f"HTTP client error: {e}")
        
        await demonstrate_file_processing()

if __name__ == "__main__":
    asyncio.run(main())

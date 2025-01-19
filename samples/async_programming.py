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

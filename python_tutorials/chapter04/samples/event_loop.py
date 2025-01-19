import asyncio
import random

async def worker(name):
    """작업을 시뮬레이션하는 코루틴"""
    for i in range(3):
        await asyncio.sleep(random.random())
        print(f'Worker {name}: Task {i} completed')

async def main():
    """이벤트 루프를 사용한 태스크 스케줄링 예제"""
    # 현재 이벤트 루프 가져오기
    loop = asyncio.get_running_loop()
    
    # 태스크 생성
    tasks = []
    for i in range(3):
        task = loop.create_task(worker(f'Worker-{i}'))
        tasks.append(task)
    
    # 모든 태스크가 완료될 때까지 대기
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    # 이벤트 루프 생성 및 실행
    asyncio.run(main())

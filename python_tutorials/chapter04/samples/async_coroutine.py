import asyncio
import time

async def say_something(delay, what):
    """비동기적으로 메시지를 출력하는 코루틴"""
    await asyncio.sleep(delay)
    print(what)

async def main():
    """여러 코루틴을 동시에 실행하는 메인 함수"""
    print(f"started at {time.strftime('%X')}")
    
    # 여러 코루틴을 동시에 실행
    await asyncio.gather(
        say_something(1, 'hello'),
        say_something(2, 'world'),
        say_something(3, '!')
    )
    
    print(f"finished at {time.strftime('%X')}")

# 이벤트 루프 실행
if __name__ == "__main__":
    asyncio.run(main())

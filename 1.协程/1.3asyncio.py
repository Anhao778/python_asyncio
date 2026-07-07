import asyncio


async def func1():
    print(123)
    await asyncio.sleep(1) # Simulating a blocking I/O operation, switching to another task
    print(456)


async def func2():
    print(789)
    await asyncio.sleep(1) # Simulating a blocking I/O operation, switching to another task
    print(101112)

async def main():
    await asyncio.gather(func1(), func2()) # Waiting for both tasks to complete

if __name__ == '__main__':
    asyncio.run(main())

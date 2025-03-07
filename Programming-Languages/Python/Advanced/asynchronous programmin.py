import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello, Async!")

async def main():
    await asyncio.gather(say_hello(), say_hello())

asyncio.run(main())

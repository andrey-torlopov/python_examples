import asyncio

# async def main():
#     print('main...')
#     task = asyncio.create_task(foo("text"))
#     # await task
#     # await asyncio.sleep(2)
#     print("finished")
    
# async def foo(text):
#     print("begin foo...")
#     await asyncio.sleep(1)
#     print(text)
#     print("end foo...")

# asyncio.run(main())

async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print("done fetching")
    return {'data': 1}

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    value = await task1
    print(value)
    await task2
    print("done")

asyncio.run(main())
    

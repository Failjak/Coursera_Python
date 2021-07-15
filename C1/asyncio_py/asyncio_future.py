import asyncio


async def slow_operation(future):
    await asyncio.sleep(1)
    future.set_result("Future is done!")
    print("I'm after 'set_result'")

loop = asyncio.get_event_loop()
future = asyncio.Future()
asyncio.ensure_future(slow_operation(future))  # создаем нашу корутину

loop.run_until_complete(future)  # ждем завершения работы объекта future, no function
print('NOW - ', future.result())

loop.close()
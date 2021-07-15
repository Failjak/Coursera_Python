### asyncio.Task - запуск несколькиз корутин, (наследник Future)

import asyncio


async def sleep_task(num):
    for i in range(5):
        print(f'process task: {num} iter: {i}')
        await asyncio.sleep(0.1)
    return num


loop = asyncio.get_event_loop()
task_list = [loop.create_task(sleep_task(i)) for i in range(2)]  # для каждого объекто, кот мы созд с пом create_task,
                                                                 # собственная корутина, кот он выполняет
print("WAIT:")
loop.run_until_complete(asyncio.wait(task_list))

print("\nCREATE TASK:")
loop.run_until_complete(loop.create_task(sleep_task(3)))
print("\nGATHER:")
loop.run_until_complete(asyncio.gather(
    sleep_task(10),
    sleep_task(20),
))

loop.close()

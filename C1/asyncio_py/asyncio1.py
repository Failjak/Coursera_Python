import asyncio

# TODO добавить еще одну корутину, и проверить будет ли она выполнятся тогда, когда эта спит

###  v.1
# @asyncio.coroutine
# def hello_world():
#     while True:
#         print("Hello World!")
#         yield from asyncio.sleep(1.)
#
#
# loop = asyncio.get_event_loop()  # получаес ЭЛ
# loop.run_until_complete(hello_world())  # запускаем в ЭЛ корутину
# loop.close()


###  v.2
async def hello_world():
    while True:
        print("Hello World!")
        await asyncio.sleep(1.)
loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()


"""
    Event loop - планировщик задач. 
    Отвечает за:
        ситевые операции
        переключание контекста между корутин
        если одна спит, то ЭЛ переключит на другую и продолжит выполнение
        
"""
import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)  # читаем данные из сокета
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print('received %r from %r' %(message, addr))
    writer.close()


loop = asyncio.get_event_loop()  # получаем ЭЛ
coro = asyncio.start_server(handle_echo, "127.0.0.1", 10001, loop=loop)
# Передаем корутину .Создаем соединение так же передаем хоста и порт, на кот будем слушать наше соединение
server = loop.run_until_complete(coro)  # установка этого соединения
try:
    loop.run_forever()  #
except KeyboardInterrupt:
    pass

"""
    Как только есть соединение, для него создается своя корутина. 
    В кот будет выполнена наша функция
"""

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
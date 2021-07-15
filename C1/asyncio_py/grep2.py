### v.1
# def grep(pattern):
#     print('Grep start')
#     while True:
#         line = yield
#         if pattern in line:
#             print(line)
#
#
# def start_coroutine(): # - обычная функция, тк нет yield
#     g = grep('python')
#     next(g)
#     g.send('python is simple')
#     g.send('My name is Nik')
#     g.close()
#
#
# start_coroutine()

### v.2
def grep(pattern):
    print("Grep start")
    while True:
        line = yield
        if pattern in line:
            print(line)


def python_coroutine():
    g = grep("python")
    yield from g


g = python_coroutine()
next(g)
g.send('python is my life')

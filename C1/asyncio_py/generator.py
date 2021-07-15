def grep(pattern):
    print("Start grep")
    try:
        while True:
            line = yield
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('grep close')


g = grep('python')
next(g) #g.send(None)
g.send("python 3.0 is simple")
g.send("chelo-robot")

g.throw(GeneratorExit, 'some_error')
g.close()
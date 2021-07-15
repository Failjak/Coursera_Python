def chain(x_iter, y_iter):
    yield from x_iter
    yield from y_iter


def same_chain(x_iter, y_iter):
    for x in x_iter:
        yield x

    for y in y_iter:
        yield y


a = [1, 2, 3]
b = (4, 5)

for i in chain(a, b):
    print(i)

for i in same_chain(a, b):
    print(i)
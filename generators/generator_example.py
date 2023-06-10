from operator import ge


def gen1():
    print("start")
    x = 0
    y = 0
    while True:
        x += 1
        y1 = yield x
        if y1 is not None:
            y = y1


def gen2():
    while True:
        yield from gen1()


g = gen1()
print(next(g))
print(g.send(12))
print(next(g))
print(next(g))
# print(next(g1))
# print(next(g1))

# print(g)

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

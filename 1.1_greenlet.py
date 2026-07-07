import greenlet

def func1():
    print(123)
    g2.switch()
    print(456)
    g2.switch()

def func2():
    print(789)
    g1.switch()
    print(101112)
    g1.switch()

g1 = greenlet.greenlet(func1)
g2 = greenlet.greenlet(func2)

g1.switch()

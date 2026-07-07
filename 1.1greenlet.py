import greenlet

def func1():
    print(123)
    g2.switch()# 切换到g2
    print(456)
    g2.switch()# 切换到g2

def func2():
    print(789)
    g1.switch()# 切换到g1
    print(101112)
    g1.switch()# 切换到g1   

g1 = greenlet.greenlet(func1)
g2 = greenlet.greenlet(func2)

g1.switch() # step1 do g1

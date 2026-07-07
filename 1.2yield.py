
# Example of a generator function using yield from
def func1():
    yield 1
    yield from func2() # Delegating to func2
    yield 2

def func2():
   yield 3
   yield 4

f1 = func1() # Creating an iterator object
for item  in f1:
    print(item) # Output: 1 3 4 2

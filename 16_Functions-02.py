def add1(a, b, c = 0):
    return a+b+c

def Test1():
    print(add1(1, 2, 3)) # Positional args
    print(add1(b = 1, a = 2, c = 3)) # Named args
    print(add1(1, 2))

def add2(*values):
    sum = 0
    for i in values:
        sum += i
    return sum

def Test2():
    print(add2(1, 2, 3, 4, 5))  # Packing / Variable args
    lst = [1, 2, 3]
    print(add1(*lst))           # Unpacking

# Test1()
Test2()
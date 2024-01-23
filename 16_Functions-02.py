def add1(a, b, c = 0):
    return a+b+c

def Test1():
    print(add1(1, 2, 3)) # Positional args
    print(add1(b = 1, a = 2, c = 3)) # Named args
    print(add1(1, 2))

def add2(*values):
    print("add2:", type(values))
    sum = 0
    for i in values:
        sum += i
    return sum

def Test2():
    print(add2(1, 2, 3, 4, 5))  # Packing / Variable args
    lst = [1, 2, 3]
    print(add1(*lst))           # Unpacking


def PrintWords(**kwWords):
    print(type(kwWords))
    for key, value in kwWords.items():
        print(key, " - ", value)
    
    for key in kwWords.keys():
        print(key)

    print()

def Test3():
    # PrintWords(1, 2, 3)
    PrintWords(roll=10, name="Manish", age=16)

def func(*args, **kwargs):
    print(args)
    print(kwargs)

def Test4():
    func(1, 2, 3, 4, 5, a = 10, b = 20)

# Special Args - '/' '*'
def SpecificFunc(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

# def Func2(a, b, c, *)
def Test5():
    SpecificFunc(1, 2, 3, 4, e = 5, f = 6)
    SpecificFunc(1, 2, c = 3, d = 4, e = 5, f = 6)
    # SpecificFunc(1, 2, 3, 4, 5, 6) # Error
    # SpecificFunc(a = 1, b = 2, c = 3, d = 4, e = 5, f = 6) # Error

# Test1()
# Test2()
# Test3()
Test4()
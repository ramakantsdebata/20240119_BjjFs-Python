# All collections are iterables
# print(dir(list))
# print()
# print(dir(tuple))

lst = [1, 2, 3, 4, 5]

def Test1():
    for x in lst:
        print(x)

def Test2():
    for i in range(len(lst)):
        print(lst[i])

def Test3():
    i = 0
    while(True):
        print(lst[i])
        i += 1

def Test4():
    it = iter(lst) # lst.__iter__()
    # print(dir(it))
    while(True):
        try:
            # print(next(it))
            print(it.__next__())
        except StopIteration:
            print("StopIteration received")
            break      
    print("Loop completed")

# Generator Function: Uses the 'yield' keyword
# Iterator class: Implements __iter__() and __next__()
    
class MyIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration

def Test5():
    it = MyIterator(5)
    for x in it:
        print(x)

class MyFib:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

def iterate(obj):
    it = iter(obj)
    for x in it:
        print(x)

def Test6():
    objFib = MyFib(7)

    print("-"*10)
    iterate(objFib)

    print("-"*10)
    iterate(objFib)

    print("-"*10)
    iterate(objFib)
    




# Test1()
# print("-"* 20)
# Test2()
# print("-"* 20)
# Test3()
# Test4()
# Test5()
Test6()
def my_decorator(func):
    def wrapper():
        print("Logging Function entry")
        func()
        print("Logging Function exit")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

#######################
# say_hello()
# my_decorator(say_hello)()

###########################################

def custom_extend(cls):
    class NewMath(cls):
        def subtract(self, x, y):
            return x - y
        
    return NewMath


@custom_extend
class MyMath:
    def add(self, x, y):
        return x + y
    

math = MyMath()
print(math.add(10, 20))
print(math.subtract(10, 20))

# nmath = NewMath()
# print(nmath.add(10, 20))
# print(nmath.subtract(10, 20))

###########################################
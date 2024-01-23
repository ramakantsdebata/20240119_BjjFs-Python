# # def Foo():
# #     pass

# def Bar():
#     print("Bar")
#     Foo()

# def Foo():
#     print("Foo")

# def main():
#     print("Main")
#     Bar()

# main()

# Not Define Higher
#  Define Earlier is acceptable


#------------------------------------------

# int Foo(); // Declaration

# int Bar()
# {
#     printf("Bar");
#     Foo();
# }

# int Foo()
# {
#     printf("Foo");
# }

# int main()
# {
#     printf("Main");
#     Bar();

#     return 0;
# }

# def Add(a: int, b: int)->int:
#     '''
#     Adds two values and returns the sum
#     a: [IN]; type restricted to 'int'
#     b: [IN]; type restricted to 'int'
#     ret: type restricted to 'int'
#     '''
#     return a + b

# a = 10; b = 20
# print(Add(a, b))
# print(Add.__doc__)

# ###########################################################

def SquareAreaCircumference(side):
    area = side**2
    cir = side * 4

    return area, cir 
    # Packing into a tuple and returning the tuple

def Test1():
    len = 5
    x = SquareAreaCircumference(len)
    print(type(x), x)

    a, c = x    # unpacking
    print(a, c)

def Test2():
    lst = [1, 2, 3, 4, 5]
    a, b, c = lst
    print("a", type(a), a)
    print("b", type(b), b)
    print("c", type(c), c)

Test1()
# Test2()
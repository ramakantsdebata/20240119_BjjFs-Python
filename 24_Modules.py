# from math import sqrt as squareroot

# def Test1():
#     print(squareroot(81))

##############################

# import greet

# def Test2():
#     greet.greet()

##############################
# from _24_ModuleCollection import greet

# def Test3():
#     greet.greet()
#     greet.greetName("Manish")

# from _24_ModuleCollection import math

# def Test4():
#     print(math.add(1, 2))

##############################

# from _24_ModuleCollection import *

# def Test5():
#     print(greet.greet())
#     # print()

#############################
    
from TestModule import *
from TestModule import swap

def Test6():
    Testing()
    sort([1, 2, 3])
    swap(1, 2)

# from  _24_ModuleCollection import *
# from _24_ModuleCollection import math

def main():
    # Test1()
    # Test2()
    # Test3()
    # Test4()
    # Test5()
    Test6()

main()
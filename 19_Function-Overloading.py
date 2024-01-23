# def add(a, b):
#     return a + b

# # print(type(add), add)

# def add(a, b, c = 0):
#     return a + b + c

# def add(a: str, b: str):
#     return a + b

# print(type(add), add)

# fn = add # add(a: Any, b: Any)->Any

## Using var args #######################################

# def add(dataType, *args):
#     if dataType == int:
#         # iterate and add to identity element
#         return sum(args)
#     elif dataType == float:
#         # Similar to above using float specific operations
#         return sum(args)
#     elif dataType == str:
#         # Concatenation
#    elif dataType == MyType:
#         # Operate on the objects as permitted by the type

## Using multiple dispatch #######################################
from multipledispatch import dispatch

@dispatch(int, int)
def add(a: int, b: int):
    return a + b

@dispatch(float, float)
def add(a: float, b: float):
    return a + b

@dispatch(str, str)
def add(a: str, b: str):
    return a + b

# @dispatch(Transaction, Transaction)
# def add(a: Transaction, b: Transaction):
#     return a.amount + b.amount

      
def main():
    print(add(1, 2))
    print(add(1.0, 2.0))
    print(add("Hello ", "World"))
    # print(add(Transaction(12345, 100, "NEFT", "12-01-2024"), Transaction(12346, 200, "UPI", "19-01-2024")))

main()


# CPP code ##############

# int add(int, int)           --> add_2@int
# float add(float, float)     --> add_2@float

# a(1, 2)     --> add_2@int(1, 2)
# a(1.0, 2.0) --> add_2@float(1.0, 2.0)

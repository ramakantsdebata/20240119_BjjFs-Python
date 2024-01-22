# # List - Mutable

# l1 = [1, 2, 3, 4]
# l2 = list()

# l1.pop()
# l1.append(5)
# l1.insert(3, 4)
# print(l1)

# # 1, 2, 3, 4, 5, 4, 6, 7, 4
# l1.remove(4)

# 7 in l1

# len()

##########################################################

# def Modify1(a, b):
#     print("Modify->", id(a), id(b))
#     a = 40
#     print("Modify->", id(a), id(b))

# def Test1():
#     x = 10
#     y = 20
#     print("Main->", id(x), id(y))
#     Modify(x, y)

#     print(x)

# def Modify2(a):
#     a.pop()

# def Test2():
#     lst = [1, 2, 3, 4, 5]

#     Modify2(lst)
#     print(lst)


# # Test1()
# Test2()

##########################################################

lst1 = [1, 2, 3, 4, 5]
lst2 = lst1[:]
lst2.pop()


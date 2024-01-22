fruits = ["apple", "banana", "cherry", "dragonfruit", "emuberry", "kiwi", "mango"]

newColl = [x    for x in range(10)     if x%2 == 0]
print(newColl)

newColl = [x     for x in fruits       if 'a' in x]
print(type(newColl), newColl)

newColl = {x     for x in fruits       if 'a' in x}
print(type(newColl), newColl)

newColl = {x:x**2    for x in range(10)}
print(type(newColl), newColl)

newColl = (x     for x in fruits       if 'a' in x)
print(type(newColl), newColl)

newColl = tuple(x     for x in fruits       if 'a' in x)
print(type(newColl), newColl)

print("\n\n")

dataType = type(str)
print(type(dataType), dataType)

strMethods = tuple(x   for x in dir(str) if x.startswith('_') == False)
print(strMethods)

print("-------------------------------------")
# tp = tuple()
lst = list()
for x in dir(str):
    if x.startswith('_') == False:
        lst.append(x)
tp = tuple(lst)
print(lst)

print("\n\n--------------------------------------\n\n")
MyType = set()
publicMethods = tuple(x   for x in dir(MyType) if callable(getattr(MyType, x)) ==True and x.startswith('_') == False)
print(publicMethods)

# Type - Integer, Value = 10
a = 10000
b = 10000

print("a:", id(a), "\nb:", id(b))
b = b + 1
print("a:", id(a), "\nb:", id(b))

c = 20000
print("\nc:", id(c))

c = c - 10000
print("\nc:", id(c))

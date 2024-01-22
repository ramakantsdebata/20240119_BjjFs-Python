# Mutable
# Contains key-value pairs
# key - must be hashable
# value - any type

dt = dict(A=10, B=20, C=30)
# dt = dict.fromkeys(<set>)

key = 'A'
len(dt)
dt[key] = value
key in dt
iter(dt)

for keys in dt.keys():
    print(keys)

for value in dt.values():
    print(value)

for key, value in dt.items():
    print(key, "-->", value)

dt2 = dict()

dt2.update(dt1)

print(dt[key])
if(key in dt):
    print(dt[key])
dt.get(key)
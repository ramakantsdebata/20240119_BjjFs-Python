x = ["manish", "abhijeet", "rakesh", "vinayak", "shankar"]

res = map(lambda n: n.capitalize(), x)
print(type(res))
print(res)

resMap = list(map(lambda n: n.capitalize(), x))
print(resMap)

resFilter = list(filter(lambda n: n.startswith("a"), x))
print(resFilter)

from functools import reduce
resReduce = reduce(lambda a, b: a + b, x)
print(resReduce)
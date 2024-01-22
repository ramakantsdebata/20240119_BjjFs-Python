# Set is mutable
# Collection of keys i.e. elements should be hashable
#       i.e. elements should be immutable

st1 = {1, 2, 3, 4}
st2 = set()

lst1 = ['a', 'b']
str1 = "This is a stest string"
st3 = {str1}
str1 = "Changing the string again"

# Set is mutable
st1.add(6)
st1.update(lst1)
print(st1)
st1.remove(5)
st1.remove(15)
st1.discard(15)

st1.union(st2)
st1.intersection(st2)
st1.difference(st2)
st1.symmetric_difference(st2)

st1.issubset(st2)
st1.issuperset(st2)
st1.isdisjoint(st2)


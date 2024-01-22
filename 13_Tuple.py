# Immutable
# Non-homogeneous

# Compare with a List - like an immutable list

tp1 = (1, 2, 3, "Test", {1, 2, 3})
print(tp1)

print(tp1[4])

tp1[4].add(4)

print(tp1)

# Named Tuple
print("\n\n")

from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
Point = namedtuple('Point', 'x y')

p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1[0], p1[1])
print(p1.x, p1.y)

Student = namedtuple('Student', 'name age standard')
s1 = Student("Abhijeet", 16, 9)
s2 = Student("Manish", 18, 12)

print(s1.name, s1.age, s1.standard)
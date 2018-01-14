from collections import Counter
from collections import namedtuple

# ------------------Zip------------------
# zip takes in iterables as input and returns list of tuples
s = 'abc'
l = [1, 2, 3]
print zip(s, l)  # [('a', 1), ('b', 2), ('c', 3)]

s = 'abc'
l = [1, 2]
print zip(s, l)  # [('a', 1), ('b', 2)]

s = 'abc'
l = [1, 2, 3]
t = (4, 5, 6)
print zip(s, l, t)  # [('a', 1, 4), ('b', 2, 5), ('c', 3, 6)]

# ------------------Counter------------------
count = Counter('parrot')
print count  # Counter({'r': 2, 'a': 1, 'p': 1, 't': 1, 'o': 1})

# ------------------Named tuple------------------
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=10, y=20)
print p  # Point(x=10, y=20)

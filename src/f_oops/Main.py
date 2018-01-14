import Point

p1 = Point.Point(10, 20)
p2 = Point.Point(15, 25)

# ---------------------------Operator Overloading---------------------------
# operator overloading example. __add__ is invoked here
print p1 + p2

# adding an integer to Point works, however the opposite won't work
# since it is not commutative. To make this work, __radd__ needs to implemented
print p1 + 10
print 10 + p1


# ---------------------------Polymorphism---------------------------
# Polymorphic function is function that work with several types of input
# Below function is an example and it works with lists, tuples and even dictionaries

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


list1 = ['a', 'b', 'c', 'b', 'c']
print histogram(list1)  # {'a': 1, 'c': 2, 'b': 2}
print histogram(tuple(list1))  # {'a': 1, 'c': 2, 'b': 2}

# ---------------------------Abstract classes---------------------------
# In Python, interface and abstract class are one and the same
# Python supports multiple inheritance
import collections

collections.Set

# ---------------------------Duck typing---------------------------

# ---------------------------Mixins---------------------------

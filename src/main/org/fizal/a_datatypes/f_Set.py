# Mutable set
set1 = set()  # empty set
print set1
set1 = {1, 2, 3, 1, 2, 3, 1, 2, 3}
set1.add(4)
print ("Set1 = ", set1)  # prints set([1, 2, 3, 4]

list3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
set2 = set(list3)  # mutable set
set2.add(4)
print ("Set2 = ", set2)

# Immutable frozen set
set3 = {1, 2, 3, 1, 2, 3, 1, 2, 3}
set3 = frozenset(set3)

# comparison
set1 = {1, 2, 3}
set2 = {1, 3, 2}
print set1 == set2  # True
print 1 in set2  # True
print type(set1) == type(set())  # True, don't use this to compare types
print isinstance(set1, set)  # True

# iteration
for i, x in enumerate(set2):
    print i, x

# set comprehension
set4 = {x + 1 for x in set1}
print set4

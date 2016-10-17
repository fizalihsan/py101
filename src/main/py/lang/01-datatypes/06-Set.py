# Mutable set
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

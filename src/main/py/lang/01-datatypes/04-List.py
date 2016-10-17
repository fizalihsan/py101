# definition
list0 = []
print list0
list1 = [1, 2.0, 'c', 2, 3, 4, 5]
print list1  # [1, 2.0, 'c']

# setters
list1.append("d")
print list1  # prints [1, 2.0, 'c', 'd']

print list1 + 'e' # + operator creates a new list and leaves the original list unchanged

list1.insert(0, "apple")
print list1  # prints ['apple', 1, 2.0, 'c', 'd']

list1.extend(["apple", "orange"])  # like appendAll
print list1

# getters
list2 = [1, 2, 3, 4, 5]
print list2.pop(0)  # element at index 0 is popped
print list2.pop()  # last element is popped
print list2  # [2, 3, 4]

# deletion
del list2[0]
print list2

# converting
print tuple(list1)
t = (1, 2, 3, 4)
print list(t)

# sorting
list3 = [2, 3, 5, 6]
list3.reverse()
print list3  # [6, 5, 3, 2]

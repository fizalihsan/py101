list1 = [1, 2.0, 'c', 2, 3, 4, 5]
print list1  # [1, 2.0, 'c']
list1.append("d")
print list1  # prints [1, 2.0, 'c', 'd']
list1.insert(0, "apple")
print list1  # prints ['apple', 1, 2.0, 'c', 'd']

list1.extend(["apple", "orange"])  # like appendAll
print list1

list2 = [1, 2, 3, 4, 5]
print list2.pop(0)  # element at index 0 is popped
print list2.pop()  # last element is popped
print list2  # [2, 3, 4]

# List to tuple and vice versa
print tuple(list1)
print list(tuple1)
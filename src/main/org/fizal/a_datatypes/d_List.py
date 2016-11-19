# definition
list0 = []
print list0
list0 = list()
print list0
list1 = [1, 2.0, 'c', 2, 3, 4, 5]
print list1  # [1, 2.0, 'c']

# setters
list1.append("d")
print list1  # prints [1, 2.0, 'c', 'd']

print list1 + ["e"]  # + operator creates a new list and leaves the original list unchanged

list1.insert(0, "apple")
print list1  # prints ['apple', 1, 2.0, 'c', 'd']

list1.extend(["apple", "orange"])  # like appendAll
print list1

# getters
# Subscripting is the term for describing when you access an element in a list or a tuple as well as a dictionary
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

# ------------------------List comprehension------------------------
# bracket [] operator indicates that we are constructing a new list. This is called list comprehension
list4 = list('fizal')

# without condition
print [c.capitalize() for c in list4]  # ['F', 'I', 'Z', 'A', 'L']

# with condition
print [c.capitalize() for c in list4 if c in ('a', 'e', 'i', 'o', 'u')]  # ['I', 'A']

# ------------------------Generator expressions------------------------
# Generator expressions are similar to list comprehensions, but with parentheses instead of square brackets.
# The result is a generator object that knows how to iterate through a sequence of values.
# But unlike a list comprehension, it does not compute the values all at once; it waits to be asked.
# The built-in function next gets the next value from the generator.
g = (x ** 2 for x in range(5))

# The generator object keeps track of where it is in the sequence, so the for loop picks up
# where next left off. Once the generator is exhausted, it continues to raise StopException
print next(g)  # 0
print next(g)  # 1
print next(g)  # 4
print next(g)  # 9
print next(g)  # 16
# print next(g) # 16 # StopIteration exception is thrown

g = (x ** 2 for x in range(5))

# looping through the generator expression
for val in g: print val

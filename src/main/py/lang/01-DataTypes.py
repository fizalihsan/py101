# ----------------------
print("Hello World")

#####################################################
#                    NUMBER
#####################################################
int1 = 23  # integer
float1 = 12.345  # integer
print int1, float1
infinity = 2e304 * 3923817273929
print(infinity)  # prints 'inf' for infinity

# ~~~~~~~~~~~~~Division~~~~~~~~~~~~~
print 44 / 10  # Before Python 3, an integer 4 is returned skipping the reminder. Now, a float 4.4

# ~~~~~~~~~~~~~Number formatting~~~~~~~~~~~~~
print("Integer = %d" % int1)  # passing single argument
print("Integer = %d Float = %f Octal = %o Hex = %x" % (int1, float1, int1, int1))  # passing multiple arguments
print("Number formatting = %0.4f" % (5 / 3.0))

num1 = 10
num2 = 20
print("v1 = %d v2 = %d" % (num1, num2))
num1, num2 = num2, num1
print("v1 = %d v2 = %d" % (num1, num2))

#####################################################
#                    STRING
#####################################################
str1 = "Hello "  # double quote. Strings are immutable
str2 = 'world, '  # single quote
str3 = """How
are
you?
"""
print(str1 + str2 + str3)  # string concatenation
print str1[2]
for c in str1: print c  # printing characters

# ~~~~~~~~~~~~~String formatting~~~~~~~~~~~~~
print("Float as int = %d Int as float = %f Int as string = %s" % (float1, int1, int1))  # mixing argument types

#####################################################
#                    COLLECTION
#####################################################

# ~~~~~~~~~~~~~Tuples~~~~~~~~~~~~~
tuple1 = ()  # immutable empty tuple
print tuple1  # ()
tuple1 = (1, 2.0, 'c')
print tuple1  # (1, 2.0, 'c')
print "First element = %s Length = %d" % (tuple1[0], len(tuple1))
print tuple1[-1]  # access last element

tuple2 = (tuple1, "second", "third")
print ("Accessing a tuple through another tuple = %s" % tuple2[0][1])  # prints 2.0
# tuple1[10] <-- throws IndexError: tuple index of range

# ~~~~~~~~~~~~~Lists~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~Ranges~~~~~~~~~~~~~
print "Sliced tuple = ", tuple1[0:3]  # slicing a tuple returns a tuple
print "Sliced list = ", list1[0:3]  # slicing a list returns a list

# ~~~~~~~~~~~~~Sets~~~~~~~~~~~~~
# Mutable set
set1 = {1, 2, 3, 1, 2, 3, 1, 2, 3}
set1.add(4)
print ("Set1 = ", set1) # prints set([1, 2, 3, 4]

list3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
set2 = set(list3) # mutable set
set2.add(4)
print ("Set2 = ", set2)

# Immutable frozen set
set3 = {1, 2, 3, 1, 2, 3, 1, 2, 3}
set3 = frozenset(set3)

# ~~~~~~~~~~~~~Dictionaries~~~~~~~~~~~~~
dict1 = {}  # empty dictionary
print dict1  # {}
dict1 = {"a": 1, "b": 2}
print dict1["a"]
print dict1.keys()
print dict1.values()

# accessing non-existent element
try:
    print(dict1["x"])
except StandardError, e:
    print "Error occurred: ", e.args

for k in dict1:
    print k

#####################################################
#                    SPECIAL
#####################################################
vNone = None  # like void
vTrue = True
vFalse = False
print(vTrue == 1)
print(vFalse == '2')

# ~~~~~~~~~~~~~OOPS~~~~~~~~~~~~~

# Finding an object type
print(type(int1))  # <type 'int'>
print(type(str1))  # <type 'str'>
print(type(type(str1)))  # <type 'type'>

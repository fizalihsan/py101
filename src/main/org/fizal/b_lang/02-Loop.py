# While
i = 4
while i > 0:
    print i
    i -= 1

# For
for x in range(4, 0, -1):
    print x

# Enumerate
# iterate a collection with index of the elements
list1 = [1, 2, 3]
for index, element in enumerate(list1):
    print("%d : %d" % (index, element))

# filter pattern?
result = [(element + 1) for element in list1 if element >= 2]
print result

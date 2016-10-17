# ------------------While------------------
i = 4
while i > 0:
    print i
    i = i - 1

# ------------------For------------------
for x in range(4, 0, -1):
    print x

# ------------------Enumerate------------------
# iterate a collection with index of the elements
l = [1, 2, 3]
for index, element in enumerate(l):
    print("%d : %d" % (index, element))

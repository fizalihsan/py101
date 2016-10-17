# tuples are immutable.

# definition
tuple1 = ()  # immutable empty tuple
print tuple1  # ()
tuple1 = (1, 2.0, 'c')
print tuple1  # (1, 2.0, 'c')

# getters
print "First element = %s Length = %d" % (tuple1[0], len(tuple1))
print tuple1[-1]  # access last element

tuple2 = (tuple1, "second", "third")
print ("Accessing a tuple through another tuple = %s" % tuple2[0][1])  # prints 2.0
# tuple1[10] <-- throws IndexError: tuple index of range

# iterating values
t = (('john', 'doe'), ('jack', 'smith'), ('bill', 'clinton'))
for x in t:
    print x

for first, last in t:
    print first, last

# sorting a tuple. since tuple is immutable, tuple.sort() is not provided
print sorted((3, 2, 1, 0))  # returns a list [0, 1, 2, 3]

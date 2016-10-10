
#####################################################
#                    CONDITIONS
#####################################################
# comparing lists
list1 = ["apple", "orange"]
list2 = ["apple", "orange"]
print list1 == list2
print len(list1) > 0 and not len(list1) > 5

# If-else

if len(list1) == 0:
    print "List is empty"
elif len(list1) == 1:
    print "Has 1 element only"
else:
    print "Has more than 1 element"

#####################################################
#                    LOOPS
#####################################################

# While
i = 4
while i > 0:
    print i
    i = i - 1

# For

for x in range(4, 0, -1):
    print x



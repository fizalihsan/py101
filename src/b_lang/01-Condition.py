# If-else
list1 = ["apple", "orange"]
list_size = len(list1)

if list_size == 0:
    print "List is empty"
elif list_size == 1:
    print "Has 1 element only"
else:
    print "Has more than 1 element"

# and operator
print list_size > 0 and list_size < 10
print 0 < list_size < 10  # this is called a 'simplified chained comparison'

if 0 < list_size < 10:
    print 'List size is optimal'
else:
    print 'List size is out of control'

# or operator
print list_size < 0 or list_size < 10

# Ternary operator or Conditional Expression
print 'List is empty' if list_size == 0 else 'List is not empty'

# assert statement
assert list_size == 2  # AssertionError is thrown when not satisfied

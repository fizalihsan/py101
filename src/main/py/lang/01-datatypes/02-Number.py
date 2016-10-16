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
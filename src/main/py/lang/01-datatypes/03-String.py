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

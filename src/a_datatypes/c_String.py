# -*- coding: utf-8 -*-
# the line above allows unicode in the scripts

str1 = "Hello "  # double quote. Strings are immutable
str2 = 'world, '  # single quote
str3 = """How
are
you?
"""
str4 = str('welcome')  # explicit definition
print(str1 + str2 + str3)  # string concatenation
print str1[2]
print str4

# string types
unicode_string = u'unicode string'
raw_string = r'raw string'
print unicode_string
print raw_string

# iterating
for c in str1: print c  # printing characters

# slicing
name = "fizal"
print name[0:3]  # prints 'fiz'
print name[:4]  # prints 4 characters from start 'fiza'
print name[3:]  # prints from 4th character till end 'al'
print name[:]  # prints the entire string

# String formatting
print("Float as int = %d Int as float = %f Int as string = %s" % (12.34, 12, 23))  # mixing argument types

# comparison
print str1 == str2
str5 = "Hello"
str6 = "Hello"
print str5 is str6  # checks if both str5 and str6 both refer to the same object
print isinstance(str1, str)

# searching
print name.__contains__('z')  # returns True
print 'z' in name  # returns True

# sorting
print sorted(name)  # ['a', 'f', 'i', 'l', 'z']

i = reversed(name)  # returns an iterator
for c in i:
    print c

# split
l = list(name)  # list function breaks a string into individual letters
str = "Hello, How are you?"
print str.split()  # spilt function breaks a string into words
print str.split(",")

# join
lst = ['f', 'i', 'z', 'a', 'l']
delimiter = ''
print delimiter.join(lst)

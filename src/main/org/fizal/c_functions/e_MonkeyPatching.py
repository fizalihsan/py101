"""
This example demonstrates the following

* How to dynamically add a new function to a class
* How to define a new implementation to an existing function (called monkey patching)
* How to remove a method implementation from a class
* How to dynamically add new attributes to a class
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        print "inside __init__"

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


person = Person('John', 'Doe')
print person.full_name()


# dynamically add a new function to a class
def last_first_name(self):
    return "%s, %s" % (self.last_name, self.first_name)


Person.last_name_first = last_first_name
print person.last_name_first()


# monkey patching: defining a new method implementation
def name_in_braces(self):
    return "{%s %s}" % (self.first_name, self.last_name)


Person.full_name = name_in_braces
print person.full_name()

# removing a method implementation
del Person.full_name
try:
    print person.full_name()
except AttributeError:
    print "full_name() method is no longer found in Person"


# adding new attributes at runtime
def __getattr__(self, item):
    # this special method is called when normal attribute lookup fails
    if item == 'hyphenated_name':
        return lambda: "%s-%s" % (self.first_name, self.last_name)

    raise AttributeError(item)


Person.__getattr__ = __getattr__

print person.hyphenated_name()

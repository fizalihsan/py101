def func1():
    """ This is a docstring or documentation string. No indentation needed here.
    It can be access via <funcName>.__doc__"""
    return "Hello World"


print func1()

# Function dir() shows all the properties of the object in which it is called
print dir()  # ['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'func1']

print func1.__doc__  # Accessing the docstring of a function
print func1.__name__

# -----------------------Variable Scope-----------------------
PI = 3.1415  # global module variable


def func2():
    global PI  # global definitions must be placed at the beginning of the function
    print PI  # prints 3.1415
    PI = "blah"


func2()
print PI  # prints 'blah'
PI = 3.1415  # global module variable


def func3():
    PI = "blah"
    print PI  # prints 'blah'

    global PI  # no effect
    print PI  # prints 'blah'


func3()

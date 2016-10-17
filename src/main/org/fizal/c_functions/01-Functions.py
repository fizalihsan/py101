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


def function_with_default_param_value(name='fizal'):  # method parameter with default value
    print 'Hello %s' % name


function_with_default_param_value()  # prints 'Hello fizal'
function_with_default_param_value('Ihsan')  # prints 'Hello Ihsan'


def function_within_function():
    def func_inside(num):
        def isEven(num):
            return num % 2 == 0

        return (num + 1) if isEven(num) else (num + 2)

    print func_inside(3)
    print func_inside(4)


function_within_function()


def function_calling_with_named_args(name, age):
    print 'Name = %s Age = %d' % (name, age)


function_calling_with_named_args('fizal', 20)
function_calling_with_named_args(name='mohamed', age=20)
function_calling_with_named_args(age=20, name='ihsan')  # with named args, order can be changed

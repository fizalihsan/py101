import inspect

import Point

p = Point.Point()
print dir(p)  # to see all the methods and variables defined in an object

print inspect.getfile(Point)  # returns the file where the module is defined
print inspect.getfile(Point.Point)  # returns the file where the object is defined

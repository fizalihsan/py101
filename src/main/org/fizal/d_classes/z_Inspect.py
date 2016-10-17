import inspect

import Point

p = Point.Point()
print dir(p)  # to see all the methods and variables defined in an object

print inspect.getfile(Point)  # C:\Fizal\...\src\main\org\fizal\d_classes\Point.pyc
print inspect.getfile(Point.Point)
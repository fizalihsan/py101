import copy
from Point import Point


p1 = Point(3, 4)
p2 = copy.copy(p1) # shallow copy
p3 = copy.deepcopy(p1) # deep copy

print p1 == p2 # False
print p1 is p2 # False. Indicates they are not the same object

from src.main.org.fizal.d_classes.Point import Point

# p = src.main.org.fizal.d_classes.Point()
print "@@@@@@@", type(Point)
print Point  # __main__.Point
p = Point()  # creating a new instance of Point
print p  # <__main__.Point instance at 0x00000000021F02C8>
print p.x  # returns 0
print p.get_x()  # returns 0
print p.get_y()  # returns 0
# print p.get_z()  # throws 'AttributeError: Point instance has no attribute 'z''

print hasattr(p, 'z')  # returns False

p = Point(12, 24)
print p.get_x()
print p.get_y()

# p = Point(x=-1, y=-2)  # ArithmeticError is thrown
# p = Point(101, 101)  # ArithmeticError is thrown



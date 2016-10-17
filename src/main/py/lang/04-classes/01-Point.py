my_var = 123
print my_var


class Point:
    '''Documentation about this class goes here
    Methods:
        get_x():
        get_y():
    '''

    def __init__(self):  # default constructor
        pass  # means do nothing

    def __init__(self, x=0, y=0):  # Overloaded constructor
        """

        :param x:
        :param y:
        """
        if x < 0 or x > 100:
            raise ArithmeticError

        self.x = x
        self.y = y
        return

    def get_x(self):
        """
        A public method is called an interface

        :return: x
        :rtype integer
        """
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z


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

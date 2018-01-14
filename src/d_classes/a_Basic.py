class Point(object):
    """Documentation about this class goes here
    Methods:
        get_x():
        get_y():
    """

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
        * This is a method since it belongs to a class. Though syntactically same as a function,
        a method is associated with a class, and a function isn't.

        * A public method is called an interface.

        :return: x
        :rtype integer
        """
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def __str__(self):
        return 'x=%.2d y=%.2d' % (self.x, self.y)

        # def __eq__(self, other):
        #     """Override the default equals behavior"""
        #     if isinstance(other, self.__class__):
        #         return self.__dict__ == other.__dict__
        #
        #     return False


print type(Point)  # <type 'type'>
print Point.__class__  # <type 'type'>
print Point.__class__.__base__  # <type 'object'>
print Point  # <class '__main__.Point'>
p = Point()  # creating a new instance of Point
print p  # x=00 y=00
print p.x  # 0
print p.get_x()  # 0
print p.get_y()  # 0
# print p.get_z()  # throws 'AttributeError: Point instance has no attribute 'z''
print hasattr(p, 'z')  # returns False

p = Point(12, 24)
print p.get_x()  # 12
print p.get_y()  # 24


# p = Point(x=-1, y=-2)  # ArithmeticError is thrown
# p = Point(101, 101)  # ArithmeticError is thrown


# ~~~~~~~~~~~~~~~~~~~~~~~ Setting dynamic attributes ~~~~~~~~~~~~~~~~~~~~~~~
class Rectangle(object):
    def area(self):
        return self.length * self.width


r = Rectangle()
r.length, r.width = 10, 20  # though this is allowed, it adds confusion
print r.area()  # 200


# ~~~~~~~~~~~~~~~~~~~~~~~ Constructor takes dynamic parameters~~~~~~~~~~~~~~~~~~~~~~~
class Player(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def display(self):
        for k, v in self.__dict__:
            print "k={0}, v={1}".format(k, v)


player1 = Player(key1="value1")
print player1.__getattribute__('key1')
player2 = Player(key1="value1", key2="value2")
print player2.__getattribute__('key2')

# ~~~~~~~~~~~~~~~~~~~~~~~ The Zen of Python ~~~~~~~~~~~~~~~~~~~~~~~
import this

print this  # prints the Zen of python poem

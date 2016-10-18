class Point:
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

    def addPoint(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def increment(self, value):
        return Point(self.x + value, self.y + value)

    def __add__(self, other):
        """Operator overloading example

        Based on the type of input parameter, different method is invoked. This technique
        is called 'type based dispatching'
        """
        if isinstance(other, Point):
            return self.addPoint(other)
        elif isinstance(other, int):
            return self.increment(other)

    def __radd__(self, other):
        """ This implementation makes the operator overloading commutative """
        return self.__add__(other)

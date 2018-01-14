class Point:
    def __init__(self, x=0, y=0):  # Overloaded constructor
        if x < 0 or x > 100:
            raise ArithmeticError

        self.x = x
        self.y = y
        return

    def get_x(self):
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


# -------------------------Gather-------------------------
def print_all(*args):
    print type(args)  # tuple
    for arg in args:
        print arg


print_all(1, 2, 3, 4)  # all the args are 'gathered' as single arg


# to gather keywords
def print_all_with_keywords(*args, **kwargs):
    print args, kwargs


print_all_with_keywords(1, 2, a=3, c=4)


# -------------------------Scatter-------------------------
def scatter(a, b, c):
    print a
    print b
    print c


tuple1 = (4, 5, 6)
scatter(*tuple1)  # all the args are 'scattered into multiple args here

# Scatter operator **
d = dict(x=1, y=2)
p = Point(**d)
print p  # x=01 y=02

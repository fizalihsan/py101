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

    # def __eq__(self, other):
    #     """Override the default equals behavior"""
    #     if isinstance(other, self.__class__):
    #         return self.__dict__ == other.__dict__
    #
    #     return False


from math import cos, sin


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @classmethod
    def polar(cls, r, theta):
        return cls(r * cos(theta), r * sin(theta))


p1 = Point(x=10, y=20)
p2 = Point.polar(r=10, theta=20)

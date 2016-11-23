from src.main.org.fizal.d_classes.Point import Point


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

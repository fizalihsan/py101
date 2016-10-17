def printall(*args):
    print type(args)  # tuple
    for arg in args:
        print arg


printall(1, 2, 3, 4)  # all the args are 'gathered' as single arg


def scatter(a, b, c):
    print a
    print b
    print c


tuple = (4, 5, 6)
scatter(*tuple)  # all the args are 'scattered into multiple args here

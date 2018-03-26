def hello_solar_system(original_function):
    """ This is a decorator.
    :param original_function: function to be decorated
    :return: function with decoration applied
    """

    def wrapper():
        original_function()  # invoke original_function
        print "Hello, solar system"

    return wrapper


def hello_galaxy(original_function):
    def wrapper():
        original_function()  # invoke original_function
        print "Hello, galaxy"

    return wrapper


"""This is equivalent to hello_galaxy( hello_solar_system( hello() ) )"""


@hello_galaxy
@hello_solar_system
def hello():
    print "Hello, world"


# Below call prints the following
# Hello, world
# Hello, solar system
# Hello, galaxy
hello()
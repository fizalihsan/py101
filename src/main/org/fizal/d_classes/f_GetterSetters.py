print "----------------------------------------- GETTER SETTER  -----------------------------------------------------"

class Car(object):
    def __init__(self, make):
        self._make = make

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        self._make = make

    def __str__(self):
        return 'Car:{0}'.format(self._make)

print Car('Honda').make
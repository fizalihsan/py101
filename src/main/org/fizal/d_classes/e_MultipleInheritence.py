class Animal(object):
    def get_type(self):
        return 'Animal'


class Fish(object):
    fish_type = ''

    def get_type(self):
        return 'Fish'


class Salmon(Fish, Animal):
    def get_type(self):
        print super(Salmon, self).get_type()
        return 'Salmon'

    category = get_type  # alias to a method


class Tilapia(Fish):
    pass


fish = Salmon()
fish.fish_type = 'salmon'

print fish.get_type()
print fish.category()
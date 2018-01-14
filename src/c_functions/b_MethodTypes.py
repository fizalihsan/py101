# This demonstrates the difference between instance method, static method and class methods

class Pizza:
    radius = 32

    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size

    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def get_radius(cls):
        return cls.radius


print Pizza.get_size  # <unbound method Pizza.size>
# print Pizza.size() # unbound method size() must be called with Pizza instance as first argument (got nothing instead)
print Pizza.get_size(Pizza(123))  # 123
print Pizza(123).get_size  # <bound method Pizza.get_size of <__main__.Pizza instance at 0x7f7dbc52d710>>
print Pizza(123).get_size()  # 123

method = Pizza(123).get_size
print method()  # 123
print method.__self__  # <__main__.Pizza instance at 0x7fa4e1e15710>
print method.__self__.get_size  # <bound method Pizza.get_size of <__main__.Pizza instance at 0x7f13c0267710>>
print method.__self__.get_size()  # 123

print Pizza(123).get_size is Pizza(123).get_size()  # False. Python method is an object too
print Pizza.add is Pizza.add  # True
print Pizza.add  # <function add at 0x7fd7ba645ed8>
print Pizza.add(1, 2)  # 3

print Pizza.get_radius  # <bound method classobj.radius of <class __main__.Pizza at 0x7f535ec193f8>>
print Pizza(123).get_radius  # <bound method classobj.radius of <class __main__.Pizza at 0x7f535ec193f8>>
print Pizza.get_radius()  # 32
print Pizza(123).get_radius()  # 32

class Number(object):

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __len__(self):
        return self.num

a = Number(10)
b = Number(20)
print a+b
print len(a)
print len('asdf')
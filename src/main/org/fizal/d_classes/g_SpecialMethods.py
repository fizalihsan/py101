
print "----------------------------------------- len(), add() -----------------------------------------------------"
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

print "----------------------------------------- str(), repr() -----------------------------------------------------"


class Hand:
    def __init__(self, *cards):
        self.cards = list(cards)

    def __str__(self):
        """human-friendly representation of an object"""
        return ", ".join(map(str, self.cards))

    def __repr__(self):
        """
        more technical representation of an object. For many types, this function makes an attempt to return a string
         that would yield an object with the same value when passed to eval()
        """
        return "{__class__.__name__}(cards={cards})".format(__class__=self.__class__, cards=self.cards)


hand = Hand(1, 2, 3, 4)
print map(str, hand.cards)
print hand  # calls __str__
print("%s" % hand)  # calls __str__
print("%r" % hand)  # calls __repr__
print("%r".format(hand))  # calls __repr__
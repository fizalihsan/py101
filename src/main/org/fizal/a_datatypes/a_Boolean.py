# every variable has these 3 things
# 1. Identity (reference or variable name)
# 2. Data Type
# 3. Value

vNone = None  # like void
vTrue = True
vFalse = False
print(vTrue == 1)
print(vFalse == '2')

# ------------------------any and all------------------------
print any([False, False, True])  # True

# used with generator expression
# Using any with a generator expression is efficient
# because it stops immediately if it finds a True value
print any(letter == 't' for letter in 'monty')  # True

print all(x <= 4 for x in [1, 2, 3, 4, 5])  # False
print all(x <= 4 for x in [1, 2, 3, 4])  # True


def avoids(word, forbidden):
    """word avoids forbidden if there are not any forbidden letters in word"""
    return not any(letter in forbidden for letter in word)

print avoids('Fizal', 'xyz')

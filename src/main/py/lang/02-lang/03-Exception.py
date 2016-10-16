fridge = {"apple": 2, "lemon": 4}

# catching error
try:
    qty = fridge["orange"]
    print "Qty = %s" % qty
except KeyError:
    print("Orange not found")
else:  #
    print "No exception is thrown"

# catching error: 2
try:
    qty = fridge["orange"]
    print "Qty = %s" % qty
except KeyError as e:  # missing key name is passed as string to 'e'
    print("%s not found" % e)

# catching error: 3
try:
    x = "123"
    y = 2
    z = x / y
    print z
except (KeyError, TypeError) as e:  # TypeError is like type case exception
    print("Error occurred: %s" % e)

# catching error: 4
try:
    x = "123"
    y = 2
    z = x / y
    print z
except KeyError as e:  # TypeError is like type case exception
    print("%s not found" % e)
except TypeError as e:
    pass  # do nothing with the exception

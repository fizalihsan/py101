# ----------------- Definition -----------------
dict1 = {}  # empty dictionary
print dict1  # {}
dict1 = dict()  # empty dictionary
print dict1  # {}
dict1 = {"a": 1, "b": 2}
print dict1.keys()
print dict1.values()

# setters
dict1["c"] = 3
dict2 = {"e": 7, "f": 8}
dict1.update(dict2)  # this is like putAll(Map) in Java

# getters
print dict1["a"]  # if key does not exist, KeyError is thrown
print dict1.get("a")  # returns None when key is missing
print dict1.get("x", 321)  # default value when key is missing

# check if key exists
print dict1.has_key("a")  # deprecated in 3+
print "a" in dict1  # new way

# Iterating keys
for k in dict1:
    print "key = %s value = %s" % (k, dict1[k])

# iterating values
for v in dict1.values():
    print v

# iterating items
for k, v in dict1.items():
    print "key = %s value = %s" % (k, v)

# type
print type(dict1.keys())  # <type 'list'>
print type(dict1.values())  # <type 'list'>
print type(dict1.items())  # <type 'list'>

# converting list of tuples into a dict
t = [('a', 0), ('c', 2), ('b', 1)]
print dict(t)  # {'a': 0, 'c': 2, 'b': 1}

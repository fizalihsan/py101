dict1 = {}  # empty dictionary
print dict1  # {}
dict1 = {"a": 1, "b": 2}
print dict1["a"]
print dict1.keys()
print dict1.values()

# check if key exists
print dict1.has_key("a")  # deprecated in 3+
print "a" in dict1

# accessing non-existent element
x = dict1.get("x")  # get() method on dictionary returns None when key is not found

try:
    print(dict1["x"])  # dict[key] throws KeyError when key is not found
except KeyError, e:
    print "Error occurred: ", e.args

for k in dict1:
    print k

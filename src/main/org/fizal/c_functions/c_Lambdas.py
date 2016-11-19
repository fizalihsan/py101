# -----------------------Map-Filter-----------------------

# map
a = [1, 2, 3, 4]
square_lambda = lambda x: x ** 2
squares = map(square_lambda, a)
print squares  # [1, 4, 9, 16]

# filter
filter_odd_lambda = lambda x: x % 2 == 0
squares = map(square_lambda, filter(filter_odd_lambda, a))
print squares  # [4, 16]

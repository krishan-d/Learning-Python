# List comprehension:
# To create new lists from other iterable like Tuple,string,Array,List...
# Syntax: newList = [ expression(element) for element in oldList if condition ]

from math import pi
import functools

roundPi = [str(round(pi, i)) for i in range(1, 6)]
print(roundPi)

odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# List of squares
sq = [x ** 2 for x in range(10)]
print(sq)
# Equivalently:
# sq = []
# for i in range(10):
#     sq.append(i**2)
# or
# sq = list(map(lambda x: x**2, range(10)))


# combine items of two list if ain't equal
combineList = [(x, y) for x in range(1, 4) for y in [3, 1, 4] if x != y]
print("Combined List:", combineList)
# Equivalently
# combs = []
# for x in range(1, 4):
#     for y in [3, 1, 4]:
#         if x != y:
#             combs.append((x, y))

a, b = zip(*combineList)
print(a)
print(b)

# Using filter() and lambda:
a = filter(lambda x: x % 2 == 1, range(1, 10))
print(list(a))

b = functools.reduce(lambda x, y: x if x > y else y, [7, 12, 45, 100, 15])
print(b)

"""
Looping: for Loop, while Loop
"""

import math


# break / continue/ pass:
# break : Terminates the loop containing break.
# continue : Skip current iteration only and continues with next iteration.
# pass : To avoid error, when loop or function has no content

# For Loop Syntax:
"""
for item_name in iterable:
    Do something
else:
    Do something
"""

for x in [0, 1, 2]: pass
else:
    print('Finished For!/Executed when No Break.')

# _ in For Loop:
# Use when don't intend to use variable name in iteration
for _ in range(2, 4):
    print('Hi')


# Important operators:
# zip(*iterables, strict=False) -> Yield tuples until an input is exhausted.
for s, a, r in zip('abcd', ['Eve', 'coding', 100027], range(6)):
    print('{} / {} / {}'.format(s, a, r))


# reversed(sequence, /):
# Return a reverse iterator over the values of the given sequence.
for i in reversed(range(1, 10, 2)):
    print(i, end=' ')
print('\r')  # Ending Line


# sorted(iterable, key=None, reverse=False) -> Sorted List
# key : Function can be supplied to customize the sort order
nLis = ['a', 'o', 'p', 'a', 'b']
for i in sorted(nLis):
    print(i, end=' ')
print('\r')

# set() : Eliminates duplicate elements
for x in sorted(set(nLis)):
    print(x, end=' ')
print('\r')


# Enumerate:
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print("List Enumerate :", list(enumerate(seasons)))  # -> [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1)))

for n, v in enumerate(['a', 'e', 'i']):
    print(n, v)


# in keyword:
print('x' in ['x', 'o', 'r'])


# While Loop Syntax:
"""
while boolean_condition:
    do something
else:
    do something
"""


while i in range(1, 3):
    print(i)
    break
else:  # Not executed as there is a break
    print("Finished while!")


# Iterable object: An object supporting iteration
# __iter__()
# iter(iterable) -> iterator :
# The argument must supply its own iterator, or be a sequence.
# iter(callable, sentinel) -> iterator
# The callable is called until it returns the sentinel.

# __next__()
# next(iterator[, default]) :
# Return the next item from the iterator. If default is given and the iterator
# is exhausted, it is returned instead of raising StopIteration.

aList = ['a', 'o', 'k']
itr_ob = iter(aList)  # aList.__iter__()
while True:
    try:
        x = next(itr_ob)
        print(x)
        # or
        # print(itr_ob.__next__())
    except StopIteration:
        break


dumData = [27.07, float('NaN'), 17.23, 42.01, 54.40, float('NaN')]
reqData = [v for v in dumData if not math.isnan(v)]
print(reqData)

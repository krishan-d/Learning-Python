""""""
# The enumerate method adds a counter to an iterable and returns it (enumerate object).
"""
Syntax: enumerate(iterable, start=0) -> enumerate object
iterable : an object supporting iteration.
Enumerate object yields pairs containing a count (from start) and a value yielded by the iterable argument.
For obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""

grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)
print("Type:", type(enumerateGrocery))
print("To List:", list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

# Looping:
for item in enumerate(grocery):
    print(item)

print('\n')
for count, item in enumerate(grocery):
    print(count, item)

print('\n')
for count, item in enumerate(grocery, 10):
    print(count, item)

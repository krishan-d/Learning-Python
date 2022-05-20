"""
Counters:
"""

from collections import Counter

# Built-in containers: Tuple, List, Dictionary
# collection Module in Python provides containers-
# Counters
# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString

# Counter:
# Counter([iterable-or-mapping])
# subclass of the dictionary.
# To keep the count of the elements in an iterable in the form of an unordered dictionary.
# key : Element in the iterable.
# value : count of that element in the iterable.


# Initialization:
c = Counter()  # a new, empty counter
c = Counter('Eve')  # a new counter from an iterable
c = Counter({'a': 4, 'b': 2})  # a new counter from a mapping
c = Counter(a=4, b=2)  # a new counter from keyword args

# most_common():
# List the n most common elements and their counts from the most common to the least.
# If n is None, then list all element counts.
print(Counter('Forever').most_common(3))  # -> [('r', 2), ('e', 2), ('F', 1)]

# elements(self):
# Iterator over elements repeating each as many times as its count.
c = Counter('Evina')
print(sorted(c.elements()))  # -> ['E', 'a', 'i', 'n', 'v']
nList = []
for i in c.elements():
    nList.append(i)
print(nList)  # -> ['E', 'v', 'i', 'n', 'a']

# update(self, iterable=None, /, **kwds):
# Like dict.update() but add counts instead of replacing them.
# Source can be an iterable, a dictionary, or another Counter instance.
c = Counter('which')
c.update('witch')  # add elements from another iterable
d = Counter('watch')
c.update(d)  # add elements from another counter
print(c['h'])

# subtract(self, iterable=None, /, **kwds):
# Like dict.update() but subtracts counts instead of replacing them.
c0 = Counter(A=4, B=3, C=10)
c1 = Counter(A=10, B=3, C=4)
c0.subtract(c1)
print(c0)

# copy(self):
cn = c.copy()
print(cn)

print(c1.popitem())
print(c1)
print(c1.pop('B'))
print(c1)

c1.clear()
print(c1)

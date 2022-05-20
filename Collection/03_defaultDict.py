"""
Default dictionary:
"""

from collections import defaultdict

# defaultdict(default_factory=None, /, [...]) --> dict with default factory
# default_factory: called without arguments to produce a new value when a key is not present, in __getitem__ only.

dd = defaultdict()
print(dd)  # -> defaultdict(None, {})

dd = defaultdict(lambda: 'DEFAULT VALUE')
dd['E'] = 1
dd['V'] = 2

print(dd['E'])  # -> 1
print(dd['WRONG KEY!'])  # -> DEFAULT VALUE
print("Dictionary :", dd)


# Using List as default_factory:
dd = defaultdict(list)
for i in range(4): dd[i].append(i)

print(dd)  # -> defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3]})

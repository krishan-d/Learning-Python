"""
ChainMap
"""

from collections import ChainMap


# ChainMap(*maps):
# Encapsulates many dictionaries into one unit.

# Initialize a ChainMap by setting *maps* to the given mappings.
# If no mappings are provided, a single empty dictionary is used.

d0, d1 = {'E': 4, 'v': 8, 'e': 2}, {"H": 6, 'i': 10}
c = ChainMap(d0, d1)
print(c)  # -> ChainMap({'E': 4, 'v': 8, 'e': 2}, {'H': 6, 'i': 10})

print(c.maps)  # -> [{'E': 4, 'v': 8, 'e': 2}, {'H': 6, 'i': 10}]
print(list(c.keys()))  # -> ['H', 'i', 'E', 'v', 'e']
print(list(c.values()))  # -> [6, 10, 4, 8, 2]


# new_child(self, m=None, **kwargs):
# new_child(self: Self, m: MutableMapping[_KT, _VT] | None = ...) -> Self: ...
d2 = {'v': 0}
cm = c.new_child(d2)
print(cm.maps)  # -> [{'v': 0}, {'E': 4, 'v': 8, 'e': 2}, {'H': 6, 'i': 10}]
cm = cm.new_child()
print(cm.maps)  # -> [{}, {'v': 0}, {'E': 4, 'v': 8, 'e': 2}, {'H': 6, 'i': 10}]
print(cm['v'])  # -> 0

cm.maps = reversed(cm.maps)
print(cm['v'])  # -> 8




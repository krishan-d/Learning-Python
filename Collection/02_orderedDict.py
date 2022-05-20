"""
OrderedDict:
"""

from collections import OrderedDict

# subclass of the dictionary.
# Dictionary that remembers insertion order.

# class OrderedDict(Dict[_KT, _VT], Reversible[_KT], Generic[_KT, _VT]):
#     def popitem(self, last: bool = ...) -> tuple[_KT, _VT]: ...
#     def move_to_end(self, key: _KT, last: bool = ...) -> None: ...
#     def copy(self: _S) -> _S: ...
#     def __reversed__(self) -> Iterator[_KT]: ...
#     def keys(self) -> _OrderedDictKeysView[_KT, _VT]: ...
#     def items(self) -> _OrderedDictItemsView[_KT, _VT]: ...
#     def values(self) -> _OrderedDictValuesView[_VT, _KT]: ...


od = OrderedDict({'E': 1, 'v': 2, 'i': 3, 'n': 4, 'a': 5})
print(od)  # -> OrderedDict([('E', 1), ('v', 2), ('i', 3), ('n', 4), ('a', 5)])


# od.values() / od.keys() / od.items():
for k, v in od.items(): print(k, v)


# Key value change:
od['n'] = 10
print(od)


# Deletion and reinserting:
print("popitem :", od.popitem())  # -> ('a', 5)
print(od)  # -> OrderedDict([('E', 1), ('v', 2), ('i', 3), ('n', 10)])

# pop(self, key: _KT) -> _VT: ...
# od.pop(k[,d]) -> v, remove specified key and return the corresponding value.
# If key is not found, d is returned if given, otherwise KeyError is raised.
print("pop :", od.pop('n'))  # -> pop : 10
print(od)  # -> OrderedDict([('E', 1), ('v', 2), ('i', 3)])

for k, v in od.items(): print(k, v)


# move_to_end(self, key, last=True) -> None:
# Move an existing element to the end (or beginning if last is false).
# Raise KeyError if the element does not exist.
od.move_to_end('v')
print(od)  # -> OrderedDict([('E', 1), ('i', 3), ('v', 2)])


# setdefault(self, key, default=None):
od.setdefault('a', 0)
print(od)  # -> OrderedDict([('E', 1), ('i', 3), ('v', 2), ('a', 0)])

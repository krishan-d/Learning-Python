"""
Named Tuple:
"""

from collections import namedtuple


# namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
# namedtuple(typename: str, field_names: str | Iterable[str], *, verbose: bool = ..., rename: bool = ...,
# module: str | None = ...) -> Type[Tuple[Any, ...]]: ...
# Returns a new subclass of tuple with named fields.

Person = namedtuple('Person', ['name', 'id'])
print(Person.__doc__)
me = Person(name="Eve", id=100200)
print("Type :", type(me))
print(me)


# Accessing:
print(me[0], '|', me.name)
print(me.id)
print(getattr(me, 'name'))
n, i = me  # unpacking Tup
print(n, i)


# List To Named Tuple:
# _make(cls, iterable) -> _T: ...
# Return a namedtuple() from the iterable passed as argument.
cherry = ['Lynn', 100000]
print(Person._make(cherry))  # -> Person(name='Lynn', id=100000)


# Named Tuple To ordered dictionary:
# _asdict() -> dict[str, Any]: ...
# returns the OrderedDict() as constructed from the mapped values of namedtuple().
ord_d = me._asdict()
print(ord_d)  # -> {'name': 'Eve', 'id': 100200}
print(ord_d['name'])  # -> Eve


# Dictionary To Named Tuple:
# ** operator:
sam = {'name': 'Evina', 'id': 100302}
evina = Person(**sam)
print(evina)  # -> Person(name='Evina', id=100302)


# _fields variable:
# _fields: Tuple[str, ...]
# Return all the keynames of the namespace declared.
print(me._fields)  # -> ('name', 'id')


# _replace() method:
# _replace(self: _T, **kwargs: Any) -> _T: ...
# _replace() is like str.replace() but targets named fields( does not modify the original values)
q = me._replace(name='Edwina')
print(q)  # -> Person(name='Edwina', id=100200)
print(me)  # -> Person(name='Eve', id=100200)


# Examples:
print('\n')
Point = namedtuple('Point', ['x', 'y'])
print(Point.__doc__)            # docstring for the new class
# 'Point(x, y)'
p = Point(11, y=22)             # instantiate with positional args or keywords
print(p[0] + p[1])              # index-able like a plain tuple
# 33
x, y = p                        # unpack like a regular tuple
print(x, y)                     # (11, 22)

print(p.x + p.y)                # fields also accessible by name
# 33
d = p._asdict()                 # convert to a dictionary
print(d['x'])
# 11
print(Point(**d))               # convert from a dictionary
# Point(x=11, y=22)
print(p._replace(x=100))        # _replace() is like str.replace() but targets named fields
# Point(x=100, y=22)
print(p)
# Point(x=11, y=22)

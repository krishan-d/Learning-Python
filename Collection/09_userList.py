"""
User List:
"""

from collections import UserList

# wrapper around list objects for easier list subclassing.
# Class that simulates a list.
# The instance’s contents are kept in a regular list,
# which is accessible via the data attribute of UserList instances.

# collections.UserList([list])
# __init__(self, initlist: Iterable[_T] | None = ...) -> None: ...


uL = UserList()
print(uL.data)  # -> []

print(UserList([]).data)  # -> []

uL = UserList([1, 2, 3, 4])
print(uL.data)  # -> [1, 2, 3, 4]

print(UserList(uL).data)  # -> [1, 2, 3, 4]


# Example:
class MyList(UserList):
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")


L = MyList([1, 2, 3, 4])
L.append(5)
print(L)  # -> [1, 2, 3, 4, 5]

# L.remove()  # -> raise Error

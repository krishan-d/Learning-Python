"""
User Dictionary:
"""

from collections import UserDict

# wrapper around dictionary objects for easier dict subclassing.
# Class that simulates a dictionary.
# NOTE:
# The instance’s contents are kept in a regular dictionary,
# which is accessible via the data attribute of UserDict instances.


# UserDict([initial_data]):
# a reference to initial_data will not be kept, allowing it to be used for other purposes.
# __init__(self, __dict: Mapping[_KT, _VT] | None = ..., **kwargs: _VT) -> None: ...
ud = UserDict()
print(ud)

d = {'E': 4, 'v': 0, 'e': 2}
ud = UserDict(a=1, b=2)
ud = UserDict(d)
print(ud)
# A real dictionary used to store the contents of the UserDict class.
print(ud.data)                  # -> {'E': 4, 'v': 0, 'e': 2}


# Example:
# class inheriting UserDict to implement a customized dictionary:
class MyDict(UserDict):
    # def __del__(self):
    #     raise RuntimeError("Deletion not allowed")

    def pop(self, key=None):
        raise RuntimeError("Deletion not allowed!")

    def popitem(self, key=None):
        raise RuntimeError("Deletion not allowed")

md = MyDict(d)
print(md)
# md.pop('a')                   # raises Error

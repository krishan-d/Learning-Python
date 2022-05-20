"""
User String:
"""

from collections import UserString

# wrapper around string objects for easier string subclassing.
# Class that simulates a string object.
# The instance’s content is kept in a regular string object,
# which is accessible via the data attribute of UserString instances.

# collections.UserString(seq)
# __init__(self, seq: object) -> None: ...


us = UserString("")
print(us)  # Empty string

# A real str object used to store the contents of the UserString class.
us = UserString("Hi Eve.")
print(us.data)  # -> Hi Eve.


# Example:
class MyString(UserString):
    def append(self, s):
        self.data += s

    def remove(self, s):
        self.data = self.data.replace(s, "")

s1 = MyString("Forever")
s1.append('!')
print(s1.data)  # -> Forever!

s1.remove("ever")
print(s1.data)  # -> For!

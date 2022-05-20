"""
Name Mangling:
"""


class Person:
    __sName = 'MIT'  # private class attribute

    def __init__(self, name, salary):
        self.__name = name  # private instance attribute
        self.__salary = salary  # private instance attribute

    def __display(self):  # private method
        print('This is private method.')


s = Person("Eve", 10000)

# Uncommenting These Raise AttributeError
# print(s.__sName)
# print(s.__name)
# s.__display()


"""
Python performs name mangling of private variables.
Every member with a double underscore will be changed to _object._class__variable.
So, it can still be accessed from outside the class,
but the practice should be refrained """

print(s._Person__name)  # private member mangling
s._Person__display()

s._Person__name = 'Evina'
print(s._Person__name)

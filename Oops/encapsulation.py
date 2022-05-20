"""
Encapsulation
"""

# This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data

# Protected members:
# cannot be accessed outside the class but can be accessed from within the class and its subclasses
# prefix member with single underscore “_”.


# private member:
# similar to protected.
# neither be accessed outside the class nor by any base class.
# prefix the member name with double underscore “__”.

# NOTE:
# Python’s private and protected member can be accessed outside the class through python name mangling.


class Base:
    def __init__(self):
        self.a = 0
        # Protected member
        self._b = 2
        self._d = 3
        # Private member
        self.__c = 4

    @property
    def d(self):
        return self._d
    # Define property decorator to make _d is protected since obj._d is accessible


class Derived(Base):
    def __init__(self):

        # Base class constructor
        Base.__init__(self)
        # Calling protected member of base class
        print("Base class Protected member:", self._b)


class DerivedPri(Base):
    def __init__(self):
        Base.__init__(self)
        # Calling private member of base class
        print("base class Private member:", self.__c)


b = Base()
d = Derived()
print("a:", b.a)


# Protected members:
# print(b.b)  # Uncommenting this, will raise AttributeError without property decorator.
print(b._b)
print(b._d)
print(b.d)  # After defining property decorator d is protected.
print(b._d)  # Still accessible


# private members:
# print(b.c)  # raise AttributeError
# p = DerivedPri()  # raise AttributeError as private member of base class is called inside derived class.

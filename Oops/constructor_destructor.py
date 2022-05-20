"""
Constructor and Destructor:
"""

# Constructor:
# instantiating an object.
# To initialize(assign values) to class data members when object is created.
# __init__() method

# Destructor:
# called when an object is destroyed.
# Not needed, since python has garbage collector.
# __del__() method :
# called when all references to the object have been deleted i.e when an object is garbage collected.


class Base:
    # Initializing
    # def __init__(self):  # default constructor
    #     pass

    def __init__(self, name='None'):
        self.name = name
        print("Base Object Initiated.")

    # calling destructor:
    def __del__(self):
        print('Base Destructor called! Object deleted.')


class Derived(Base):
    def __init__(self, x):
        self.x = Base(self)  # circular reference
        print("Derived object initiated.")

    def __del__(self):
        print("Dead!")


def main():
    o = Base("Eve")
    print(o.name)


if __name__ == '__main__':
    main()
    d = Derived("Pi")

    print("End Here!")


# NOTE:
# The destructor was called after the program ended or when all the references to object are deleted.
# i.e. when the reference count becomes zero, not when object went out of scope.

# NOTE:
# If your instances are involved in circular references they will live in memory for as long as the application run.

"""
Meta classes:
"""

print("Type :", type([2, 4, 6]))  # <class 'list'>
print("Type :", type('Eve'))  # <class 'str'>


# NOTE : Every type in Python is defined by Class


class Person: pass


p = Person()
print("Type :", type(Person))  # <class 'type'>
print("Instance Type :", type(p))  # <class '__main__.Person'>


# A class is also an object, and just like any other object.
# An instance of Metaclass.
# A special class 'type' creates these Class objects.
# The 'type' class is default metaclass which is responsible for making classes.


class Test: pass


Test.x = 10  # defining class variable
Test.newMethod = lambda self: print("Hi Eve!")  # defining class method
nOb = Test()
print(nOb.x)  # 10
nOb.newMethod()  # Hi Eve!


# NOTE : Metaclass create Classes and Classes creates objects.
# object-----(instance of)----->class-----(instance of)----->metaclass

# Custom metaclass
# inherit 'type' metaclass and usually override –
# __new__():
# It’s a method which is called before __init__(). It creates the object and returns it.
# We can override this method to control how the objects are created.
# __init__():
# This method just initialize the created object passed as a parameter.

# type():
# With one argument, return type.
# With 3 parameters, creates class.
# class name, Tuple(base classes inherited by class), class dictionary(local namespace/populated methods and variables)

class Base:
    def __init__(self): pass
    @staticmethod
    def show(): print("Inherited method!")


def someMethod(self): print("Derived class method!")


# Creating class using type() method :
Derived = type('Derived', (Base,), dict(a=1000, derivedMethod=someMethod))
print("Derived Type :", type(Derived))  # <class 'type'>
d = Derived()
print("Derived object Type :", type(d))  # <class '__main__.Derived'>
d.show()  # Inherited method!
d.derivedMethod()  # Derived class method!
print(d.a)  # 1000


# Creating Metaclass

class MuBases(type):
    # overriding new method
    def __new__(cls, cname, bases, cdist):
        # If number of base class is grater than 1, raise error.
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!")

        return super().__new__(cls, cname, bases, cdist)


class Base(metaclass=MuBases): pass


# No Error is raised
class A(Base): pass


# raise Error, because no of base class is more than 1.
# class B(Base, A): pass


# Use:
# If we want to change class automatically, when it is created, we use metaclasses.
# API development.

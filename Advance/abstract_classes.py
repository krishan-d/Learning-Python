"""
Abstract class:
"""

# -A class which contains one or more abstract methods is called an abstract class.
# -Considered as a blueprint for other classes.
# -Allows to create a set of methods that must be created within any child classes built from the abstract class.
# -An abstract method is a method that has a declaration but does not have an implementation.
# -To provide common interface for different implementations.
# abstract classes may contain both concrete methods and abstract methods.
# an abstract class is not a concrete class, it cannot be instantiated. raises TypeError.

#  module name is ABC.
#  ABC works by decorating methods of the base class as abstract and
#  -then registering concrete classes as implementations of the abstract base.
#  A method becomes abstract when decorated with the keyword @abstractmethod.


# Example 1:
import abc
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def side_count(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def side_count(self):
        print("I have 3 sides")


class Hexagon(Polygon):
    # overriding abstract method
    def side_count(self):
        print("I have 6 sides")


r = Triangle()
r.side_count()
h = Hexagon()
h.side_count()


# Example 2:
# Concrete Methods in Abstract Base Classes :
class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass ")


r = K()
r.rk()


# Example 3:
# Abstract properties:
# Abstract classes include attributes in addition to methods,
# you can require the attributes in concrete classes by defining them with @abstractproperty.
class Parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"


class Child(Parent):
    @property
    def geeks(self):
        return "child class"

try:
    r = Parent()
    print(r.geeks)
except Exception as err:
    print(err)

r = Child()
print(r.geeks)

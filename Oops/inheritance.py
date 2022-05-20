"""
Inheritance
"""

# object is root of all classes.
# class Base(object) and “class Base” are same.
"""
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

class DerivedClassName(modname.BaseClassName):
"""

# Multiple Inheritance:
"""
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
"""


# isinstance() :
# To check an instance’s type: isinstance(obj, int) -> True, if obj.__class__ is int or some class derived from int.
# issubclass() :
# To check class inheritance


class Person:  # Parent class
    # __init__ is known as the constructor
    def __init__(self, name, idn):
        self.name = name
        self.idn = idn
        # private instance variable
        self.__d = 'Eve'

    def display(self):
        print("Name:", self.name)
        print("Id Number:", self.idn)

    def details(self):
        print("Name: {}, IdNumber: {}".format(self.name, self.idn))


class Employee(Person):  # child class
    def __init__(self, name, idn, salary, post):
        self.salary = salary
        self.post = post
        # Person.name = name  # Access using Person class
        # Person.idn = idn
        # or
        # invoking the __init__ of the parent class
        # Person.__init__(self, name, idn)  # Access method using Person (Base)class
        # or super()
        super(Employee, self).__init__(name, idn)

    def details(self):  # method overriding # Polymorphism
        print("Name: {}, IdNumber: {}, Post: {}".format(self.name, self.idn, self.post))
        # print(Person.__d)   # --> Error


if __name__ == '__main__':
    # creation of an object variable or an instance
    e = Employee('Pie', 886012, 200000, "Intern")

    # calling a function of the class Person using its instance
    e.display()
    e.details()

    p = Person('Evina', 000000)
    p.details()

    # issubclass()
    print(issubclass(Employee, Person))  # True
    print(issubclass(Person, Employee))  # False

    # isinstance()
    print(isinstance(e, Person))  # True  # e is instance of Person class
    print(isinstance(p, Employee))  # False

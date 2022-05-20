"""
OOPs:
"""

"""
----------------------
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
----------------------
# Class : collection of objects.
# Logical entity that contains some attributes and methods.
# Contains the blueprints or the prototype from which the objects are being created.
----------------------
# Object :
# Entity that has a state and behavior associated with it.
----------------------
"""

# class architecture :
"""
class MyClass:
    # member/class variables
	variable1 = something
	variable2 = something

	# member functions
	def function1(self, parameter1, ...):
		self.variable1 = something else
		# defining a new variable
		self.variable3 = something
		function1 statements...

	def function2(self, parameter1, ...):
		self.variable2 = something else
		function2 statements...
"""

# NOTES:
"""
----------------------
self:
self represents the instance of the class.
binds the attributes with the given arguments.
----------------------
__init__ method:
same as constructors, 
----------------------
class attributes/static variables:
-belong to the class and not to objects/instances.
-shared by all instances/objects.
----------------------
instance attributes:
-Every object has its own copy of instance attribute.
To list attributes of instance/object, have functions:
----------------------
vars():
This function displays the attribute of an instance in the form of an dictionary.
----------------------
dir():
Displays instance attributes, class attributes and attributes of ancestor classes.
----------------------
Class method: To create factory methods.(return class objects(as constructor))
class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
fun: function that needs to be converted into a class method
returns: a class method for function.
----------------------
Static method: To create utility functions.
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
        ...
returns: a static method for function fun.
----------------------
"""


class Person:
    def __init__(self, name='None', grade=0):  # constructor
        self.name = name  # Instance attribute
        self.grade = grade  # 0-10

    def get_grade(self):  # class method
        return self.grade


class Course:
    def __init__(self, name, max_person):  # constructor
        # Instance attributes:
        print("A course is created!")
        self.name = name
        self.max_person = max_person
        self.persons = []

    def add_person(self, person):  # class method
        if len(self.persons) < self.max_person:
            self.persons.append(person)
            return True
        return False

    def get_average_grade(self):
        v = 0
        for per in self.persons:
            v += per.get_grade()
        return v / len(self.persons)

    def show_list(self):
        print(self.persons)

    # special methods:
    def __del__(self):
        print("A course is destroyed!")

    def __str__(self):
        print("Course name : %s, max persons : %s" % (self.name, self.max_person))


def main_method():
    p = Person("Krish", 10)
    q = Person("Eve", 8)
    r = Person("Unknown", 8)

    print(p.name, "/", p.grade)

    c = Course("B.Tech", 2)
    c.add_person(p)
    c.add_person(q)
    c.add_person(r)  # False

    print(c.persons[1].name, "/", c.persons[1].grade)
    print(c.get_average_grade())


class Example:
    """Class Documentation Here"""

    # static variable : declared within class but outside method.
    myVariable = "This is static variable!"  # class attribute or static variable

    count = 0  # class variable

    def anoFunction(self, param):  # class method
        self.myVariable = param  # instance attribute
        # self.myVariable = input()

    """
    def disp(obj):  # The first parameter of the method need not be named self.
        pass
    """

    # Static method:
    # No access to 'self' or 'cls' keyword
    @staticmethod  # decorator
    def staticMethod():
        print("This is Static Method!")

    # class method
    # can access and modify class variable, takes class name as required param.
    @classmethod
    def classMethod(cls):
        cls.count += 1


def main():
    obj = Example()  # class object
    print(obj.__doc__)
    print(obj.myVariable)  # some value

    # Changing class member/class variable
    obj.myVariable = "TENET!"
    print(obj.myVariable)
    # Static variable value not changed
    print(Example.myVariable)

    obj.anoFunction("ELITE")
    print(obj.myVariable)
    print("Type:", type(obj))  # <class '__main__.Example'>

    # Class and Instance Attributes:
    print("Class and Instance attributes Dictionary Form :", vars(obj))
    print("Directory:", dir(obj))

    # static method and class method:
    Example.staticMethod()
    obj.staticMethod()

    # Before calling class method
    print(obj.count)  # 0
    print(Example.count)  # 0
    Example.classMethod()  # calling class method on class.
    print(obj.count)  # 1
    print(Example.count)  # 1
    obj.classMethod()  # calling class method on class instance/object.
    print(obj.count)  # 2
    print(Example.count)  # 2


if __name__ == '__main__':
    # main_method()
    main()

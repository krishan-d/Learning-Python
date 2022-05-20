# Decorators:
# Add functionality to an existing code.
# Known as metaprogramming because a part of code tries to modify another part of code at compile time.

# Note: Everything in python are objects.

# Note: Functions and methods are known as callable as they can be called.
# Any object which implements special __call__() method is termed callable.
# A decorator is a callable that returns a callable.

# First class objects...
# In Python, functions are first class objects that mean that functions in Python can be used or passed as arguments.

# Properties of first class functions:
# A function is an instance of the Object type.
# Can store the function in a variable.
# Can pass the function as a parameter to another function.[High order functions take other functions as argument]
# Can return the function from a function.
# Can store them in data structures such as hash tables, lists, …

# Use:
# To tack/add on extra functionality to an already existing function and return it.
# Use @ operator and placed on top of the original function.

import math
import time


def changeToUpper(string=None):
    return string.upper() if string is not None else 'None'


print(changeToUpper)
print(changeToUpper())

# Function as Object...
cu = changeToUpper
print(cu)
print(cu('Hi Evina!'))

# print(changeToUpper())
# del changeToUpper
# print(changeToUpper())  # Raise Error
# print(cu('Evina'))


# Passing Function as Argument
def passAsArg(function):
    # storing Function in variable.
    a = function('Hi, Function passed as argument!')
    print(a)


passAsArg(changeToUpper)


# Return Function From another Function
def makeAdder(x):
    def adder(y): return x + y
    return adder


print(makeAdder)
add_10 = makeAdder(10)
print(add_10)
print(add_10(30))


# Decorators:
# Used to modify the behaviour of function or class.
# Functions are taken as the argument into another function and then called inside the wrapper function.


def decorateMsg(func):
    def addMsg(*args):  # Nested Function
        return "Hi, " + str([func(arg) for arg in args])

    return addMsg  # Decorator returns Function


@decorateMsg  # Decorator
def someName(name):
    return name


ms = someName('Cherry', '!')
print(ms)


# Decorator to calculate duration taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments, can be added like this.
    def inner(*args, **kwargs):
        # storing time before function execution
        begin = time.time()
        func(*args, **kwargs)
        # storing time after function execution
        end = time.time()
        print("Time Taken In :", func.__name__, end - begin)

    return inner


@calculate_time
def factorial(numb):
    # Using sleep, since takes very less time.
    time.sleep(2)
    print(math.factorial(numb))


factorial(10)

# NOTE:
# decorator is used to avoid this line.
# calculate_time(factorial(10))


# chaining decorators:
def square(func):
    def inner():
        x = func()
        return x * x
    return inner


def twice(func):
    def inner():
        x = func()
        return 2 * x
    return inner


@square
@twice
def num(): return 10


# Works as square(twice(num))
print(num())  # 400


# Decorators with parameters:
def new_decorator(*args, **kwargs):
    print("Inside decorator")

    def inner(function):
        print("Inside Inner Function")
        print("Some code here As in / I Like {}...".format(kwargs['like']))
        function()

    return inner


@new_decorator(like="Evina")
def demoFun():
    print("Inside Actual Function")

# new_decorator()(demoFun)


def decoratorFunc(x, y):
    def Inner(func):
        def wrapper(*args, **kwargs):  # Extra Functionality goes in here for original function
            # some code before original function
            print("Inside wrapper...")
            print("Summation of values - {}".format(x + y))
            func(*args, **kwargs)  # Original function
            # some code after original function

        return wrapper

    return Inner


# Not using decorator
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using decorators
decoratorFunc(12, 15)(my_fun)('I', 'You', 'Hi')

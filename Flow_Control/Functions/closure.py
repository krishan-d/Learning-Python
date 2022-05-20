"""
Closure Function: """

# A function object that remembers values in enclosing scopes even if they are not present in memory.
# To invoke functions outside their scope.
# Can easily extend its scope to invoke a function outside its scope.

# criteria for creating closures...
# Must have a nested function.
# The nested function must refer to a value defined in enclosing function.
# The enclosing function must return nested function.


def print_msg(msg):
    def printer():
        print(msg)
    return printer


another = print_msg("Hi!")
print(another)
another()

# Function deleted/removed from memory
del print_msg
another()  # Returned function works

# when to use closures...
# --closure can avoid use of global values and provides some form of data hiding. It can provide an
# object-oriented solution to the problem.

# --when there are few methods(one method in most cases) to be implemented in a class, closure can provide an alternate
# and more elegant solution. But when number of attributes and methods get larger, implement a class.

# --decorators make an extensive use of closures.


def make_adder(n):
    def add(x):
        return x + n
    return add

add_10 = make_adder(10)  # Function object
z = add_10(2)
print(z)

# (closure)Function objects have a __closure__ attribute that returns a tuple of cell objects.
print(add_10.__closure__)


"""
import logging as nL
nL.basicConfig(filename='Example.log', level=nL.INFO)


def Logger(func):
    def function_Log(*args):
        nL.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    # function_Log(*args) -> Accessible inside outer Function, not outside body.
    # Necessary for closure to work (returning WITHOUT parenthesis)
    return function_Log


def add(x, y): return x+y
def sub(x, y): return x-y


addLogger = Logger(add)
subLogger = Logger(sub)
addLogger(3, 3)
subLogger(10, 5)
"""

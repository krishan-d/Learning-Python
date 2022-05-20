# Function :
# Function definition should always be present before the function call.

def emptyFun(): pass  # Empty Function


def fibonacci(n):
    """
    This is documentation:
    Return List containing Fibonacci series up to n
    """
    respList = []
    a, b = 0, 1
    while a < n:
        # print(a, end=' ')
        respList.append(a)
        a, b = b, a + b
    return respList


print(fibonacci(2000))
print("Function Documentation :", fibonacci.__doc__)
print("Function Annotations :", fibonacci.__annotations__)


# Function Arguments...
# 1. Default arguments:
def something(ask, retries=4, reminder='Try again!'):
    pass


# 2. keyword arguments:
def person(pid, name='None', passion='Unknown', kind='M'):
    print(pid, name, passion, kind)


person(108687)
person(pid=107655)
person(pid=107655, name='Eve')
person(name='Cherry', pid=107523, kind='Female')
person(109236, kind='Female')
# person(id=102874, 'Eva')  # Invalid : Positional argument after keyword argument
# person(103465, pid=103465)  # Invalid : duplicate value for the same argument

# Argument unpacking:
d = {'name': 'None', 'passion': 'Unknown', 'kind': 'M'}
person(108230, **d)


# 3. Variable Length arguments:
def cheeseShop(kind, *args, **kwargs):
    print(kind)
    for arg in args:
        print("arg ::", arg)
    for kw in kwargs:
        print("kwarg ::", kw, ":", kwargs[kw])


cheeseShop("Limburger", "Pie", "Cheese", owner="Edwina", customer='Eve')


# Special parameter :
"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    -----------    ----------     ----------
    |             |                  |
    |        Positional or keyword   |
    |                                - Keyword only
    -- Positional only
"""


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


standard_arg(2)  # -> 2
standard_arg(arg=2)  # -> 2
pos_only_arg(1)  # -> 1
# pos_only_arg(arg=1)  # Error
# kwd_only_arg(3)  # Error
kwd_only_arg(arg=3)  # -> 3
combined_example(1, 2, kwd_only=3)  # -> 1 2 3


# def foo(pid, **kwargs):  # Error : foo() got multiple values for argument 'id'
def foo(pid, /, **kwargs): return 'id' in kwargs

print(foo(1, **{'pid': 2}))


# Arbitrary argument:
def concat(*arg, sep="/"): return sep.join(arg)

print(concat("e", "m", "v"))  # -> e/m/v
print(concat("e", "m", "v", sep="."))  # -> e.m.v

L = ['H', 'i', '!']
print(*L)


# Unpacking argument List:
print(list(range(4, 7)))  # normal call with separate arguments
args = [4, 7]
print(list(range(*args)))  # call with arguments unpacked from a list


# Function annotations:
def f(ham: str, eggs: str = 'eggs') -> str: pass

print("Annotations :", f.__annotations__)

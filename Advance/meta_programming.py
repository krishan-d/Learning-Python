"""
Meta programming:
"""

from functools import wraps


def debug(func):
    """decorator for debugging passed function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Full name of this method:", func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def debug_methods(cls):
    """class decorator make use of debug decorator
    to debug class methods """

    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls


class DebugMeta(type):
    """metaclass which feed created class object
    to debug-method to get debug functionality
    enabled objects"""

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debug_methods(obj)
        return obj


# base class with metaclass 'debugMeta'
# now all the subclass of this
# will have debugging applied
class Base(metaclass=DebugMeta): pass


# inheriting Base
class Calc(Base):
    def add(self, x, y):
        return x + y


# inheriting Calc
class CalcAdv(Calc):
    def mul(self, x, y):
        return x * y


# Now Calc_adv object showing debugging behaviour
c = CalcAdv()
print(c.mul(2, 3))

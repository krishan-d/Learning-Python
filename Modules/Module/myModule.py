"""
myModule.py
"""

# Import someModule.py module
# dir() : List Functions in module

# Import specific function from module
from someModule import person as p, factorial
import math


def main():
    print(p["name"])
    print(factorial(3))

    # Module documentation
    print(math.__doc__)


# Means that, if this script(myModule.py) is executed, then main() will be executed
if __name__ == '__main__':
    print("File __name__ = %s" % __name__)
    main()


"""
import someModule
a = someModule.person["name"]
print(someModule.__name__)
print(someModule.factorial(4))
print(dir(someModule))
"""

"""
import someModule as sm
a = sm.person["passion"]
"""

# Import * from a module
"""
from someModule import *
print(person["year"])
print(fibonacci(10))
"""
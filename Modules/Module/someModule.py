"""
This is simple module: someModule.py
"""

# Modules/Libraries
# Module must have File Extension .py


from functools import reduce
import math
import io


print("Module __name__ = %s" % __name__)  # Module name

person = {
    "name": "Eve",
    "passion": "Programmer",
    "year": 2000}

# Fibonacci sequence up-to N Terms
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])


# Fibonacci sequence up-to number N
def fibonacci(n):
    r = []
    a, b = 0, 1
    while a < n:
        r.append(a)
        a, b = b, a + b
    return r


# Factorial
def factorial(num=0): return 1 if num <= 1 else num * factorial(num - 1)


"""When you run a Python module with the code in the module will be executed, just as if you imported it, 
but with the __name__ set to "__main__". That means that by adding this code at the end of your module, you can make 
the file usable as a script as well as an importable module, because the code that parses the command line only runs 
if the module is executed as the “main” file: """

if __name__ == '__main__':
    import sys
    print(sys.argv)
    series = fib(int(6))
    print(series)
    print(math.__doc__)
    print(io.__file__)
    print(math.__dict__)

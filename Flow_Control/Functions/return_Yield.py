# Return: sends specific value to its caller.

from dataclasses import dataclass


# Yield:
# produce a sequence of values. Use when need to iterate over a sequence,
# But don't want to store entire sequence in memory.

# NOTE: Yield are used in Python generators.
# A generator function is defined like a normal function, but whenever it
# needs to generate a value, it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.


# Example:
# Generator Function
def nexSquare():
    i = 1
    while True:  # An Infinite loop to generate square
        yield i * i
        i += 1  # Next execution resume from this point


for n in nexSquare():
    if n > 100:
        break
    print(n)


# Return Multiple Values:
# 1. Using object:
class Test:
    def __init__(self):
        self.name = "Eve"
        self.x = 100


def some():  # Function returns an object of Test
    return Test()


s = some()
print(s.name, "/", s.x)


# 2. Using Tuple:
def someTup():
    name = "Eva"
    z = 10
    return name, z  # Return Tuple / could be (name, z)


e, x = someTup()
print(e, "/", x)
print(someTup())


# 3. Using List:
def someLi():
    name = "Evina"
    z = 20
    return [name, z]


print(someLi())


# 4. Using Dictionary:
def someDi():
    d = dict()
    d['name'] = "Evan"
    d['x'] = 30
    return d


print(someDi())


# 5. Using data class:
@dataclass
class BookList:
    name: str
    cost: float
    available: int = 0


b = BookList(name='Python programming',
             cost=200,
             available=3)
print(b)

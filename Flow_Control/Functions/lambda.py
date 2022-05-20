# Lambda Expressions : Anonymous functions/Functions without name

"""
Syntax :
lambda arguments : expression

def <lambda>(arguments): return expression
"""


def addNum(n): return lambda x: x + n

p = addNum(10)
print(p(20))


# q = lambda x: lambda y: x + y
# print(q(1)(2))
def addition(): return lambda x: lambda y: x + y

q = addition()
print(q(17)(3))


# Lambda with map() and filter():
mList = [1, 4, 6, 7, 8, 11, 3, 4, 6]

nList = list(filter(lambda x: x > 5, mList))
print(nList)

aList = list(map(lambda x: x+1, mList))
print(aList)

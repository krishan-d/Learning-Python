"""
Operators
"""

import operator


# Arithmetic Operators:
# +  : addition
# -  : subtraction
# /  : division
# *  : multiplication
# ** : exponential
# // : integer division (removes decimal portion)
# %  : modulus (gives remainder of division)
print(5 // 2)  # 2
print(-5 // 2)  # -3

# Comparison Operator:  -> Returns True/False
# <   : less than
# <=  : less than or equal to
# >   : greater than
# >=  : greater than or equal to
# ==  : equal to
# !=  : not equal to


# Logical Operators:
# and : Logical AND, True if Both operands are True
# or  : Logical OR,  True if either of operand is True
# not : Logical NOT, True if operand is False


# Bitwise Operator: act on bits, perform bit by bit operation
# operates on binary numbers
# &	: Bitwise AND	x & y
# |	: Bitwise OR	x | y
# ~	: Bitwise NOT	~x
# ^	: Bitwise XOR	x ^ y
# >> : Bitwise right shift	x>>
# << : Bitwise left shift	x<<

a, b = 10, 4

# Assignment Operator:
# =
# +=	Add AND: a+=b     a=a+b
# -=	Subtract AND: a-=b     a=a-b
# *=	Multiply AND: a*=b     a=a*b
# /=	Divide AND:	a/=b     a=a/b
# %=	Modulus AND:a%=b     a=a%b
# //=	Divide(floor) AND: a//=b     a=a//b
# **=   Power AND: a**=b  a=a**b

# Example 1:
x = 10
x = x + 10  # Modifying value creates new object
print("Id :", id(x), "Value :", x)
x += 10  # Modifying variable's value creates new object
print("Id :", id(x), "Value :", x)
z = [0, 1]
z = z + [3]
print("Id :", id(z), "Value :", z)
z += [4]  # Modify value in current reference.
print("Id :", id(z), "Value :", z)


# Identity Operator:
# is          True if the operands are identical
# is not      True if the operands are not identical
print(a is b)  # False
print(a is not b)  # True

# Membership Operator:
# in          True if value is found in the sequence
# not in      True if value is not found in the sequence

# ------------------------------------------------------------
# Ternary Operator:

# Syntax: [on_true] if [expression] else [on_false]
minValue = a if a < b else b
print(minValue)

# Using Tuple for selecting item: (if_test_false,if_test_true)[test]
# if [a<b] is True, return 1 and element with index 1 will print
print((b, a)[a < b])

# Use Dictionary :
print({True: a, False: b}[a < b])

# Use lambda: More Efficient
print((lambda: b, lambda: a)[a < b]())

# NOTE : Ternary operators can be written as nested if-else
print("Equal" if a == b else "a>b" if a > b else "b>a")
# ------------------------------------------------------------

# Any All:
# Any: Returns true if any of the items is True. It returns False if empty or all are false.
# As a sequence of OR operations on the provided iterables.
print(any([False, True, False, False]))

# All: Returns true if all the items are True (or if the iterable is empty).
# As a sequence of AND operations on the provided iterables.
print(all([True, True, True, True]))
# ------------------------------------------------------------

# Inplace / Standard operators:
# __add__ : store sum in another variable without modifying arguments.
# implements c=a+b
# __iadd__: makes an inplace change in 1st argument passed by storing sum in it.
# implements a+=b in case of immutable targets(list, dictionary)

q = [0, 4]
r = operator.add(q, [3])  # r = q + [3]
print(r, "/", q)

p = operator.iadd(q, [7, 8])  # q+=[7, 8]
print(p, '/', q)
# ------------------------------------------------------------


# Operator overloading:
class Complex:
    def __init__(self, i, k):
        self.a = i
        self.b = k

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Ob1, Ob2 = Complex(1, 2), Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

# Special Functions:
# 1. Mathematical Operator:
# Addition	+	            __add__(self, other)
# Subtraction	-	        __sub__(self, other)
# Division	/	            __truediv__(self, other)
# Floor Division	//	    __floordiv__(self, other)
# Modulus(or Remainder)	%	__mod__(self, other)
# Power	**	                __pow__(self, other)

# 2. Assignment Operator:
# Increment	+=	__iadd__(self, other)
# Decrement	-=	__isub__(self, other)
# Product	*=	__imul__(self, other)
# Division	/=	__idiv__(self, other)
# Modulus	%=	__imod__(self, other)
# Power	   **=	__ipow__(self, other)

# Relation Operator:
# Less than	                <	__lt__(self, other)
# Greater than	            >	__gt__(self, other)
# Equal to	               ==	__eq__(self, other)
# Not equal	               !=	__ne__(self, other)
# Less than or equal to	   <=	__le__(self, other)
# Greater than or equal to >=	__ge__(self, other)

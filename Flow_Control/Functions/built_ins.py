"""
Built-in Functions:
"""

# Partial Function:
# Allow to fix a certain number of arguments of a function and generate a new function.
# Can drive special function from general function and reuse code.

import functools
import tkinter
from functools import *


# Normal Function
def adder(a, b, c): return 100 * a + 10 * b + c


# Partial Function with b=1 and c=2
p = partial(adder, c=2, b=1)

print(p(3))  # 312 # passing a=3 here.


# -----------------------------------------------------------
# functools.reduce(func, seq):
# To apply a particular function passed in its argument to all the list elements, mentioned in sequence passed along.
# Initially first two elements of sequence are picked and result is obtained.
# Then attained result and element (succeeding second element) are picked and result stored.
# continues and Final result returned.
lst = [1, 3, 5, 6, 2, ]
print("\nReduce :", functools.reduce(lambda x, y: x + y, lst))  # -> 17


# -----------------------------------------------------------
# zip() Function:
# zip() makes an iterator that aggregates elements from each of the iterables.
# Returns an iterator of tuples.
print("\nzip Function:")
x, y = [1, 2, 3], [4, 5, 6, 7, 8]
print(list(zip(x, y)))  # [(1, 4), (2, 5), (3, 6)]

d1, d2 = {'a': 1, 'b': 2}, {'c': 3, 'd': 4}
print(list(zip(d1, d2)))
print(list(zip(d1, d2.values())))

new_dict = {}
for d1key, d2val in zip(d1, d2.values()):
    new_dict[d1key] = d2val

print(new_dict)

# -----------------------------------------------------------
# range(start, stop, step):
print("\nrange Function:")
r = range(4)
print(r)  # range(0, 4)
print(r.start)
print(r.stop)
print(r.step)
print(r.index(3))
# NOTE: Range does not return iterator.
# print(next(r))  # raise Error
# NOTE: Range is iterable
de = iter(range(6))
print(de)
for d in de: print('\t', d)

# -----------------------------------------------------------
# __import__() Function:
# Syntax: __import__(name, globals, locals, fromList, level)
# name : Name of the module to be imported
# globals and locals : Interpret names
# formList : Objects or submodules to be imported (as a list)
# level : Specifies whether to use absolute or relative imports. Default is -1(absolute and relative).

# Application:
# When there is a need of importing modules during the runtime.

print("\n__import__ Function:")
# Example 1:
# np = __import__('numpy', globals(), locals(), [], 0)
# a = np.array([1, 2, 3])
# print(type(a))

# Example 2:
np = __import__('numpy', globals(), locals(), ['complex128', 'array'], 0)
arr = np.array
print(arr)

# -----------------------------------------------------------
# Functions on int(bit_length,to_bytes,from_bytes)
# int.bit_length():
# Returns the number of bits required to represent an integer in binary, excluding the sign and leading zeros.
num = 7
print(num.bit_length())  # 3
print((-7).bit_length())  # 3

# int.to_bytes(length, byteorder, *, signed=False)
# Return an array of bytes representing an integer.
# byteorder is “big”, the most significant byte is at the beginning of the byte array.
# byteorder is “little”, the most significant byte is at the end of the byte array.
# The signed argument determines whether two’s complement is used to represent the integer.
print((1024).to_bytes(2, 'big'))  # b'\x04\x00'

# int.from_bytes(bytes, byteorder, *, signed=False):
# Returns the integer represented by the given array of bytes.
print(int.from_bytes(b'\x00\x10', byteorder='big'))  # 16

# -----------------------------------------------------------
# complex() Function:
# complex() returns a complex number with the value real + imag*1j or converts a string or number to a complex number.
print("Complex:", complex(2, 3), '||', complex('12+2j'))

# -----------------------------------------------------------
# all()	: Returns true if all element is true or if the list is empty.
# any()	: Return true if any element of the list is true. if the list is empty, return false.
booList = [True, True, False, True]
print("All:", all(booList))
print("Any:", any(booList))

# -----------------------------------------------------------
# sum()	: Sums up the numbers in the list.
# ord()	: Returns an integer representing the Unicode code point of the given Unicode character.
# cmp()	: This function returns 1 if the first list is “greater” than the second list.
# max()	: Return maximum element of a given list.
# min()	: Return minimum element of a given list.

# len()	: Returns length of the list or size of the list

# enumerate()  : Returns enumerate object of the list
# Included in loops

# accumulate() : Apply a particular function passed in its argument to all the list elements-
# -returns a list containing the intermediate results
# lambda() : This function can have any number of arguments but only one expression, which is evaluated and returned.

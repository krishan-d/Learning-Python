"""
Tuple:
"""
# ordered, immutable(unchangeable) and allow duplicates.
# Built-in Immutable sequence.

# NOTE: Tuples are immutable lists.

# Creating Tup...
emptyTup = ()
aTup = (1, 'rose')
packingTup = 10, 'Pudding', True  # Tup packing
uTup = packingTup, (0, 00, 100)
print("Tup packing :", uTup)
ssTup = ("Hi!",)  # Single string Tup...
# noTup = ("Hi!")  # Invalid Tup

# Constructor: tuple(iterable=())
emp_Tup = tuple()
arg_Tup = tuple(("apple", "banana", "cherry"))  # Tuple as argument
List_Tup = tuple([3, 7, 9])
string_Tup = tuple('Cherries')

# Concatenation...
conTup = arg_Tup + ssTup
print("\nConcatenation :", conTup)

# Indexing/ Negative Indexing/ Tup slicing...
print('\n\r')
newTup = 1000, 7, 'Hi!', [2, 4, 6], (3, 7)
print(newTup)
print(newTup[0])  # -> 1000
print(newTup[3][2])  # -> 6
print(newTup[-1])  # -> (3, 7)
print(newTup[1:2])  # -> (7,)
print(newTup[::-1])  # -> ('Hi!', 7, 1000)

# NOT ALLOWED OPERATIONS...
# newTup[1] == 4  # TypeError
# newTup.append(2)
# newTup.remove(4)
# del newTup[3]

# Changing...
# newTup[2] = 10  # TypeError : Tuple object doesn't support item assignment.
# However, Item of mutable element can be changed.
newTup[3][1] = 0
print("\nChanged:", newTup)

# Methods...
# index(value, start=0, stop)-> Return index :
print("Tup index :", newTup.index(1000))
print("Tup count :", newTup.count(7))

# Membership...
print("Membership:", 7 in newTup)

# Unpacking Tup...
vagTup = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = vagTup
print("\nUnpacking Tup.........")
print("Green :", green)
print("Tropic :", tropic)
print("Red :", red)

# Looping/ Iteration...
for (a, b) in [(3, 7), (0, 2), (4, 6)]:
    print(a)
    print(b)

# Pros over List:
# Use Tup for heterogeneous (different) data and Lists for homogeneous (similar) data.
# Tup.. are immutable, iterating through a tuple is faster than with list.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# Immutable data remains write-protected.

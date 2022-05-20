# List...
# ordered
# mutable(changeable),
# duplicate elements
# indexed

# List creation...
empty_List = []  # Empty List
mixed_List = ["Naomi", 0, 7.0, True]
range_List = range(5, 9)
string_List = ["Hi", "Eve", "Edwina"]
number_List = [1, 4, -8]
comp_List = [x**2 for x in range(5)]

# Constructor: list(mutable-sequence):
empList = list()  # Empty List
conList = list(("Hi", 'There!', 0))


# Accessing elements with Indexing And Slicing...
aList = [0, ('I', 10), 'snow', [7, 'Eve'], {1: 'Ice', 2: 'Burg'}]
print(aList[0])
print(aList[3][1])
print(aList[-1].get(1))
print(aList[-3])

print(aList[-1])
print(aList[:-2])
print(aList[-2:])
print(aList[::-1])  # Reverse


# Methods...
# Add/ Change List Elements:
odd = [2, 4, 6, 8]
odd[0] = 1
print(odd)
odd[1:4] = [3, 5, 7]
print(odd)

L = [1, 2, 4, 3, 2]
print("\nList L:", L)
print("List count(2):", L.count(2))
print("List Length:", len(L))

# Adding Element to List...
# concatenation:
concat_List = string_List + number_List
# append(object)-> None:
L.append(4)  # Equivalent to a[len(a):] = [x]
print("L.append(4):", L)
# nList.append([0, 1])

# extend(iterable)-> None:
# nList.extend(0)  # TypeError
L.extend([5, 7])  # Equivalent to a[len(a):] = iterable
print("L.extend([5, 7]):", L)

# insert(index, object):
L.insert(3, 0)
print("L.insert(3, 0):", L)


# index(value, start, stop):
print("L.index(2):", L.index(2))
print("L.index(2, 3):", L.index(2, 3))


# Removing Element From List...
# pop(index=-1) -> Removes Last Item:
pooped = L.pop(2)
print("pooped:", pooped, "And", L.pop(), ",L:", L)

# remove(value) -> None:
# Remove first item from list whose value is equal to x.
L.remove(2)
print("L.remove(2):", L)


# Reverse()-> None:
L.reverse()
print("L.reverse():", L)


# sort(key=None, reverse=False)-> None:
L.sort(reverse=True)
print("Reverse L.sort:", L)
L.sort()
print("L.sort:", L)


def sortKey(x):
    return x % 2 == 0


L.sort(key=lambda x: (x % 2 != 0))
print("Key[Even First] sorted:", L)


# copy():
reference_List = L  # not coping but reference
print("Reference List:", reference_List)
# Note: Any change in reference list reflect in original list.

copy_List = L.copy()
print("Copy:", copy_List)
another_copy_List = list(L)  # creates new List.
print("Copy using constructor:", another_copy_List)


# Min/Max...
print("Max :", max(L))
print("Min :", min(L))

# clear():
L.clear()  # Makes List empty
print(L)

"""
Set:
"""
# Set is : Iterable, mutable, unordered and un-indexed
# Every set element is unique(no duplicate) and must be immutable.

# NOTE:
# Sets being mutable are un-hashable, so they can't be used as dictionary keys.

# Creation...
mixed_set = {"Hi", 2, True, 27.04, 'Eve'}
print("Type :", type(mixed_set))
# no_set = {1, 2, [3, 4]}  # TypeError due to [3, 4] mutable item

# set() Constructor:
empty_set = set()  # Empty set
se0 = set(("apple", "banana", "cherry"))
se1 = set('Pudding Pie')
print(se1)
se2 = set([1, 0, 4, 0])
print(se2)


# Adding/ Updating...
new_set = {1, 3}
new_set.add(2)
print("Added:", new_set)

# update(*Iterable)-> None:
new_set.update({7})
# new_set.update("Hi")
print(new_set)
sList = [2, 3, 4]
new_set.update(sList)
print(new_set)
new_set.update([4, 5], {1, 6, 8})
print("Updated set:", new_set)

# Removing...
# remove(element)-> None:
# new_set.remove(element="WRONG KEY")  # TypeError
new_set.remove(8)
print("Removed:", new_set)

# discard(element)-> None:
new_set.discard("WRONG KEY")  # No Error/ Nothing discarded.
new_set.discard(5)
print("Discarded:", new_set)

# pop(): pop random element
popped_item = new_set.pop()
print("Popped item:", popped_item)
print(new_set)

# clear()-> None:
print("Cleared set:", new_set.clear())

del new_set  # Delete set


# Set operations...
A, B = {'a', 'b', 'c'}, {1, 2, 'a'}
N = {'a', 'd', 'b'}
print("\nOperations...")
print("A:", A, "\nB:", B)

# union(Iterable) -> Set[_T]: // (A | B)
# update(Iterable): Updates a set with the union of itself and others.
U_s = A.union(B)
print("union() :", U_s)  # -> {1, 2, 'c', 'b', 'a'}
# print(A | B)
N.update(B)  # -> {'d', 1, 2, 'a', 'b'}
print("update() :", N)


# difference(Iterable) -> Set[_T]: // (A - B)
# Returns the difference of two or more sets as a new set.
D_s = A.difference(B)
print("difference() :", D_s)  # -> {'c', 'b'}
# print(A - B)
N = {'a', 'd', 'b'}
# difference_update(Iterable) -> None:
N.difference_update(B)
print("difference_update() :", N)  # -> {'b', 'c'}


# intersection(Iterable) -> Set[_T]: // (A & B)
# Return new set, contains common item(duplicate) in both set.
In = A.intersection(B)  # -> {'a'}
print("intersection() :", In)
# print(A & B)
N = {'a', 'd', 'b'}
# intersection_update(Iterable) -> None:
N.intersection_update(B)  # -> {'a'}
print("intersection_update() :", N)


# symmetric_difference() -> Set[_T]: // (A ^ B)
# Returns the symmetric difference(elements in A and B excluding the intersection) of two sets as a new set.
Sd_s = A.symmetric_difference(B)  # -> {1, 2, 'b', 'c'}
print("symmetric_difference() :", Sd_s)
# print(A ^ B)
N = {'a', 'd', 'b'}
# symmetric_difference_update() -> None:
N.symmetric_difference_update(B)  # -> {1, 2, 'b', 'c'}
print("symmetric_difference_update() :", N)


print("\nMethods...")
# isdisjoint():
# Returns True if two sets have a null intersection.
a, b, c = {2, 3, 4, 5}, {7, 8, 9, 0}, {1, 2}
print("isdisjoint() :", a.isdisjoint(b))  # -> False
print("isdisjoint() :", a.isdisjoint(c))  # -> True


# issubset():
# Returns True if another set contains this set.
x, y = {2, 3}, {1, 2, 3, 4}
print("issubset() :", y.issubset(x))  # -> False
print("issubset() :", x.issubset(y))  # -> True


# issuperset():
# Returns True if this set contains another set.
print("issuperset() :", y.issuperset(x))  # -> True
print("issuperset() :", x.issuperset(y))  # -> False


# Frozen Set: Immutable object.
# Frozen sets are immutable sets. Its elements can not be changed once assigned.
# Frozen sets being immutable are hashable and can be used as keys to a dictionary.
# Being immutable, it does not have methods that add or remove elements.
empty_frozen_set = frozenset()

sFrozen = frozenset(('a', 'e', 'i', 'o', 'u'))
print("\nFrozen Set :", sFrozen)

# Membership...
print("\nMembership:", 'i' in set("Hi Edwina!"))

# Loop/ Iteration...
for i in set([1, 2, 2, 3]):
    print('\t', i)

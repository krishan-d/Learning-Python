# sorted(iterable, key=None, reverse=False) -> sorted List
# iterable : A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
# key: Function that serves as a key for the sort comparison.


print(*sorted("HiThere!"))  # String

numbers = [4, 2, 12, 8]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
# NOTE: List has sort() method that doesn't return any value and changes original List.

v_Tup = ('e', 'a', 'u', 'o', 'i')
print(sorted(v_Tup))

# Sorting in descending order:
v_set = set(v_Tup)
print(sorted(v_set, reverse=True))

v_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}
print(sorted(v_dict, reverse=True))

frozen_set = frozenset(v_Tup)
print("Frozen set:", frozen_set)
print(sorted(frozen_set, reverse=True))

# Using key parameter in sorted:
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
print(random)
sorted_List = sorted(random, key=lambda x: x[1])
print(sorted_List)

# Sorting with multiple keys:
# List elements: (Student's Name, Marks out of 100, Age)
# manner:
# Student with the highest marks is in the beginning.
# On having equal marks, younger comes first.
participant_List = [('Alison', 50, 18), ('Terence', 75, 12), ('David', 75, 20), ('Jimmy', 90, 22), ('John', 45, 12)]

# NOTE:
# Achieved with multiple keys by returning tuple instead of a number.

# Two tuples can be compared by comparing their elements starting from first.
# If elements are equal, the second element is compared, and so on.
print((1, 3) > (1, 4))

sorted_List = sorted(participant_List, key=lambda item: (100-item[1], item[2]))
print(sorted_List)

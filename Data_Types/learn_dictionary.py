"""
Dictionary :
"""
# Collection
# ordered*, changeable and, do not allow duplicates.

# dict() -> new empty dictionary
# dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs.
# dict(iterable) -> initialized as if via:
#     d = {}
#     for k, v in iterable:
#         d[k] = v
# dict(**kwargs) -> initialized with the name=value pairs
# in the keyword argument list.


# dict() constructor:
empty_dict = dict()  # Empty Dictionary
print(empty_dict)
dict1 = dict([('Edwina', 4139), ('Noah', 4127), ('Eve', 4098)])
print(dict1)
dict2 = dict(a=12, b=16, c=20)
print(dict2)

# Dictionary Comprehensions:
comprehension_dict = {x: x ** 2 for x in (2, 4, 6)}
print(comprehension_dict)

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}

# Creation...
emp_dict = {}  # Empty Dictionary
mixed_key_dict = {'name': 'Edwina', 1: [2, 6, 8]}  # Mixed Keys

newDict = {
    "brand": "Ford",
    "year": 1964
}

print("\nDictionary :", newDict)
print("Type :", type(newDict))

# Produces a printable string representation of a dictionary.
print("To String :", str(newDict))

# Adding/ Changing...
newDict["year"] = 2020  # Updating/Changing
newDict["option"] = ["red", "white"]  # Adding
print("Dictionary:", newDict)

# copying...
new_copy = newDict.copy()
print("\nDictionary's copy :", new_copy)

# Accessing...
print("\nAccessing Elements From Dictionary :...")
print("brand :", newDict["brand"])
# print(newDict['WRONG KEY!'])  # KeyError
# get(key: _KT) -> _VT_co | None:
year = newDict.get("year")
print("year :", year)
print("Accessing wrong key using get method :", newDict.get('WRONG KEY!'))

print("Keys: :", newDict.keys())
print("Values :", newDict.values())
print("Items :", newDict.items())


# setdefault(key, default=None) : _VT: ...
# Return value of key.
# If the key does not exist: insert the key, with the default value.
newDict.setdefault("owner")
print('\nsetdefault :', newDict['owner'])
print("Dictionary :", newDict)

# in / not in:
print("\nMembership: ", "WRONG KEY!" in newDict)

# update(Mapping[K, V]) || update(Iterable[Tuple[K, V]]):
newDict.update({"year": 2022})  # Changing
# add item using .update():
newDict.update([("racer", True), ('max_speed', 400)])  # Adding
print("Insert using update() :", newDict)


# __hash__:
print("__hash__ :", newDict.__hash__)


# class methods...
# fromkeys(iterable, value=None, /)-> dict[_T, Any | None]:
# Create a new dictionary with keys from iterable and values set to value.
seq = ['Never', 'give', 'up']
d = dict.fromkeys(seq)
print("Fromkeys :", d)

marks = {}.fromkeys(["M", "S", "E"], 0)
print(marks)

# Removing...
print("\nRemoving Items From Dictionary :...")
# pop(k[,d]) -> v : Remove specified key and return the corresponding value.
# If the key is not found, return the default if given; otherwise, raise a KeyError.

p = newDict.pop("racer")  # True
print("Popped :", p)
print("Dictionary past pop :", newDict)
# empty_dict.pop()  # KeyError

# popitem():
# Remove and return a (key, value) pair as a 2-tuple.
# Pairs are returned as LIFO order. Raises KeyError if the dict is empty.
x = newDict.popitem()
print("Popped item :", x)
print("Dictionary past popitem :", newDict)
# empty_dict.popitem()  # KeyError

# Using del keyword:
del newDict["owner"]
print("Dictionary past del :", newDict)
# del newDict['WRONG KEY!']  # raise KeyError

# clear()->None: Make dictionary empty
newDict.clear()
print("Clear dictionary :", newDict)


# Looping/Iteration in Dictionary...
carDict = {"brand": "Odi", "model": "X", "year": 2022}
for x in carDict:
    print(carDict[x], end='||')
print('\r\n')

# dict.items()/ dict.values()/ dict.keys():
for x, y in carDict.items():
    print(x, y)

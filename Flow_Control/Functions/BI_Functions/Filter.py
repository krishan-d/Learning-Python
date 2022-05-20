# Filter() function extracts elements from an iterable for which a function returns True.

# Syntax:
# filter(function|None, iterable) -> filter object/ Iterator
# Return an iterator yielding those items of iterable for which function(item) is true.
# If function is None, return the items that are true.
# Similar to the map function.

# NOTE: Iterator can be converted to sequence like lists, tuples, strings...

def isOne(x): return x == 1

nums = [1, 1, 3, 6, 8, 0, 1, 7, 1]
is_one_iterator = filter(isOne, nums)
print("Filter Object To List:", list(is_one_iterator))

# Using Lambda inside Filter:
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_num_iterator = filter(lambda x: x % 2 != 0, numbers)  # odd numbers
print("Odd Number List:", list(odd_num_iterator))


randomList = [1, 'a', 0, False, True, '0']
filtered_iterator = filter(None, randomList)
print("Filtered List:", list(filtered_iterator))  # [1, 'a', True, '0']

"""
Deque:
"""

from collections import deque

# Doubly Ended Queue.
# quicker append and pop operations then List, from both ends of container.
# deque provides O(1) Time complexity.
# List provides O(n) Time complexity.

# deque([iterable[, maxlen]]) --> deque object
# A list-like sequence optimized for data accesses near its endpoints.

newList = [10, -40, 77]
dq = deque(newList)
print(dq)                       # -> deque([10, -40, 77])


# append()
# append(self, x: _T) -> None: ...
# Add an element to the right side of the deque.
dq.append(-26)
print(dq)
# appendleft(self, x: _T) -> None: ...
dq.appendleft(27)
print(dq)                       # -> deque([27, 10, -40, 77, -26])


# copy(self) -> deque[_T]: ...
d0 = dq.copy()
print(d0)                       # -> deque([27, 10, -40, 77, -26])


# count(self, value):
# count(self, x: _T) -> int: ...
print(d0.count(27))             # -> 1


# clear(self) -> None: ...
d0.clear()
print(d0)                       # -> deque([])


# pop()
# pop(self) -> _T: ...
x = dq.pop()
print("popped :", x)            # -> -26
# popleft(self) -> _T: ...
z = dq.popleft()
print("Left popped :", z)       # -> 27
print(dq)


# extend()
# extend(self, iterable: Iterable[_T]) -> None: ...
# Extend the right side of the deque with elements from the iterable.
dq.extend([4, 12])
print(dq)                       # -> deque([10, -40, 77, 4, 12])
# extendleft(self, iterable: Iterable[_T]) -> None: ...
dq.extendleft('No')
print(dq)                       # -> deque(['o', 'N', 10, -40, 77, 4, 12])


# index(self, value, start=None, stop=None):
# index(value, [start, [stop]]) -> integer...
# return first index of value. Raises ValueError if the value is not present.
print(dq.index('N'))            # -> 1


# insert(index, object)
# insert(self, i: int, x: _T) -> None: ...
dq.insert(2, (True, 0))
print(dq)                       # -> deque(['o', 'N', (True, 0), 10, -40, 77, 4, 12])


# remove(value)
# remove(self, value: _T) -> None: ...
# Remove first occurrence of value. otherwise, raise ValueError.
dq.remove(10)
print(dq)                       # -> deque(['o', 'N', (True, 0), -40, 77, 4, 12])


# reverse()
# reverse(self) -> None: ...
# Reverse *IN PLACE*
dq.reverse()
print("reverse :", dq)          # -> deque([12, 4, 77, -40, (True, 0), 'N', 'o'])


# rotate()
# rotate(self, n: int = ...) -> None: ...
# Rotate the deque n steps to the right (default n=1).
# If n is negative, rotates left.
dq.rotate(-3)
print(dq)                       # -> deque([-40, (True, 0), 'N', 'o', 12, 4, 77])
dq.rotate(4)
print(dq)                       # -> deque(['o', 12, 4, 77, -40, (True, 0), 'N'])


# Maximum size of a deque or None if unbounded.
print("max length :", dq.maxlen)

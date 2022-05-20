"""
Heap queue:
"""

import heapq

# Heap DS used to represent a priority queue.
# each time the smallest of heap element is popped(min heap).
# Whenever elements are pushed or popped, heap structure in maintained.
# The heap[0] element also returns the smallest element each time.

# Applications:
# Heapsort algorithm has limited uses because Quicksort is better in practice.

# 1.Priority Queues:
# Priority queues can be efficiently implemented using Binary Heap,
# -because it supports insert(), delete() and extractmax(), decreaseKey() operations in O(logn) time.
# Binomoial Heap and Fibonacci Heap are variations of Binary Heap.
# These variations perform union also in O(logn) time which is a O(n) operation in Binary Heap.

# 2.Order statistics:
# Heap Implemented priority queues are used in Graph algorithms like Prim’s Algorithm and Dijkstra’s algorithm.

nL = [0, 4, 2, 8]
# heapify(x):
# heapify(__heap: list[Any]) -> None: ...
# Transform list into a heap, in-place, in O(len(x)) time.
heapq.heapify(nL)
print(list(nL))  # -> [0, 4, 2, 8]
# Smallest element.
print(nL[0])  # -> 0

# heappush(__heap: list[_T], __item: _T) -> None: ...
# Push item onto heap, maintaining the heap invariant.
heapq.heappush(nL, 10)
print(list(nL))  # -> [0, 4, 2, 8, 10]

# heappop(__heap: list[_T]) -> _T: ...
# Pop the smallest item off the heap, maintaining the heap invariant.
print(heapq.heappop(nL))  # -> 0
print(list(nL))  # -> [2, 4, 10, 8]

# heappushpop(__heap: list[_T], __item: _T) -> _T: ...
# Fast version of a heappush followed by a heappop.
print(heapq.heappushpop(nL, 6))  # -> 2
print(list(nL))  # -> [4, 6, 10, 8]

# heapreplace(__heap: list[_T], __item: _T) -> _T: ...
# Pop and return the current smallest value, and add the new item.
# This is more efficient than heappop() followed by heappush(),
# and can be more appropriate when using a fixed-size heap.
print(heapq.heapreplace(nL, 0))  # -> 4
print(list(nL))  # -> [0, 6, 10, 8]

# nlargest(n: int, iterable: Iterable[_T], key: Callable[[_T], SupportsLessThan] | None = ...) -> list[_T]: ...
# nlargest(n, iterable, key=None):
# Find n the largest elements in a dataset.
# Equivalent :  sorted(iterable, key=key, reverse=True)[:n]
print(heapq.nlargest(2, nL))  # -> [10, 8]

# nsmallest(n: int, iterable: Iterable[_T], key: Callable[[_T], SupportsLessThan] | None = ...) -> list[_T]: ...
# nsmallest(n, iterable, key=None):
# Find n the smallest elements in a dataset.
# Equivalent to:  sorted(iterable, key=key)[:n]
print(heapq.nsmallest(3, nL))  # -> [0, 6, 8]


# merge(*iterables: Iterable[_T], key: Callable[[_T], Any] | None = ..., reverse: bool = ...) -> Iterable[_T]: ...
# merge(*iterables, key=None, reverse=False):
m = heapq.merge(nL, [4, 2])
print(type(m))  # -> <class 'generator'>
print(list(m))  # -> [0, 4, 2, 6, 10, 8]

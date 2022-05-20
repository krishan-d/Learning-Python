
# map(func, *iterables) --> map (class) object / Iterator
# Parameter:
# func: perform some action to each element of an iterable.
# iterable: Sets/Lists/...
# Returned value passed to function/ constructor functions such as set(), list()

# Make an iterator that computes the function using arguments from each of the iterables.
# Stops when the shortest iterable is exhausted.

def doSomething(x): return x + x / 2

nums = [1, 5, 6, 7, 2]
map_object = map(doSomething, nums)
map_To_List = list(map_object)
print(map_To_List)


# Lambda Function with Map And Passing Multiple Iterators:
num1, num2 = [1, 3, 5, 6, 2, ], [1, 2, 0, 3, 4]
res = map(lambda n1, n2: n1 + n2, num1, num2)
print("Map To Set:", set(res))

# Code: Making List of Lists using Map:
n = 2
arr = []
for _ in range(n):
    arr.append(list(map(int, input("Input Numbers!\n").rstrip().split())))
print(arr)

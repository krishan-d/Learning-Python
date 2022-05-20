"""
Garbage Collection
"""

import gc

# Python’s memory allocation and deallocation method is automatic.
# 1. Reference counting
# 2. Garbage collection
# When references to an object are removed, the reference count for an object is decremented.
# When the reference count becomes zero, the object is deallocated.
"""
Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When
the number of allocations minus the number of deallocations is greater than the threshold number, the garbage
collector is run. """

i = 0


# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = {}
    x[i + 1] = x
    print(x)


# Lists are cleared whenever a full collection or collection of the highest generation (2) is run
# Manual garbage collection
collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % collected)

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % collected)

print("Garbage collection thresholds:", gc.get_threshold())
# Garbage collection thresholds: (700, 10, 10)
"""
Means when the number of allocations vs. the number of deallocations is greater than 700,
the automatic garbage collector will run.
"""

# Make an object eligible for garbage collection
z = [1]
# delete list form memory/assign object y to None(Null)
del z
# y = None

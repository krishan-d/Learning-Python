"""
Pooling between processes:
"""

# To utilize all the cores, multiprocessing module provides a Pool class.
# The Pool class represents a pool of worker processes.
# The task is offloaded/distributed among the cores/processes automatically by Pool object.


"""
Pool(
    processes: int | None = ...,
    initializer: Callable[..., Any] | None = ...,
    initargs: Iterable[Any] = ...,
    maxtasksperchild: int | None = ...,
    ) -> pool.Pool: ...

parameters:
    processes: specify the number of worker processes.
    maxtasksperchild: specify the maximum number of task to be assigned per child.
    initializer: specify an initialization function for worker processes.
    initargs: arguments to be passed to initializer.
"""

import multiprocessing
import os


def square(n):
    print("Worker process id for {0}: {1}".format(n, os.getpid()))
    return n * n


if __name__ == "__main__":
    nList = [1, 2, 3, 4, 5]

    # creating a pool object
    p = multiprocessing.Pool()

    res = p.map(square, nList)

    print(res)

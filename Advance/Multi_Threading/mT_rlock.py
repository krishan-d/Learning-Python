# RLock - Re-entrant Lock:
# RLock can be acquired multiple times by the same thread.


# Example 1:
import threading

lock = threading.Lock()
print("Acquiring the lock :", lock.acquire())
# adding 0 as timeout value else, the below statement will wait forever
print("Acquiring the lock again :", lock.acquire(0))

rLock = threading.RLock()
print("Acquiring the lock :", rLock.acquire())
print("Acquiring the lock again :", rLock.acquire())


# Example 2:
lock = threading.RLock()


def get_first_line():
    lock.acquire()
    try:
        data = 1
    finally:
        lock.release()
    return data


def get_second_line():
    lock.acquire()
    try:
        data = 2
    finally:
        lock.release()
    return data


lock.acquire()
try:
    first = get_first_line()
    second = get_second_line()
finally:
    lock.release()
    print(first, second)

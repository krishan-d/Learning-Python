"""
Synchronization between processes:
"""

# Process synchronization is defined as a mechanism which ensures that two or more concurrent processes,
# -do not simultaneously execute some particular program segment known as critical section.

# Critical section : refers to the parts of the program where the shared resource is accessed.

# Concurrent accesses to shared resource can lead to race condition.
# Race condition :
# occurs when two or more processes can access shared data, and they try to change it at the same time. As a result,
# -the values of variables may be unpredictable and vary depending on the timings of context switches of the processes.

import multiprocessing

# Example 1:
# def withdraw(balance):
#     for _ in range(10000):
#         balance.value = balance.value - 1
#
#
# def deposit(balance):
#     for _ in range(10000):
#         balance.value = balance.value + 1
#
#
# def perform_transactions():
#     # initial balance (in shared memory)
#     balance = multiprocessing.Value('i', 100)
#
#     p1 = multiprocessing.Process(target=withdraw, args=(balance,))
#     p2 = multiprocessing.Process(target=deposit, args=(balance,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print("Final balance = {}".format(balance.value))
#
#
# if __name__ == "__main__":
#     for _ in range(10):
#         perform_transactions()

# This unpredictability in balance value is nothing but race condition in above code.
# P1                          p2                balance
# read(balance)=100                             100
#                       read(balance)=100       100
# balance=current-1=99                          99
#                       balance=current+1=101   101

# using lock:
# multiprocessing module provides a Lock class to deal with the race conditions.
# Lock is implemented using a Semaphore object provided by the Operating System.
# P1                          p2                balance
# read(balance)=100                             100
# balance=current-1=99                          99
#                       read(balance)=99        99
#                       balance=current+1=100   100


# Example 2:
def withdraw(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()


def deposit(balance, lock):
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()


def perform_transactions():
    balance = multiprocessing.Value('i', 100)

    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=withdraw, args=(balance, lock))
    p2 = multiprocessing.Process(target=deposit, args=(balance, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Final balance = {}".format(balance.value))


if __name__ == "__main__":
    for _ in range(10):
        perform_transactions()

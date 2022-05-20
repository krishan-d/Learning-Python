# Condition object:
# to synchronize the access to any resources more efficiently, we can associate a condition with tasks,
# for any thread to wait until a certain condition is met or
# notify other threads about the condition being fulfilled so that they may unblock themselves.

# Example:
# In the Producer Consumer problem, if there is one Produces producing some item and one Consumer consuming it,
# then until the Producer has produced the item the Consumer cannot consume it.
# Hence, the Consumer waits until the Produced produces an item.
# And Producer to inform the Consumer that an item is available for consumption once it is successfully produced.

# Syntax:
# condition = threading.Condition([lock])
# condition object takes in an optional lock object as argument. If not provided then creates a default lock.
# condition object has acquire() and release() methods that call the corresponding methods of the associated lock.
# wait(), notify() and notifyAll() methods must only be called after the calling thread has acquired the lock.

# Methods:
# wait([timeout]) -> bool: ...
# To block the thread and make it wait until some other thread notifies it by calling notify() or notifyAll()
# method on the same condition object or until the timeout occurs.
# returns True if it is released because of notify() or notifyAll() method.
# False when timeout occurs.

# notify(self, n: int = ...) -> None: ...
# wakes up any one thread waiting on the corresponding condition.

# notifyAll(self) -> None: ...
# wakes up all the threads waiting on this condition.


import threading
import time
from random import randint


class SomeItem:
    # init method
    def __init__(self):
        # initialize empty list
        self.list = []

    # add to list method for producer
    def produce(self, item):
        print("Adding item to list...")
        self.list.append(item)

    # remove item from list method for consumer
    def consume(self):
        print("consuming item from list...")
        item = self.list[0]
        print("Item consumed: ", item)
        self.list.remove(item)


def producer(si, cond):
    r = randint(1, 5)
    # creating random number of items
    for i in range(1, r):
        print("working on item creation, it will take: " + str(i) + " seconds")
        time.sleep(i)
        print("acquiring lock...")
        cond.acquire()
        try:
            si.produce(i)
            cond.notify()
        finally:
            cond.release()


def consumer(si, cond):
    cond.acquire()
    while True:
        try:
            si.consume()
        except:
            print("No item to consume...")
            # wait with a maximum timeout of 10 sec
            val = cond.wait(10)
            if val:
                print("notification received about item production...")
                continue
            else:
                print("waiting timeout...")
                break

    cond.release()


if __name__ == '__main__':
    # condition object
    cond = threading.Condition()
    # SomeItem object
    si = SomeItem()
    # producer thread
    p = threading.Thread(target=producer, args=(si, cond,))
    p.start()
    # consumer thread
    c = threading.Thread(target=consumer, args=(si, cond,))
    c.start()

    # print('Waiting for producer and consumer threads...')
    p.join()
    c.join()
    print("Done")

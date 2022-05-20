# Event class:
# Used for thread synchronization.
# This class is used for inter thread communication by generating events.

# The Event class object provides a simple mechanism which is used for communication between threads where,
# one thread signals an event while the other threads wait for it.
# So, when one thread which is intended to produce the signal produces it, then the waiting thread gets activated.

# An internal flag is used by the event object known as the event flag which can be set as true using the set() method,
# and it can be reset to false using the clear() method.
# The wait() method blocks a thread until the event flag for which it is waiting is set true by any other thread.

# Syntax:
# threading.Event()

# Methods:
# is_set(self) -> bool: ...
# Returns true if and only if the internal flag is true.

# set(self) -> None: ...
# Set the internal flag to true.
# All threads waiting for it to become true are awakened.
# Threads that call wait() once the flag is true will not block at all.

# clear(self) -> None: ...
# Resets the internal flag to False.

# wait(self, timeout: float | None = ...) -> bool: ...
# To make any thread wait for an event.
# If the internal flag is true on entry, then the thread will never get blocked.
# else, it is blocked until another thread calls set() to set the flag to true, or until the optional timeout occurs.

import threading
import time


def task(event, timeout):
    print("Started thread but waiting for event...")
    # make the thread wait for event with timeout set
    event_set = event.wait(timeout)
    if event_set:
        print("Event received, releasing thread...")
    else:
        print("Time out, moving ahead without event...")


if __name__ == '__main__':
    # initializing the event object
    e = threading.Event()

    # starting the thread
    # Timeout max then sleep time
    thread1 = threading.Thread(name='Event-Blocking-Thread', target=task, args=(e, 4))

    # Timeout less than sleep time
    # thread1 = threading.Thread(name='Event-Blocking-Thread', target=task, args=(e, 2))

    thread1.start()
    # sleeping the main thread for 3 seconds
    # time.sleep(10)
    time.sleep(3)
    # generating the event
    e.set()
    # e.clear()
    print(e.is_set())
    print("Event is set.")

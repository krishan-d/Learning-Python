# Thread Synchronizing and Locking:
# This essentially means waiting for a specific thread to finish running before any other can go.
# online payment checkout: tasks
# – Verifying Payment/Card Details
# – Sending Confirmation email or shipping details
# – Loading a Thank-you page or redirecting back to main website.

# Primitive lock can have two States: locked or unlocked(initially)

import time
from threading import Thread, Lock


class NewThread(Thread):
    def __init__(self, threadId, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count
        self.threadId = threadId

    def run(self):
        print("Starting: " + self.name + "\n")
        # acquire(blocking=True, timeout=-1)
        # timeout argument is used to provide a positive floating-point value,
        # which specifies the number of seconds for which the calling thread will be blocked
        # if some other thread is holding the lock right now. The default value which is -1 means the thread will be
        # blocked for indefinite time if it cannot acquire the lock immediately.
        threadLock.acquire()
        print_time(self.name, 1, self.count)
        threadLock.release()
        print("Exiting: " + self.name + "\n")


class NewThread2(Thread):
    def __init__(self, threadId, name, count):
        Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.count = count

    def run(self):
        print("Starting: " + self.name + "\n")
        threadLock.acquire()
        threadLock.release()
        print_time(self.name, 1, self.count)
        print("Exiting: " + self.name + "\n")


def print_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s: %s %s" % (name, time.ctime(time.time()), count) + "\n")
        count -= 1


if __name__ == '__main__':
    threadLock = Lock()

    thread1 = NewThread(1, "Payment", 5)
    thread2 = NewThread2(3, "Sending Email", 10)
    thread3 = NewThread2(4, "Loading Page", 3)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    print("Done main thread")

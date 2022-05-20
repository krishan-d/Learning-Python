# Barrier object:
# Used where we want a set of threads to wait for each other.

# Example:
# we have two threads, we want both the threads to execute when both are ready.
# In such situation both the threads will call the wait() method on the barrier object once they are ready and
# both the threads will be released simultaneously only when both of them have called the wait() method.

# Syntax:
# threading.Barrier(parties, action=None, timeout=None)
# parties : Number of threads waiting at the barrier,
# action : can be used to specify a function which will be executed by any one thread waiting for the barrier.
# timeout : Timeout value in seconds after which the barrier will be released from all the waiting threads.

# Methods:
# wait(timeout=None):
# Barrier will be released only when the same number of threads call the wait() method of the barrier object.
# returns an integer value from 0 to parties-1.
# Use this value to identify which all threads have reached the waiting point of the barrier and
# which all are still not there.
# If the wait call times out, the barrier is put into the broken state.
# The wait() method may raise a BrokenBarrierError if the barrier breaks or resets as a thread waits.

# reset()
# This function resets the barrier to its default, empty state.
# If there are threads waiting for the barrier to get released will receive BrokenBarrierError.

# abort()
# This method when called on a barrier puts it into the broken state.
# Once this method is called by any of the waiting thread, the rest of the threads waiting for the barrier,
# to be released will receive BrokenBarrierError.
# may want to use this method in case of some deadlock situation to release the waiting threads.

# parties:
# Returns the number of threads we need to pass the barrier.

# n_waiting:
# This returns the number of threads that currently are waiting for the barrier to be released.

# broken:
# This is a Boolean value that is True if the barrier is in the broken state.


import threading
import time


def start_server():
    # starting server
    print("starting the server...")
    # do some startup work
    time.sleep(2)


def server(b):
    start_server()
    b.wait()
    print("Server is ready.")


def client(b):
    print("waiting for server getting ready...")
    try:
        b.wait()
        b.abort()
    except threading.BrokenBarrierError:
        print("BrokenBarrierError")
    print("sending request to server...")


if __name__ == '__main__':
    b = threading.Barrier(2, timeout=5)
    # server thread
    s = threading.Thread(target=server, args=(b,))
    s.start()
    # client thread
    c = threading.Thread(target=client, args=(b,))
    c.start()

    print(b.n_waiting)
    print(b.parties)
    print(b.broken)
    s.join()
    print(b.n_waiting)
    print(b.parties)
    print(b.broken)
    c.join()
    print("Done")

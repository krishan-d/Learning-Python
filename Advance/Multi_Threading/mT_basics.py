# Thread class:
# There are two ways to create the Thread object and specify the activity to be performed:
# 1.by passing a callable object to the constructor
# 2.by overriding the run() method in a subclass.

# --initialize Thread object.
# --call start() method to start Thread.
# --Threads call join() method to join any Thread.
# --This blocks the calling thread until the thread whose join() method is called is terminated.

# Every thread has a name associated with it. The name can be passed to the constructor,
# or we can set or retrieve name by using setname() and getname() methods respectively.

# A flag daemon thread can be associated with any thread.
# The significance of this flag is that the entire python program exits when only daemon threads are left.
# The flag can be set or retrieved by using setDaemon() method and getDaemon() method respectively.

# syntax Thread constructor:
# Thread(group=None, target=None, name=None, args=(), kwargs={})
# target: This is the callable object or task to be invoked by the run() method.
# name: This is used to specify the thread name. By default, a unique name is generated following the format Thread-N.
# args: This is the argument tuple for the target invocation.
# kwargs: This is keyword argument dictionary for the target invocation.

# start() method:
# This method is used to start the thread's activity.
# When we call this method, internally the run() method is invoked,
# which executes the target function or the callable object.

# run() method:
# Method representing the thread's activity.
# You may override this method in a subclass extending the Thread class of the threading module.
# The standard run() method invokes the callable object passed to the object's constructor as the target argument
# with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

# join([timeout]) method:
# When we call this method for any thread,
# it blocks the calling thread until the thread whose join() method is called terminates,
# either normally or through an unhandled exception.
# If you want to provide the timeout argument, it should be a floating point number.


import threading
import os
import time


# Example 1:
def Task0():
    time.sleep(3)
    print("Task 1 assigned Thread: {}".format(threading.current_thread().name))
    print("Process Id: {}".format(os.getpid()))
    print(threading.current_thread().is_alive())


def Task2():
    time.sleep(3)
    print("Task 2 assigned Thread: {}".format(threading.current_thread().name))
    print("Process Id: {}".format(os.getpid()))


def hook(frame, event, arg):
    print("Hello, I am a trace hook.")


if __name__ == "__main__":
    print("main program process id: {}".format(os.getpid()))
    print("Current Thread :", threading.current_thread())
    print("Main Thread name: {}".format(threading.current_thread().name))

    # get_ident() -> int: ...
    # returns the thread identifier of the current thread.
    print("Thread Identifier :", threading.get_ident())

    # main_thread() -> Thread: ...
    print("Main Thread :", threading.main_thread())

    t1 = threading.Thread(target=Task0)
    t2 = threading.Thread(target=Task2)

    # settrace(func: (FrameType, str, Any) -> (...) -> Any | None)-> None
    # Set a trace function for all threads started from the threading module.
    # The func will be passed to sys.settrace() for each thread, before its run() method is called.

    # threading.settrace(hook)

    # threading.setprofile(hook)

    t1.start()
    t2.start()

    print(threading.enumerate())
    print("Active Threads Number :", threading.active_count())

    # join main Thread
    # here, main thread will wait for the threads t1 and t2 to terminate and then end.
    t1.join()
    t2.join()

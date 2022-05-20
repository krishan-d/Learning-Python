# Timer:
# subclass of the Thread class.
# Using this class we can set a delay on any action that should be run only after a certain amount of time has passed
# (timer) and can easily be cancelled during that delay.

# Used to implement scheduled tasks which supposed to be executed only after a certain instant of time.

# Syntax:
# threading.Timer(interval, function, args=[], kwargs={})

# Methods:
# start(self) -> None: ...
# This method is used to start the execution of the timer object.
# When we call this method, then the timer object starts its timer.

# cancel():
# This method is used to stop the timer and cancel the execution of the timer object's action.
# This will only work if the timer has not performed its action yet.


import threading
import time


def task():
    print("Timer object is getting executed...")


if __name__ == '__main__':
    t = threading.Timer(5, task)
    print("Starting the timer object...")
    t.start()  # after 5 seconds, task will be executed

    # cancelling the timer object before start
    # print("cancelling the timer object")
    # t.cancel()

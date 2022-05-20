"""
Multiprocessing:
"""
# run independently
# have their own memory space.

# Example 1:
import multiprocessing
import os


def worker1():
    print("ID of process running worker1: {}".format(os.getpid()))


def worker2():
    print("ID of process running worker2: {}".format(os.getpid()))


if __name__ == "__main__":
    print("ID of main process: {}".format(os.getpid()))

    # creating processes
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)

    # starting processes
    p1.start()
    p2.start()

    # process IDs
    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    # wait until processes are finished
    p1.join()
    p2.join()

    # both processes finished
    print("Both processes finished execution!")

    # check if processes are alive
    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))


# Example 2:
# result = []
#
#
# def square_list(mylist):
#     global result
#     for num in mylist:
#         result.append(num * num)
#     print("Result(in process p1): {}".format(result))  # -> [1,4,9,16]
#
#
# if __name__ == "__main__":
#     myLis = [1, 2, 3, 4]
#     p1 = multiprocessing.Process(target=square_list, args=(myLis,))
#     p1.start()
#     p1.join()
#     print("Result(in main program): {}".format(result))  # -> []


# process 1/Memory space : result=[]
# process 2(P1)/Memory space: result=[]--> result=[1,4,9,16]

# Sharing data between processes
# 1. Shared memory:
# multiprocessing module provides Array and Value objects to share data between processes.
def sqList(mylist, res, square_sum):
    for idx, num in enumerate(mylist):
        res[idx] = num * num
    # square_sum value
    square_sum.value = sum(res)
    print("Result(in process p1): {}".format(res[:]))
    print("Sum of squares(in process p1): {}".format(square_sum.value))


if __name__ == "__main__":
    m = [1, 2, 3, 4]
    # creating Array of int data type with space for 4 integers
    # Array('typecode_or_type', 'size_or_initializer)
    result = multiprocessing.Array('i', 4)
    # creating Value of int data type
    # Value(typecode_or_type, *args, lock=lock,...)
    sq_sum = multiprocessing.Value('i')

    p1 = multiprocessing.Process(target=sqList, args=(m, result, sq_sum))
    p1.start()
    p1.join()
    print("Result(in main program): {}".format(result[:]))
    print("Sum of squares(in main program): {}".format(sq_sum.value))


# 2. Server process:
def print_records(records):
    # function to print record(tuples) in records(list)
    for record in records:
        print("Name: {0}\nScore: {1}\n".format(record[0], record[1]))


def insert_record(record, records):
    # function to add a new record to records(list)
    records.append(record)
    print("New record added!\n")


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        # creating a list in server process memory
        rec = manager.list([('Sam', 10), ('Adam', 9), ('Kevin', 9)])
        # new record to be inserted in records
        new_record = ('Jeff', 8)
        p1 = multiprocessing.Process(target=insert_record, args=(new_record, rec))
        p2 = multiprocessing.Process(target=print_records, args=(rec,))
        p1.start()
        p1.join()
        p2.start()
        p2.join()


# Communication btw processes:
# multiprocessing supports two types of communication channel between processes:
# 1. Queue
# use a Queue to pass messages back and forth. Any Python object can pass through a Queue.
def squareList(mylist, queue):
    for num in mylist:
        queue.put(num * num)


def print_queue(queue):
    while not queue.empty():
        print(queue.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    n = [1, 2, 3, 4]
    # creating multiprocessing Queue
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=squareList, args=(n, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()


# 2. pipes
# A pipe can have only two endpoints. Hence, it is preferred over queue when only two-way communication is required.
# returns a pair of connection objects connected by a pipe.
# The two connection objects returned by Pipe() represent the two ends of the pipe.
# Each connection object has send() and recv() methods.

def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("Sent the message: {}".format(msg))
    conn.close()


def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))


if __name__ == "__main__":
    msgs = ["hello", "hey", "hru?", "END"]
    # creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

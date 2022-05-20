"""Raise Exception"""

"""
try:
    raise NameError('HiThere')
except NameError as err:
    print('An exception flew by!')
    raise RuntimeError("Something bad happened") from err
"""

"""
try:
    print(1 / 0)
except:
    raise RuntimeError("Something bad happened")
"""

# Exception chaining...
"""
try:
    print(1 / 0)
except Exception as exc:
    raise RuntimeError("Something bad happened!") from exc
"""

# Exception chaining can be explicitly suppressed by specifying None.
"""
try:
    print(1 / 0)
except:
    raise RuntimeError("Something bad happened") from None
"""


def divide(x, y):
    try:
        r = x // y
    except ZeroDivisionError:
        print("Dividing by zero!")
    else:
        print("Answer :", r)
    finally:
        print("Finally!")


if __name__ == '__main__':
    divide(3, "3")
    # Raised error but don't have any except clause to handle it. so
    # cleanup action is taken first, then error is raised.

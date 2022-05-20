class Error(Exception):
    """
    Base class for other exceptions"""
    pass


class InputError(Error):
    """
    Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message="Exception message here!"):
        self.expression = expression
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.expression} -> {self.message}'


class TransitionError(Error):
    """
    Raised when an operation attempts a state transition that's not allowed.
    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, nex, message):
        self.previous = previous
        self.nex = nex
        self.message = message


# Use standard exception as base class:
class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


if __name__ == '__main__':

    # raise Error

    # raise InputError("Hi")
    # raise InputError(4, "Passed message!")

    try:
        raise InputError(2)
    # Exception value stored in e
    except InputError as e:
        print("Exception occurred :", e.expression, e.message, e.args)

    try:
        raise TransitionError(2, 3*2, "Not Allowed!")
    # Exception value stored in e
    except TransitionError as e:
        print("Exception occurred :", e.message)

    try:
        raise NetworkError("Error")
    except NetworkError as e:
        print("Args:", e.args)

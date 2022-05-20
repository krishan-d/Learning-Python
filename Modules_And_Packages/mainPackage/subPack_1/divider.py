# Intra-package Reference :
# Use leading dots to indicate the current and parent packages involved in the relative import.
from . import adder
from ..subPack_0 import reverse


def divide(a=1, b=1):
    try:
        return a / b
    except ZeroDivisionError as e:
        return "Exception Raised", str(e)


if __name__ == '__main__':
    adder.add(4, 8)
    # Packages.mainPackage.subPack_0.echo.echo()
    reverse.rev()
    d = divide(4, 2)
    print(d)

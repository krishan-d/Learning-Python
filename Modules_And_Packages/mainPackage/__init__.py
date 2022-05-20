"""
__init__.py:
"""
# The Python interpreter recognizes a folder as the package if it contains __init__.py file.
# __init__.py exposes specified resources from its modules to be imported.
# Empty __init__.py file makes all functions from the above modules available when this package is imported.


# __all__:
# it is taken to be the list of module names that should be imported when from package import * is encountered.


# Specified Modules:
"""
from .subPack_0 import echo, reverse
from .subPack_1.divider import divide as div
__all__ = ["echo", "reverse", "div"]
"""

# when __all__ is defined in corresponding sub package's __init__.py:
"""
from .subPack_0 import *
from .subPack_1 import *
"""

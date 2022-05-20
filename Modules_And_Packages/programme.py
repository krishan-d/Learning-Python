"""
Importing Package:
Syntax: import package_name.module_name.submodule_name:
"""

# Normal import:
from mainPackage.subPack_0 import echo, reverse
from mainPackage.subPack_1 import divider as div
from mainPackage.some_main_script import report_main

# Importing * From a Package:
# __all__ is defined For subPack_0 and subPack_1 in __init__.py

# from mainPackage import *


"""
import mPackage.subPack_0.echo
mPackage.subPack_0.echo.echo()

from mPackage.subPack_0 import echo
echo.echo()

from mPackage.subPack_0.echo import echo
echo()
"""


def main():
    report_main()

    echo.echo()
    reverse.rev()
    res = div.divide(10, 4)
    print(res)


if __name__ == '__main__':
    main()

# NOTE:
# Intra-package Reference: Look into divider.py

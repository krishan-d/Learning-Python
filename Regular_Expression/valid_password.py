"""
Validating password using regular expression
"""

import re


def valid_pass(password):

    pass_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    pattern_obj = re.compile(pass_regex)
    res = pattern_obj.search(password)

    print("Valid password.") if res else print("Invalid!")


if __name__ == '__main__':
    valid_pass("Hey0#H!pi7")
    valid_pass("0000")

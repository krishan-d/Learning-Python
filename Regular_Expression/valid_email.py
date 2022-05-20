"""
Validating email using regular expression
"""

import verbose as vb
# Importing email regular expression


def validate_email(email_id):

    regex_email = vb.gex_email
    res = regex_email.fullmatch(email_id)
    if res is not None:
        print("{} is valid email id.".format(email_id))
    else:
        print("Invalid email id!")


if __name__ == '__main__':
    validate_email("iameve00@gmail.com")
    validate_email("iam#@outlook.com")

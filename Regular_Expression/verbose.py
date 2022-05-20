"""
Verbose:
"""

# re.compile(Regular Expression, re.VERBOSE).
# re.compile() returns a RegexObject which is then matched with the given string.


# Example:
import re

email_regex = re.compile(r'^([a-z0-9_\.-]+)@([a-z0-9_.-]+)\.([a-z]{2,6})$')

# Using VERBOSE:
gex_email = re.compile(r"""
                       ^([a-z0-9_\.-]+)  # Local part
                       @                 # @
                       ([a-z0-9_\.-]+)   # Domain part
                       \.                # dot
                       ([a-z]{2,6})$     # Top level domain
                       """, flags=re.VERBOSE | re.IGNORECASE)


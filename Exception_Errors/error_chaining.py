# raise RuntimeError from exc
""""""
"""
try:
    raise ConnectionError
except ConnectionError as exc:
    raise RuntimeError('Failed to open DB') from exc
"""

"""
Exception chaining happens automatically when an exception is raised inside an except or finally section.
This can be disabled by using from None idiom:
"""

try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None

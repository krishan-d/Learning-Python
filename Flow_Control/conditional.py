
"""
if condition0:
    # something here
elif condition1:
    # something here
else:
    # something here
"""

# chained conditional:

# and : two conditions are true
# or : one of two conditions is true
# not : entire condition is false


# match:
def http_error(status):
    match status:
        case 400: return "Bad request"
        case 404: return "Not found"
        case 401 | 403: return "Not allowed"
        case _:  # 'variable name' _ acts as a wildcard and never fails to match
            return "Something's wrong with the internet!"

if __name__ == '__main__':
    print(http_error(444))

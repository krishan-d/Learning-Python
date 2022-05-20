# String:
# Sequence of characters
# Immutable(unchangeable) : can not be changed once assigned!

# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
# encoding : sys.getdefaultencoding()
# errors : 'strict'


# Creation...
from datetime import datetime

i_string = 'Hi Eve!'
print(i_string)
i_string = "Hi Noah!"
print(i_string)
i_string = '''Hi There!'''
print(i_string)
i_string = """Hi, You seem to have no 
desires whatsoever!"""
print(i_string)

# Accessing...
string = "Hi Edwina!"
print("string:", string)
print("string[0]:", string[0])
print("string[1:5]:", string[1:5])
print("string[::-1]:", string[::-1])
# print("string[10]:", string[10])  # IndexError: string index out of range

# changing...
# INVALID OPERATIONS:
# string[2] = 'i'  # TypeError
# del string[2]  # TypeError

# Operations...
# Concatenation...
str1, str2 = "Hi", "There!"
print("str1 + str2:", str1 + str2)

# Membership...
print("H" in "Hey!")

# Iteration...
count = 0
for i in "Edwina": count += 1
print(count)

# Formatting...
# Escape sequence:
print('''I'm Evina''')
string = 'I\'m "Eve"'  # or "I'm \"Eve\""
print(string)

# \n	Backslash and newline ignored
# \\	Backslash
# \'	Single quote
# \"	Double quote
# \a	ASCII Bell
# \b	ASCII Backspace
# \r	ASCII Carriage Return
# \t	ASCII Horizontal Tab
# \v	ASCII Vertical Tab
# \ooo	Character with octal value ooo
# \xHH	Character with hexadecimal value HH

print("This is \x48\x45\x58 representation")

# Raw string to ignore escape sequence:
print("This is \x49")
row_string = r"This is \x49"
print("Row string:", row_string)

# Format method:
custom_string = "String formatting"
print(f"{custom_string} is a powerful technique")

# S.format(*args, **kwargs) -> str:
# Return a formatted version of S, using substitutions from args and kwargs.
# The substitutions are identified by braces ('{' and '}').

# default (implicit) order:
print("Hi {} and {}!".format("Eve", "Edwina"))

# Positional argument:
print("Hi {1} and {0}!".format("Eve", "Edwina"))

# Keyword argument:
print("Hi {ed} and {e}!".format(e="Eve", ed="Edwina"))

# Formatting specifiers:
print("{0:.2f}% of the {1} produced worldwide is {2}!".format(0.5155675, "data", "analyzed"))

# Formatting datetime:
print("Now:", datetime.now())
print("Today's date is {:%Y-%m-%d %H:%M}".format(datetime.now()))

# Formatting Integers, Floats:
print("Binary representation of {0} is : {0:b}".format(16))
print("Exponent representation of 165.6458 is : {0:e}".format(165.6458))
print("Rounding-off 1/6 : {0:.2f}".format(1/6))

# String alignment:
print("|{:<10}|{:^10}|{:>10}|".format('I', 'and', 'Cherry'))
print("{0:^10} in {1:<4}!".format('Born', 2000))

# S.format_map(mapping) -> str
sMap = {'name': 'Eve', 'msg': 10}
print("format_map :", "{name} has {msg} new message!".format_map(sMap))

x = 12.34567
print("x is %3.2f" % x)

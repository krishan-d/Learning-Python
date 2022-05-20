"""
Variables:
"""

# Maximum possible value of Integer:
# value of an integer is not restricted by the number of bits and can expand to the limit of the available memory.


# Packing and Unpacking Arguments:
# * For Tuples,
# ** For Dictionary


# Type conversion:
# 1. Implicit: Interpreter converts one to another data type without user involvement.
x, y = 10, 2.7
x = x + y
print(type(x))  # float

# 2. Explicit:
# int(a, base):
# float():
b = '10010'
print("To Integer, base 2 :", int(b, 2))
print("To Float :", float(b))

# ord() : To convert a character to integer.
# hex() : To convert integer to hexadecimal string.
# oct() : To convert integer to octal string.
c = '4'
print("To Integer :", ord(c))
print("To Hexadecimal :", hex(52))
print("To Octal :", oct(52))

# tuple() : To convert to a tuple.
# set() : This function returns the type after converting to set.
# list() : To convert any data type to a list type.

s = "Evinaa"
print("To Tuple :", tuple(s))
print("To Set :", set(s))
print("To List :", list(s))

# dict() : To convert a tuple of order (key,value) into a dictionary.
# str() : Used to convert integer into a string.
# complex(real, imag) : This function converts real numbers to complex(real, imag) number.

a, b = 1, 2
iTup = (('E', 1), ('v', 2), ('e', 3))
print("To Complex :", complex(a, b))
print("To String :", str(a))
print("To Dictionary :", dict(iTup))

# chr(number): To convert number to its corresponding ASCII character.
print("To Char :", chr(70))

# Byte Object/ String

# Encoding: String To Byte
# Encoding Forms : PNG, JPEG, MP3, WAV, ASCII, UTF-8
# Encoding is a format to represent audio, image, text in bytes.
en = "Eve".encode(encoding='ASCII')
print("Encoding :", en)

# Decoding: Byte To String
# decode()
print("Decoding :", en.decode())

# __name__ variable:
# __name__ is a built-in variable which evaluates to the name of the current module.
# If the source file is executed as the main program,
# the interpreter sets the __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set to the module’s name.

print("This File __name__ = %s" % __name__)
if __name__ == '__main__':
    print("File is being run directly.")

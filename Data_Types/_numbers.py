"""
Numbers:
"""
import decimal
import fractions

# Number System	Prefix
# Binary	'0b' or '0B'
# Octal	    '0o' or '0O'
# Hexadecimal	'0x' or '0X'

# Hexadecimal:
print(hex(512))
print(hex(12))
print(0xFB)  # 251

# Octal
print(oct(32))  # 0o40
print(0o15)  # 13

# Binary:
print(bin(128))
print(bin(107))
print(0b1000000)  # 64

# Exponential:
print(2**4)
print(pow(2, 4))  # x^y
print(pow(2, 4, 3))  # (x^y)%z

# Absolute Value:
print(abs(-3))
print(abs(2))

# Round:
print(round(3.9))
print(round(395, -2))
print(round(3.141592, 2))

# Type conversion:
print(1 + 2.0)  # 3.0
print(int(-3.14))
print(float(5))
print(complex('3+4j'))

# Python Decimal:
print((1.1 + 2.2) == 3.3)  # False
print(0.1)
print(decimal.Decimal(0.1))

# Use in financial applications that need exact decimal representation.
# When we want to control level of precision required.
# when we want to implement the notation of significant decimal places.

# Python Fractions:
print(fractions.Fraction(1.5))
print(fractions.Fraction(5))
print(fractions.Fraction(1, 3))

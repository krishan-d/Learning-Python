"""
Math module:
"""

import math as m

# Mathematics Constants:
print(m.pi)
print(m.e)
print(m.tau)
print(m.inf, "|", float('inf'))
print(m.nan, "|", float('nan'))

# Rounding Numbers:
num = 4.354
print("Floor:", m.floor(num))
print("Ceil:", m.ceil(num))
print("Round:", round(num))


# Number Theoretic and Representation:
# math.comb(n, k):
# Return the number of ways to choose k items from n items without repetition and without order.
# Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates to zero when k > n.
print("Combination:", m.comb(5, 4))

# math.copysign(x, y)
# Return a float with the magnitude (absolute value) of x but the sign of y.
print("Copy sign:", m.copysign(1.0, -0.0))

# math.fabs(x)
# Return the absolute value of x.
print("Absolute value:", m.fabs(3))

# math.factorial(x)
# Return x factorial as an integer. Raises ValueError if x is not integral or is negative.
print("Factorial:", m.factorial(4))

# math.fmod(x, y)
print("F mod:", m.fmod(10.0, 3.0), "|", 10 % 3)

# math.fsum(iterable)
print("sum:", sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print("F sum:", m.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))

# math.frexp(x)
# Return the mantissa and exponent of x as the pair (m, e).
# m is a float and e is an integer such that x == m * 2**e exactly.
# If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m) < 1.
print(m.frexp(0))
print(m.frexp(4), "|", 0.5 * (2 ** 3))

# math.gcd(*integers)
# Return the greatest common divisor of the specified integer arguments.
print("GCD 0:", m.gcd(0))
print("GCD:", m.gcd(2, 4, 6, 8))

# math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
# Return True if the values a and b are close to each other and False otherwise.

# math.isfinite(x)¶
# Return True if x is neither an infinity nor a NaN, and False otherwise
num = 0.0
print("Is Number-({}) Finite:".format(num), m.isfinite(num))

# math.isinf(x)
# Return True if x is a positive or negative infinity, and False otherwise.

# math.isnan(x)
# Return True if x is a NaN (not a number), and False otherwise.

# math.isqrt(n)
# Return the integer square root of the non-negative integer n.
# This is the floor of the exact square root of n, or equivalently the greatest integer a such that a² ≤ n.
# computed using a = 1 + isqrt(n - 1).
x = 16
a = m.isqrt(x)
print("Integer square root:", a, "||", 1 + m.isqrt(16 - 1))

# math.lcm(*integers)
# Return the least common multiple of the specified integer arguments.
print("LCM:", m.lcm(5, 3))

# math.ldexp(x, i)
# Return x * (2**i). This is essentially the inverse of function frexp().

# math.modf(x)
# Return the fractional and integer parts of x. Both results carry the sign of x and are floats.

# math.perm(n, k=None)
# Return the number of ways to choose k items from n items without repetition and with order.
# Evaluates to n! / (n - k)! when k <= n and evaluates to zero when k > n.
print("Permutation:", m.perm(4, 2))

# math.prod(iterable, *, start=1)
# Calculate the product of all the elements in the input iterable.

# math.remainder(x, y)
print("Remainder:", m.remainder(10, 3))

# math.trunc(x)
# Return the Real value x truncated to an Integral (usually an integer).

# math.ulp(x)
# Return the value of the least significant bit of the float x:
print(m.ulp(1))
print(m.ulp(-1))


# Power and Logarithmic Values:
# math.exp(x)
# Return e raised to the power x, where e = 2.718281… is the base of natural logarithms.

# math.expm1(x)
# Return e raised to the power x, minus 1.
print("exp:", m.expm1(1e-5))
print("exp:", m.expm1(1))

# math.log(x, [base=math.e])
# Calculated as : log(x) / log(base).
print("Log:", m.log(m.e))
# print("", m.log(0))  # Raise Error

# math.log1p(x)
# Return the natural logarithm of 1+x (base e). The result is calculated in a way which is accurate for x near zero.

# math.log2(x)
# base-2 . more accurate than log(x, 2).

# math.log10(x)
# base-10 . more accurate than log(x, 10).

# math.sqrt(x)
# Return the square root of x.
print("Square root:", m.sqrt(144))

# math.pow(x, y)
# Return x raised to the power y.


# Trigonometric Functions:
# math.cos(x)
# Return the cosine of x radians.

# math.sin(x)
# Return the sine of x radians.
print("sin:", m.sin(10))

# math.tan(x)
# Return the tangent of x radians.

# math.acos(x)¶
# Return the arc cosine of x, in radians. The result is between 0 and pi.

# math.asin(x)
# Return the arc sine of x, in radians. The result is between -pi/2 and pi/2.

# math.atan(x)
# Return the arc tangent of x, in radians. The result is between -pi/2 and pi/2.


# math.dist(p, q)
# Return the Euclidean distance between two points p and q, each given as a sequence (or iterable) of coordinates.
# The two points must have the same dimension.

p = [1, 1, 0]
q = [0, 0, 0]
print("Distance B/w Tow Points:", m.sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q))))


# Angular conversion:
# math.degrees(x)
# Convert angle x from radians to degrees.
print("Radian(pi/2) To Degree:", m.degrees(m.pi/2))

# math.radians(x)
# Convert angle x from degrees to radians.
print("Degree To Radian:", m.radians(180))


# Special Functions:
# math.gamma(x)
# Return the Gamma function at x.

# math.lgamma(x)
# Return the natural logarithm of the absolute value of the Gamma function at x.

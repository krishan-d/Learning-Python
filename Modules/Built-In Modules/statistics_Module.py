"""
statistics module:
"""

import statistics as s
from decimal import Decimal as d

# statistics.mean(data)
# arithmetic mean(Average) of data which can be a sequence or iterable.
# If data is empty, StatisticsError will be raised.
# print(s.mean())  # raise StatisticsError
print("Mean :", s.mean([-1.0, 2, 3.25, 4.75]))
print("Mean :", s.mean([d("0.5"), d("0.75"), d("0.625")]))

# statistics.fmean(data)
# Fast, Convert data to floats and compute the arithmetic mean.
print("Float Mean :", s.fmean([3.5, 4.0, 5.25]))

# statistics.geometric_mean(data)
# Convert data to floats and compute the geometric mean.
# The geometric mean indicates the central tendency or typical value of the data using the product of the values
# (as opposed to the arithmetic mean which uses their sum).
# Raises a StatisticsError if the input dataset is empty, if it contains a zero, or if it contains a negative value.
print(round(s.geometric_mean([54, 24, 36]), 1))

# statistics.harmonic_mean(data, weights=None)
# Return the harmonic mean of data, a sequence or iterable of real-valued numbers.
# If weights is omitted or None, then equal weighting is assumed.
# The harmonic mean is the reciprocal of the arithmetic mean() of the reciprocals of the data.
# For example, the harmonic mean of three values a, b and c will be equivalent to 3/(1/a + 1/b + 1/c).
# If one of the values is zero, the result will be zero.
# appropriate when averaging ratios or rates, for example speeds.

# Example :
# Suppose a car travels 40 km/hr for 5 km, and when traffic clears, speeds-up to 60 km/hr for the
# remaining 30 km of the journey. What is the average speed?
print("Harmonic mean :", s.harmonic_mean([40, 60], weights=[5, 30]))

# statistics.median(data):
# Return the median (middle value) of numeric data, using the common “mean of middle two” method.
print("Median :", s.median([1, 3, 5]))
print("Median :", s.median([1, 3, 5, 7]))

# statistics.median_low(data)
# Return the low median of numeric data
print("Median Low :", s.median_low([1, 3, 5]))
print("Median Low :", s.median_low([1, 4, 5, 7]))

# statistics.median_high(data)
# Return the high median of data
print("Median High :", s.median_high([1, 3, 5]))
print("Median High :", s.median_high([1, 4, 5, 7]))

# statistics.mode(data)
# Return the single most common data point from discrete or nominal data.
# The mode (when it exists) is the most typical value and serves as a measure of central location.
print("Mode :", s.mode([1, 1, 2, 3, 3, 3, 3, 4]))

# statistics.multimode(data)
# Return a list of the most frequently occurring values in the order they were first encountered in the data.
# Will return more than one result if there are multiple modes or an empty list if the data is empty:
print("Multi-mode :", s.multimode(''))

# Measure of spread:
# statistics.pstdev(data, mu=None)
# Return the population standard deviation (the square root of the population variance).
# See pvariance() for arguments and other details.
print(s.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# statistics.pvariance(data, mu=None)
# Return the population variance of data, a non-empty sequence or iterable of real-valued numbers.

# NOTE:
# Variance, or second moment about the mean, is a measure of the variability (spread or dispersion) of data.
# Large variance means, data is spread out; Small variance indicates data, is clustered closely around the mean.
data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]
print("Population variance :", s.pvariance(data))
mu = s.mean(data)
print(s.pvariance(data, mu))  # avoid recalculation of arithmetic mean

# statistics.stdev(data, xbar=None)
# Return the sample standard deviation (the square root of the sample variance).
print("Standard deviation :", s.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75]))

# statistics.variance(data, xbar=None)
# Return the sample variance of data, an iterable of at least two real-valued numbers.
# xbar : mean of data. If it is missing or None, the mean is automatically calculated.
print("Variance :", s.variance(data, s.mean(data)))

# Statistics for relations between two inputs:
# statistics.covariance(x, y, /)
# Return the sample covariance of two inputs x and y. Covariance is a measure of the joint variability of two inputs.
# Both inputs must be of the same length (no less than two), otherwise StatisticsError is raised.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("Covariance :", s.covariance(x, y))

# statistics.correlation(x, y, /)
# Return the Pearson’s correlation coefficient(r) for two inputs.
# -1.0 <= r <= 1.0
# Measures : strength and direction of the linear relationship,
# +1 : very strong, +ve linear relationship
# -1 : very strong, -ve linear relationship, and 0 no linear relationship.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Correlation :", s.correlation(x, x))

# statistics.linear_regression(x, y, /)¶
# Return the slope and intercept of simple linear regression parameters estimated using ordinary least squares.
# Simple linear regression describes the relationship between an independent variable x and
# a dependent variable y in terms of this linear function:
# y = slope * x + intercept + noise
year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]
slope, intercept = s.linear_regression(year, films_total)
print(round(slope * 2022 + intercept))

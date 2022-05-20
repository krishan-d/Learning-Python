"""
random module:
"""

import random as r
from statistics import fmean as mean

# Real-valued Distributions:
# random.random()
# Return the next random floating point number in the range [0.0, 1.0).
a = r.random()  # Random float : 0.0 <= < 1.0
print("Random Floating Number:", a)

# Random Distribution: Uniform Distribution::
# random.uniform(a, b)
# Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a.
print("Uniform Distribution:", r.uniform(2.5, 10.0))  # Random float:  2.5 <= x <= 10.0

# Normal/Gaussian Distribution:
print("Normal/Gaussian Distribution:", r.gauss(mu=0, sigma=1))

# random.expovariate(lambd):
# Exponential distribution. lambd is 1.0 divided by the desired mean. It should be nonzero.
# if lambd +ve: 0 to positive infinity , else if lambd is -ve: 0 to negative infinity.
print("Exponential distribution:", r.expovariate(1 / 5))  # Interval between arrivals averaging 5 seconds

# Function For Bytes:
# random.randbytes(n)
# Generate n random bytes.
print("Random Bytes:", r.randbytes(4))

# Function For integers:
# random.randrange(stop)
# random.randrange(start, stop[, step])
print(r.randrange(10))  # Integer from 0 to 9 inclusive
print("random In Range:", r.randrange(1, 10, 2))  # Even integer from 0 to 9

# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
print("Random Integer:", r.randint(1, 100))
r.seed(10)  # value 10 is completely arbitrary, you can pass any number you want.
print(r.randint(0, 100))  # Now, This will return same number always.

# random.getrandbits(k)
# Returns a non-negative Python integer with k random bits.
# print(r.getrandbits(4))

# Functions For sequences:
# random.choice(seq):
# An empty sequence as argument raises an IndexError.
nList = list(range(0, 20))
print("Random choice:", r.choice(nList))
print("Random choice:", r.choice((32, 40, 38, 26)))

# Sample with Replacement:
# random.choices(population, weights=None, *, cum_weights=None, k=1)
# Return a k sized list of population elements chosen with replacement.
# If neither weights nor cum_weights are specified, selections are made with equal probability.
# It is a TypeError to specify both weights and cum_weights.
print("Random choices:", r.choices(population=nList, k=10))
# Six roulette wheel spins (weighted sampling with replacement)
print("Random choices:", r.choices(['red', 'black', 'green'], [18, 18, 2], k=6))

# Sample without Replacement:
# random.sample(population, k, *, counts=None)
# Return a k length list of unique elements chosen from the population sequence or set.
# Used for random sampling without replacement.
# Members of the population need not be hashable or unique
print("Sample:", r.sample([10, 20, 30, 40], k=3))  # Three samples without replacement

dealt = r.sample(['Tens', 'Low cards'], counts=[16, 36], k=20)
print(dealt.count('Tens') / 20)

# random.shuffle(x, random=None):
# Shuffle the sequence x in place.
# The optional argument random is a 0-argument function returning a random float in [0.0, 1.0);
# by default, this is the function random().
# To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.
r.shuffle(nList)
print("Shuffle:", nList)


# Alternative Generator:
# class random.Random([seed])
# Class that implements the default pseudo-random number generator used by the random module.

# class random.SystemRandom([seed])
# Class that uses the os.urandom() function for generating random numbers from sources provided by the operating system.


# Examples:
# Estimate the probability of getting 5 or more heads from 7 spins
# of a biased coin that settles on heads 60% of the time.
def trial():
    return r.choices('HT', cum_weights=(0.60, 1.00), k=7).count('H') >= 5


print(sum(trial() for i in range(10000)) / 10000)


# Probability of the median of 5 samples being in middle two quartiles
def trial():
    return 2_500 <= sorted(r.choices(range(10_000), k=5))[2] < 7_500


print(sum(trial() for _ in range(10_000)) / 10_000)

# Example statistics bootstrapping:
# using resampling with replacement to estimate a confidence interval for the mean of a sample:
data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
means = sorted(mean(r.choices(data, k=len(data))) for _ in range(100))
print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
      f'interval from {means[5]:.1f} to {means[94]:.1f}')

# resampling permutation test to determine the statistical significance or p-value of an observed difference between
# the effects of a drug versus a placebo:
drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
observed_diff = mean(drug) - mean(placebo)
print(observed_diff)

n = 10_000
count = 0
combined = drug + placebo
for i in range(n):
    r.shuffle(combined)
    new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
    count += (new_diff >= observed_diff)

print(f'{n} label re-shuffling produced only {count} instances with a difference')
print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
print(f'hypothesis that there is no difference between the drug and the placebo.')

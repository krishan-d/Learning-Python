# Generators:
# Generator Function: Returns generator object/Iterator
# Function contains at least one yield (may contain other yield or return).
# Difference-> return : terminates a function entirely,
# yield : pauses the function saving all its states and later continues from there on successive calls.

# Generator Function vs Function:
# contains one or more yield.
# when called, returns an object(iterator) but doesn't start execution immediately.
# __next__() and __iter__() are implemented automatically, we can iterate through the items using next().
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# When the function terminates, StopIteration is raised automatically on further calls.

# Note: range() is itself a generator.
def generatorFunc(num=0):  # generator function
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a + b


# generator object:
gen_ob = generatorFunc(2)
print("Generator object: ", gen_ob)
# Iterating over generator object using __next__().
print(gen_ob.__next__())
print(next(gen_ob))
print(next(gen_ob))
# print(next(gen_ob))  # Raise StopIteration Error

# Iterating over generator object...
for i in generatorFunc(6):
    print("\t", i)

# Converting generator To List:
print("\nGenerator To List: ", list(generatorFunc(2)))

# Generator Expression...
# creates anonymous generator functions.
# List comprehension produce entire List while generator comprehension produce one item at a time.
# Lazy execution( producing item only when asked for). For this generator is more memory efficient than List.

gen_exp = (n ** 2 for n in range(4))
print('\nGenerator Expression: ')
for i in gen_exp:
    print(i, end=' ')
print('\r\n')

# Convert String into Generator:
s = 'Hi There!'
s_iter = iter(s)
print(s_iter.__next__())
print(next(s_iter))


# Use...
# Easy to implement: as compared to their iterator class counterpart.
def reverse_gen(string):
    for m in string[::-1]: yield m


for char in reverse_gen("Hey!"):
    print("\t", char)


# Memory efficient:
# Represent infinite stream:
def every_even():
    n = 0
    while True:
        yield n
        n += 2


# Pipelining generators:
def fibonacci_nums(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x + y
        yield x


def square(nums):
    for num in nums:
        yield num ** 2


print(sum(square(fibonacci_nums(10))))

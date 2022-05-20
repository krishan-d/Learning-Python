"""
Iterator """

# Iterators are objects that can be iterated upon.
# Implemented within For Loops, comprehensions, generators etc.

# __iter__() and __next__()[Iterator object]:
# __iter__() method to return an iterator object of the class.
# The iterator object then uses the __next__() method to get the next item.
# StopIteration Exception is raised when there is no more data to be returned.

x = [4, 7, 0]
my_iter = iter(x)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
# print(my_iter.__next__())  # raise StopIteration/ No item remaining

# Loops for iterators...
while True:
    try:
        e = next(my_iter)
    except StopIteration:
        break


# Custom Iterator (Named Reverse)...
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


def Main():
    rev = Reverse('Iterator')
    for char in rev:
        print("\t", char)

    # using iter() on class object
    r = Reverse("No")
    i = iter(r)
    print(i.__next__())
    print(next(i))
    # print(next(i))  # raise StopIteration


# Infinite Iterators...
print("\nint():", int())  # 0

inf = iter(int, 1)
print(next(inf))
print(next(inf))


class InfIter:
    """Infinite iterator to return all add numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num


if __name__ == '__main__':
    Main()

    a = iter(InfIter())
    print("\nOdds:", next(a))
    print(next(a))
    print(next(a))
    print(next(a))

"""
Object printing
"""


class Base:
    def __init__(self, a, v):
        self.a = a
        self.b = v

    # Both __str__() And __repr__()
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)

    def __str__(self):
        return "From str method of Base: a is %s," \
               "b is %s" % (self.a, self.b)


b = Base(1234, 5678)
print(b)  # __str__() # From str method of Base: a is 1234,b is 5678
print([b])  # __repr__()  # [Test a:1000 b:2000]

"""
class Base:
    def __init__(self, a, v):
        self.a = a
        self.b = v

    # __repr__()
    def __repr__(self):
        return "Test a:%s b:%s" % (self.a, self.b)


c = Base(1000, 2000)
print(c)  # __repr__() # Test a:1000 b:2000
"""

# When no __str__() And __repr__() used
# print(c)  # <__main__.Base object at 0x0000013BF1A3D960>

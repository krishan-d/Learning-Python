# Python @property decorator:
# A pythonic way to use getters and setters in object-oriented programming.

# class without getters and setters:
class Celsius:
    def __int__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32


human = Celsius()
human.temperature = 37
print(human.temperature)
print(human.to_fahrenheit())

print(human.__dict__)
print(human.__dict__['temperature'])


# Using getters and setters:
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = None
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return self.get_temperature() * 1.8 + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15: raise ValueError("Temperature below -273.15 ain't possible!")
        self._temperature = value


man = Celsius(37)
print(man.get_temperature())
# man.set_temperature(-300)  # raise ValueError
print(man.to_fahrenheit())

# Note: private variables doesn't really exist in python.
man._temperature = -300
print(man.get_temperature())

# Problem with the above update is that all programs that implemented previous class have to modify their code from
# obj.temperature to obj.get_temperature() and obj.temperature = val to obj.set_temperature(val).
# This refracting can cause issues.


# Property class:
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature  # This calls [set_temperature()] automatically.

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    def get_temperature(self):
        print("getting value...")
        return self._temperature

    def set_temperature(self, value):
        print("setting value...")
        if value < -273.15: raise ValueError("Temperature below -273.15 ain't possible!")
        self._temperature = value

    # creating property object
    temperature = property(get_temperature, set_temperature)

    # temperature = property()  # Empty property
    # temperature = temperature.getter(get_temperature)


h = Celsius(37)  # [set_temperature() is called] here
print(h.temperature)
print(h.to_fahrenheit())
# h.temperature = -300  # raise ValueError

# Note: Any code that retrieves the value of [temperature] will automatically call [get_temperature()]
# instead of a dictionary [__dict__]. similarly, any code that assigns a value to [temperature] will automatically
# call [set_temperature()].

# Note: actual temperature value is stored in private [_temperature] variable. The [temperature] attribute is a
# property object which provides an interface to this private variable.

# @property decorator...
# [property()] is an in-built function that creates and returns a [property] object.
# Syntax: property(fget=None, fset=None, fdel=None, doc=None)
# where:
# fget is function to get value of the attribute
# fset is function to set value of the attribute
# fdel is function to delete the attribute
# doc is a string (like a comment)


# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
# coldest_thing = Celsius(-300)  # raise valueError

"""
Polymorphism:
Simply means having many forms
"""


class Bird:
    @staticmethod
    def intro():
        print("Too many birds")

    def fly(self):
        print("Some can fly and rest can not.")


class Sparrow(Bird):
    def fly(self):  # Method overriding
        print("Sparrows can fly.")


class Ostrich:
    @staticmethod
    def fly():
        print("Ostriches can not fly.")


ob_b = Bird()
ob_s = Sparrow()
ob_o = Ostrich()

for ob in (ob_b, ob_s, ob_o):
    ob.fly()

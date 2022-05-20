
def scope_test():
    x = "Loc"

    def inner():
        nonlocal x
        x = "NonL"
        print("Inner :", x)

    print("Outer:", x)
    inner()
    print("Outer:", x)


def foo():
    global x
    y = "L"
    print(x)
    print(y)


# Global in Nested Function:
def someFun():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling:", x)
    bar()
    print("After calling:", x)

if __name__ == "__main__":
    x = 'G'
    foo()
    scope_test()
    print("In Global scope:", x)

    someFun()
    print("x in main:", x)

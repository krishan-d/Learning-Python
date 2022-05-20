try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print("Oops!", inst.__class__, "Occurred!")
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)

# Exception in File handling...
try:
    f = open("Non_ExistingFName")  # FileNotFoundError
    f.read()
except (IOError, FileNotFoundError) as e:
    print("Exception:", e)
finally:
    print("Exit!")

"""
try:
    f = open('Data_Folder/Non_ExistingFName')
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
"""


def divide(n):
    try:
        r = 1 / n
    except ZeroDivisionError as ex:
        print("Exception raised:", ex)
    # except Exception as err:
    #     raise ZeroDivisionError("Something bad happened!") from err
    else:
        print("Response :", r)
    finally:
        print("Exit!")


if __name__ == '__main__':
    divide(0)
    # divide("0")  # Clean-up action
    # Exception raised but no except to handle.

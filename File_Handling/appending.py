"""
Writing and Appending File:
"""

# write(s: AnyStr) -> int:
# writelines(lines: List[AnyStr]) -> None:


with open("Fi_Directory/F_2", "w+") as wrF:
    h = ["There!...\n", "Have more than you show, And speak\n", "Less than you know.  -WILLIAM SHAKESPEARE\n"]
    s = "Hey.."
    i = wrF.write(s)
    print(i)
    wrF.writelines(h)

with open("Fi_Directory/F_2", "r+") as opF:
    print(opF.read())
    print("Current position:", opF.tell())


# Appending:
with open("Fi_Directory/F_2", "a+") as apF:
    apF.write("Hi Edwina!\n")
    apF.writelines(["Provide revised data.\n", "Thanks\n"])


with open("Fi_Directory/F_2", "r+") as opF:
    print("Reading:")
    print(opF.read())
    print("File descriptor:", opF.fileno())

# Methods...
# tell()-> int:
# Returns an integer that represents the current position of the file's object.

# fileno()-> int:
# Returns an integer number (file descriptor) of the file.

# flush()-> None:
# Flushes the write buffer of the file stream.

# truncate(size: int = None)-> int:
# To change the size of a file, return passed size.

# os.remove(file) : delete file

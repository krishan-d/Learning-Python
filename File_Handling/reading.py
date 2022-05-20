"""
Reading File
"""

# read(n=-1) -> AnyStr:
# Returns the read bytes in form of a string. Reads n bytes. If no n specified, reads the entire file.

# readline(limit: int = -1) -> AnyStr:
# Read one line (From current pointer(cursor) position) and returns as string.

# readlines(hint: int = -1) -> List[AnyStr]
# Read all lines (From current cursor position) and return as each line a string element in List.
# n : Number of bytes to be read

print(len('\n'))  # -> 1
# '\n' : 1 byte character


# seek(self, offset: int, whence: int = 0) -> int:
# Parameters:
# offset : number of positions to move
# whence : It sets the reference point for the offset.
# 0 - beginning(Default value) / 1 - Current position / 2 - EOF

# NOTE:
# seek(-2,2) are not allowed if file mode does not include 'b'


with open("Fi_Directory/F_1", "w+") as newF:
    print("Is writeable:", newF.writable())
    h = ["Eve and Edwina!\n", "I never had \n", "changed.\n"]
    newF.write("Hi...\n")
    newF.writelines(h)


with open("Fi_Directory/F_1", "r+") as openF:
    print("Is readable:", openF.readable())
    print("Is seekable:", openF.seekable())

    print("read:", openF.read())
    openF.seek(0)
    print("read n:", openF.read(13))

    openF.seek(0)
    print("read Line:", openF.readline())
    print("read Line (n):", openF.readline(26))

    openF.seek(0)
    print("read Lines :", openF.readlines())

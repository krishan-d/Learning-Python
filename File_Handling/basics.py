"""
File handling basics
"""

# Opening a File:
# File_object = open(r"File_Name", "Access_Mode"):
# Access Mode:
# r : reading only / pointer -> beginning
# w : writing only / pointer -> beginning / Overwrites existing File and creates if not
# a : appending / pointer -> EOF / Creates if doesn't exist
# b : For binary mode // t : For Text mode
# x : For exclusive creating a new File
# + : For updating File

# with keyword:
# More optimal than using try…finally statement
# File gets closed as soon as the program exits the indentation of the with statement.

# io module : default module to access files, can be used without importing.
# open(filename, access_mode) : returns a file object called "handle".
# IOError exception : File operations fails.
# New line character (\n) : Default EOL terminator in text file.
# Binary File : return bytes / No EOL.
# arguments: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None).


# File creation using write():
import os

newFile = open("Fi_Directory/F_0", "w+")
newFile.write("File creation using write method!")
newFile.close()

# Opening and Reading File:
f = open("Fi_Directory/F_0")
print(f.read())  # Reading from File
f.close()  # Closing File

fileName = "Fi_Directory/Non_ExistingName"
if os.path.isfile(fileName):
    pass
else:
    print("File does not exist!")

# Exception Handling...
try:
    f = open("Fi_Directory/Non_ExistingName")  # FileNotFoundError without try-finally block
    f.read()
except IOError:
    print("File Not Found!")
finally:
    print("Exit")

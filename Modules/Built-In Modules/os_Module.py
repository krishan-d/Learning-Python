"""
os module:
"""

import os
import shutil
import pathlib
import send2trash


# Current working Directory(CWD):
cwd = os.getcwd()
print("cwd :", cwd)
print("path :", os.path)
print("cur-dir :", os.curdir)

# Listing Files and Directories:
# listdir(path: PathLike[str]) -> list[str]: ...
dirList = os.listdir()  # Same as os.listdir(os.getcwd())
print("List directory :", dirList)


def changeDir(path='.'):
    """
    chdir(path: _Fd|AnyPath) -> None: ...
    Change the current working directory to the specified path.
    """
    os.chdir(path)
    print("chdir . :", os.getcwd())
    os.chdir('../..')
    print("chdir .. :", os.getcwd())
    os.chdir('./Advance')
    print("chdir ./Advance :", os.getcwd())


def createDir(path):
    """
    mkdir(path: Str|BytesPath, mode: int = ..., *) -> None: ...

    makedirs(name, mode=0o777, exist_ok=False):
    makedirs(name: Str|BytesPath, mode: int = ..., exist_ok: bool = ...) -> None: ...

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like mkdir,
    -except that any intermediate path segment (not just the rightmost) will be created if it does not exist.
    If the target directory already exists, raise an OSError if exist_ok is False.
    Otherwise, no exception is raised.  This is recursive.
    """
    try:
        print("Path provided :", path)
        directory = os.path.dirname(path)
        print("directory :", directory)
        os.makedirs(directory)
        # os.mkdir(directory)  # May raise FileNotFoundError

    except FileExistsError as ee:
        print("Exception::Existing directory :", ee.filename)
        os.stat(directory)
    # except FileNotFoundError as e:
    #     os.makedirs(directory)
    except OSError:
        print(os.error)

    # os.makedirs(os.path.join(parent_dir, 'Person\\E\\F0'))
    # os.makedirs(os.path.join(parent_dir, 'Person\\E\\F1\\Test.txt'), exist_ok=True)


# Remove/Deleting Files:
"""
os module:
    os.remove(path):
    remove(path: StrO|BytesPath, *, dir_fd: int | None = ...) -> None: ...
    Remove a file path(same as unlink()). raise FileNotFoundError.
    Can not remove directory. If specified path is directory then OSError raised.
    
    os.rmdir(path: Str|BytesPath, *, dir_fd: int | None = ...) -> None: ...
    Removes an empty directory. otherwise, raise OSError, FileNotFoundError
    
    os.unlink(path): Remove a file (same as remove()).
shutil:
    shutil.rmtree():
    Removes a directory and all its contents.
pathlib.Path:
    pathlib.Path.unlink() : Removes a file or symbolic link.
    pathlib.Path.rmdir() : Removes an empty directory.

NOTE: These methods can not be reversed!

send2trash:
    Sends deleted files to the trash bin instead of permanent removal.
"""


def removeDir(dirPath, name=None):
    try:
        if name is not None:
            path = os.path.join(dirPath, name)
            print("path :", path)
            # if os.path.exists(path): os.remove(path)
            # os.remove(path)
            os.unlink(path)
        elif os.path.getsize(dirPath) != 0 and os.path.exists(dirPath):
            os.rmdir(dirPath)
    except FileNotFoundError as e:
        print("Exception:: {}-{}.".format(e.filename, e.strerror))


def removeDirF(path):
    # if os.path.isfile(path) or os.path.islink(path): os.remove(path)
    # elif os.path.isdir(path): shutil.rmtree(path)
    # else: raise ValueError("File {} is not a file or dir.".format(path))

    try:
        send2trash.send2trash(path)
    except Exception as e:
        print('Exception ::', e)


# Commonly used Functions:
print("os name :", os.name)

# os.error:
# All functions in this module raise OSError in the case of invalid or inaccessible file names and paths,
# or other arguments that have the correct type, but are not accepted by the operating system.
# try:
#     f_name = 'F.txt'
#     f = open(f_name, 'r+')
#     f.read()
#     os.close(f)
#
# except OSError:
#     print(os.error)
#     print("Problem reading :", f_name)


# os.popen():
# This method opens a pipe to or from command.
# The return value can be read or written depending on whether the mode is ‘r’ or ‘w’.
# print(os.getcwd())
# file_name = 'T_0.txt'
# f = os.popen(file_name, 'w')
# f.write("Mr. Eve")
# os.close(f)

# os.close():
# Close file descriptor fd.
# File opened using open(), can be closed by close()only.
# File opened through os.popen(), can be closed with close() or os.close()

# os.rename(src, dst) -> None ...
# os.remove(path: Str|BytesPath, *, dir_fd: int | None = ...) -> None: ...
# os.path.exists(path: Str|BytesPath) -> bool: ...
# os.path.getsize(filename: Str|BytesPath) -> int: ..
# Return size of the file in bytes.


# Moving Files:
# shutil.move("", "")
# print(os.listdir())

# Walking through directory:
def dirTraverse():
    for folder, sub_folders, files in os.walk(os.getcwd()):
        print("Directory :", folder)
        print("\nS_Fs :")
        for i in sub_folders: print('\tS_F :', i)

        print("\nFs :")
        for i in files: print('\tF :', i)
        print('\n')


def main():
    print(os.getcwd())
    os.chdir('../../Data_Folder')
    print(os.getcwd())

    CURRENT_DIRECTORY = os.getcwd()
    
    dir_path = os.path.join(CURRENT_DIRECTORY, 'Person/FF/TT/T.txt')
    createDir(dir_path)
    os.makedirs(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1\\Test.txt'), exist_ok=True)
    # os.mkdir(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1\\Test1.txt'))
    # os.mkdir(os.path.join(CURRENT_DIRECTORY, 'PersonE/F1/Test2.txt'))
    createDir(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1\\Test3.txt'))

    removeDir(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1'), 'WRONG FILE NAME.txt')

    removeDirF(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1\\Test3.txt'))
    removeDirF(os.path.join(CURRENT_DIRECTORY, 'Person\\E\\F1\\WRONG FILE NAME.txt'))


if __name__ == '__main__':
    main()
    # filename = '../Advance/Person/E/F0'
    # print("getsize :", os.path.getsize(filename))

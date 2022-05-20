def remove_all_but_alphabets(string):
    sChar = [c for c in string if
             ord(c) in range(ord('a'), ord('z') + 1, 1) or ord(c) in range(ord('A'), ord('Z') + 1, 1)]
    return ''.join(sChar)


if __name__ == '__main__':
    print(remove_all_but_alphabets("#E^..v!e*_"))  # Eve


import re

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        s = input()
        try:
            re.compile(s)
        except re.error:
            print("Non valid regex pattern")
    exit()

    # Input: 2
    # .*\+
    # .*+

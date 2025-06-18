#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    s = len(argv)
    if s == 0:
        print("{} arguments.".format(s))
    elif s == 1:
        print("{} argument:".format(s))
    else:
        print("{} arguments:".format(s))
    for i in range(s):
        print(f"{i+1}: {argv[i]}")

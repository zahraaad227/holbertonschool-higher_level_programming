#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            if i != 8 or j != 9:
                print("{:01d}{:01d}, ".format(i,j), end="")
            else:
                print("{:01d}{:01d}".format(i,j))

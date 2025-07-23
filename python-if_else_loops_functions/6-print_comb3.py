#!/usr/bin/python3
for i in range(0,10):
    for j in range(0,10):
        m=str(i)
        n=str(j)
        if i<j:
            k=m+n
            if k!="89":
                print(k, end=" , ")
            else:
                print(k)

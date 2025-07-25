#!/usr/bin/python3
i=0
while i < len(list_result):
    if my_list[i] % 2 == 0:
        print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i=i+1    

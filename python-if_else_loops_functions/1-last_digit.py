#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    if number > 0:
        print("Last digit of", number, "is", ld, "and is greater than 5")
    else:
        print("Last digit of", number, "is", (-1)*ld, "and is less than 6 and not 0")
elif ld == 0:
    print("Last digit of", number, "is", ld, "and is 0")
else:
    if number > 0:
        print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
    else:
        print("Last digit of", number, "is", (-1)*ld, "and is less than 6 and not 0")

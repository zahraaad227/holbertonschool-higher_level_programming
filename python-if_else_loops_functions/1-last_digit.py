#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = number
ld = abs(number) % 10

if ld > 5:
    if number > 0:
        print(f"Last digit of {n} is {ld} and is greater than 5")
    else:
        # Burada f-string ilə çap etmək lazımdır, indi isə düzəltdim
        print(f"Last digit of {number} is {-ld} and is less than 6 and not 0")
elif ld == 0:
    print(f"Last digit of {n} is {ld} and is 0")
else:
    if number > 0:
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {-ld} and is less than 6 and not 0")

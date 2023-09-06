#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = str(number)[-1]
if number < 0:
    digit = f"-{digit}"
digit = int(digit)
if digit > 5:
    result = "and is greater than 5"
elif digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"
print(f"Last digit of {number} is {digit} {result}")

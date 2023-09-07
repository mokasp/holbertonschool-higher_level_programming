#!/usr/bin/python3
for digitOne in range(10):
    for digitTwo in range(10):
        if digitOne != 8:
            if digitOne != digitTwo and digitOne < digitTwo:
                print("{}{}".format(digitOne, digitTwo), end=", ")
print(89)

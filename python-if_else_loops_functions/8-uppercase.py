#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = ord(str[i])
        if letter >= 97 and letter <= 122:
            newLetter = letter - 32
        else:
            newLetter = letter
        print("{}".format(chr(newLetter)), end="")
    print("")

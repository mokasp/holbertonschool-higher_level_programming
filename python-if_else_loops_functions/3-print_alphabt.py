#!/usr/bin/python3
lowercase = range(97, 123)
for letter in lowercase:
    if letter != 101 and letter != 113:
        print("{0}".format(chr(letter)), end="")

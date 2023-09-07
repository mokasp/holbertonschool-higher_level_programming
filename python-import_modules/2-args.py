#!/usr/bin/python3
from sys import argv


def main():
    length = len(argv) - 1
    if length == 1:
        print("{} argument".format(length), end="")
    else:
        print("{} arguments".format(length), end="")
    if length == 0:
        print(".")
    else:
        print(":")
        enumerated = enumerate(argv)
        for count, string in enumerated:
            if count > 0:
                print("{}: {}".format(count, string))


if __name__ == "__main__":
    main()

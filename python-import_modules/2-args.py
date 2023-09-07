#!/usr/bin/python3
import sys


def main():
    enumerated = enumerate(sys.argv)
    cnt(enumerated)
    for count, string in enumerated:
        if count > 0:
            print(f"{count}: {string}")


def cnt(argument):
    length = len(sys.argv) - 1
    print(f"{length} argument", end="")
    if length != 1:
        print("s", end="")
    if length == 0:
        print(".")
    else:
        print(":")


if __name__ == "__main__":
    main()

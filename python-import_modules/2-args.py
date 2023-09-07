#!/usr/bin/python3
from sys import argv


def main():
    enumerated = enumerate(argv)
    cnt(enumerated)
    for count, string in enumerated:
        if count > 0:
            print(f"{count}: {string}")


def cnt(argument):
    length = len(argv) - 1
    if length == 1:
        print(f"{length} argument:")
    elif length == 0:
        print(f"{length} arguments.")
    else:
        print(f"{length} arguments:")


if __name__ == "__main__":
    main()

#!/usr/bin/python3
from sys import argv


def main():
    add = 0
    argc = len(argv)

    for i in range(1, argc):
        add += int(argv[i])

    print(add)


if __name__ == "__main__":
    main()

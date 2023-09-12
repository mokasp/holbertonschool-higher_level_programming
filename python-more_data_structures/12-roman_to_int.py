#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or len(roman_string) == 0:
        return 0
    diction = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    new_list = []
    result = 0
    for x in range(len(roman_string)):
        new_list.append(diction.get(roman_string[x]))
    for y in range(len(new_list)):
        if y < len(new_list) - 1:
            if new_list[y] >= new_list[y + 1]:
                result += new_list[y]
            else:
                result -= new_list[y]
    result += new_list[y]
    return result


if __name__ == "__roman_to_int__":
    roman_to_int()

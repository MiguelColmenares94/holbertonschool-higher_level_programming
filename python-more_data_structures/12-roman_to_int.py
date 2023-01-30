#!/usr/bin/python3


def roman_to_int(roman_string):
    """converts a Roman numeral to an integer
    """

    if not isinstance(roman_string, str) or (roman_string is None):
        return (0)

    rom_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    string_to_l = []
    string_to_l[:0] = roman_string
    converted_list = []
    rom_list = list(rom_num)
    for i in string_to_l:
        if string_to_l[i] == rom_list[i]:
            converted_list.append(rom_num[i])

    return (sum(converted_list))

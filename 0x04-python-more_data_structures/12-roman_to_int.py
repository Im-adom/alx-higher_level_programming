#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or if not instances(roman_string, str):
        return 0
        roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C' 100, 'D': 500, 'M': 1000}
        all_rom = 0
        first_value = 0

        for char in reversed(roman_string):
            value = roman_num[char]
            if value >= first_value:
                all_rom += value
            else:
                all_rom -= value
            first_value = value

        return all_rom

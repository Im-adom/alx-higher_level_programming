#!/usr/bin/python3
def sub_tract(list_numb):
    sub = 0
    maxi_list = max(list_numb)

    for numb in list_numb:
        if maxi_list > numb:
            sub += numb

    return (maxi_list - sub)


def roman_to_int(roman_string):
    if not roman_string or if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_num.keys())

    numb = 0
    l_rom = 0
    list_numb = [0]

    for char in roman_string:
        for r_num in list_keys:
            if r_num == char:
                if rom_num.get(char) <= l_rom:
                    numb += sub_tract(list_numb)
                    list_numb = [rom_num.get(char)]
                else:
                    list_numb.append(rom_num.get(char))

                l_rom = rom_num.get(char)

    numb += sub_tract(list_numb)

    return (numb)

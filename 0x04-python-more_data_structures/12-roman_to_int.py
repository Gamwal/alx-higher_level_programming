#!/usr/bin/python3
def roman_to_int(roman_string):
    lookup = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if type(roman_string) == str:
        new_list = list(map(lambda x: lookup[x], list(roman_string)))
        rom_sum = new_list[-1]
    for idx in range(len(new_list) - 1, 0, -1):
        if new_list[idx] > rom_sum[idx-1]:
            rom_sum -= new_list[idx-1]
        else:
            rom_sum += new_list[idx-1]
    return rom_sum

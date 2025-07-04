#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    r_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
    sum = 0
    for i in range(len(roman_string) - 1):
        if r_dict[roman_string[i]] >= r_dict[roman_string[i + 1]]:
            sum += r_dict[roman_string[i]]
        else:
            sum -= r_dict[roman_string[i]]
    sum += r_dict[roman_string[-1]]
    return sum

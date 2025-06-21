#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    i = 0
    while i < len(roman_string):
        # Əgər növbəti simvol var və kiçik dəyər əvvəl gəlirsə
        if (i + 1 < len(roman_string) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            total += roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
            i += 2
        else:
            total += roman_dict[roman_string[i]]
            i += 1
            return total

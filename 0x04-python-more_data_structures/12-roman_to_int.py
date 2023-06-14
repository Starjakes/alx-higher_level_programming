#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
	"XC": 90, "C": 100, "CD": 400, "D": 500, "DM": 900, "M": 1000
    }
    if not isinstance(roman_string, str):
        return 0
    a = 0
    b = 0
    l = len(roman_string)
    while b < l:
        if b + 1 < l and roman_string[b:b + 2] in roman:
            a += roman[roman_string[b:b + 2]]
            b += 2
        else:
            a += roman[roman_string[b]]
            b += 1
    return a

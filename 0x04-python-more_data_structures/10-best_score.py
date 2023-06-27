#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    result = ""
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value > max:
                result = key
                max = value
        return (result)
    else:
        return (None)

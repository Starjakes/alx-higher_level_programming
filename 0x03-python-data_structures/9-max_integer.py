#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    m = my_list[0]
    for a in my_list:
        if a > m:
            m = a
    return (m)

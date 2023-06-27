#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for unint in set(my_list):
        add += unint
    return add

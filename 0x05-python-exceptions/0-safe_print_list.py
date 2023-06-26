#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for int_str in range(x):
        try:
            print(my_list[int_str], end="")
            count += 1
        except IndexError:
            break
    print()
    return count

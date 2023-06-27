#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for int_str in range(list_length):
        try:
            result = my_list_1[int_str] / my_list_2[int_str]
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        finally:
            new_list.append(result)
    return new_list

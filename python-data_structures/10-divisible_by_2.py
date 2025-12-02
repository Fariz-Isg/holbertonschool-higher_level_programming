#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans_list = []
    for num in my_list:
        if num % 2 == 0:
            ans_list.append(True)
        else:
            ans_list.append(False)
    return ans_list

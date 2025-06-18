#!/usr/bin/python3
#additional method 
"""def common_elements2(set_1, set_2):
    new_set = set()
    new_set=set_1.intersection(set_2)
    return new_set"""
def common_elements(set_1, set_2):
    new_set = set()
    for i in set_1:
        if i in set_2:
            new_set.add(i)
        else: pass
    return new_set

#!/usr/bin/python3
def best_score(a_dictionary):
    max = float('-inf')
    max_key = ""
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if max < v:
            max = v
            max_key = k
    return max_key

#!/usr/bin/python3
def multiple_returns(sentence):
    char = sentence[0]
    if len(sentence) == 0:
        char = None
    return len(sentence),char

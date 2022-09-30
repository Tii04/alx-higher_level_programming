#!/usr/bin/python3


def multiple_returns(sentence):
    if sentence is False:
        return None
    leng = len(sentence)
    first = sentence[0]
    return(leng, first)

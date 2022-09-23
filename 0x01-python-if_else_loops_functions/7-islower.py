#!/usr/bin/python3

def islower(s):
    inspect = ord(s)
    if inspect >= 97 and inspect <= 122:
        return True
    else:
        return False

#!/usr/bin/python3

def magic_string(s, n):
    i = 1
    while i <= n:
        for j in range(1, n + 1):
            print(s * i)
            i += 1

#!/usr/bin/python3
def print_last_digit(number):
    s = 0
    if number < 0:
        number *= - 1
    s = 1
    ld = number % 10
    if s == 1:
        number *= - 1
    print("{:d}".format(ld), end="")
    return ld

#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    if n == 0:
        return str[1:]
    elif n == len(str) - 1:
        return str[:len(str - 1)]
    else:
        return str[:n] + str[n + 1:]

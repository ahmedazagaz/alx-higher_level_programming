#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            upper_c = chr(ord(c) - 32)
            result_str += upper_c
        else:
            result_str += c
    print("{}".format(result_str))

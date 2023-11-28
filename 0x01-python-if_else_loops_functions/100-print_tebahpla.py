#!/usr/bin/python3
def uppercase(str):
    result_str = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            upper_c = chr(ord(c) - 32)
            result_str += upper_c
        else:
            result_str += c
    return result_str


for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 != 0:
        alpha = ord(uppercase(chr(alpha)))
    print("{}".format(chr(alpha)), end="")

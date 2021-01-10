#!/usr/bin/env python
if __name__ == '__main__':
    str_ = ''

    # a-z repeated 8 times per char (aaaaaaaabbbbbbbb...)
    for c in range(ord('a'), ord('z')+1):
        str_ += chr(c)*8

    # A-Z repeated 8 times per char (AAAAAAAABBBBBBBB...)
    for c in range(ord('A'), ord('Z')+1):
        str_ += chr(c)*8

    # 0-9 repeated 8 times per char (0000000011111111...)
    for c in range(ord('0'), ord('9')+1):
        str_ += chr(c)*8

    print(str_)

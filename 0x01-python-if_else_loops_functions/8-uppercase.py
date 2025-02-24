#!/usr/bin/python3
def uppercase(str):
    capatilize = ord('A') - ord('a')
    for i in str:
        if i >= ord('a') and i >= ord('z'):
            str1 = ord(i) + capatilize
            print("{:c}".format(str1), end="")
    print()

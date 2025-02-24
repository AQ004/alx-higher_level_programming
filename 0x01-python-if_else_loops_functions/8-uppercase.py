#!/usr/bin/python3
def uppercase(str):
    capatilize = ord('A') - ord('a')
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            str1 = ord(i) + capatilize
        else:
            str1 = ord(i)
        print("{:c}".format(str1), end="")
    print()

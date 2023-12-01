#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    lenArg = len(argv)
    sum = 0
    for x in range(1, lenArg):
        sum += int(argv[x])
    print("{}".format(sum))

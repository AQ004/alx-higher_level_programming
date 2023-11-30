#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lenOfArgs = len(sys.argv) - 1
    if lenOfArgs == 0:
        print("0 arguments.")
    elif lenOfArgs == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(lenOfArgs))

    for args in range(1, lenOfArgs + 1):
        print("{}: {}".format(args, sys.argv[args]))

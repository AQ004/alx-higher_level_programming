#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 3:
        print("{}".format(int(argv[1]) + int(argv[2])))

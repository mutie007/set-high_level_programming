#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{:d}: {}".format(i, argv[i]))

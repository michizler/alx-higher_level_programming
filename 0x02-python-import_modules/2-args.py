#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    n_arg = len(sys.argv) - 1
    arg_list = sys.argv[1:]

    if n_arg == 0:
        print("{} arguments.".format(n_arg))
    else:
        if n_arg == 1:
            print("{} argument:".format(n_arg))
        else:
            print("{} arguments:".format(n_arg))
        for arg in arg_list:
            print("{}: {}".format((arg_list.index(arg)) + 1, arg))

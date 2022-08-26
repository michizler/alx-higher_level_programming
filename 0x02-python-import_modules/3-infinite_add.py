#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sum_list = sys.argv[1:]
    i = 0
    num = 0

    while i != len(sum_list):
        num += int(sum_list[i])
        i += 1
    print("{}".format(num))

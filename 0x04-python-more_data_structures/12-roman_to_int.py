#!/usr/bin/python3

from functools import reduce

def roman_to_int(roman_string):
    if not roman_string:
        return None
    else:
        test_dic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
        val = []
        final_sum = 0
        for i in roman_string:
            val.append(test_dic.get(i))
        final_sum = reduce(lambda x, y: x+y if x > y else y-x, val)
        return final_sum

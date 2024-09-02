#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of map and reduce functions '

__author__ = 'victor yu'

# Use map and reduce to write a str2float function that converts the string '123.456' into the float 123.456:

# from functools import reduce

# def str2float(s):
#     pass

# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('Test passed!')
# else:
#     print('Test failed!')


from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
   

    def str2int(s):
      def fn(x, y):
        return x * 10 + y
      def char2num(s):
        return DIGITS[s]
      return reduce(fn, map(char2num, s))
    
    return str2int(s.replace('.',''))/(10**s.find('.'))


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('test passed!')
else:
    print('test failed!')
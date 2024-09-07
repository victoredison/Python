#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of except handling '

__author__ = 'victor yu'

# Run the following code, analyze the exception message, locate the source of the error, and fix it:

# 
# from functools import reduce

# def str2num(s):
#     return int(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# main()

from functools import reduce

def str2num(s):
    
    try:

       v=int(s)

    except ValueError as e:
       
       #print('ValueError:', e)

       return float(s)

    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of filter function '

__author__ = 'victor yu'

# A palindrome is a number that reads the same from left to right as it does from right to left, for example, 12321 or 909. 
# Use filter() to filter out palindromes:

# def is_palindrome(n):
#     pass

# # Test:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('Test passed!')
# else:
#     print('Test failed!')



def is_palindrome(n):
    a=str(n)
    b=a[::-1]
    c=int(b)

    if n==c:
        return True
    else:
        return False

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('test passed!')
else:
    print('test failed!')
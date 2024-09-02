#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of returning function '

__author__ = 'victor yu'

# Use a closure to return a counter function that returns an incrementing integer each time it is called:

# def createCounter():
#     def counter():
#         return 1
#     return counter

# # Test:
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('Test passed!')
# else:
#     print('Test failed!')

def createCounter():
    def counter():
        return 1
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Test passed!')
else:
    print('Test failed!')
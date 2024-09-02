#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of decorators '

__author__ = 'victor yu'

# Please design a decorator that can be applied to any function and print the execution time of that function:
# python
# 
# import time, functools

# def metric(fn):
#     print('%s executed in %s ms' % (fn.__name__, 10.24))
#     return fn

# # Test
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('Test failed!')
# elif s != 7986:
#     print('Test failed!')


import time, functools

def metric(fn):
    millseconds1=0
    def wrapper(*args, **kw):
      current_time1=time.time()

      print('before %s to be called' %fn.__name__)
      result= fn(*args, **kw)
      print('after %s being called' %fn.__name__)
    
      current_time2=time.time()
      elapse_time=current_time2-current_time1

      print('%s executed in %s ms' % (fn.__name__, elapse_time*1000))

      return result
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('test failed!')
elif s != 7986:
    print('test failed!')
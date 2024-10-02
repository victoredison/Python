#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# write itertools module to calculate pi

__author__ = 'victor yu'



import itertools

def pi(N):
   
    # step 1: create a list of odd numbers
    odd_num = itertools.count(1,2)
   

    # step 2: create a slice of the first N numbers
    odd_num_n = itertools.islice(odd_num,  N)



    # step 3: add +/- and divided by 4 4/1, -4/3, 4/5, -4/7, 4/9, ...
    result=[]
    count=1
    for item in odd_num_n:
        if count%2==1:
            result.append(4/item)
        else:
            result.append(-4/item)
        count+=1

    # step 4: calcumlate the sum:

    return sum(result)
         

# testing:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

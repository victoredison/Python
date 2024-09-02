#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of lamada function '

__author__ = 'victor yu'

#lamada function exercise

#def is_odd(n):
#   return n % 2 == 1

#L = list(filter(is_odd, range(1, 20)))


import numpy

L= list(filter(lambda x: x%2==1, range(1,20)))
print(L)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of sorted function '

__author__ = 'victor yu'

#sorted() exercise

# Suppose we use a list of tuples to represent student names and scores:

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# # Use sorted() to sort the list above by name:

# def by_name(t):
#     pass

# L2 = sorted(L, key=by_name)
# print(L2)

# # Now, sort by score in descending order:

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_score(t):
#     pass

# L2 = sorted(L, key=by_score)
# print(L2)



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of file operation '

__author__ = 'victor yu'


fpath = '/usr/local/temp/test.txt'

with open(fpath, 'a+') as f:
    f.write('Hello World')
    f.seek(0)
    print(f.read())

# with open(fpath, 'r') as g:    
#     s=g.read()
#     print(s)
    

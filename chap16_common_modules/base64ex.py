#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of base64 module'

#write a decode function which can truncate the '==' at the end of encoding

__author__ = 'victor yu'

import base64

def safe_base64_decode(s):
   
    # for i in range(len(s)%4):
    #     s +='='
    
    # return base64.b64decode(s)


    return base64.b64decode(s + '='* (len(s)%4))

# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
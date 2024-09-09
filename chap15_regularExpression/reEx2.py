

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of regular expression '

__author__ = 'victor yu'

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# please try to write a regular expression that can validate an email address
# First edition of this expression should be able to validate email address like
# someone@gmail.com
# bill.gates@microsoft.com


import re

def is_valid_email(addr):
    return  re.match(r'^[0-9a-zA-Z\.]*\@[a-z]*\.com$',addr)
    

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

import re

def is_valid_email(addr):
    return  re.match(r'^[0-9a-zA-Z\.]*\@[a-z]*\.com$',addr)
    

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
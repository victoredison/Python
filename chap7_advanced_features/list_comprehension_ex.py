
L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [s for s in L1 if isinstance(s, str)]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('test success!')
else:
    print('test failure!')
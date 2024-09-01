def trim(s):
    if s=='':
        return s
    while(s[0] == ' '):
        s=s[1:len(s)]
        if s=='':
            return s
    while(s[-1]==' '):
        s=s[0:len(s)-1]
        if s=='':
            return s
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')


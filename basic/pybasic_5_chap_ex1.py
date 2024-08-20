print('''line1
line2
line3''')

print(ord('中'))

print(chr(66))

print('中文'.encode('UTF-8'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)


s1=71
s2=85
r=(s2-s1)/s1
print('\'%.1f%%\'' % r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

print(L[0][0])

print(L[1][1])

print(L[2][2])

height=1.75
weight=80.5
bmi = weight/(height**2)

if bmi > 32:
    print("严重肥胖")
elif bmi > 28:
    print('肥胖')
elif bmi > 25:
    print('过重')
elif bmi > 18.5:
    print('正常')
else:
    print('过轻')



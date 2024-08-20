fpath = '/usr/local/temp/test.txt'

with open(fpath, 'a+') as f:
    f.write('Hello World')
    f.seek(0)
    print(f.read())

# with open(fpath, 'r') as g:    
#     s=g.read()
#     print(s)
    

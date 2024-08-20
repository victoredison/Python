import re

def name_of_email(addr):
    n1=re.split(r'\@',addr)
   # print(n1[0],' ', n1[1])

    n2=re.split(r'\<',n1[0])
    

    if(len(n2)==1):
     #  print(n2[0])
       return n2[0]

    else:
     #  print(n2[1])
       n3=re.split(r'\>',n2[1])
     #  print(n3[0])
       return  n3[0]

    return None


#name_of_email('<Tom Paris>tom@voyager.org')
#name_of_email('tom@voyager.org')
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
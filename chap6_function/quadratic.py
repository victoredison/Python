import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand')
    if not isinstance(b,(int,float)):
        raise TypeError('bad operand')
    if not isinstance(c,(int,float)):
        raise TypeError('bad operand')
    return (-b+math.sqrt(b*b-4*a*c))/(2*a), (-b-math.sqrt(b*b-4*a*c))/(2*a)


print('quadratic(2,3,1)=', quadratic(2,3,1))
print('quadratic(1,3,-4)=', quadratic(1,3,-4))

if(quadratic(2,3,1)!=(-0.5,-1.0)):
    print('test fail')
elif(quadratic(1,3,-4)!=(1.0,-4.0)):
    print('test failure')
else:
    print('test success')
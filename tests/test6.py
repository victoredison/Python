def triangles():
    n=1
    t=[1]
    a=0
    while(n<=10):
      
        h=[]
           
        for i in range (n):
            print('i:',i)
            if (i!=0) and (i != n-1):
                a = t[i-1]+t[i]      
            elif i==0:
                a = t[i]
                print('a:',a)
            elif i==(n-1):
                a=t[-1]
                print('a:',a)
            h.append(a)
        t=h
        
        
        print('h',h) 
        print('t',t)
          
        
        n=n+1        
    


triangles()
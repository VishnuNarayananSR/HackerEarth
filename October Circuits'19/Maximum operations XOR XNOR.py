import math  
def swap(a,b):   
    temp=a 
    a=b 
    b=temp 
def xnor(a, b): 
   if (a < b): 
        swap(a, b) 
   if (a == 0 and b == 0) : 
        return 1 
   a_rem = 0 
   b_rem = 0 
   count = 0
   xnornum = 0 
   while (a!=0) : 
        a_rem = a & 1 
        b_rem = b & 1 
        if (a_rem == b_rem):      
            xnornum |= (1 << count)
        count=count+1    
        a = a >> 1
        b = b >> 1
   return xnornum
def xor(x, y): 
    return ((x | y) &  
            (~x | ~y)) 
testCase=int(input())
while testCase > 0:
    testCase -= 1
    str1 = input()
    l = str1.split(" ")
    print (l)
    a = int(l[0])
    b = int(l[1]))
    n = int(l[2])
    n = n % 3
    if n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
        print(max(xor(a,b),xnor(a,b)))

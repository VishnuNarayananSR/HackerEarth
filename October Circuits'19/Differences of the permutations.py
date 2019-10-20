testCase = int(input())
while testCase >0: 
    N = int(input())
    list1ToN = list(range(1,N+1))
    diff = sum(list1ToN) - N
    from math import factorial
    ans = diff*factorial(N)
    print(ans)
    testCase-=1

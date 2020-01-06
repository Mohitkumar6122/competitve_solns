import math
t=int(input())
while(t):
    sum=0
    s,a,b,c=map(int,input().split())
    sum=a+b+c
    print(math.ceil(sum/s))
    t-=1

n=int(input())
v=n*n
x=0
while(n>0):
    r=n%10
    x=x*10+r
    n=n//10
a=x*x
k=0
while(a>0):
    b=a%10
    k=k*10+b
    a=a//10
if(v==k):
    print('True')
else:
    print('False')
 
def rev(n):
    s=0
    while n:
        s=s*10+(n%10)
        n=n//10
    return s
n=int(input())
t=rev(n)
if(t==n):
    print('True')
else:
    print('False')
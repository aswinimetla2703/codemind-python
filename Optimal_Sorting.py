n=int(input())
for i in range(n):
    t=int(input())
    l=list(map(int,input().split()))
    c=sorted(l)
    if c==l:
        print('0')
        break
    else:
        d=c[-1]-c[0]
        print(d)
_=int(input())
v=list(map(int,input().split()))
a=0
for k in range(len(v)):
    if k%2==0:
        a+=v[k]
print(a)
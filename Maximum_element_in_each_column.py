n,m=map(int,input().split())
v=[]
for _ in range(n):
    v.append(list(map(int,input().split())))
for i in range(n):
    k=0
    for j in range(m):
        if v[j][i]>=k:
            k=v[j][i]
    print(k)
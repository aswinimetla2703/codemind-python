n=int(input())
v=0
k=1
r=0
j=0
for i in range(1,n+1,1):
    r=v+k
    v=k
    k=r
    if r==n:
        j+=1
if j==0:
    print('False')
else:
    print('True')
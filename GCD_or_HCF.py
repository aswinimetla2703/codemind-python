v,k=map(int,input().split())
l=0
for i in range(1,v+1 and k+1,1):
    if v%i==0 and k%i==0:
        l=i
print(l)
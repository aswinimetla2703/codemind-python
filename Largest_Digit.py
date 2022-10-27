v=int(input())
s=0
while(v>0):
    r=v%10
    if(s<r):
        s=r
    v=v//10
print(s)
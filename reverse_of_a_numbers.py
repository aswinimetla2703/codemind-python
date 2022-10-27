v=int(input())
s=0
while(v>0):
    r=v%10
    s=s*10+r
    v=v//10
print(s)
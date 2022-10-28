n=int(input())
v=list(map(int,input().split()))
for k in v:
    if v.count(k)>(n//2):
        print(k)
        break
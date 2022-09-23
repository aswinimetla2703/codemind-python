t=int(input())
for i in range(t):
    n,m,b,k=map(int,input().split())
    p=n//m
    q=n//b
    if p+q>=k:
        print("Win")
    else:
        print("Lose")